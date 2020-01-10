import arcpy
import sys
import os
import traceback
import datetime
import time
import shutil
import webbrowser

from utils.messages import (LOGFILE_HEADER, LOGFILE_BODY, LOGFILE_ENTRY)


sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
'''
    I think the architecture to clean this mess up
    is to create a bonafide package and have it installed
    which would update sys.path upon installation
'''


class SuiteGeoOne(object):
    def __init__(self):
        """
            SuiteGeoOne
        """
        #import structure_data_lib as shared_lib
        self.label = "SuiteGeoOne"
        self.description = self.label
        self.category= ""
        self.canRunInBackground = False
        self.alias = "dynseg_tvc_data"
        '''
        Start Non-Esri properties
        '''
        #self.homepath = os.path.dirname(os.path.dirname(__file__))
        self.homepath = "C:\gp"
        self.title = "SuiteGeoOne"
        self.logpath = ""
        self.log_title = "SuiteGeo - " + self.label
        self.webmap_as_wms = os.path.join(self.homepath, "SDEConnections", "SuiteGeo.sde")
        self.get_parameter = {}
        self.rid = None
        self.view_paths = None
        self.recordset = None
        self.appdata = self.set_appdata()
        self.logsetup("SuiteGeo_One_Log.htm")
        # This causes the mxd to be opened on many cycles in the ArcMap event loop for actions:
        # 1. Opening Tool
        # 2. Opening ArcMap
        # 3. Try to do in library once on class
        self.layer_list = None
        self.gdb_path = None
        self.errors = None
        self.computer_name = os.getenv('COMPUTERNAME')


    def getParameterInfo(self):
        self.logit("Inside getParameterInfo")
        '''Custom Paramater Management'''
        import dynseg_tvc_data_params as param_mgr
        params = param_mgr._get_parameters(self)
        for p in params:
            self.logit(p.name)
            self.get_parameter[p.name] = p
        '''
        rid = '37803DC9-99ED-46F7-8C61-34B681D28820'
        params = [rid]
        self.rid = rid
        '''
        return params


    def isLicensed(self):
        return True


    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        
        '''
            For some reason self.get_parameter dict created in the getParamterInfo method or
            class seems to be destroyed because I'm having to do it again here.

            Not sure why?!
        '''

        import suite_geo_one_params as param_mgr
        
        for p in parameters:
            self.get_parameter[p.name] = p

        '''
        param_mgr._update_parameters(self)
        '''

        return
        

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return


    def execute(self, parameters, messages):
        """The source code of the tool."""
        self.run_tool(parameters)
        #arcpy.AddMessage(self.recordset)
        #print self.recordset
        arcpy.SetParameter(1, self.recordset)
        '''
            It seems that the SetParameterAsText method generates a arcpy.Result object.
            I would like to instead return a json string...
        '''
        return


    def run_tool(self, parameters):
        arcpy.AddMessage("***************************************")
        arcpy.AddMessage(" ")
        arcpy.AddMessage(" ")
        arcpy.AddMessage("  * * * * " + self.label + " * * * *")
        arcpy.AddMessage(" ")
        arcpy.AddMessage(" ")

        self.rid = parameters[0].value
        self.suite_geo_one_lib()
        
        arcpy.AddMessage(" ")
        arcpy.AddMessage(" ")
        arcpy.AddMessage("***************************************")


    def suite_geo_one_lib(self):
        try:
            pass
        except:
            self.errors = 1
            arcpy.AddMessage("General Error")
            arcpy.AddMessage(traceback.format_exc())
            self.logit("General Error")
            self.logit(traceback.format_exc())
        if self.errors == 1:
            shared_path = shared_path = "\\\\" + self.computer_name + "\\" + "c$" + self.logpath.split("C:")[1]
            arcpy.AddMessage(shared_path)
            webbrowser.open(shared_path)


    def logsetup(self, logfilename):
        logdir = os.path.join(self.homepath, "Log")
        appdir = os.path.join(logdir, self.title)
        dirlist = [self.homepath, logdir, appdir]
        for i in dirlist:
            try:
                if not os.path.exists(i):
                    os.mkdir(i)
            except:
                arcpy.AddMessage(traceback.format_exc())
        self.logpath = self.create_logfile(appdir, logfilename)
        self.logit("Tool Initialized...")
        self.logit("")


    def timestamp(self):
        dtn = str(datetime.datetime.now()).split(" ")
        return dtn[1]


    def create_logfile(self, logdir, logfilename):
        dtn = str(datetime.datetime.now()).split(" ")
        day = dtn[0].split("-")
        day_value = day[0] + "-" + day[1] + "-" + day[2]
        starttime = dtn[1].split(".")[0]
        timestamp = day_value + "-" + "".join(str("".join(dtn[1].split(":"))).split("."))
        logfile = os.path.join(logdir, logfilename)
        with open(logfile, 'w') as logme:
            logme.write(LOGFILE_HEADER)
            logme.write(LOGFILE_BODY.format(self.log_title, day_value, starttime))
        return logfile


    def logit(self, message):
        with open(self.logpath, 'a') as logme:
            logme.write(LOGFILE_ENTRY.format(str(message), str(self.timestamp())))


    def set_appdata(self):
        appdata_home = os.path.join(self.homepath, "AppData")
        appdata = os.path.join(appdata_home, self.title)
        dirlist = [appdata_home, appdata]
        for i in dirlist:
            try:
                if not os.path.exists(i):
                    os.mkdir(i)
            except:
                arcpy.AddMessage(traceback.format_exc())
        return appdata


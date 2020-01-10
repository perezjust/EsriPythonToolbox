import arcpy
import os
import json


compname = os.getenv('COMPUTERNAME')

if compname == 'AWS0ISPV2' or compname == 'AWS0TSPV1A':
	sys.path.append(r"\\boardwalk.corp\Global\AppData\GIS\Cloud\Applications\Boardwalk\GISCommon\PROD")
elif compname == 'AWS0ISQV2' or compname == 'AWS0TSQV1A':
	sys.path.append(r"\\boardwalk.corp\Global\AppData\GIS\Cloud\Applications\Boardwalk\GISCommon\QA")
else:
	sys.path.append(r"\\boardwalk.corp\Global\AppData\GIS\Cloud\Applications Delivery\Boardwalk\GISCommon\DEV")



from tvc_tools import toolbox_loader


for import_text in toolbox_loader.IMPORT_LIST:
    exec(import_text)


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "SuiteGeo Tools"
        self.alias = "SuiteGeo"
        self.description = "SuiteGeo Tools"
        self.tools = toolbox_loader.get_toolbox_classes()





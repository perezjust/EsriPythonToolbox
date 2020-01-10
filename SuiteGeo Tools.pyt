import arcpy
import os
import json


compname = os.getenv('COMPUTERNAME')

if compname == 'AWSPRODBOX1' or compname == 'AWSPRODBOX2':
	sys.path.append(r"\\some\directory\PROD")
elif compname == 'AWSQABOX1' or compname == 'AWSQABOX2':
	sys.path.append(r"\\some\directory\QA")
else:
	sys.path.append(r"\\some\directory\DEV")



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





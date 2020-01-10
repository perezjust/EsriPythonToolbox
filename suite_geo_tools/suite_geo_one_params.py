import arcpy
import sys
import os
import json
import webbrowser
import ast
import traceback
import datetime
import time
import getpass


sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
'''
    I think the architecture to clean this mess up
    is to create a bonafide package and have it installed
    which would update sys.path upon installation
'''




def _get_parameters(self):

    rid = arcpy.Parameter(
    displayName="Route Event ID",
    name="rid",
    datatype="GPString",
    parameterType="Required",
    direction="Input")

    recordset = arcpy.Parameter(
    displayName="Dynamic Segmentation Output",
    name="output",
    datatype="DETable",
    parameterType="Derived",
    direction="Output")

    #mxd_path.value = ""
    #override_missing_fields.value = False

    params = [rid, recordset]

    return params


def _update_parameters(self):
    pass











IMPORT_LIST = ['from suite_geo_tools.suite_geo_one import SuiteGeoOne',
               'from suite_geo_tools.suite_geo_two import SuiteGeoTwo'
               ]

TOOL_LIST = ['SuiteGeoOne', 'SuiteGeoTwo'
             ]
import sys
print sys.path

for import_text in IMPORT_LIST:
    exec import_text


def get_toolbox_classes():
    return [eval(tool) for tool in TOOL_LIST]

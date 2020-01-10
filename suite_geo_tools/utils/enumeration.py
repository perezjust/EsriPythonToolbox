"""
Enums
"""

#designator = 'str(!ll_Designator!) + ": " + '
designator = '!ll_Designator! + ": " + '
common = designator + 'str(!TypeCL!)'

DisplayFields = {
    'Appurtenance' : common,
    'ClassRating' : designator + '"Class " + str(!RatingCL!)',
    'Coating' : common,
    'Equation' : designator + '!Description!',
    'ForeignLineCrossing' :  common,
    'HCA' : designator + '"HCA " + str(!HCAName!)',
    'ILIData' : 'str(!insp_ll_designator!) + ": " + ' + 'str(!CallTypeCL!)',
    'Incident' : designator + 'str(!FailureCategoryCL!)',
    'Meter' : designator + 'str(!MeterNumber!)',
    'Milepost' : designator + 'str(!Milepost!)',
    'PipeSegment' : '!linename! + ": " + ' + 'str(!SMYSCL!) + " | " + str(!NominalDiameterCL!) + ' + '"' + "''" + '"' + ' + " | " + "x" + str(!NominalWallThicknessCL!)',
    'RailroadCrossing' : designator + '!Description!',
    'RegulatoryBoundary' : common,
    'RoadCrossing' : designator + '!Description!',
    'Sleeve' : common,
    'TestLead' : designator + '!ll_Description!',
    'TestPressure' : designator + 'str(!TestPressure!) + " psi"',
    'Valve' : designator + 'str(!ValveIdentifier!)',
    'Tap' : designator + '!Description!',
    'MAOP' : designator + 'str(!Pressure!)'
    }




if __name__ == '__main__':
    pass

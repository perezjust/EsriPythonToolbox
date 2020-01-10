"""
Messages
"""

ERR_MESSAGE = '**Error {0} {1}'

VIEW_MESSAGE = 'Organizing View.. '

EXPORT_MESSAGE = 'Exporting View.. '

SPATIALIZE_MESSAGE = 'Spatializing Table.. '

TRUNC_APPEND_MESSAGE = 'Truncating and Appending.. '

APPENDING_MESSAGE = 'Appending Data.. '

TRUNCATING_MESSAGE = 'Truncanting Data.. '

PROJECTING_MESSAGE = 'Projecting Data.. '

FIELD_CALC_MESSAGE = 'Field Calculating Data.. '



"""
Logging
"""

LOGFILE_HEADER = (
    "<html><head><title>Logs</title>"
    "<style type='text/css'>body {margin: 30px auto;font-family: Verdana}td {font-family: Verdana, Arial, Helvetica, sans-serif;"
    "font-size: 15px;color: #555555;text-align: left;}.header {height: 25px;background-color: #2E86C1;font size: 20px; color: #EBDEF0;}</style>"
    )

LOGFILE_BODY = (
    "<body><b>{0}</b>"
    "<p/>"
    "<b>Run Date: {1} @ {2} </b>"
    "<table width=100%>"
    "<tr><td class='header' valign='top'>Message</td><td class='header' valign='top'>Timestamp</td></tr>"
    )

LOGFILE_ENTRY = "<tr bgcolor=#F8F9F9><td>{0}</td><td>{1}</td></tr>"





if __name__ == '__main__':
    pass

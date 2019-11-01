import requests

def searchamt(ss, searchurl, sql_data, header):
    return ss.post(searchurl, data=sql_data, verify=False, headers=header)
import requests
import re

def link_to_json(link):
    id = re.findall(pattern=r'(?:id=)([0-9]+)', string=link)
    url = 'https://kd.99bill.net/dapi/visitor/interface/detail.do'
    data = {
        'id': id,
        'password':'',
        'visitCode':''
    }
    D ={}
    L ={}
    T = []

    response = requests.get(url, params=data)
    response.encoding = 'utf-8'
    html = response.text    #soup
    key = r'"crShowParamList":.+}],'    #取出request所有内容的正则表达式
    paramscontent = re.search(pattern=key, string=html, flags=0).group(0)  #提取crShowParamList的内容
    paramsvalue = r'(?:"name":")([\w>-]+)(?:")' #取出list值的正则表达式
    paramslist = re.findall(pattern=paramsvalue, string=paramscontent)  #提取出"name"和对应的值组成的list
    temp = ''
    listformat = r'(\w+)(->)(\w+)'
    for index in range(0, len(paramslist)-1):
        listitem1 = re.search(pattern=listformat, string=paramslist[index])
        listitem2 = re.search(pattern=listformat, string=paramslist[index+1])
        if listitem1 == None and listitem2 == None:
            D[paramslist[index]] = '参数'
        elif listitem1 == None and listitem2 != None:
            temp = paramslist[index]
        else:
            L[listitem1.group(3)] = '参数'
    T.append(L)
    D[temp] = T
    return D
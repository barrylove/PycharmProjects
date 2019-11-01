import re

arr = ["merchantName", "province", "city", "county", "legalName", "legalId", "registDate", "address", "businesslicenseNumber", "fileList", "fileList->fileExtName", "fileList->fssId", "fileList->fileType", "companyType", "merchantType", "mcc", "businessEndDate", "businessStartDate", "idCardStartDate", "idCardEndDate", "mccDesc", "faceImageFssId"]
arr2 = ["fileList->fileExtName"]
D ={}
L ={}
T = []
temp = ''
listformat = r'(\w+)(->)(\w+)'
for index in range(0, len(arr)-1):
    listitem1 = re.search(pattern=listformat, string=arr[index])
    listitem2 = re.search(pattern=listformat, string=arr[index+1])
    if listitem1 == None and listitem2 == None:
        D[arr[index]] = '参数'
    elif listitem1 == None and listitem2 != None:
        temp = arr[index]
    else:
        L[listitem1.group(3)] = '参数'

T.append(L)
D[temp] = T
print(D)



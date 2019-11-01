import random,string
import xlwt

def random_Series(count,len):
    #初始化字库
    str = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #初始化list
    series_set = []

    #生成随机数
    for i in range(0,count):
        series = ""
        for j in range(0,len):
            series = random.choice(str) + series
        if series not in series_set:
            series_set.append(series)
    print(series_set)

    return series_set

def writeExcel(genkeys):
    data = xlwt.Workbook()
    table = data.add_sheet("genkeys")
    for i in range(0,len(genkeys)):
        table.write(i,0,genkeys[i])
    data.save("e:/demo.xls")

genkeys = random_Series(20,20)

writeExcel(genkeys)
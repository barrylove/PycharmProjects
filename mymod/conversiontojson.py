#--coding:utf-8--
import xlrd


def conversion_to_json(fielname):
    data = xlrd.open_workbook(fielname)
    table = data.sheet_by_index(0)
    nrows = table.nrows

    D = {}

    for row in range(1,nrows):
        D[table.cell(row, 0).value] = table.cell(row, 1).value

    return D
import pdfplumber
import pandas as pd

path = 'E:\\1.pdf'
pdf = pdfplumber.open(path)
i = 1
#writer = pd.ExcelWriter('output.xlsx')
df = pd.DataFrame(columns=['项目编码', '项目名称', '项目内涵', '除外内容', '计价单位', '计价说明', '项目价格(元)', '备注', '医保类别', '工伤保险类别'])
for page in pdf.pages:
    # 获取当前页面的全部文本信息，包括表格中的文字
    # print(page.extract_text())
    for table in page.extract_tables():
        #print(table)
        df = df.append(pd.DataFrame(table[1:], columns=table[0]), ignore_index=True)

writer = pd.ExcelWriter('output3.xlsx')
new_df = pd.DataFrame()
j=1
index=[]
#记录序号==1的行索引，用于后面的表格拆分
for i in range(len(df)):
    if df.ix[i, 0] =='1':
        index.append(i)
        print("################")
index.append(len(df))

for t in range(len(index)-1):
    new_df=df.ix[index[t]:index[t+1]-1,:]
    #print (new_df)
    new_df.to_excel(writer, sheet_name="sheet1", encoding='gb2312', index=None)
writer.save()
pdf.close()
print('finished')

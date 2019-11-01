import yaml
import os

yamlPath = "D:\yamlstudy\dbconfig.yaml"
"""
fw = open(yamlPath, 'a', encoding='utf-8')
data = {"COEDB":{
    "host":"192.168.9.147",
    "port": 3320,
    "user": "qamodify",
    "password": "ybvaulx7fh5497fh",
    "db": "ocean",
    "charset": "utf8"
    }
}
yaml.dump(data, fw)
fw.close()"""

f = open(yamlPath, 'r', encoding='utf-8')
cont = f.read()
x = yaml.load(cont, Loader=yaml.FullLoader)
print(x)
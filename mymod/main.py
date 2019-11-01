#--coding:utf-8--
from flask import request
from linktojson import link_to_json
from conversiontojson import conversion_to_json
from flask import Flask, jsonify

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
@app.route('/', methods = ['GET'])
def home():
    return '''
        <form action="/" method="post">
                  <p><input name="link" type="text" style="width:900px;" /></p>
                  <h1>填入DAPI接口管理平台连接,获取json</h1>
                   <p><button type="submit">提取request参数</button></p>
                  </form>
        '''
@app.route('/', methods = ['post'])
def getrequestjson():
    if request.form['link'] != None:
        link = request.form['link']
        re = link_to_json(link)
    return jsonify(re)

if __name__ == '__main__':
    app.run(host='10.11.66.110', port=3002)  # 默认不填写的话，是5000端口

    """
#读取excel
    filename = 'D://test.xlsx'
    dict = conversion_to_json(filename)
    jsonfile = json.dumps(dict, ensure_ascii=False)
    print(jsonfile)
    link = 'https://kd.99bill.net/dapi/project.do#/interface/detail?projectId=156170108711307001122&id=156903232013212001612'
    link_to_json(link)
    """
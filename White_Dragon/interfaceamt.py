#!flask/bin/python
from flask import Flask
from flask import request
from caltotalamt import calamt

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def home():
    return '<h1>hello</h1>'

@app.route('/calamt',methods = ['GET'])
def amt_form():
    return '''
    <form action="/calamt" method="post">
              <p><input name="date"></p>
              <h1>日期的格式你得像“2019-10-15"这个样子的才可以</h1>
               <p><button type="submit">计算总额</button></p>
              </form>
    '''
@app.route('/calamt' , methods=['POST'])
def amt():
    # 需要从request对象读取表单内容：
    if request.form['date'] != None:
        trdate = request.form['date']
        result = trdate + "交易量为:" + str(calamt(trdate))
        return result

@app.route('/1' , methods=['POST'])
def aa(): #传什么返回什么
    with open('1.txt','a') as f:
        print(str(request.data, encoding='utf-8'),file=f)

    return request.data

if __name__=='__main__':
    app.run(host= '10.11.66.110', port=3002)#默认不填写的话，是5000端口
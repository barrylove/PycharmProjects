#!flask/bin/python
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def home():
    return '<h1>hello</h1>'

@app.route('/signin',methods = ['GET'])
def signin_form():
    return '''
    <form action="/signin" method="post">
              <p><input name="date"></p>
               <p><button type="submit">Sign In</button></p>
              </form>
    '''
@app.route('/signin' , methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['date'] != None:
         result = request.form['date'] + "交易量为:"
    return result

@app.route('/1' , methods=['POST'])
def aa(): #传什么返回什么
    with open('1.txt','a') as f:
        print(str(request.data, encoding='utf-8'),file=f)

    return request.data

if __name__=='__main__':
    app.run(port=3002)#默认不填写的话，是5000端口
#!flask/bin/python
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def home():
    return '<h1>hello</h1>'

@app.route('/signin' , methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    username = request.json.get('username')
    password = request.json.get('password')
    return "your username is:" + username + " and your password is:" + password

@app.route('/1' , methods=['POST'])
def aa(): #传什么返回什么
    with open('1.txt','a') as f:
        print(str(request.data, encoding='utf-8'), file=f)

    return request.data

if __name__=='__main__':
    app.run(port=3002)#默认不填写的话，是5000端口
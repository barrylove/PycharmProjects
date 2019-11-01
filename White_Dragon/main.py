from flask import Flask

app = Flask(__name__)
@app.route('/')
def first_flask():
    return 'hello world' #response

if __name__ == '__main__':
    app.run(host='10.11.16.102', port=5000)
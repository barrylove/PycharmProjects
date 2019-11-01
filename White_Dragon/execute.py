from flask import Flask
import requests

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello World'

@app.route('/bye')
def say_bye():
    return 'Bye Bye'

def execute_job(execute_url, triggerName):
    login_url = 'http://srv-monitor-st2.99bill.net/app-monitor-website/userLoginSub.do'
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
    login_params = {
        "userName": "admin",
        "userPwd": "billadmin",
        "Submit": "登录"
    }

    FO_params = {
        "triggerGroup":"ino.mbp.t",
        "triggerName": triggerName,
        "remark":"test",
        "Submit":"确定",
        "formKeys":{"triggerGroup":"应用名称","triggerName":"任务名称","remark":"操作原因","demandUser":"需求人"}
    }
    sess = requests.session()
    sess.post(login_url, params=login_params, headers=headers, verify=False)
    response = sess.post(execute_url, params=FO_params, headers=headers, verify=False).text
    return response

@app.route('/PaymentOutFoJob')
def PaymentOutFoJob():
    execute_url = 'http://srv-monitor-st2.99bill.net/app-monitor-website/quartz-framework/runJob.do'
    triggerName = "mbp.t.PaymentOutFoJob.jobTrigger"
    return execute_job(execute_url, triggerName)

@app.route('/QueryPayResultFoJob')
def QueryPayResultFoJob():
    execute_url = 'http://srv-monitor-st2.99bill.net/app-monitor-website/quartz-framework/runJob.do'
    triggerName = "mbp.t.QueryPayResultFoJob.jobTrigger"

    return execute_job(execute_url, triggerName)

if __name__ == '__main__':
    app.run(host='10.11.16.102', port=5000)
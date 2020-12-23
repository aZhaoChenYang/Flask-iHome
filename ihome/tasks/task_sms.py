
from celery import Celery
from ihome.libs.yuntongxun.sms import CCP

# 定义celery对象
celery_app = Celery("ihome", broker="redis://:123456@182.92.175.165:6379/1")

@celery_app.task
def send_sms(to, data, temp_id):
    """发送短信的异步任务"""
    ccp = CCP()
    ccp.send_message(to, data, temp_id)

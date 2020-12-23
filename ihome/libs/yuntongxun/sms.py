from ronglian_sms_sdk import SmsSDK
import ast

accId = '8a216da8762cb4570176767d6be11e7a'
accToken = '7456def42a5c4196a4c23913724aea97'
appId = '8a216da8762cb4570176767d6ce11e81'

class CCP(object):
    """自己封装的发送短信的辅助类"""
    # 用来保存对象的类属性
    instance = None
    def __new__(cls):
        # 判断CCP类有没有已经创建好的对象,如果没有,创建一个对象,并且保存
        # 如果有则将保存的对象直接返回
        if cls.instance is None:
            obj = super(CCP, cls).__new__(cls)
            accId = '8a216da8762cb4570176767d6be11e7a'
            accToken = '7456def42a5c4196a4c23913724aea97'
            appId = '8a216da8762cb4570176767d6ce11e81'
            obj.sdk = SmsSDK(accId, accToken, appId)
            cls.instance = obj
        return cls.instance



    def send_message(self, mobile, datas, tid):
        """"""
        resp = self.sdk.sendMessage(tid, mobile, datas)
        resp = ast.literal_eval(resp)
        status_code = resp.get("statusCode")
        if status_code == "000000":
            # 表示发送成功
            return 0
        else:
            # 发送失败
            return -1

if __name__ == '__main__':
    ccp = CCP()
    ret = ccp.send_message("18210170170", ["1234", "5"], 1)
    print(ret)
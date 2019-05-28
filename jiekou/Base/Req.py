import requests,time

class Req():
    def __init__(self,url,para=None,header=None):
        self.url=url
        self.para=para
        self.header=header

    def req_get(self):
        try:
            r=requests.get(url=self.url,params=self.para,headers=self.header)
            return r
        except BaseException as e:
            print("get 请求失败",str(e))
    def req_post(self):
        try:
            r=requests.post(url=self.url,data=self.para,headers=self.header)
            return r
        except BaseException as e:
            print("post 请求失败",str(e))



if __name__ == '__main__':
    a=Req('https://test.tianxun123.cn/api/cartList',para={'is_up_level':1},header={'Authorization':
'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzOTciLCJhdWQiOiJBUFAiLCJpc3MiOiJodHRwczovL3RpYW54dW4uY29tIiwiZX'
'hwIjoxNTkwNjQ3MDcwLCJpYXQiOjE1NTkwMjQ2NzB9.WBaSxmauqEpK2XLqvs4P64PuGLM-Fe9DnaxKPIhpp_s'}).req_post()
    print(type(a.text))
    print(a.json())
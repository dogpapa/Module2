import requests
import urllib
import json



class MemberStore:

#  modey.py에서 호출하도록 하기

    
#====== 참고 blog==========================================
    # https://twpower.github.io/124-python-requests-usage
    # https://velog.io/@wimes/node.js-REST-API-%EC%84%9C%EB%B2%84-%EB%A7%8C%EB%93%A4%EA%B8%B0-3.-%EB%A7%8C%EB%93%A4%EA%B8%B0
    # https://requests.readthedocs.io/en/latest/user/quickstart/#passing-parameters-in-urls
    # https://my-devblog.tistory.com/27


#====== Node.js 작성시 참고사항============================
#  1. 직접 url창에 /users, /users/1 과 같이 입력하는 대신 
#     python에서 url창에 원하는 형식의 url을 직접 호출한다. 
#     (/users등으로 기존과 동일하게 작성)
#     이를 통해 해당 app.get() 함수가 실행되도록 조작됩니다. 
#     따라서 /이후의 항목에 따라 알맞은 app.get/post/delete/put()을 추가 및 조작해주세요~

# 2.  req, res
#     rea = request(송신) / res = response(수신)
#     따라서 송신과 수신은 json형태로 주고 받도록 한다.
#     
# 3.  entity로 넘겨줄 때 vs email로 넘길 때
#     entity는 body로, email은 param으로 해체하는 듯 합니다.
#     사실 뇌피셜이긴 한데...ㅠㅠㅠ일단 강사님 코드는 entity는 body, id는 param으로 해체하셔서 그렇게 넘깁니다.
# 
# 4.  users => users 그대로 사용
#     id => email = primary key 

#========================================================

    def __init__(self):
        self.url = 'http://ec2_url/' # url은 nodejs를 작성한 ec2로 해야함
        # URL NODEJS로 된것 받아서 수정해야함

    # 이메일, 패스워드 확인
    def login_ok(self,email, passwd):
        if bool(email) and bool(passwd):
            api_result =requests.get(self.url + "users/" + email)
            api_result = api_result.json()
            return api_result
            # fetchaone으로 가져옴 -> 예상 return email

            
    # 이메일 검증
    def email_Validation(self,email):
        if bool(email):
            api_result = requests.get(self.url + "users/" + email)
            api_result = api_result.json()
        return api_result 
        # fetchaone으로 가져옴 -> 예상 return email

    # 유저 등록
    def insert_member(self,entity):
        body = {'email':entity.u_email, 'passwd':entity.u_passwd,'name':entity.u_name,
                'nickname':entity.u_nick_name,'phonenumber': entity.u_phone_number,
                'birthday':entity.u_birthday,'address':entity.u_address}
        res = requests.post(self.url, data=json.dumps(body))
        res = res.json()
        return res['ok']
        # 딕셔너리 값으로 안주기 때문에 dic의 value를 가져오기 위해서 이렇게 변경함!
        # POST로 보내서 JSON으로 ENTITY 보냄 -> json으로 ok key의 값 보냄

        # app.post('/users', (req, res) => {
        #   var name = req.body.name;
        #   var email = req.body.email;
        #   connection.query("INSERT INTO Users(NAME, EMAIL) VALUES(?,?)", 
        # 		[name, email], (error, resutls, fields) => {
        #     if (error) throw error;
        #     res.json({ok:"true"});
        #   });
        # });

    # 유저 수정
    def update_member(self,email,passwd,nickname,phonenumber,address):
        body = {'passwd':passwd, 'nickname': nickname, 
                'phonenumber':phonenumber,"address":address}
        requests.put(self.url +"users/"+email, data=json.dumps(body))
        return 1

    # 유저 탈퇴
    def delete_member(self,email):
        if bool(email):
            api_result = requests.delete(self.url + "users/" + email)
        return api_result

    # 유저 정보
    def select_one_member(self,email):
        if bool(email):
            api_result = requests.get(self.url + "users/" + email)
        return api_result
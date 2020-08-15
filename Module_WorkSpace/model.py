# from store import MemberStore
from resAPI import MemberStore
import domain
class Member_Model:

    def __init__(self):
        self.ms = MemberStore()

    # 이메일, 패스워드 확인
    def login_clear(self,email,passwd):
        result = self.ms.login_ok(email,passwd)
        if not bool(result):
            return 1
        else:
            return 0

    # 이메일 유효성 검사
    def email_Validation_model(self,email):
        return self.ms.email_Validation(email)

    # 멤버 등록
    def insert_member_model(self,entity):
        print("멤버등록",entity)
        return self.ms.insert_member(entity)

    # 멤버 정보
    def member_select_one(self,email):
        return self.ms.select_one_member(email)
    # 로그인 멤버 확인
    def get_select_one_model(self,email,passwd):
        return self.ms.login_ok(email,passwd)

    # 멤버 정보 수정
    def update_member_info(self,email,passwd,nickname,phonenumber,address):
        return self.ms.update_member(email,passwd,nickname,phonenumber,address)
    
    # 멤버 탈퇴
    def delete_member_model(self,email):
        return self.ms.delete_member(email)

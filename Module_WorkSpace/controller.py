import tkinter
from model import Member_Model
from view import MemberView, SignInView, SignUpView, UpdateMember, ClubView, DeleteMember
import domain
import controller
import re

class Member_Controller:
    window = tkinter.Tk()
    cookie_email = ""
    def __init__(self):  
        self.member_view = MemberView(Member_Controller.window)
        self.member_model = Member_Model()
        self.siv = SignInView(Member_Controller.window)
        self.suv = SignUpView(Member_Controller.window)
        self.um = UpdateMember(Member_Controller.window)
        self.cv = ClubView(Member_Controller.window)
        self.dm = DeleteMember(Member_Controller.window)
        
    # 프로그램 실행

    def run(self):
        print("프로그램 실행")
        self.window.title("클럽 관리 프로그램")
        self.window.geometry("300x250-800+100")    
        self.window.resizable(False, False)
        self.member_view.main_title()
        # 로그인 버튼
        self.siv.sign_in_button(self.window)
        # 회원가입 버튼
        self.suv.sign_up_button(self.window)
         # 마이페이지 버튼
        self.um.mypage_button(self.window)
        # 로그아웃 버튼
        self.um.log_out_button(self.window)
        # 회원 탈퇴 버튼
        self.dm.delete_member_button(self.window)
        # # 클럽 메뉴 버튼
        # self.cv.club_button(self.window)

    
    # 프로그램 종료
    def close_window(self):
        self.window.mainloop()
    
    # 쿠키 값 없애기
    def delete_cookie(self):
        controller.Member_Controller.cookie_email = None

    # 회원가입 정보 받아오고 가입 및 오류
    def sign_up_info(self,email,passwd,name,nickname,phonenumber,birthday,address):
        print("회원가입 정보 받아오고 가입 및 오류")
        d = domain.MemberDomain(email,passwd,name,nickname,phonenumber,birthday,address)
        print("d의정보",d.u_email,d.u_passwd,d.u_nick_name,d.u_phone_number,d.u_birthday,d.u_address)
        mm = self.member_model.email_Validation_model(d.u_email)
        print("mm의 결과",mm)
        if not bool(mm):
            result = self.member_model.insert_member_model(d)
            if bool(result):
                self.suv.sign_up_success()
        else:
            self.suv.sign_up_false()
    
    # 로그인 정보 받아오기
    def sign_in_info(self,email,passwd):
        d = domain.LoginMemberDomain(email,passwd)
        self.mm = self.member_model.login_clear(d.email,d.passwd)
        if self.mm == 0:
            self.siv.login_success()
            self.result = self.member_model.get_select_one_model(d.email,d.passwd)
            print("result",self.result)
            Member_Controller.cookie_email = self.result
            print("cookieemail", Member_Controller.cookie_email)
        else:
            self.siv.login_false()

    # 멤버 상세 정보 받아오기
    def detail_member_info(self):
        # self.d = domain.MemberDomain(email,passwd,name,nickname,phonenumber,birthday,address)
        # cm = Member_Controller.cookie_email  
        # print("cm",cm.get("email"))
        if bool(cm.get("email")):
            result = self.member_model.member_select_one(cm.get("email"))
            print("result",result)
            d = domain.MemberDomain(result["email"],result["passwd"],result["name"],result["nickname"],result["phonenumber"],result["birthday"],result["address"])
            # self.um.my_update_detail_info(self.d.u_email,self.d.u_passwd,self.d.u_name,self.d.u_nick_name,self.d.u_phone_number,self.d.u_birthday,self.d.u_address,self.d.u_clubid)
            return d
        else:
            pass
        
    # 회원 정보 수정
    def update_info_con(self,email,passwd,nickname,phonenumber,address):
        d = domain.UpdateDomain(email,passwd,nickname,phonenumber,address)
        print("update Domain", d.email)
        result = self.member_model.update_member_info(d.email,d.passwd,d.nickname,d.phonenumber,d.address)
        print("회원정보수정Controller",result)
        if result == 1:
            self.um.my_update_message()
        else:
            pass

    # 회원 탈퇴
    def delete_info_controller(self):
        cm = Member_Controller.cookie_email
        cm_var = cm["email"]
        print("회원탈퇴 CONTROLLER", cm_var)
        if bool(cm_var):
            # 가입한 클럽 삭제(클럽멤버십)
            result = self.member_model.drop_clubmembership_model(cm_var)
            if result == 1:
                # 생성한 클럽 삭제
                result = self.member_model.drop_travelclub_model(cm_var)
                print("회원탈퇴 result",result)
                if result == 1:
                    # 멤버 삭제
                    result = self.member_model.delete_member_model(cm_var)
                    if result == 1:
                        pass
                        # self.dm.drop_club_message()
                    else:
                        pass
                else:
                    pass
            else:
                pass
            return 1
        else:
            pass
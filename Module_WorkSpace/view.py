import tkinter
import tkinter.font as tkfont   
import tkinter.messagebox
import tkinter.ttk
from domain import MemberDomain
import controller
import model
import re

class ViewInit:
    def __init__(self,window):
        window.geometry("500x400")
        self.frame = tkinter.Frame(window, width=500,height=400)
        self.frame.pack()
        
        # self.frame1 = tkinter.Frame(window)
        # self.frame1.pack()
        # self.frame2 = tkinter.Frame(window)
        # self.frame2.pack()
        # self.frame3 = tkinter.Frame(window)
        # self.frame3.pack()
        

class MemberView:
    
    def __init__(self,window):
        self.view = ViewInit(window)
        
    # 메인 화면 큰제목
    def main_title(self):
        self.h1 = tkinter.Label(self.view.frame, text="Travel Club Manager", font="bold",height=7,bg="#FFE4C4", relief="solid",width=480 )
        self.h1.pack()

class SignInView:
    def __init__(self,window):
        self.view = ViewInit(window)
        
   
    # 로그인 버튼
    def sign_in_button(self,window):
        print("로그인") 
        signin = tkinter.Button(self.view.frame, text="로그인", command= lambda : self.input_login_info(window))
        signin.grid(row=1,column=0)

    # 로그인할 때 입력 정보
    def input_login_info(self,window):
        print("로그인할 때 입력 정보")
        self.toplevel = tkinter.Toplevel(window)
        self.toplevel.geometry("300x100")
        self.l_email = tkinter.Label(self.toplevel, text="이메일")
        self.e_email = tkinter.Entry(self.toplevel)
        self.l_passwd = tkinter.Label(self.toplevel, text="패스워드")
        self.e_passwd = tkinter.Entry(self.toplevel)
        self.ok_button = tkinter.Button(self.toplevel, text="확인", command=self.is_exist_view)
        self.l_email.grid(row=0,column=0)
        self.e_email.grid(row=0,column=1)
        self.l_passwd.grid(row=1,column=0)
        self.e_passwd.grid(row=1,column=1)
        self.ok_button.grid(row=2,column=1)
    
    # 로그인 정보 검증
    def is_exist_view(self):
        self.mc = controller.Member_Controller()
        # self.e = self.e_email.get()
        # self.p = self.e_passwd.get()
        self.mc.sign_in_info(self.e_email.get(),self.e_passwd.get())
        self.toplevel.destroy()
    
    # 로그인 성공
    def login_success(self):
        tkinter.messagebox.showinfo("로그인","로그인 성공") 
    # 로그인 실패
    def login_false(self):
        tkinter.messagebox.showwarning("로그인","입력하신 정보와 일치하는 회원이 없습니다. 다시 입력해주세요.") 
    
    

class SignUpView:
    def __init__(self,window):
        self.view = ViewInit(window)
    
    # 회원가입 버튼
    def sign_up_button(self,window):
        print("회원가입")
        signup = tkinter.Button(self.view.frame, text="회원가입", command= lambda : self.input_entity(window))
        signup.grid(row=1,column=1)

    # 회원가입할 때 입력 정보
    def input_entity(self,window):
        print("회원가입할 때 입력 정보")
        self.toplevel = tkinter.Toplevel(window)
        self.toplevel.geometry("600x200")
        self.l_email = tkinter.Label(self.toplevel, text="이메일: ")
        self.l_email.grid(row=0,column=0)
        self.e_email = tkinter.Entry(self.toplevel)
        self.e_email.grid(row=0,column=1)
        self.l_email1 = tkinter.Label(self.toplevel, text="@")
        self.l_email1.grid(row=0,column=2)
        self.e_email1 = tkinter.Entry(self.toplevel)
        self.e_email1.grid(row=0,column=3)

        self.l_passwd = tkinter.Label(self.toplevel, text="패스워드: ")
        self.l_passwd.grid(row=1,column=0)
        self.e_passwd = tkinter.Entry(self.toplevel)
        self.e_passwd.grid(row=1,column=1)

        self.l_name = tkinter.Label(self.toplevel, text="이름: ")
        self.l_name.grid(row=2,column=0)
        self.e_name = tkinter.Entry(self.toplevel)
        self.e_name.grid(row=2,column=1)

        self.l_nick_name = tkinter.Label(self.toplevel, text="닉네임: ")
        self.l_nick_name.grid(row=3,column=0)
        self.e_nick_name = tkinter.Entry(self.toplevel)
        self.e_nick_name.grid(row=3,column=1)

        self.l_phone_number = tkinter.Label(self.toplevel, text="전화번호: ")
        self.l_phone_number.grid(row=4,column=0)
        self.e_phone_number = tkinter.Entry(self.toplevel)
        self.e_phone_number.grid(row=4,column=1)
        self.l_phone_number1 = tkinter.Label(self.toplevel, text="-")
        self.l_phone_number1.grid(row=4,column=2)
        self.e_phone_number1 = tkinter.Entry(self.toplevel)
        self.e_phone_number1.grid(row=4,column=3)
        self.l_phone_number2 = tkinter.Label(self.toplevel,text="-")
        self.l_phone_number2.grid(row=4,column=4)
        self.e_phone_number2 = tkinter.Entry(self.toplevel)
        self.e_phone_number2.grid(row=4,column=5)

        self.l_birth_day = tkinter.Label(self.toplevel, text="생년월일: ")
        self.l_birth_day.grid(row=5,column=0)
        self.e_birth_day = tkinter.Entry(self.toplevel)
        self.e_birth_day.grid(row=5,column=1)
        self.l_birth_day1 = tkinter.Label(self.toplevel,text="-")
        self.l_birth_day1.grid(row=5,column=2)
        self.e_birth_day1 = tkinter.Entry(self.toplevel)
        self.e_birth_day1.grid(row=5,column=3)

        self.l_address = tkinter.Label(self.toplevel, text="거주지: ")
        self.l_address.grid(row=6,column=0)
        self.e_address = tkinter.Entry(self.toplevel)
        self.e_address.grid(row=6,column=1)

        self.ok_button = tkinter.Button(self.toplevel, text="확인",command = self.insert_ok, width=10)
        self.ok_button.grid(row=7,column=0)
        self.cancle_button = tkinter.Button(self.toplevel, text="취소", command= self.insert_cancle,width=10)
        self.cancle_button.grid(row=7,column=1, sticky="w")


    # 확인버튼
    def insert_ok(self):
        num = 0
         # 이메일 정규 표현식
        self.email_re = re.compile('^[a-zA-Z0-9+-_.]')
        self.email_match = self.email_re.match(self.e_email.get())
        self.email1_re = re.compile('[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$')
        self.email1_match = self.email1_re.match(self.e_email1.get())

        # 전화번호 정규 표현식
        self.phone_re = re.compile('010')#'\\d{3}'
        self.phone_match = self.phone_re.match(self.e_phone_number.get())
        self.phone1_re = re.compile('\\d{4}')
        self.phone1_match = self.phone1_re.match(self.e_phone_number1.get())
        self.phone2_re = re.compile('\\d{4}')
        self.phone2_match = self.phone2_re.match(self.e_phone_number2.get())

        # 생일 정규 표현식
        self.birth_day_re = re.compile('\\d{6}')
        self.birth_day_match = self.birth_day_re.match(self.e_birth_day.get())
        self.birty_day1_re = re.compile('\\d{7}')
        self.birth_day1_match = self.birty_day1_re.match(self.e_birth_day1.get())

        if bool(self.email_match) and bool(self.email1_match):
            num += 1
            email_result = self.e_email.get()+'@'+self.e_email1.get()
            print(email_result)
        if bool(self.phone_match) and bool(self.phone1_match) and bool(self.phone2_match):
            num += 10
            phone_result = self.e_phone_number.get()+'-'+self.e_phone_number1.get()+'-'+self.e_phone_number2.get()
            print(phone_result)
        if bool(self.birth_day_match) and bool(self.birth_day1_match):
            num += 20
            birth_day_result = self.e_birth_day.get()+'-'+self.e_birth_day1.get()
            print(birth_day_result)
   
        print("확인버튼")
        if num == 31:
            self.mc = controller.Member_Controller()
            num = 0
            # self.mc.sign_up_info(self.e_email.get(),self.e_passwd.get(),self.e_name.get(),self.e_nick_name.get(),self.e_phone_number.get(),self.e_birth_day.get(),self.e_address.get())
            self.mc.sign_up_info(email_result,self.e_passwd.get(),self.e_name.get(),self.e_nick_name.get(),phone_result,birth_day_result,self.e_address.get())
        elif num == 1:
            tkinter.messagebox.showwarning("정규표현식","전화번호,생년월일과 나머지 정보를 다시 입력하세요.")
        elif num == 11:
            tkinter.messagebox.showwarning("정규표현식","생년월일과 나머지 정보를 입력하세요.")
        elif num == 21:
            tkinter.messagebox.showwarning("정규표현식","전화번호와 나머지 정보를 입력하세요.")
        elif num == 30:
            tkinter.messagebox.showwarning("정규표현식","이메일과 나머지 정보를 다시 입력하세요.")
        else:
            tkinter.messagebox.showwarning("정규표현식","정보를 모두  입력하세요.")


       
    # 취소버튼
    def insert_cancle(self):
        
        self.toplevel.destroy()
    
    # 회원가입 성공
    def sign_up_success(self):
        tkinter.messagebox.showinfo("회원가입","회원가입 성공")
        # self.toplevel.destroy()   

    # 회원가입 실패
    def sign_up_false(self):
        tkinter.messagebox.showwarning("회원가입","이미 존재하는 회원입니다.")
        # self.toplevel.destroy()

class UpdateMember:
    def __init__(self,window):
        self.view = ViewInit(window)
    
    # 마이페이지 버튼
    def mypage_button(self,window):
        self.update_button = tkinter.Button(self.view.frame,text="마이페이지", command=lambda : self.update_info(window))
        self.update_button.grid(row=1,column=2)

    # 로그아웃 버튼
    def log_out_button(self,window):
        self.logout_button = tkinter.Button(self.view.frame,text="로그아웃", command=self.log_out)
        self.logout_button.grid(row=1,column=3)

    # 로그아웃
    def log_out(self):
        cm = controller.Member_Controller()
        cmc = controller.Member_Controller.cookie_email
        if bool(cmc):
            cm.delete_cookie()
            tkinter.messagebox.showinfo("TravelClub","로그아웃 완료")
        else:
            tkinter.messagebox.showwarning("TravelClub","로그인이 되어있지 않습니다.")

        

    # 마이페이지 정보
    def update_info(self,window):
        cm = controller.Member_Controller()
        cmc = controller.Member_Controller.cookie_email
        if bool(cmc):
            result = cm.detail_member_info()
            print("result",result)
            self.toplevel = tkinter.Toplevel(window)
            self.toplevel.geometry("300x250")
            self.l_email = tkinter.Label(self.toplevel, text="이메일: ")
            self.e_email = tkinter.Entry(self.toplevel)
            self.l_passwd = tkinter.Label(self.toplevel, text="패스워드: ")
            self.e_passwd = tkinter.Entry(self.toplevel)
            self.l_name = tkinter.Label(self.toplevel, text="이름: ")
            self.e_name = tkinter.Entry(self.toplevel)
            self.l_nick_name = tkinter.Label(self.toplevel, text="닉네임: ")
            self.e_nick_name = tkinter.Entry(self.toplevel)
            self.l_phone_number = tkinter.Label(self.toplevel, text="전화번호: ")
            self.e_phone_number = tkinter.Entry(self.toplevel)
            self.l_birth_day = tkinter.Label(self.toplevel, text="생년월일: ")
            self.e_birth_day = tkinter.Entry(self.toplevel)
            self.l_address = tkinter.Label(self.toplevel, text="거주지: ")
            self.e_address = tkinter.Entry(self.toplevel)
            self.l_clubid = tkinter.Label(self.toplevel, text="가입한 클럽: ")
            self.e_clubid = tkinter.Entry(self.toplevel)
            
            self.ok_button = tkinter.Button(self.toplevel, text="수정", command = self.my_update_button ,width=10)
            self.cancle_button = tkinter.Button(self.toplevel, text="취소", command=self.cancle_func ,width=10)
            
            self.l_email.grid(row=0,column=0)
            self.e_email.grid(row=0,column=1)
            self.l_passwd.grid(row=1,column=0)
            self.e_passwd.grid(row=1,column=1)
            self.l_name.grid(row=2,column=0)
            self.e_name.grid(row=2,column=1)
            self.l_nick_name.grid(row=3,column=0)
            self.e_nick_name.grid(row=3,column=1)
            self.l_phone_number.grid(row=4,column=0)
            self.e_phone_number.grid(row=4,column=1)
            self.l_birth_day.grid(row=5,column=0)
            self.e_birth_day.grid(row=5,column=1)
            self.l_address.grid(row=6,column=0)
            self.e_address.grid(row=6,column=1)
            self.l_clubid.grid(row=7,column=0)
            self.e_clubid.grid(row=7,column=1)

            self.ok_button.grid(row=8,column=0, sticky="w")
            self.cancle_button.grid(row=8,column=1, sticky="w")


            self.e_email.insert(0,result.u_email)
            self.e_email.configure(state="readonly")
            self.e_passwd.insert(0,result.u_passwd)
            self.e_name.insert(0,result.u_name)
            self.e_name.configure(state="readonly")
            self.e_nick_name.insert(0,result.u_nick_name)
            self.e_phone_number.insert(0,result.u_phone_number)
            self.e_birth_day.insert(0,result.u_birthday)
            self.e_birth_day.configure(state="readonly")
            self.e_address.insert(0,result.u_address)
            self.e_clubid.configure(state="readonly")
            # if not bool(result.u_clubid):
            #     self.e_clubid.configure(state="readonly")
            # else:
            #     self.e_clubid.insert(0,result.u_clubid)
            #     self.e_clubid.configure(state="readonly")
        else:
            self.login_plz()

    # 로그인 하세요
    def login_plz(self):
        tkinter.messagebox.showwarning("TravelClub","로그인 해주세요")

    # 마이페이지 수정 버튼
    def my_update_button(self):
        cm = controller.Member_Controller()
        cm.update_info_con(self.e_email.get(),self.e_passwd.get(),self.e_nick_name.get(),self.e_phone_number.get(),self.e_address.get())
    # 마이페이지 취소 버튼 
    def cancle_func(self):
        self.toplevel.destroy()

    # 마이페이지 수정 완료
    def my_update_message(self):
         tkinter.messagebox.showinfo("마이페이지","수정이 완료되었습니다.")

    login_plz
class DeleteMember:
    def __init__(self,window):
        self.view = ViewInit(window)

    # 회원 탈퇴 버튼
    def delete_member_button(self,window):
        self.member_delete_button_message = tkinter.Button(self.view.frame,text="회원탈퇴" , command=lambda : self.delete_member(window))
        self.member_delete_button_message.grid(row=1,column=4)
        
    # 회원 탈퇴 폼
    def delete_member(self,window):
        print("회원 탈퇴 폼 접근")
        cm = controller.Member_Controller()
        cmc = cm.cookie_email
        print("회원탈퇴폼 cmc",cmc)
        # toplevel = tkinter.Toplevel(window)
        if bool(cmc):
            toplevel = tkinter.Toplevel(window)
            self.delete_label = tkinter.Label(toplevel, text= "확인 버튼을 누르시면 계정이 생성한 클럽도 같이 삭제 됩니다. 정말 탈퇴하시겠습니까?")
            self.delete_button = tkinter.Button(toplevel, text="확인", command=self.delete_yn)
            self.delete_cancle_button = tkinter.Button(toplevel, text="취소", command=lambda : self.delete_cancle(toplevel))
            self.delete_label.pack()
            self.delete_button.pack()
            self.delete_cancle_button.pack()
        else:
            self.login_plz()

        # self.delete_button = tkinter.messagebox.askyesno("회원탈퇴","확인 버튼을 누르시면 계정이 생성한 클럽도 같이 삭제 됩니다. 정말 탈퇴하시겠습니까?")
        # if self.delete_button == "yes":
        #     if bool(cmc["email"]):
        #         print("회원탈퇴폼 if문")
        #         cm.delete_info_controller()
        #     else:
        #         self.login_plz()
        # else:
        #     pass
            # self.login_plz()
    # 회원탈퇴 확인 처리
    def delete_yn(self):
        cm = controller.Member_Controller()
        result = cm.delete_info_controller()
        if result == 1:
            self.drop_club_message()
        else:
            self.drop_club_fale_message()
    
    # 회원탈퇴 취소 버튼
    def delete_cancle(self,toplevel):
        toplevel.destroy()

    # 로그인 하세요
    def login_plz(self):
        tkinter.messagebox.showwarning("TravelClub","로그인 해주세요")

    # 회원탈퇴 메시지
    def drop_club_message(self):
        tkinter.messagebox.showinfo("TravelClub","회원탈퇴 완료.")
    
    # 회원탈퇴 실패 메시지
    def drop_club_fale_message(self):
        tkinter.messagebox.showinfo("TravelClub","회원탈퇴 실패.")


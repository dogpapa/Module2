# 청일점 프로젝트
# travel community & travel club

# 명세서
# IAM
	* [역할/codedeploy]
	- Module2-service-code-deploy
	* [정책]
	- Module2-s3-policy
	* [역할/ec2]
	- Module2-ec2-code-deploy
	* [역할/ec2]
	- Module2-cloud-watch
# EC2
	- module2-ec2-app-server
# S3
	- module2-bucket

# Load Balancer
	- Module2-ec2-LB

# 대상그룹
	- Module2-grp
# CloudFront
    * 추후 완성 및 배포 후 수정 예정*
	[Origin Domain Name]
	- module2-bucket.s3.amazonaws.com
	[Origin Path]
	- / (defalut)
# Auto Scaling
	- Module2-ec2-AScaling
# 시작 템플릿
	- Module2-ec2-template
# AMI
	- Module2-ec2-image

# Code Deploy
	* [애플리케이션]
	- Module2-code-deploy
	* [배포그룹]
	- Module2-code-deploy-grp

# Cloud Watch
	* [주제1]
	- Default_CloudWatch_Alarms_Topic-Module2
	* [경보이름]
	- Module2-CPU-Alarm(i-00927b6fc6d42b998)
	* [주제2]
	- Default_CloudWatch_Alarms_Topic-Module2-1
	* [경보이름]
	- Module2-CPU-Alarm-1(i-034f7c8c04308efb8)

# restAPI

|함수 |http|query|sql 결과값 가져오는 것|설명|
|------|-----|-----|----|------------------|
|login_ok|GET|SELECT *ONE*|fetchone()|이메일 페스워드 확인|
|email_Validation|GET|SELECT *ONE*|fetchone()|이메일 검증|
|insert_member|POST|INSERT|-|유저 등록|
|update_member|POST|UPDATE|-|유저 수정|
|delete_member|DELETE|DELETE|-|유저 탈퇴|
|select_one_member|GET|SELECT *ONE*|fetchone()|유저정보|
|delete_all_club_membership|GET|DELETE|-|회원탈퇴 클럽멤버십 삭제|
|drop_club_all|DELETE|DELETE|-|생성한 클럽 전체 탈퇴|
|close|GET|CONNECTION.RELEASE|-|error발생시 수행되던 것. 연결 끊기|
|추가적으로 전체 목록의 경우|GET|SELECT *ALL*|fetchall()|-|

<span style="color:red">
*기존 db코드가 dict형식으로 불러왔기 때문에 송신(resAPI)과 수신(index.js)은 json형태로 주고 받도록 한다.*
</span>
# 참고 blog
- https://twpower.github.io/124-python-requests-usage
- https://velog.io/@wimes/node.js-REST-API-%EC%84%9C%EB%B2%84-%EB%A7%8C%EB%93%A4%EA%B8%B0-3.-%EB%A7%8C%EB%93%A4%EA%B8%B0
- https://requests.readthedocs.io/en/latest/user/quickstart/#passing-parameters-in-urls
- https://my-devblog.tistory.com/27


# Node.js 작성시 참고사항
1. 직접 url창에 /users, /users/1 과 같이 입력하는 대신 python에서 url창에 원하는 형식의 url을 직접 호출한다. 
    - (/users등으로 기존과 동일하게 작성)
    - 이를 통해 해당 app.get() 함수가 실행되도록 조작됩니다. 
    - 따라서 /이후의 항목에 따라 알맞은 app.get/post/delete/put()을 추가 및 조작해주세요~

2.  req, res
    - rea = request(송신) / res = response(수신)
    - 따라서 송신과 수신은 json형태로 주고 받도록 한다.
     
3. entity로 넘겨줄 때 vs email로 넘길 때
    - entity는 body로, email은 param으로 해체하는 듯 합니다.
    - 사실 뇌피셜이긴 한데...ㅠㅠㅠ일단 강사님 코드는 entity는 body, id는 param으로 해체하셔서 그렇게 넘깁니다.

4.  users => users 그대로 사용

|변수 | 값|비고|
|-----|--------|-----|
|table 명|users|url뒤에 users로 호출함|
|id => email|:email처럼 사용하기 |primary key |
|기타 삭제 OR UPDATE|URL 뒤에 



5. req와 res 규칙

|함수 |http|query|sql 결과값 가져오는 것|
|------|-----|-----|----|
|login_ok|GET|SELECT *ONE*|fetchone()|
|email_Validation|GET|SELECT *ONE*|fetchone()|
|insert_member|POST|INSERT|-|
|update_member|POST|UPDATE|-|
|delete_member|GET|DELETE|-|
|select_one_member|GET|SELECT *ONE*|fetchone()|
|추가적으로 전체 목록의 경우|GET|SELECT *ALL*|fetchall()|
"""
[ 실습 1 ]
1. dicLab3.py 라는 소스를 생성한다.
2. 다음 내용으로 구성되는 딕셔너리를 하나 생성한다.
   키 : 우리 팀원 이름
   값 : 다음 내용으로 구성되는 딕셔너리
       키 : 나이, 거주지역, 메일주소, 취미,  좋아하는음식
       값 : 실제값 (^^)
이름 : 임호진 , 나이: 27, 거주지: 서울 노원구, 메일주소: imhojin1104@naver.com, 취미: 역사공부, 좋아하는 음식: 닭죽
이름 : 이준영, 나이: 31, 거주지: 서울시 강남구, 메일주소: joonzzang3@naver.com, 취미: 여행,게임, 좋아하는 음식: 초밥
이름 : 정승희, 나이: 35, 거주지: 경기도 용인시, 메일주소: sseung15@gmail.com, 취미: 커피, 좋아하는 음식: 떡볶이

3. 모든 팀원들의 이름과 정보를 출력해 본다.(출력시 f 문자열을 사용한다.)
    이름      나이    거주지역    메일주소   [취미 , … ]   [좋아하는 음식, …]
"""
myTeam = dict(zip(['이름','나이','거주지역','메일주소','취미','좋아하는음식'],
                  ['임호진',27,'서울시 노원구','imhojin1104@naver.com',['역사공부'],['닭죽']]))
vallist = myTeam.values()
for val in vallist:
    print(f'{val} ', end='')
print('')

myTeam = dict(zip(['이름','나이','거주지역','메일주소','취미','좋아하는음식'],
                  ['이준영', 31, '서울시 강남구', 'joonzzang3@naver.com', ['여행','게임'], ['초밥']]))
vallist = myTeam.values()
for val in vallist:
    print(f'{val} ', end='')
print('')
myTeam = dict(zip(['이름','나이','거주지역','메일주소','취미','좋아하는음식'],
                  ['정승희', 35, '경기도 용인시', 'sseung15@gmail.com', ['커피'], ['떡볶이']]))
vallist = myTeam.values()
for val in vallist:
    print(f'{val} ', end='')
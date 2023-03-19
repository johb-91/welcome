# print(abs(-5)) # 절대값을 출력함
# print(pow(4, 2)) # 4의 2승 = 4x4 = 16
# print(max(5,12)) # 두 개의 값 중 큰 값
# print(min(5,12)) # 두 개의 값 중 작은 값
# print(round(3.14))
# print(round(4.99))

#-------------------------------------------------------
# from random import *

# print(random()* 10) #0~10까지 랜덤
# print(int(random()*10))
# print(randrange(1,45))
# print(randint(1,45))

# print("오프라인 스터디 모임 날짜는 매월 " , randint(4,28) , "일로 선정되었습니다.")
# print("오프라인 스터디 모임 날짜는 매월 " , randint(4,28) , "일로 선정되었습니다.")
# print("오프라인 스터디 모임 날짜는 매월 " , randint(4,28) , "일로 선정되었습니다.")


#---------------------------------------------------
# jumin = "991020-1234567"

# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2]) # 0부터 2 직전까지
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])

# print("생년월일 :" + jumin[0:6]) #처음 문자부터 6번째 직전까지 즉, 0번째 ~ 5번째글자
# print("뒤 7자리 :" + jumin[7:14])

# print("뒤 7자리(뒤에부터) " +jumin[-7:]) #맨 뒤에서 7번째부터 끝까지

# python = "Python is amazing"
# print(python.lower())
# print(python.upper())

# print(python[0].isupper())
# print(len(python))

# print(python.replace("Python", "Java"))


# index = python.index("n")
# print(index)
# print(python.index("n", index+1))

# print(python.find("Java"))
# # print(python.index("Java"))

# print(python.count("n"))

#------------------------------------------------------------
#
# 방법 1
# print("나는 %d살 입니다." % 20)
# # print("나는 %s을 좋아해요." % "파이썬")
# # print("Apple 은 %c로 시작해요" %"A")

# # # %d 는 정수, %s 는 문장, %c는 하나의 문자
# # print("나는 %s살 입니다." % 20)
# # print("나는 %s색과 %s색을 좋아해요." %("파란", "빨간"))

# # # 방법 2
# # print("나는 {}살 입니다." .format(20))
# # print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
# # print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간"))
# # print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))

# # #방법 3
# # print("나는 {age}살이며, {color}색을 좋아해요." .format(age=20, color ="빨간"))
# # print("나는 {age}살이며, {color}색을 좋아해요." .format(color ="빨간", age=20))

# # #방법 4(v3.6 이상)
# # age=20
# # color="빨간"
# # print(f"나는 {age}살이며, {color}색을 좋아해요.")

#4-4강까지 끝났고, 4-5강부터 시작하면 됨.

#4-5강 시작
#print("백문이 불여일견 \n백견이 불여일타")
# 저는 "나도코딩" 입니다.
#print("저는 '나도코딩' 입니다.")
#print("저는 \"나도코딩\" 입니다.")

# \\: 문장 내에서 \
#print("c:\\Users\\user\\OneDrive\\바탕 화면\\PythonWorksSpace")

#\r :커서를 맨 앞으로 이동
#print("Red Apple\rPine")

#\b : 백스페이스 (한 글자 삭제)
#print("Redd\bApple")

#\t : 탭
#print("Red\tApple")

#Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.


# url = "http://naver.com"
# my_str=url.replace("http://", "") #조건 1
# my_str=my_str[:my_str.index(".")] #조건 3

# password = my_str[0:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

# print("{0}의 비밀번호는 {1} 입니다." .format(url, password))

#리스트 []
# 지하철 칸별로 10명, 20명, 30명이 있다
# subway =10
# subway2 =20
# subway = 30

# subway =[10,20,30]
# print(subway)

# subway=["유재석", "조세호", "박명수"]
# print(subway)

# #조세호씨가 몇 번째 칸에 타고 있는가?
# print(subway.index("조세호"))

# #하하씨가 다음 정류장에서 다음 칸에 탐
# subway.append("하하") #append 는 항상 함수 맨 뒤에 추가됨
# print(subway)

# #정형돈씨를 유재석 / 조세호 사이에 태워봄
# subway.insert(1, "정형돈")
# print(subway)

# #지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)

# # print(subway.pop())
# # print(subway)

# # print(subway.pop())
# # print(subway)

# # 같은 이름의 사람이 몇 명 있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# 정렬도 가능
# num_list =[5,2,4,3,1]
# num_list.sort()
# print(num_list)

# # 순서 뒤집기 가능
# num_list.reverse()
# print(num_list)

# # 모두 지우기
# num_list.clear()
# print(num_list)

#다양한 자료형 함께 사용
# mix_list=["조세호", 20, True]
# num_list =[5,2,4,3,1]
# #print(mix_list)

# #리스트 확장
# num_list.extend(mix_list)
# print(num_list)

#---------------------------------------------------------
#5-2강 시작

# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# print(cabinet.get(100))
# # print(cabinet.get(5)) #get은 error 후 프로그램 종료하지 않음.
# print(cabinet.get(4,"사용 가능"))

# print(3 in cabinet) #True
# print(100 in cabinet) #False



# cabinet ={"A-3":"유재석", "B-100" : "김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# # 새 손님
# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"

# print(cabinet)


# # 간 손님
# del cabinet["A-3"]
# print(cabinet)

# #key 들만 출력
# print(cabinet.keys())

# #value 들만 출력
# print(cabinet.values())


# #key, value 쌍으로 출력
# print(cabinet.items())

# #목욕탕 폐점
# cabinet.clear()
# print(cabinet)

# menu =("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])


# #menu.add("생선까스")예시처럼 값을 추가하거나 변경하는 것은 불가함.

# # name ="김종국"
# # age =20
# # hobby = "코딩"
# # print(name,age,hobby)


# name, age, hobby = ("김종국", 20, "코딩")
# print(name, age, hobby)


#집합(set)
#중복 안됨, 순서가 없음

# my_set ={1,2,3,3,3}
# print(my_set)

# java={"유재석", "김태호", "양세형"}
# python=set(["유재석", "박명수"])

# #교집합 (java와 python을 모두 할 수 있는 개발자)

# print(java&python)
# print(java.intersection(python))

# #합집합(java도 할 수 있거나 python을 할 수 있는 개발자)
# print(java | python)
# print(java.union(python))

# # 차집합(java는 할 줄 알지만 python은 할줄 모르는 개발자)
# print(java-python)
# print(java.difference(python))

# #python 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)

# #java를 잊었어요
# java.remove("김태호")
# print(java)


# #자료 구조의 변경
# menu = {"커피", "우유",  "주스"}
# print(menu, type(menu))

# menu=list(menu)
# print(menu, type(menu))

# menu=tuple(menu)
# print(menu, type(menu))

# menu=set(menu)
# print(menu, type(menu))


#Quiz4 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.

# from random import *
# users=range(1,21) #1 부터 20까지 숫자를 생성
# # print(type(users))
# users=list(users)
# # print(type(users))

# shuffle(users)
# print(users)

# winners = sample(users, 4) #4명 중에서 1명은 치킨, 3명은 커피

# print(" --당첨자 발표--")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))

# print("-- 축하합니다 --")

#-----------------------------------------------6-1강 시작

# weather = input("오늘 날씨는 어때요?")
# if weather == "비" or weather =="눈" :
#     print("우산을 챙기세요")
# elif weather == "미세먼지" :
#     print("마스크를 챙기세요")
# else :
#     print("오늘은 준비물이 필요 없어요.")


# temp =int(input("기온은 어때요?"))
# if 30<= temp :
#     print("너무 더워요. 나가지 마세요")
# elif 10<=temp and temp<30:
#     print("괜찮은 날씨에요")
# elif 0<=temp and temp<10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요")


# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")


# starbucks = ["아이언맨", "토르","그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))


# while
customer = "토르"
index = 5
while index >= 1:
  print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer, index))
  index -= 1
if index == 0:
  print(" 커피는 폐기처분 되었습니다.")

  ######################################################## 6-3강 진행중
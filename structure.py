import random


'''

게임 시작 화면
    선택지 : 시작 , 종료, 후원

게임 시작하고 배경 스토리 설명 (교문 ~ 교실)

랜덤한 첫 히로인 조우

하루 일과 반복 (1주일 주말 포함X 5일)
    랜덤 남성 3명과 대화
    하교 시 방문할 곳 선택

엔딩

'''

#이름, 호감도, 대사(상황 묘사, 대사, 선택지(대사, 호감도 증감, 대사(0)or상황묘사(1), 이어지는 대사))
att_males = [["손만민", 0, [("이 긴 갈색 머리카락을 휘날리며 다가온다", "안녕하세요.", ("인사한다", 2, 1, "이 밝게 웃어준다"), ("무시한다", -2, 1, "은 어색한 웃음을 보이고 자리로 돌아간다")),
                         ()]], 
             ["죄준연", 0, [("이 민트색의 머리를 양갈래로 묶은채 다가온다", "안녕", ("인사한다", 2, 0, "ㅋ"), ("경멸한다", 0, 1, "도 같이 째려본다"))]]]
enc_male = 0
chat_cho = 0

def chat(day):
    print(enc_male[0] + enc_male[2][day][0])
    print(enc_male[0] + " : " + enc_male[2][day][1])
    chat_cho = int(input(f"\n 1.{enc_male[2][day][2][0]}\n 2.{enc_male[2][day][3][0]}\n"))
    if enc_male[2][day][chat_cho+1][2] == 0:
        print(enc_male[0] + " : " + enc_male[2][day][chat_cho+1][3] + f" [호감도 : {enc_male[2][day][chat_cho+1][1]}]")
    elif enc_male[2][0][chat_cho+1][2] == 1:
        print(enc_male[0] + enc_male[2][day][chat_cho+1][3] + f" [호감도 : {enc_male[2][day][chat_cho+1][1]}]")
    else:
        print("!")

print("박태건 미연시")
st_cho = input("시작 or 종료")
if st_cho == "종료":
    print("종료")
else:
    print("나는 박태건. 오늘 미래산업과학고등학교로 전학을 오게되었다. ~~ (배경 스토리)")
    for cur_day in range(0, 5):
        for meet_count in range(0, 2):
            enc_male = att_males[random.randint(0, 1)]
            chat(cur_day)
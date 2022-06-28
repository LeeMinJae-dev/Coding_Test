def studentDataProgram():
    profile = dict()

    while 1:
        selectNum = input("1.학생 저장하기\n2. 학생 조회하기\n0. 종료\n")
        # 원래 코드 보면 a라고 변수이름을 지정했던데 변수이름은 for문에 들어가는 i를 제외하고는
        # 항상 의미가 담긴 이름을 지어야 나중에 코드 볼때 안 헷갈림

        if selectNum == '1':
            name = input("학생의 이름을 적어주세요\n")
            age = input("학생의 나이를 적어주세요\n")
            kg = input("학생의 몸무게를 적어주세요\n")

            profile[name] = [age, kg]
            # 이름을 key로 사용해서 배열로 나이와 키를 저장함

        if selectNum == '2':
            findname = input('학생의 이름을 입력하세요\n')

            if findname in profile:  # 해당 key가 딕셔너리에 있는지를 확인하는 in 함수
                print("학생의 나이는 " + profile[findname][0] + "세 입니다.")
                print("학생의 몸무게는 " + profile[findname][1] + "kg 입니다.\n")
                # 파이썬은 개꿀언어라 굳이 %s이런식으로 사용안하고 위 코드처럼 날로먹어도 됨

            if findname not in profile:
                print("존재하지 않는 학생입니다")
                # 코딩테스트에서는 상관없긴하지만 else 문법은 아예 사용안하는걸 습관화 하는게 좋음
                # else를 사용하면 코드를 보고 직관적으로 어떤 경우에 해당 기능을 실행하는지 헷갈리기 떄문
        if selectNum != '1' and selectNum != '2':
            print("잘못된 메뉴선택입니다")

        if selectNum == '0':
            # 함수 종료는 항상 return으로
            return

studentDataProgram()
# 추가로 띄어쓰기나 줄바꿈 깔끔하게 코드 작성하는것도 습관화 해놔야 나중에 가독성이 좋아서 안헷갈림
# 코드도 글쓴다고 생각하고 의미가 좀 변하거나, if 문 사이는 항상 한칸씩 띄워서 연습하면 좋음
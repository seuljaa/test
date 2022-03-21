import random

def mix_members():
    members = []

    while True:

        members = list(input("이름을 입력해주세요 : ").split())

        if len(members) < 10 or len(members) > 100:
            print('10명 이상 100명 이하의 인원만 가능 합니다.')
            continue
        else:
            break

    num = [6, 10, 11, 12, 15, 16]
    num2 = [0, 5, 10, 15]
    random.shuffle(members)
    i = len(members)
    joe = {}
    seven = 0
    six = 0
    five = 0

    if i % 7 == 0:
        seven = int(i / 7)
        i = 0
    else:
        if i not in num:
            while i not in num:
                seven = seven + 1
                i = i - 7
            if i not in num2:
                while i not in num2:
                    six = six + 1
                    i = i - 6
            if i == 5:
                five = five + 1
                i = i - 5
            if i == 10:
                five = five + 2
                i = i - 10
            if i == 15:
                five = five + 3
                i = i - 15
        else:
            if i % 6 == 0:
                six = six + int(i / 6)
                i = 0
            elif i % 5 == 0:
                five = five + int(i / 5)
                i = 0
            elif i == 11:
                six = six + 1
                five = five + 1
                i = 0
            elif i == 16:
                six = six + 1
                five = five + 2
                i = 0

    for num in range(1, seven + six + five + 1):
        if seven != 0:
            member = []
            seven = seven - 1
            for i in range(0, 7):
                member.append(members.pop(0))
            joe['%d조' % num] = member
            continue

        if six != 0:
            member = []
            six = six - 1
            for i in range(0, 6):
                member.append(members.pop(0))
            joe['%d조' % num] = member
            continue

        if five != 0:
            member = []
            five = five - 1
            for i in range(0, 5):
                member.append(members.pop(0))
            joe['%d조' % num] = member
            continue

    print(joe)
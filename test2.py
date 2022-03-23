
def make_timetable(a_time: list, b_time: list, c_time: list, d_time: list):
    mon_pos = {'10시': [], '11시': [], '12시': [], '13시': [], '14시': [], '15시': [], '16시': [], '17시': []}
    tue_pos = {'10시': [], '11시': [], '12시': [], '13시': [], '14시': [], '15시': [], '16시': [], '17시': []}
    wed_pos = {'10시': [], '11시': [], '12시': [], '13시': [], '14시': [], '15시': [], '16시': [], '17시': []}
    thu_pos = {'10시': [], '11시': [], '12시': [], '13시': [], '14시': [], '15시': [], '16시': [], '17시': []}
    fri_pos = {'10시': [], '11시': [], '12시': [], '13시': [], '14시': [], '15시': [], '16시': [], '17시': []}

    mon_final = {'10시': "", '11시': "", '12시': "", '13시': "", '14시': "", '15시': "", '16시': "", '17시': ""}
    tue_final = {'10시': "", '11시': "", '12시': "", '13시': "", '14시': "", '15시': "", '16시': "", '17시': ""}
    wed_final = {'10시': "", '11시': "", '12시': "", '13시': "", '14시': "", '15시': "", '16시': "", '17시': ""}
    thu_final = {'10시': "", '11시': "", '12시': "", '13시': "", '14시': "", '15시': "", '16시': "", '17시': ""}
    fri_final = {'10시': "", '11시': "", '12시': "", '13시': "", '14시': "", '15시': "", '16시': "", '17시': ""}

    worker = ['a', 'b', 'c', 'd']

    data = []

    for count in range(0, 5):
        a_times = a_time[count]
        days = []
        if ';' in a_times:
            for counts in range(0, len(a_times.split(';'))):
                time = a_times.split(';')[counts].split('~')
                length = range(int(time[0][0:2]), int(time[1][0:2]))
                for i in length:
                    days.append(i)
        else:
            a_times = a_times.split('~')
            length = range(int(a_times[0][0:2]), int(a_times[1][0:2]))
            for i in length:
                days.append(i)
        for day in days:
            if count == 0:
                mon_pos['%d시' % day] = ['a']
            if count == 1:
                tue_pos['%d시' % day] = ['a']
            if count == 2:
                wed_pos['%d시' % day] = ['a']
            if count == 3:
                thu_pos['%d시' % day] = ['a']
            if count == 4:
                fri_pos['%d시' % day] = ['a']

    for count in range(0, 5):
        b_times = b_time[count]
        days = []
        if ';' in b_times:
            for counts in range(0, len(b_times.split(';'))):
                time = b_times.split(';')[counts].split('~')
                length = range(int(time[0][0:2]), int(time[1][0:2]))
                for i in length:
                    days.append(i)
        else:
            b_times = b_times.split('~')
            length = range(int(b_times[0][0:2]), int(b_times[1][0:2]))
            for i in length:
                days.append(i)
        for day in days:
            if count == 0:
                data = mon_pos.get('%d시' % day)
                data.append('b')
                mon_pos['%d시' % day] = data
                data = []
            if count == 1:
                data = tue_pos.get('%d시' % day)
                data.append('b')
                tue_pos['%d시' % day] = data
                data = []
            if count == 2:
                data = wed_pos.get('%d시' % day)
                data.append('b')
                wed_pos['%d시' % day] = data
                data = []
            if count == 3:
                data = thu_pos.get('%d시' % day)
                data.append('b')
                thu_pos['%d시' % day] = data
                data = []
            if count == 4:
                data = fri_pos.get('%d시' % day)
                data.append('b')
                fri_pos['%d시' % day] = data
                data = []

    for count in range(0, 5):
        c_times = c_time[count]
        days = []
        if ';' in c_times:
            for counts in range(0, len(c_times.split(';'))):
                time = c_times.split(';')[counts].split('~')
                length = range(int(time[0][0:2]), int(time[1][0:2]))
                for i in length:
                    days.append(i)
        else:
            c_times = c_times.split('~')
            length = range(int(c_times[0][0:2]), int(c_times[1][0:2]))
            for i in length:
                days.append(i)
        for day in days:
            if count == 0:
                data = mon_pos.get('%d시' % day)
                data.append('c')
                mon_pos['%d시' % day] = data
                data = []
            if count == 1:
                data = tue_pos.get('%d시' % day)
                data.append('c')
                tue_pos['%d시' % day] = data
                data = []
            if count == 2:
                data = wed_pos.get('%d시' % day)
                data.append('c')
                wed_pos['%d시' % day] = data
                data = []
            if count == 3:
                data = thu_pos.get('%d시' % day)
                data.append('c')
                thu_pos['%d시' % day] = data
                data = []
            if count == 4:
                data = fri_pos.get('%d시' % day)
                data.append('c')
                fri_pos['%d시' % day] = data
                data = []

    for count in range(0, 5):
        d_times = d_time[count]
        days = []
        if ';' in d_times:
            for counts in range(0, len(d_times.split(';'))):
                time = d_times.split(';')[counts].split('~')
                length = range(int(time[0][0:2]), int(time[1][0:2]))
                for i in length:
                    days.append(i)
        else:
            d_times = d_times.split('~')
            length = range(int(d_times[0][0:2]), int(d_times[1][0:2]))
            for i in length:
                days.append(i)
        for day in days:
            if count == 0:
                data = mon_pos.get('%d시' % day)
                data.append('d')
                mon_pos['%d시' % day] = data
                data = []
            if count == 1:
                data = tue_pos.get('%d시' % day)
                data.append('d')
                tue_pos['%d시' % day] = data
                data = []
            if count == 2:
                data = wed_pos.get('%d시' % day)
                data.append('d')
                wed_pos['%d시' % day] = data
                data = []
            if count == 3:
                data = thu_pos.get('%d시' % day)
                data.append('d')
                thu_pos['%d시' % day] = data
                data = []
            if count == 4:
                data = fri_pos.get('%d시' % day)
                data.append('d')
                fri_pos['%d시' % day] = data
                data = []

    count_dic = {'a_count': 0, 'b_count': 0, 'c_count': 0, 'd_count': 0}

    for num in range(10, 18):
        if len(mon_pos.get('%d시' % num)) == 0:
            mon_final['%d시' % num] = '불가'
        if len(tue_pos.get('%d시' % num)) == 0:
            tue_final['%d시' % num] = '불가'
        if len(wed_pos.get('%d시' % num)) == 0:
            wed_final['%d시' % num] = '불가'
        if len(thu_pos.get('%d시' % num)) == 0:
            thu_final['%d시' % num] = '불가'
        if len(fri_pos.get('%d시' % num)) == 0:
            fri_final['%d시' % num] = '불가'
        for name in worker:
            if len(mon_pos.get('%d시' % num)) == 1:
                if mon_pos.get('%d시' % num)[0] == name and count_dic.get('%s_count' % name) < 10:
                    mon_final['%d시' % num] = mon_pos.get('%d시' % num)[0]
                    mon_pos['%d시' % num] = []
                    count_dic['%s_count' % name] = count_dic.get('%s_count' % name) + 1
                elif mon_pos.get('%d시' % num)[0] == name and count_dic.get('%s_count' % name) >= 10:
                    mon_final['%d시' % num] = '불가'
                    mon_pos['%d시' % num] = []

            if len(tue_pos.get('%d시' % num)) == 1:
                if tue_pos.get('%d시' % num)[0] == name and count_dic.get('%s_count' % name) < 10:
                    tue_final['%d시' % num] = tue_pos.get('%d시' % num)[0]
                    tue_pos['%d시' % num] = []
                    count_dic['%s_count' % name] = count_dic.get('%s_count' % name) + 1
                elif tue_pos.get('%d시' % num)[0] == name and count_dic.get('%s_count' % name) >= 10:
                    tue_final['%d시' % num] = '불가'
                    tue_pos['%d시' % num] = []
            if len(wed_pos.get('%d시' % num)) == 1:
                if wed_pos.get('%d시' % num)[0] == name and count_dic.get('%s_count' % name) < 10:
                    wed_final['%d시' % num] = wed_pos.get('%d시' % num)[0]
                    wed_pos['%d시' % num] = []
                    count_dic['%s_count' % name] = count_dic.get('%s_count' % name) + 1
                elif wed_pos.get('%d시' % num)[0] == name and count_dic.get('%s_count' % name) >= 10:
                    wed_final['%d시' % num] = '불가'
                    wed_pos['%d시' % num] = []
            if len(thu_pos.get('%d시' % num)) == 1:
                if thu_pos.get('%d시' % num)[0] == name and count_dic.get('%s_count' % name) < 10:
                    thu_final['%d시' % num] = thu_pos.get('%d시' % num)[0]
                    thu_pos['%d시' % num] = []
                    count_dic['%s_count' % name] = count_dic.get('%s_count' % name) + 1
                elif thu_pos.get('%d시' % num)[0] == name and count_dic.get('%s_count' % name) >= 10:
                    thu_final['%d시' % num] = '불가'
                    thu_pos['%d시' % num] = []
            if len(fri_pos.get('%d시' % num)) == 1:
                if fri_pos.get('%d시' % num)[0] == name and count_dic.get('%s_count' % name) < 10:
                    fri_final['%d시' % num] = fri_pos.get('%d시' % num)[0]
                    fri_pos['%d시' % num] = []
                    count_dic['%s_count' % name] = count_dic.get('%s_count' % name) + 1
                elif fri_pos.get('%d시' % num)[0] == name and count_dic.get('%s_count' % name) >= 10:
                    fri_final['%d시' % num] = '불가'
                    fri_pos['%d시' % num] = []

    for count in range(0, 4):
        for name in worker:
            if count_dic.get('%s_count' % name) >= 10:
                for key, value in list(mon_pos.items()):
                    if name in value:
                        value.remove(name)
                for key, value in list(tue_pos.items()):
                    if name in value:
                        value.remove(name)
                for key, value in list(wed_pos.items()):
                    if name in value:
                        value.remove(name)
                for key, value in list(thu_pos.items()):
                    if name in value:
                        value.remove(name)
                for key, value in list(fri_pos.items()):
                    if name in value:
                        value.remove(name)
            for num in range(10, 18):
                if len(mon_pos.get('%d시' % num)) == 1:
                    if mon_pos.get('%d시' % num)[0] == name and count_dic.get('%s_count' % name) < 10:
                        mon_final['%d시' % num] = mon_pos.get('%d시' % num)[0]
                        mon_pos['%d시' % num] = []
                        count_dic['%s_count' % name] = count_dic.get('%s_count' % name) + 1
                    elif mon_pos.get('%d시' % num)[0] == name and count_dic.get('%s_count' % name) >= 10:
                        mon_final['%d시' % num] = '불가'
                        mon_pos['%d시' % num] = []
                if len(tue_pos.get('%d시' % num)) == 1:
                    if tue_pos.get('%d시' % num)[0] == name and count_dic.get('%s_count' % name) < 10:
                        tue_final['%d시' % num] = tue_pos.get('%d시' % num)[0]
                        tue_pos['%d시' % num] = []
                        count_dic['%s_count' % name] = count_dic.get('%s_count' % name) + 1
                    elif tue_pos.get('%d시' % num)[0] == name and count_dic.get('%s_count' % name) >= 10:
                        tue_final['%d시' % num] = '불가'
                        tue_pos['%d시' % num] = []
                if len(wed_pos.get('%d시' % num)) == 1:
                    if wed_pos.get('%d시' % num)[0] == name and count_dic.get('%s_count' % name) < 10:
                        wed_final['%d시' % num] = wed_pos.get('%d시' % num)[0]
                        wed_pos['%d시' % num] = []
                        count_dic['%s_count' % name] = count_dic.get('%s_count' % name) + 1
                    elif wed_pos.get('%d시' % num)[0] == name and count_dic.get('%s_count' % name) >= 10:
                        wed_final['%d시' % num] = '불가'
                        wed_pos['%d시' % num] = []
                if len(thu_pos.get('%d시' % num)) == 1:
                    if thu_pos.get('%d시' % num)[0] == name and count_dic.get('%s_count' % name) < 10:
                        thu_final['%d시' % num] = thu_pos.get('%d시' % num)[0]
                        thu_pos['%d시' % num] = []
                        count_dic['%s_count' % name] = count_dic.get('%s_count' % name) + 1
                    elif thu_pos.get('%d시' % num)[0] == name and count_dic.get('%s_count' % name) >= 10:
                        thu_final['%d시' % num] = '불가'
                        thu_pos['%d시' % num] = []
                if len(fri_pos.get('%d시' % num)) == 1:
                    if fri_pos.get('%d시' % num)[0] == name and count_dic.get('%s_count' % name) < 10:
                        fri_final['%d시' % num] = fri_pos.get('%d시' % num)[0]
                        fri_pos['%d시' % num] = []
                        count_dic['%s_count' % name] = count_dic.get('%s_count' % name) + 1
                    elif fri_pos.get('%d시' % num)[0] == name and count_dic.get('%s_count' % name) >= 10:
                        fri_final['%d시' % num] = '불가'
                        fri_pos['%d시' % num] = []

    print('<이번주 시간표>')
    print('월요일 : ', end='')
    print(mon_final)
    print('화요일 : ', end='')
    print(tue_final)
    print('수요일 : ', end='')
    print(wed_final)
    print('목요일 : ', end='')
    print(thu_final)
    print('금요일 : ', end='')
    print(fri_final)

a = ['10:00~14:00', '15:00~18:00', '11:00~13:00;14:00~16:00', '10:00~11:00', '15:00~18:00']
b = ['11:00~14:00', '14:00~16:00', '16:00~18:00', '10:00~11:00;12:00~13:00', '14:00~16:00']
c = ['14:00~16:00', '16:00~18:00', '10:00~12:00', '12:00~14:00', '14:00~16:00']
d = ['14:00~18:00', '10:00~18:00', '12:00~14:00', '14:00~15:00;16:00~17:00', '10:00~12:00']
make_timetable(a, b, c, d)

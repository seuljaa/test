import re


def make_timetable(a_time: list, b_time: list, c_time: list, d_time: list):

    mon_final = {'10시': [], '11시': [], '12시': [], '13시': [], '14시': [], '15시': [], '16시': [], '17시': []}
    tue_final = {'10시': [], '11시': [], '12시': [], '13시': [], '14시': [], '15시': [], '16시': [], '17시': []}
    wed_final = {'10시': [], '11시': [], '12시': [], '13시': [], '14시': [], '15시': [], '16시': [], '17시': []}
    thu_final = {'10시': [], '11시': [], '12시': [], '13시': [], '14시': [], '15시': [], '16시': [], '17시': []}
    fri_final = {'10시': [], '11시': [], '12시': [], '13시': [], '14시': [], '15시': [], '16시': [], '17시': []}

    mon = {'a': [], 'b': [], 'c': [], 'd': []}
    tue = {'a': [], 'b': [], 'c': [], 'd': []}
    wed = {'a': [], 'b': [], 'c': [], 'd': []}
    thu = {'a': [], 'b': [], 'c': [], 'd': []}
    fri = {'a': [], 'b': [], 'c': [], 'd': []}

    for count in range(0, 5):
        a_times = a_time[count]
        day = []
        if ';' in a_times:
            for counts in range(0, len(a_times.split(';'))):
                time = a_times.split(';')[counts].split('~')
                length = range(int(time[0][0:2]), int(time[1][0:2]))
                for i in length:
                    day.append(i)
        else:
            a_times = a_times.split('~')
            length = range(int(a_times[0][0:2]), int(a_times[1][0:2]))
            for i in length:
                day.append(i)
        if count == 0:
            mon['a'] = day
        if count == 1:
            tue['a'] = day
        if count == 2:
            wed['a'] = day
        if count == 3:
            thu['a'] = day
        if count == 4:
            fri['a'] = day

    for count in range(0, 5):
        b_times = b_time[count]
        day = []
        if ';' in b_times:
            for counts in range(0, len(b_times.split(';'))):
                time = b_times.split(';')[counts].split('~')
                length = range(int(time[0][0:2]), int(time[1][0:2]))
                for i in length:
                    day.append(i)
        else:
            b_times = b_times.split('~')
            length = range(int(b_times[0][0:2]), int(b_times[1][0:2]))
            for i in length:
                day.append(i)
        if count == 0:
            mon['b'] = day
        if count == 1:
            tue['b'] = day
        if count == 2:
            wed['b'] = day
        if count == 3:
            thu['b'] = day
        if count == 4:
            fri['b'] = day

    for count in range(0, 5):
        c_times = c_time[count]
        day = []
        if ';' in c_times:
            for counts in range(0, len(c_times.split(';'))):
                time = c_times.split(';')[counts].split('~')
                length = range(int(time[0][0:2]), int(time[1][0:2]))
                for i in length:
                    day.append(i)
        else:
            c_times = c_times.split('~')
            length = range(int(c_times[0][0:2]), int(c_times[1][0:2]))
            for i in length:
                day.append(i)
        if count == 0:
            mon['c'] = day
        if count == 1:
            tue['c'] = day
        if count == 2:
            wed['c'] = day
        if count == 3:
            thu['c'] = day
        if count == 4:
            fri['c'] = day

    for count in range(0, 5):
        d_times = d_time[count]
        day = []
        if ';' in d_times:
            for counts in range(0, len(d_times.split(';'))):
                time = d_times.split(';')[counts].split('~')
                length = range(int(time[0][0:2]), int(time[1][0:2]))
                for i in length:
                    day.append(i)
        else:
            d_times = d_times.split('~')
            length = range(int(d_times[0][0:2]), int(d_times[1][0:2]))
            for i in length:
                day.append(i)
        if count == 0:
            mon['d'] = day
        if count == 1:
            tue['d'] = day
        if count == 2:
            wed['d'] = day
        if count == 3:
            thu['d'] = day
        if count == 4:
            fri['d'] = day

    print(mon)


a = ['10:00~14:00', '15:00~18:00', '11:00~13:00;14:00~16:00', '10:00~11:00', '15:00~18:00']
b = ['11:00~14:00', '14:00~16:00', '16:00~18:00', '10:00~11:00;12:00~13:00', '14:00~16:00']
c = ['14:00~16:00', '16:00~18:00', '10:00~12:00', '12:00~14:00', '14:00~16:00']
d = ['14:00~18:00', '10:00~18:00', '12:00~14:00', '14:00~15:00;16:00~17:00', '10:00~12:00']
make_timetable(a, b, c, d)

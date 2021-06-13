import time


def convert(sec):
    minits = sec // 60
    second = sec % 60
    milli_sec = (second - int(second)) * 1000
    hour = minits // 60
    min = minits % 60
    return f"{int(hour)}:{int(min)}:{int(second)}:{int(milli_sec)}"


start_signal = input('Push "ENTER" to Start')
start_time = time.time()

print('Push "ENTER" to lap time')
print('Push "p and ENTER" to Stop')
lap_num = 0
while True:
    stop_signal = input()
    stop_time = time.time()
    if stop_signal == '':
        lap_num += 1
        result = stop_time - start_time
        time_result = convert(result)
        print(f"lap {lap_num}：{time_result}")
    elif stop_signal == 'p':
        result = stop_time - start_time
        time_result = convert(result)
        print(f"Stop Time：{time_result}")
        break
    else:
        print('Push "ENTER" to lap time')
        print('Push "p and ENTER" to Stop')

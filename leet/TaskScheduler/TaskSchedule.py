import os.path
from datetime import datetime


def get_curr_time():
    start_day = datetime.now().day
    start_hour = datetime.now().hour
    start_minute = datetime.now().minute
    return int(start_day * 24 * 60) + int(start_hour * 60) + int(start_minute)


def validate_last_run(var_name, script_freq):
    dir_name = 'last_run'
    dir_exists = os.path.isdir(dir_name)
    cur_path = os.getcwd()
    dir_path = cur_path + '/' + dir_name
    if not dir_exists:
        os.mkdir(dir_path)

    fname = var_name + '.lastrun'
    f_path = dir_path + '/' + fname
    f_exists = os.path.isfile(f_path)
    curr_time = get_curr_time()

    if not f_exists:
        f = open(f_path, 'w+')
        f.write(str(curr_time))
        f.close()
        return True

    f = open(f_path, 'r+')
    start_time = f.read()
    time_difference = curr_time - int(start_time)
    f.close()

    if time_difference > script_freq:
        print("run")
        f = open(f_path, 'w+')
        f.write(str(get_curr_time()))
        f.close()
        return True

    return False


if __name__ == '__main__':
    script_freq = 6
    var_name = 'loan'
    print(validate_last_run(var_name, script_freq))

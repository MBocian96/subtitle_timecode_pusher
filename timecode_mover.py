from datetime import timedelta, datetime


def get_proper_milisecond(mic):
    if len(mic) != 3:
        return '0' + mic
    return mic


def get_proper_time(hour):
    if len(hour) != 2:
        return '0' + hour
    return hour


def increment_time_code(time_code, time_to_increment: timedelta) -> str:
    new_hour = int(time_code[0:2])
    new_min = int(time_code[3:5])
    new_sec = int(time_code[6:8])
    new_mic = int(time_code[9:12])
    start_time = datetime(year=1, month=1, day=1, hour=new_hour, minute=new_min, second=new_sec, microsecond=new_mic)
    new_start_time = start_time + time_to_increment

    end_hour = int(time_code[17:19])
    end_min = int(time_code[20:22])
    end_sec = int(time_code[23:25])
    end_mic = int(time_code[26:29])
    end_time = datetime(year=1, month=1, day=1, hour=end_hour, minute=end_min, second=end_sec, microsecond=end_mic)
    new_end_time = end_time + time_to_increment

    new_start_time_result = get_proper_time(str(new_start_time.hour)) + ':' \
                            + get_proper_time(str(new_start_time.minute)) + ':' \
                            + get_proper_time(str(new_start_time.second)) + ',' \
                            + get_proper_milisecond(str(new_start_time.microsecond)[-3:])

    new_end_time_result = get_proper_time(str(new_end_time.hour)) + ':' \
                          + get_proper_time(str(new_end_time.minute)) + ':' \
                          + get_proper_time(str(new_end_time.second)) + ',' \
                          + get_proper_milisecond(str(new_end_time.microsecond)[-3:])

    return new_start_time_result + ' --> ' + new_end_time_result + '\n'


def increment_for(hours, minutes, seconds, microseconds):
    time_to_increment = timedelta(hours=hours, minutes=minutes, seconds=seconds, microseconds=microseconds)
    with open('oigf.srt', 'w') as new_subtitiles_file:
        with open('napisy.srt', 'r') as subtitle_file:
            for line in subtitle_file:
                if ' --> ' in line:
                    print(line)
                    new_line = increment_time_code(line, time_to_increment)
                    new_subtitiles_file.write(new_line)
                    print(new_line)
                else:
                    new_subtitiles_file.write(line)


increment_for(0, minutes=5, seconds=51, microseconds=60)

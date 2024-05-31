# this is exercise 1.1
import datetime

print("cron.py")

def write_times():
    time_now = datetime.datetime.now()
    xmas = datetime.datetime(year=2024, month=12, day=24)#, hour=0, minute=0, second=0, microsecond=0)
    summer_break = datetime.datetime(2024, 6, 14)
    lia = datetime.datetime(2024, 9, 16)
    td_xmas = -(time_now - xmas)
    td_Xmas_h, remainder1 = divmod(td_xmas.seconds, 3600)
    td_Xmas_m = divmod(remainder1, 60)
    td_summerbreak = time_now - summer_break
    td_lia = -(time_now - lia)
    td_lia_h, remainder2 = divmod(td_lia.seconds, 3600)
    td_lia_m = divmod(remainder2, 60)

    print(f"|---------------------------------------------------|")
    print(f"|  Countdown from: {time_now}       |")
    print(f"|---------------------------------------------------|")
    print("|                   |   Remaining time to event     |")
    print("|---------------------------------------------------|")
    print("|      Event        | (days) |(hours)| (mins)| (sec)|")
    print(f"| X-Mas             |  {td_xmas.days}   |  {td_Xmas_h}   |   {td_Xmas_m[0]}   |   {td_Xmas_m[1]} |")
    print(f"| LIA               |  {td_lia.days}   |   {td_lia_h}  |   {td_lia_m[0]}   |   {td_lia_m[1]} |")
    print("|---------------------------------------------------|")
    print(" ")

#if __name__ == '__main__':
write_times()



def duesXifres(num):
    out = ""
    if (num) < 10:
        out += "0"
    out += str(num)
    
    return out

def incrementSegon(hh,mm,ss):
    ss += 1

    if (ss == 60):
        ss = 0
        mm += 1
    if (mm == 60):
        mm = 0
        hh += 1
    if (hh == 24):
        hh = 0

    return hh,mm,ss

time = input("Introdueix hora en format hh:mm:ss : ")

hh = int(time[0:2])
mm = int(time[3:5])
ss = int(time[6:8])

hh,mm,ss = incrementSegon(hh,mm,ss)


new_time = ""
new_time += duesXifres(hh) + ":"
new_time += duesXifres(mm) + ":"
new_time += duesXifres(ss)


print(new_time) 

    
s='09:01:00PM'

def timeConversion(s):

    if s[8:]=='AM':
        if int(s[:2])>=12:
            h=int(s[:2])-12
            if h>9:
                s=str(h)+s[2:8]
            else:
                s='0'+str(h)+s[2:8]
        s=s[:8]
    else:
        if s[:2]=='12':
            s=s[:8]
            return s
        h=int(s[:2])+12
        s=str(h)+s[2:8]
    return s

print(timeConversion(s))

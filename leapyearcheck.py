yeari = int(input())
if yeari%4==0:
    if yeari%100==0:
        if yeari%400==0:
            print("yes")
        else:
             print("no")
from time import *
import random

def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
               if partest[i] != usertest[i]:
                    error +=1
        except:
            error +=1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)

while(True):
    ck=input("To start enter yes/no : ")
    if ck == 'yes':
        test=("A quick brown fox jumps over the lazy dog.")
        test1 = random.choice(test)
        print("****Typing Speed****")
        print(test1)
        print()
        print()
        time1 = time()
        testinput = input("Enter : ")
        time2 = time()

        print("Speed : ",speed_time(time1,time2,testinput)," w/sec")
        print("Error : ",mistake(test1,testinput))
    elif ck== 'no':
        print("Thank You")
        break
    else:
        print("Wrong input")
        
    




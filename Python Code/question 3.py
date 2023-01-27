import math

def temperature_check(x,temp):
    if temp== "C":
        if(x>40):
            print("The patient's temperature is hyperthermic")
        elif(x<37):
            print("The patient temperature is hypothermic")
        else:
             print("The patient temperature is normal")
    if temp=="F":
        if(x>104):
            print("The patient's temperature is hyperthermic")
        elif(x<95):
            print("The patient temperature is hypothermic")
        else:
             print("The patient temperature is normal")

temperature_check(14,"C")
temperature_check(37,"C")
temperature_check(37,"F")


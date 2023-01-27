import math
#num=int(input("Please enter the number of resistors"))
#v=[]
#def potiential_divider(x,list):
    #length=len(list)
    #i=x/sum(list)
    #for num in list(0,length):
        #n=0
        #v[length]=i*list[n]
        #n=n+1

def potiential_divider(x,list):
    total=0
    for y in list:
        total=total+x
    current=x/total
    for z in list:
        vol=current*z
        print(vol,"volts")


potiential_divider(9,[3000,1000])


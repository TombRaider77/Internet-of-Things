
import  math
#print("Hello world")
#rnum=[]

#def parallel():
   # num = int(input("How many resistors are in the circuit"))
  #  print("Please enter the values of the resistors")
   # for i in range(num):
     #   x=int(input("Enter the next value"))
      #  rnum.append(x)
      #  return rnum


#parallel()
#print(rnum)
#num1=float(input("Please enter first resistor value"))
#num2=float(input("Please enter second resistor value"))
#num3=float(input("Please enter third resistor value"))

#def parallel(list):
  #  value= (1/num1 + 1/num2 + 1/num3)
    #pow(value,-1)
   # print(value)

#parallel(num1,num2,num3)
#print("Hello world")
#rnum=[]

#def parallel():
   # num = int(input("How many resistors are in the circuit"))
  #  print("Please enter the values of the resistors")
   # for i in range(num):
     #   x=int(input("Enter the next value"))
      #  rnum.append(x)
      #  return rnum


#parallel()
#print(rnum)
#num1=float(input("Please enter first resistor value"))
#num2=float(input("Please enter second resistor value"))
#num3=float(input("Please enter third resistor value"))

#def parallel(list):
  #  value= (1/num1 + 1/num2 + 1/num3)
    #pow(value,-1)
   # print(value)

#parallel(num1,num2,num3)import  math

def parallel(list):
    v=0
    for x in list:
        v = v+ (1/x)
       # value +=(1/x)
    finalval=pow(v,-1)
    print(finalval,"Ohms")

parallel([330,100,2200])

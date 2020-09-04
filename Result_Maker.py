x=input("Your Name:")
a,b,c=-1,-1,-1
while(a<0 or a>100):
    a=int(input("please Enter your Maths marks :"))
    if(a<0 or a>100):
        print("Please enter the value between -1 to 101")
while(b<0 or b>100):
    b=int(input("please Enter your Chemistry marks :"))
    if(b<0 or b>100):
        print("Please enter the value between -1 to 101")
while(c<0 or c>100):
    c=int(input("please Enter your Physics marks :"))
    if(c<0 or c>100):
        print("Please enter the value between -1 to 101")
print("****************** Mark sheet of ",x,"******************")
z=a+b+c
print(z,"/300")
avg=z/3
print("average:","{:.2f}".format(avg),"%")
if(100>=avg>81):
  g='A'
  print("Congratulations! ",x,"you scored '",g,"' Grade.")
elif(80>=avg>61):
  g='B'
  print("Congratulations! ",x,"you scored '",g,"' Grade.")
elif(60>=avg>40):
  g='C'
  print("Congratulations! ",x,"you scored '",g,"' Grade.")
else:
  print("soory! Better luck next time.")

print("==========================================================")

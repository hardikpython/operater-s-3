print("enter your all subjects marks")
math=int(input("enter your math marks"))
socialscience=int(input("enter your socialscience marks "))
english=int(input("enter your english marks"))
gk=int(input("enter your G.k marks"))
science=int(input("enter your science marks"))
sum=(math+socialscience+english+gk+science)
avg=sum/5
print(avg)
if avg>=91 and avg<=100:
 print("grade is A1")
elif avg>=81 and avg<91:
 print("grade is A2")
elif avg>=71 and avg<81:
 print("grade is B1")
elif avg>=61 and avg<71:
 print("grade is B2")
else:
 print("invalid input80")
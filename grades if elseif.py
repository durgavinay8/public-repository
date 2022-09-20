#write a python program to input percentage and give grade according to following table
s1=eval(input("enter the marks of subject 1: "))
s2=eval(input("enter the marks of subject 2: "))
s3=eval(input("enter the marks of subject 3: "))
s4=eval(input("enter the marks of subject 4: "))
p=((s1+s2+s3+s4)/400)*100
print(p,"%")

if(p>=90):
    print("you have secured A grade")
elif(p>=80):
    print("you have secured B grade")
elif(p>=70):
    print("you have secured C grade")
elif(p>=60):
    print("you have secured D grade")
elif(p>=40):
    print("you have secured E grade")
else:
    print("Jeevitham ante poratam bro")
    

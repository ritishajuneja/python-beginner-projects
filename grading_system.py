name=input("Enter you name")
per=int(input("Enter your percentage"))
if(per>=90):
    print("Congratulations",name,"You got A+")
    print("Keep it up")
elif(per>=80):
    print("Congratulations",name,"You got A")
    print("Keep it up")
elif(per>=70):
    print("Congratulations",name,"You got B+")
    print("Keep it up")
elif(per>=60):
    print("Congratulations",name,"You got B")
    print("Keep it up")
elif(per>=50):
    print("Congratulations",name,"You got C")
    print("Try harder...")
elif(per<=40):
    print("Sorry",name,"You got failed!")
    print("Better luck next time")
else:
    print("INVALID PERCENTAGE")

    

class sample():
    def subfields():
        List=["Machine Learning","Neural Networks","vision","Robotics","Speech Processing","Natural Language Processing"]
        print("subfields in AI are")
        for name in List:
            print(name)
        
    def oddEven():
        num=int(input("Enter a number"))
        if num%2==0:
            print(num,"is Even number")
        else:
            print("Number is odd")

    def eligible():
        gender=input("your gender")
        age=int(input("your Age"))
        if gender=="male" and age>21:
            print("eligible for marriage")
        elif gender=="female" and age>21:
            print("eligible for marriage")
        else:
            print("not eligible for marriage")

    def percentage():
        subject1=int(input("subject1"))
        subject2=int(input("subject2"))
        subject3=int(input("subject3"))
        subject4=int(input("subject4"))
        subject5=int(input("subject5"))
        total=subject1+subject2+subject3+subject4+subject5
        print("Total:",total)
        per=total/5
        print("percentage: {:.15f}".format(per))

    def Triangle():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        print("Area formula:(Height*Breadth)/2")
        Area=(Height*Breadth)/2
        print("Area of Triangle:",Area)
        Height1=int(input("Height1"))
        Height2=int(input("Height2"))
        Breadth=int(input("Breadth"))
        print("Perimeter formula:Height1+Height2+Breadth")
        perimeter=(Height1+Height2+Breadth)
        print("perimeter of Triangle",perimeter)
    
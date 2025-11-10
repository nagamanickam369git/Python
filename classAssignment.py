class multipleFunction():
    def Subfields(list):
        print("Sub-fields in AI are:")
        for item in list:
            print(item)

    def OddEven():
        num1 = int(input("Enter a number:"))
        if(num1%2 == 1):
            print(num1,"is Odd number")
            OddEven = num1,"is Odd number"
        else:
            print(num1,"is Even number")
            OddEven = num1,"is Even number"
        return OddEven


    def Elegible():
        gender = input("Your Gender:")
        age = int(input("Your Age:"))
        if ((gender == "Male" or gender =="male") and age >=21):
            print("Eligible")
            ElegiblityForMarriage = "Eligible"
        elif ((gender == "Female" or gender =="female") and age >=18):
            print("Eligible")
            ElegiblityForMarriage = "Eligible"
        else: 
            print("Not Eligible")
            ElegiblityForMarriage = "Not Eligible"
        return ElegiblityForMarriage


    def percentage(Subject1, Subject2, Subject3, Subject4, Subject5):
        print("Subject1=", Subject1)
        print("Subject2=", Subject2)
        print("Subject3=", Subject3)
        print("Subject4=", Subject4)
        print("Subject5=", Subject5)
        Total = Subject1 + Subject2 + Subject3 + Subject4 + Subject5
        Percentage = float(Total / 5)
        print("Total:",Total)
        print("Percentage:",Percentage)
        return Total,Percentage


    def triangle():
        height = int(input("Height:"))
        breadth = int(input("Breadth:"))
        print("Area formula: (Height*Breadth) / 2")
        areaOfTriangle = (height * breadth) / 2
        print("Area of Traingle:", areaOfTriangle)
        height1 = int(input("Height1:"))
        height2 = int(input("Height2:"))
        breadth1 = int(input("Breadth:"))
        print("Perimeter formula: Height1 + Height2 + Breadth")
        perimeterOfTriangle = height1 + height2 + breadth1
        print("Perimeter of Traingle:", perimeterOfTriangle)
        return areaOfTriangle,perimeterOfTriangle 



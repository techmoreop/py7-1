m1 = int(input("marks of maths"))
m2 = int(input("marks of science"))
m3 = int(input("marks of english"))
m4 = int(input("marks of hindi"))
sum = m1 + m2 + m3 + m4 
average = sum / 4
if average >= 91 and average <= 100:
    print("Grade A1")
elif average >= 81 and average <= 91:
    print("Grade A2")
elif average >= 71 and average <= 81:
    print("Grade B1")
elif average >= 61 and average <= 71:
    print("Grade B2")
elif average >= 51 and average <= 61:
    print("Grade C1")
elif average >= 41 and average <= 51:
    print("Grade C2")   
elif average >= 33 and average <= 41:
    print("Grade D")  
elif average >= 21 and average <= 33:
    print("Grade E1")
elif average >= 0 and average <= 21:
    print("Grade E2")
else:
    print("Invalid input")

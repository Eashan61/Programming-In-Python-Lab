import math
#task 1 swapping
print('Swaping:')
a = input("Enter the 1st value: ")
b = input("Enter the 2nd value: ")
print('Before swap: a =', a, ', b =',b)
a, b = b, a
print('After swap: a =', a, ', b =',b)

# task 2 distance between 2 point
print("Distance between two points: \n")
x1 = float(input("Enter the value of x1: "))
y1 = float(input("Enter the value of y1: "))
x2 = float(input("Enter the value of x2: "))
y2 = float(input("Enter the value of y2: "))
d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("Distance =", round(d, 4))

#task 3 cheking even or odd
print("Even or Odd: \n")
n = int(input("Enter an number: "))
if n % 2 == 0:
    print(n,  "is Even")
else:
    print(n, "is Odd")

#task 4 check vowel or not
print("Check vowel or not: \n")
cha = input("Enter a character: ")

while len(cha) != 1 or not cha.isalpha():
    print("Please enter a letter.")
    cha = input("Enter a character: ") 

if cha.lower() in "aeiou":
    print(cha, "is a vowel")
else:
    print(cha, "is not a vowel")

#task 5 grade
print("Grading system of AIUB: \n")
mark = float(input("Enter your marks (0-100): "))
if mark < 0 or mark > 100:
    print("Invalid mark detected!")
elif mark >= 90:
    print("Grade: A+  (CGPA 4.00)")
elif mark >= 85:
    print("Grade: A   (CGPA 3.75)")
elif mark >= 80:
    print("Grade: B+  (CGPA 3.50)")
elif mark >= 75:
    print("Grade: B   (CGPA 3.25)")
elif mark >= 70:
    print("Grade: C+  (CGPA 3.00)")
elif mark >= 65:
    print("Grade: C   (CGPA 2.75)")
elif mark >= 60:
    print("Grade: D+  (CGPA 2.50)")
elif mark >= 50:
    print("Grade: D   (CGPA 2.25)")
else:
    print("Grade: F   (CGPA 0.00)")
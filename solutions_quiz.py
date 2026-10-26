"""write a python program to classfy students based on activity students based on activities attended and punctuality percentage. Reject invalid inputs: negative activities or punctuality outside 0-100%"""

"""activity = int(input("Enter your activiy number:"))
punctuality = int(input("Enter your punctuality parsentage:"))

if activity < 0 or 0 > punctuality or punctuality > 100:
    print("Invalid Input")
else:
    if activity >= 8 and punctuality >= 80:
        print("Highly Engaged")
    elif activity < 4 or punctuality < 60:
        print("Needs Improvement")
    else:
        print("Moderately Engaged")"""
"""Write a python programe that takes a positive integer n and counts and sums the numbers from 1 through n (inclusive) that are divisible by 3 but not by 5. Use a loop and a conditional statement"""

"""n = int(input("Enter a positive Number:"))
if n < 0:
    print("Please Enter a positive number:")
    n = int(input())
count = 0
sum = 0
for i in range (1, n+1):
    if i % 3 == 0 and i % 5 != 0:
        count += 1
        sum = i + sum
print(f"count: {count}")
print(f"sum: {sum}")"""

"""Write a function named adjusted_score(score, bonus=5) that returns a students score after applying a bonus. The bonus is 5 by default, but the caller may provide a different bonus. The returned score must not exceed 100."""

def adjusted_score(score, bonus = 5):
    score = score + bonus
    if score > 100:
        print("Score Exceeded 100")
    else:
        return score
adjusted_score(90)
adjusted_score(90, 4)
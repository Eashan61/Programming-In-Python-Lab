#task 1 loop over a sequence
# 1. Looping over a list sequence
fruits = ["apple", "banana", "cherry"]
print("Looping over a list:")
for item in fruits:
    print(item)

print()

#task 2 countdown
print("Countdown: \n")
num = int(input("Enter a number for countdown: "))
while num >= 0:
    print(num)
    num -= 1
#task 3 finding exponentiation
print("Exponentiation:\n")

base = float(input("Enter base: "))
expo = int(input("Enter exponent (integer): "))
result = 1
for _ in range(abs(expo)):
    result *= base
if expo < 0:
    result = 1 / result
print(f"{base} ^ {expo} = {result}")
print("Check with ** operator:", base ** expo)
#task 4 finding sum of all primes below 1000
print("Sum of primes below 1000\n")
sum = 0
for n in range(2, 1000):
    is_prime = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        sum += n
print("Sum of primes below 1000 =", sum)

# task 5 fibbonacci number
print("Fibonacci Number:\n")
n = int(input("Enter Number: "))
a, b = 0, 1
while a < n:
    print(a, end=" ")
    a, b = b, a + b
print()
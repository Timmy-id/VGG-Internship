#  Function to calculate the number of uppercase and lowercase letters in a sentence
def num_uppercase_lowercase():
    print("Determine the number of uppercase and lowercase letters in a sentence")
    sentence = str(input("Enter your sentence: "))
    uppercase_lowercase = {"Upper": 0, "Lower": 0}
    for s in sentence:
        if s.isupper():
            uppercase_lowercase["Upper"] += 1
        elif s.islower():
            uppercase_lowercase["Lower"] += 1
        else:
            pass
    print("No. of uppercase characters:", uppercase_lowercase["Upper"])
    print("No. of lowercase characters:", uppercase_lowercase["Lower"])
num_uppercase_lowercase()

# Function to find the maximum off three numbers
def max_num():
    print("Find the maximim of three numbers")
    num1 = float(input("Enter 1st number: "))
    num2 = float(input("Enter 2nd number: "))
    num3 = float(input("Enter 3rd number: "))
    if (num1 >= num2) and (num1 >= num3):
        print("The maximumof the three numbers is ", num1)
    elif (num2 >= num1) and (num2 >= num3):
        print("The maximumof the three numbers is ", num2)
    else:
        print("The maximum of the three numbers is", num3)
max_num()        

# Function to determine if a number is a prime number
def prime_num():
    print("Check if a number is prime")
    num = int(input("Enter number: "))
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print("Enter a number greater than 1")
        return prime_num()
prime_num()

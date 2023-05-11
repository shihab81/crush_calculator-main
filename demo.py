
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()
count1 = lower_case_name1.count("t")
count2 = lower_case_name2.count("t")
count3 = lower_case_name1.count("r")
count4 = lower_case_name2.count("r")
count5 = lower_case_name1.count("u")
count6 = lower_case_name2.count("u")
count7 = lower_case_name1.count("e")
count8 = lower_case_name2.count("e")
count9 = lower_case_name1.count("l")
count10 = lower_case_name2.count("l")
count11 = lower_case_name1.count("o")
count12 = lower_case_name2.count("o")
count13 = lower_case_name1.count("v")
count14 = lower_case_name2.count("v")
count15 = lower_case_name1.count("e")
count16 = lower_case_name2.count("e")

true = (count1 + count2 + count3 + count4 + count5 + count6 + count7 + count8)
love = (count9 + count10 + count11 + count12 + count13 + count14 + count15 + count16)


def numConcat(num1, num2):
    # Convert both the numbers to
    # strings
    num1 = str(num1)
    num2 = str(num2)

    # Concatenate the strings
    num1 += num2

    return int(num1)


total = (numConcat(true, love))
if (total < 10) or (total > 90):
    print(f"Your score is {total}, you go together like coke and mentos.")
elif (total >= 40) and (total <= 50):
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}")


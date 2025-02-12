# This is a sample Python script.
from question_logic_function_thingy import questions
from question_logic_function_thingy import question_check
from question_logic_function_thingy import generate_decider
decider_1 = generate_decider()
decider_2 = generate_decider()
decider_2 += 10
decider_3 = generate_decider()
decider_3 += 20
decider_4 = generate_decider()
decider_4 += 30
decider_5 = generate_decider()
decider_5 += 40
decider_6 = generate_decider()
decider_6 += 50
decider_7 = generate_decider()
decider_7 += 60
decider_8 = generate_decider()
decider_8 += 70
decider_9 = generate_decider()
decider_9 += 80
decider_10 = generate_decider()
decider_10 += 90

start = input("Do you want to become a Millionaire? Then enter 'yes' now!: ")

while start.lower() != "yes":
    print("Why not? :( Please enter 'yes'!")
    start = input("Do you want to become a Millionaire? Then enter 'yes' now!: ")

print("Great! Let's get started on your journey to becoming a millionaire!")

print("Lets start with ur first question")
print("""    *****************************************
    *          100$ QUESTION                *
    *****************************************
""")
print(questions(decider_1))
answer_1 = input("Please Enter ur answer(type out the option): ")
question_check(answer_1, decider_1)
print("Correct lets move onto the 500$ Question")

print("""    *****************************************
    *          500$ QUESTION                *
    *****************************************
""")
print(questions(decider_2))
answer_2 = input("Please Enter ur answer(type out the option): ")
question_check(answer_2, decider_2)
print("Correct lets move onto the 1000$ Question")

print("""    *****************************************
    *          1000$ QUESTION                *
    *****************************************
""")
print(questions(decider_3))
answer_3 = input("Please Enter ur answer(type out the option): ")
question_check(answer_3, decider_3)
print("Correct lets move onto the 5000$ Question")

print("""    *****************************************
    *          5000$ QUESTION                *
    *****************************************
""")
print(questions(decider_4))
answer_4 = input("Please Enter ur answer(type out the option): ")
question_check(answer_4, decider_4)
print("Correct lets move onto the 10000$ Question")

print("""    *****************************************
    *          10000$ QUESTION                *
    *****************************************
""")
print(questions(decider_5))
answer_5 = input("Please Enter ur answer(type out the option): ")
question_check(answer_5, decider_5)
print("Correct lets move onto the 25000$ Question")

print("""    *****************************************
    *          25000$ QUESTION                *
    *****************************************
""")
print(questions(decider_6))
print(decider_6)
answer_6 = input("Please Enter ur answer(type out the option): ")
question_check(answer_6, decider_6)
print("Correct lets move onto the 50000$ Question")

print("""    *****************************************
    *          50000$ QUESTION                *
    *****************************************
""")
print(questions(decider_7))
print(decider_7)
answer_7 = input("Please Enter ur answer(type out the option): ")
question_check(answer_7, decider_7)
print("Correct lets move onto the 100000$ Question")

print("""    *****************************************
    *          100000$ QUESTION                *
    *****************************************
""")
print(questions(decider_8))
print(decider_8)
answer_8 = input("Please Enter ur answer(type out the option): ")
question_check(answer_8, decider_8)
print("Correct lets move onto the 250000$ Question")

print("""    *****************************************
    *          250000$ QUESTION                *
    *****************************************
""")
print(questions(decider_9))
print(decider_9)
answer_9 = input("Please Enter ur answer(type out the option): ")
question_check(answer_9, decider_9)
print("Correct lets move onto the 1000000$ Question")

print("""    *****************************************
    *          1000000$ QUESTION                *
    *****************************************
""")
print(questions(decider_10))
print(decider_10)
answer_10 = input("Please Enter ur answer(type out the option): ")
question_check(answer_10, decider_10)
print("Wohoo goodjob u won it all (:")













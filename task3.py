while True:
    user_input = input("Welcome to math quizz! Calculate the product of 89 * 6. Enter the numeric answer or type 'e' to exit ")
    if user_input == 'e':
        break
    elif user_input.isdigit():
        if user_input == '534':
            print("Corrent! Good job!")
            break
        else:
            print("The answer is wrong. Please try again")
            continue
    else:
        print("Invalid input, should be a number")
        continue



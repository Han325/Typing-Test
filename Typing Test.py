# Typing Test
# Version 1.0
# Created by Han
# Finished on 15/4/2020
# Note: This version is to be revised for a different type of typing test.


# import random, textwrap and Timer dir from threading module
import random
import textwrap
from threading import Timer


# function to introduce program
def intro_and_level():
    print("Welcome to the typing test!")
    print("This test consists of three difficulty levels: Easy, Moderate and Hard.\n")
    print("Easy -- 5 words and length of characters for each word is less than six characters")
    print("Moderate -- 10 words and length of characters for each word is between six and ten characters")
    print("Hard -- 15 words and length of characters for each word is more than ten characters")
    print("\nYou have 10 seconds to type in each word.\n")


# function to generate words based on difficulty level configurations
def gen_word_config(min_length, max_length, amount):
    print("Generating words.......\n")
    global gen_words
    gen_words = []
    for i in range(amount):
        # extracts words from sowpods.txt
        with open("sowpods.txt") as wordbook:
            words = (line.rstrip('\n') for line in wordbook)
            # extract words based on a specific amount of character length
            words_in_range = [word for word in words if min_length < len(word) <= max_length]
            # chooses one word randomly, and for (amount) of times according to the loop
            chosen_word = random.choice(words_in_range)
        # allocates generated words into a list for modifications
        gen_words.append(chosen_word)


# function to configure difficulty levels
def dif_config():
    dif_level = input("What level do you wish to choose?\n>>>")
    if dif_level == "Easy" or dif_level == "easy" or dif_level == "e":
        print('You have chosen...(easy)')
        gen_word_config(3, 6, 5)

    elif dif_level == "Moderate" or dif_level == "moderate" or dif_level == "m":
        print('You have chosen...(moderate)')
        gen_word_config(6, 10, 10)

    elif dif_level == "Hard" or dif_level == "hard" or dif_level == "h":
        print('You have chosen...(hard)')
        gen_word_config(10, 20, 15)
    else:
        print("Invalid input.")
        dif_config()


# function to set a time limit for user input
def time_limit_ans_input():
    global answer
    timeout = 10
    # configures timer with timeout limit
    t = Timer(timeout, print, ['Sorry, times up\nPress enter to continue....'])
    # starts timer
    t.start()
    print("Press enter when you have finished typing!")
    raw_answer = input("Type now!\n>>>")
    answer = raw_answer.upper()
    # cancels timer
    t.cancel()


# function to execute main typing test
def type_test():
    global typed_words
    typed_words = []
    # displays the generated word according the length of the list: gen_words
    for i in range(len(gen_words)):
        if i == 0:
            print("The " + str(i + 1) + "st word is " + gen_words[i])
            time_limit_ans_input()
            # adds the input from user into a list: typed_words
            typed_words.append(answer)
        elif i == 1:
            print("The " + str(i + 1) + "nd word is " + gen_words[i])
            time_limit_ans_input()
            typed_words.append(answer)
        elif i == 2:
            print("The " + str(i + 1) + "rd word is " + gen_words[i])
            time_limit_ans_input()
            typed_words.append(answer)
        else:
            print("The " + str(i + 1) + "th word is " + gen_words[i])
            time_limit_ans_input()
            typed_words.append(answer)


# function to calculate accuracy of typing of the user
def accu_cal():
    global char_list, accuracy
    global typed_char_list
    global aver_accuracy
    accu_num_list = []

    for i in range(len(gen_words)):
        # breaks down the each word in the list:gen_words into individual characters
        char_list = textwrap.wrap(gen_words[i], 1)

        # breaks down the each word in the list:typed_words into individual characters
        typed_char_list = textwrap.wrap(typed_words[i], 1)
        accu_count = 0

        # calculates accuracy by cross referencing individual characters of each typed word with the generated word
        if len(typed_char_list) < len(char_list):
            print("")
            break
        else:
            for i in range(len(char_list)):
                if char_list[i] == typed_char_list[i]:
                    accu_count += 1
                    accuracy = accu_count / len(char_list) * 100
            # allocates the calculated accuracies of each words into a list
            accu_num_list.append(accuracy)

    if len(typed_char_list) < len(char_list):
        aver_accuracy = "Insufficient data to calculate accuracy"
    else:
        # calculates the total accuracy by adding up the list:acc_num_list
        total_accuracy = sum(accu_num_list)
        aver_accuracy = total_accuracy//len(typed_words)


# function to check the input of the user and reveal results
def check_ans_and_results():
    print("Checking your answers......\nChecking completed.")
    count = 0
    for i in range(len(gen_words)):
        if typed_words[i] == gen_words[i]:
            count += 1

    print("Summary:")
    print("You typed " + str(count) + " out of " + str(len(gen_words)) + " words correctly.")
    print("Result: " + str(count) + "/" + str(len(gen_words)))
    print("Overall accuracy: " + str(aver_accuracy))
    raw_repeat = input("Do you wish to continue? (Y/N)")
    repeat = raw_repeat.upper()
    if repeat == "YES" or repeat == "Y":
        intro_and_level()
        dif_config()
        type_test()
        accu_cal()
        check_ans_and_results()
    elif repeat == "N0" or repeat == "N":
        print("Alright then, bye bye !")
    else:
        print("Invalid input, please try again.")


intro_and_level()
dif_config()
type_test()
accu_cal()
check_ans_and_results()

NEGATIVE = -1
POSITIVE = 1

def main():

    print("This program is an implementation of the Rosenberg Self-Esteem Scale.\nThis program will show you ten statements that you could possibly\napply to yourself. Please rate how much you agree with each of the\nstatements by responding with one of these four letters:")
    print()
    print("D means you strongly disagree with the statement.")
    print("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print("A means you strongly agree with the statement.")
    print()

    score = 0
    score += ask_question("1. I feel that I am a person of worth, at least on an equal plane\nwith others.", POSITIVE)
    score += ask_question("2. I feel that I have a number of good qualities.", POSITIVE)
    score += ask_question("3. All in all, I am inclined to feel that I am a failure.", NEGATIVE)
    score += ask_question("4. I am able to do things as well as most other people.", POSITIVE)
    score += ask_question("5. I feel I do not have much to be proud of.", NEGATIVE)
    score += ask_question("6. I take a positive attitude toward myself.", POSITIVE)
    score += ask_question("7. On the whole, I am satisfied with myself.", POSITIVE)
    score += ask_question("8. I wish I could have more respect for myself.", NEGATIVE)
    score += ask_question("9. I certainly feel useless at times.", NEGATIVE)
    score += ask_question("10. At times I think I am no good at all.", NEGATIVE)

    print()
    print(f"Your score is {score}.")
    print("A score below 15 may indicate problematic low self-esteem.")


def ask_question(statement, positive_or_negative):
    print(statement)
    user_answer = input("Enter D, d, a, or A: ")
    if user_answer == "D":
        score = 0
    elif user_answer == "d":
        score = 1
    elif user_answer == "a":
        score = 2
    elif user_answer == "A":
        score = 3

    if positive_or_negative == NEGATIVE:
        score = 3 - score
    return score

if __name__ == "__main__":
    main()


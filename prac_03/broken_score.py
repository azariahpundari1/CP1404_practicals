"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

# TODO: Fix this!


def main():
    score = float(input("Enter score: "))
    random_score = random.randint(0, 100)
    random_score_result = get_result(random_score)
    result = get_result(score)
    print(f"A random score of {random_score:.1f} is {random_score_result}\nA score of {score} is {result}")


def get_result(score):
    if score > 100 or score < 0:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()

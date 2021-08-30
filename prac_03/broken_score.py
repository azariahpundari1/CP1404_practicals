"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


# TODO: Fix this!
def main():
    score = float(input("Enter score: "))
    result = get_result(score)
    print(result)


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

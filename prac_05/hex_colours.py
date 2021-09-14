COLOUR_NAMES = {"f0f8ff": "AliceBlue", "faebd7": "AntiqueWhite", "f0ffff": "Azure1", "7fffd4": "aquamarine1", "f5f5dc":
                "Biege", "000000": "Black", "0000ff": "Blue1", "a52a2a": "Brown", "f8f8ff": "GhostWhite", "ffd700":
                "Gold"}

print(COLOUR_NAMES)
colour = input("# ").lower()
while colour != "":
    if colour in COLOUR_NAMES:
        print(colour, "is", COLOUR_NAMES[colour])
        colour = input("# ")
    else:
        print("Invalid colour")
        colour = input("# ")
# read the question wrong sorry

def main():
    emails = {}
    email = input("Email: ")
    get_name(email)
    while email != "":
        name = get_name(email)
        yes_or_no = input(f"Is your name {name} Y/N: ")
        if yes_or_no != "Y" and yes_or_no != "":
            name = input("Name: ")
        emails[email] = name
        email = input("Email: ")

    for email, name in emails.items():
        print(f"{name} {email}")


def get_name(email):
    split_at = email.split('@')[0]
    split_fullstop = split_at.split(".")
    name = " ".join(split_fullstop).title()
    return name

main()
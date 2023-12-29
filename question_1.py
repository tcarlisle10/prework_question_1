def hello_name(user_name):
    user_name = (first_name + ' ' + last_name)
    return user_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    first_name = input("first name: ")
    if first_name == 'q':
        break
    last_name = input("last name: ")
    if last_name == 'q':
        break
    formatted_name = hello_name(first_name)
    print("\nHello, " + formatted_name + "!")
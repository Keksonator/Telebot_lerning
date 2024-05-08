user_name = input()


if (
    user_name.startswith('@')
    and 5 <= len(user_name) <= 15
    and user_name[1:].isalnum()
    and user_name == user_name.lower()
):
    print('Correct')
else:
    print('Incorrect')

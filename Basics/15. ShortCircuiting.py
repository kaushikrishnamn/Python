# Short Circuiting => Checks the first condition and in case of or operator,
# if the first one is TRUE then the next expressions is not evaluated.

is_friend = True
is_user = False

if is_friend or is_user:
    print("You're friend")

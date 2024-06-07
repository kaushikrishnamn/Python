is_magician = True
is_expert = False

# check if magician and expert => "You are a master magician"
# check if magician but not expert => "At least you are getting there"
# check not a magician => "You need magic powers"

if is_magician and is_expert:
    print("You are a master magician")
elif is_magician and not is_expert:
    print("At least you are getting there")
elif not is_magician:
    print("You need magic powers")

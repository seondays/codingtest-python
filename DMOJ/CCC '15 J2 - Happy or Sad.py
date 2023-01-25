# https://dmoj.ca/problem/ccc15j2

input = input()
happy_emoji = ":-)"
sad_emoji = ":-("

if input.count(happy_emoji) > input.count(sad_emoji) :
    print("happy")
elif input.count(happy_emoji) < input.count(sad_emoji) :
    print("sad")
elif input.count(happy_emoji) == 0 and input.count(sad_emoji) == 0:
    print("none")
elif input.count(happy_emoji) == input.count(sad_emoji) :
    print("unsure")



s = input("Enter word: ")
w = list(s)
while len(w) != 0:
    x = input("enter a letter")
    if x == w[0] or w[1] or w[2] or w[3] or w[4]:
        print("1 of the letters is", x, "there are ", (len(w) - 1), "more to go")
        x = input("please enter another letter")
        len(w) - 1
    else:
        print("try once more")
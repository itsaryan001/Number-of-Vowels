def check_vowels():
    text = input('Enter your text: ')
    vowels = 0
    for v in text:
        if v == 'a' or v == 'e' or v == 'i' or v == 'o' or v == 'u':
            vowels += 1

    print(vowels)

    repeat = input('Want to check another text? "y" or "n": ').lower()

    if repeat == 'y':
        check_vowels()
    else:
        exit()


# Better code ;)

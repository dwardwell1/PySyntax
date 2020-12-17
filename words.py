def  print_upper_words(list, set):
    """ isolate each word in list and check it against the letters in the set """
    for word in list:
        for letter in set:
            if word[0] == letter:
                print(word.upper())


tester = ['apple', 'banana', 'carrot', 'dikon', 'elephant']
print_upper_words(tester,{'a','b','e'})
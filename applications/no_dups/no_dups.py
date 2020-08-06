def no_dups(s):
    # Your code here
    #split string into words
    #assign list for duplicate words
    #final string
    #add word to dups list if not already in there
    #combine dups list into string again
    words = s.split()
    dups = []
    string = ""
    for word in words:
        if word not in dups:
            dups.append(word)
    string += " ".join(dups)

    return string


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
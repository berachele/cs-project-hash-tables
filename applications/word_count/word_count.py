def word_count(s):
    # Your code here
    symbols = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&', '\r', '\n', '\t', '\\' ]
    #ignore spaces and symbols
    for i in symbols:
        s = s.replace(i, " ")
    #all lowercase
    s.lower()
    #split each word based on space, ignoring spaces as well
    words = s.lower().split()
    counter = {}
    for word in words:
        # word.lower()
        #add to counter if word is there
        if word not in counter:
            # print(f'{word}: only one')
            counter[word] = 0
            #otherwise counter is 1 for one appearance
        # print(f'{word}: Adding one')
        counter[word] += 1
    return counter



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('a a\ra\na\ta \t\r\n'))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))
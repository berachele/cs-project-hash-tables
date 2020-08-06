def word_count(s):
    # Your code here
    #ignore spaces and symbols
    #all lowercase
    #split each word based on space, ignoring spaces as well
        #add to counter if word is there
        #otherwise counter is 1 for one appearance
    symbols = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&', '\r', '\n', '\t', '\\' ]
    for i in symbols:
        s = s.replace(i, " ")
    s.lower()
    words = s.lower().split()
    counter = {}
    for word in words:
        if word not in counter:
            counter[word] = 0
        counter[word] += 1
    return counter



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('a a\ra\na\ta \t\r\n'))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))
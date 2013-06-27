def greet():
    name = raw_input("Enter your name: ")
    print "hello,", name
    
    name_copy = name
    
    print "goodbye, ", name

if __name__ == '__main__':
    greet()
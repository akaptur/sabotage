import sabotage
sabotage.assignment(__file__)

print "done sabotaging"
raw_input("Hit enter to continue")

def say_greeting():
    name = raw_input("Enter your name: ")
    print "hello,", name
    
    print "goodbye, ", name

if __name__ == '__main__':
    say_greeting()
# Mantra: Evey function is an object!

def yell(text):
    return text.upper()

def whisper(t):
    return t.lower() + '...'

# functions can be passed as arguments
def greet(func):
    greeting = func("Hello, stranger.")
    print(greeting)

# inner functions == closures. Local state == text parameter, is kept and used outside this context, in the call in main()
# closure is like configuring with text parameter
def get_speak_func(text, volume):
    def speak_quiet():
        return text.lower() + '...'
    def speak_loud():
        return text.upper()
    if volume > 0.5:
        return speak_loud
    else:
        return speak_quiet

def make_chain(s):
    def chain(x):
        return s + ' ' + x
    return chain


def main():  
    '''
    # Greeting using yell or whisper as parameter
    greet(yell)
    greet(whisper)

    # map, convert to list to see values
    m = map(yell, ('apple', 'pear', 'berry'))
    print(list(m))
    
    # return inner function references and call function with '()'
    speech = get_speak_func("I have a dream", 0.6)()
    print(speech)

    murmur = get_speak_func("I am Not SUre about THis", 0.1)()
    print(murmur)
    
    # chain strings
    intro = make_chain("My name is")
    intro_john = intro("John")
    print(intro_john)
    print(intro("Step"))
    '''

if __name__ == "__main__":
    main()

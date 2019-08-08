def break_words(stuff):
    """Takes a string in input, breaks where there are spaces, returns single words"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sort the words that are arcument of the function"""
    return sorted(words)

def print_first_word(words):
    """Print first word after popping it off"""
    first_word = words.pop(0)
    print(first_word)

def print_last_word(words):
    """Print first word after popping it off"""
    last_word = words.pop(-1)
    print(last_word)

def sort_sentence(sentence):
    """Returns sorted words from sentence"""
    words = break_words(sentence)
    sorted_words = sort_words(words)
    return sorted_words

def print_first_and_last(sentence):
    """Prints first and last word of a sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(worqds)

def print_first_and_last_sorted(sentence):
    """Prints first and last word of a previously sorted sentence"""
    sorted_words = sort_sentence(sentence)
    print_first_word(sorted_words)
    print_last_word(sorted_words)
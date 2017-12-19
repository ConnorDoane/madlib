from mad_libs import *

mad_libs = ["Christmas", "Thanksgiving", "Graduation", "Amusement Park"]

def introduction():
    return """
    WELCOME TO MAD LIB INTERACTIVE
    I will ask you for a few types of words
    then, after I have enough I will
    fill out a Mad Lib for you and
    give it back to you! To start,
    Which Mad Lib would you like to fill out?

    \t1. Christmas
    \t2. Thanksgiving
    \t3. Graduation
    \t4. Amusement Park
    """

def select_mad_lib():
    user_selection = int(raw_input("\t> "))
    if user_selection in range(1, len(mad_libs)+1):
        user_selection = user_selection-1
        return user_selection
    else:
        return "ERROR: Try inputting an integer"

def run(mad_lib):
    if mad_lib == 0:
        return christmas_output(fill_out_christmas())
    elif mad_lib == 1:
        return thanksgiving_output(fill_out_thanksgiving())
    elif mad_lib == 2:
        return graduation_output(fill_out_graduation())
    elif mad_lib == 3:
        return amusement_output(fill_out_amusement())
    else:
        return "ERROR"

def fill_out_amusement():
    words = []
    for i in amusement_word_types:
        print "Give me a", i
        answer = raw_input('> ')
        if answer == 'test_inputs':
            return amusement_example
        else:
            words.append(answer)
    return words

def fill_out_graduation():
    words = []
    for i in graduation_word_types:
        print "Give me a", i
        answer = raw_input("> ")
        if answer == 'test_inputs':
            return graduation_example
        else:
            words.append(answer)
    return words

def fill_out_thanksgiving():
    words = []
    for i in thanksgiving_word_types:
        print "Give me a", i
        answer = raw_input('> ')
        if answer == 'test_inputs':
            return thanksgiving_example
        else:
            words.append(answer)
    return words

def fill_out_christmas():
    words = []
    for i in christmas_word_types:
        print "Give me a", i
        answer = raw_input('> ')
        if answer == 'test_inputs':
            return christmas_example
        else:
            words.append(answer)
    return words

def amusement_output(words):
    current_word = 0
    final = ''
    for i in range(0, len(amusement_blank)):
        if amusement_blank[i] == '@':
            final += u"\u001b[4m" + words[current_word] + u"\u001b[0m"
            current_word += 1
        else:
            final += amusement_blank[i]
    return final

def graduation_output(words):
    current_word = 0
    final = ''
    for i in range(0, len(graduation_blank)):
        if graduation_blank[i] == '@':
            final += u"\u001b[4m" + words[current_word] + u"\u001b[0m"
            current_word += 1
        else:
            final += graduation_blank[i]
    return final

def thanksgiving_output(words):
    current_word = 0
    final = ''
    for i in range(0, len(thanksgiving_blank)):
        if thanksgiving_blank[i] == '@':
            final += u"\u001b[4m" + words[current_word] + u"\u001b[0m"
            current_word += 1
        else:
            final += thanksgiving_blank[i]
    return final

def christmas_output(words):
    current_word = 0
    final = ''
    for i in range(0, len(christmas_blank)):
        if christmas_blank[i] == '@':
            final += u"\u001b[4m" + words[current_word] + u"\u001b[0m"]
            current_word += 1
        else:
            final += christmas_blank[i]
    return final
def letter_counter(string, type=None):
    if (type == 'c'):
        return {letter: str(string).count(letter) for letter in 'bcdfghjklmnpqrstvwxyz'}
    elif (type == 'v'):
        return {letter: str(string).count(letter) for letter in 'aeiou'}  
    return {letter: str(string).count(letter) for letter in 'abcdefghijklmnopqrstuvwxyz'}

def type_counter(string, type=None):    
    return sum(letter_counter(string, type).values())
    
def type_ratio(string, type=None):
    if (len(string) == 0):
        return 0
    return type_counter(string, type)/len(string)

def ttr(string):
    if (len(string) == 0):
        return 0
    ttr = len(set(string)) / len(string)
    return ttr
# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    input_IF=input()
    if input_IF[0]=="I":
        pattern=input().rstrip()
        text=input().rstrip()
        return (pattern, text)
    elif input_IF[0]=="F":
        with open("tests/06", 'r') as f:
            pattern=f.readline().rstrip()
            text=f.readline().rstrip()
            return (pattern, text)
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    pattern_length=len(pattern) 
    text_length=len(text)
    for i in range(pattern_length):
        pattern_hash+=ord(pattern[i])*pow(256,pattern_length-i-1)
        text_hash+=ord(text[i])*pow(256,pattern_length-i-1)
    pattern_hash%=101
    text_hash%=101
    occ = []
    for i in range(text_length-pattern_length+1):
        if pattern_hash==text_hash:
            if text[i:i+pattern_length]==pattern:
                occ.append(str(i))
        if i < text_length-pattern_length:
            text_hash=(text_hash-ord(text[i])*pow(256,pattern_length-1,101))%101
            text_hash=(text_hash*256+ord(text[i+pattern_length]))%101
            text_hash=(text_hash+101)%101
    # and return an iterable variable
    return occ


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))


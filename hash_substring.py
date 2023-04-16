# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    input_IF=input()
    if input_IF[0]=="I":
        pattern=input().rstrip()
        text=input().rstrip()
    elif input_IF[0]=="F":
        tests = "/tests/06" 
        with open(tests, 'r') as f:
            pattern=f.readline().rstrip()
            text=f.readline().rstrip()
    else:
        print("I/F error")
    return pattern,text
    
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
    pattern_hash=hash(pattern)
    text_length=len(text)
    text_hash=0
    for i in range(pattern_length):
        text_hash=text_hash*2 + ord(text[i])
    occ = []
    for i in range(text_length-pattern_length+1):
        if text_hash==pattern_hash:
            check=True
            for j in range(pattern_length):
                if text[i+j]!=pattern[j]:
                    check=False
                    break
            if check==True:
                occ.append(i)
        if i<(text_length-pattern_length):
            text_hash=(2*(text_hash-ord(text[i])*2**(pattern_length-1))+ord(text[i+pattern_length]))



    # and return an iterable variable
    return occ


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))



def part1(text):
    total_sum = 0
    i = 0
    while i>=0 and i<len(text):
        i = text.find("mul(",i)
        if i==-1:
            break
        i+=4

        # consecutive digits followed by comma
        # digit phase
        start_1 = i
        while i<len(text) and text[i].isdigit():
            i+=1
        if i-start_1<=0:
            continue
        if text[i]!=",":
            continue
        
        first_digit = int(text[start_1:i])
        i+=1
        start_2 = i
        while i<len(text) and text[i].isdigit():
            i+=1
        if i-start_2<=0:
            continue
        if text[i]!=")":
            continue
        second_digit = int(text[start_2:i])
        total_sum += first_digit * second_digit
    
    print(total_sum)

DO = 1
DONT = 2
MUL = 3
INVALID = 4

def myfind(text,i):
    a = text.find("do()",i)
    b = text.find("don't",i)
    c = text.find("mul(",i)

    if a!=-1 and b!=-1 and c!=-1:
        if a<b and a <c:
            return a,DO
        elif b<a and b<c:
            return b,DONT
        else:
            return c,MUL
    
    if a==-1 and b!=-1 and c!=-1:
        if b<c:
            return b,DONT
        else:
            return c,MUL
    
    if a!=-1 and b==-1 and c!=-1:
        if a<c:
            return a,DO
        else:
            return c,MUL

    if a==-1 and b==-1:
        if c==-1:
            return c,INVALID
        else:
            return c,MUL


def part2(text):
    total_sum = 0
    i = 0
    enabled = True

    while i>=0 and i<len(text):
        
        i,status = myfind(text,i)
        if status == INVALID:
            break
        if status == DO:
            i+=4
            enabled = True
            continue
        if status == DONT:
            enabled = False
            i+=7
        elif status == MUL and enabled:
            i+=4
            # consecutive digits followed by comma
            # digit phase
            start_1 = i
            while i<len(text) and text[i].isdigit():
                i+=1
            if i-start_1<=0:
                continue
            if text[i]!=",":
                continue
            
            first_digit = int(text[start_1:i])
            i+=1
            start_2 = i
            while i<len(text) and text[i].isdigit():
                i+=1
            if i-start_2<=0:
                continue
            if text[i]!=")":
                continue
            second_digit = int(text[start_2:i])
            total_sum += first_digit * second_digit
        else:
            i+=4

    print(total_sum)

if __name__ == "__main__":

    with open("3.txt") as f:
        text = f.read()

    part2(text)


            


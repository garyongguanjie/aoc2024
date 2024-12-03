def is_safe_fn(ls):
    is_increasing = ls[1]-ls[0]>0
    for i in range(len(ls)-1):
        diff = ls[i+1]-ls[i]
        if not is_increasing:
            diff*=-1
        if diff<1 or diff>3:
            return False
    return True

    
def part1():
    safe_count = 0

    with open("2.txt") as f:
        for line in f:
            ls = line.split()
            ls = [int(i) for i in ls]

                
            if is_safe_fn(ls):
                safe_count +=1

        print(safe_count)


def part2():
    safe_count = 0
    with open("2.txt") as f:
        for line in f:
            ls = line.split()
            ls = [int(i) for i in ls]
            # is there linear time here?
            # abit hard to write
            for i in range(len(ls)):
                new_ls = ls[:i] + ls[i+1:]
                if is_safe_fn(new_ls):
                    safe_count+=1
                    break
    print(safe_count)

if __name__ == "__main__":
    part2()
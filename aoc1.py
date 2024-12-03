def part1(lines):
    l1 = []
    l2 = []
    d=0

    for l in lines:
        a,b = l.strip().split()
        a,b = int(a),int(b)
        l1.append(a)
        l2.append(b)

    l1.sort()
    l2.sort()

    
    for i in range(len(l1)):
        d+=abs(l1[i]-l2[i]) 

    print(d)

def part2(lines):
    l1 = []
    count_d = {}

    s = 0

    for l in lines:
        a,b = l.strip().split()
        a,b = int(a),int(b)
        count_d[b] = count_d.get(b,0) + 1
        l1.append(a)

    for n in l1:
        s+= count_d.get(n,0) * n

    print(s)

if __name__ == "__main__":
    with open("1.txt") as f:
        lines = f.readlines()
    part2(lines)

        

def part1(lines):
    rows = len(lines)
    cols = len(lines[0])
    
    text = "XMAS"

    count = 0
    for i in range(rows):
        for j in range(cols):
            for di in range(-1,2):
                for dj in range(-1,2):
                    if not (di==0 and dj==0):
                        for x in range(4):
                            ni = i+di*x
                            nj = j+dj*x
                            if ni>=0 and ni<rows and nj>=0 and nj<cols:
                                letter = lines[ni][nj]
                                if letter != text[x]:
                                    break
                                if x==3 and letter==text[x]:
                                    count +=1
    print(count)

def part2(lines):
    count = 0
    rows = len(lines)
    cols = len(lines[0])

    # MAS
    for i in range(1,rows-1):
        for j in range(1,cols-1):
            if lines[i][j] == "A":
                left_top_corner = lines[i-1][j-1]
                right_top_corner = lines[i-1][j+1]
                left_bottom_coner = lines[i+1][j-1]
                right_bottom_coner = lines[i+1][j+1]

                n_diag = 0
                # \
                if left_top_corner=="M" and right_bottom_coner=="S" or left_top_corner=="S" and right_bottom_coner=="M":
                    n_diag+=1

                # \
                if right_top_corner=="M" and left_bottom_coner=="S" or right_top_corner=="S" and left_bottom_coner=="M":
                    n_diag+=1

                if n_diag == 2:
                    count+=1
    print(count)
                    

if __name__ == "__main__":
    with open("4.txt") as f:
        lines = f.read().split()
    
    part2(lines)

        

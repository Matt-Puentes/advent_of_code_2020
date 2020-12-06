lines = []
with open("input", "r") as f:
    lines = f.readlines()

def is_tree(x, y):
    index = x % (len(lines[y]) - 1)
    return(lines[y][index] == "#")


slope_counts = []
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
for slope in slopes:
    x = 0
    y = 0
    count = 0
    while y + 1 < len(lines):
        x += slope[0]
        y += slope[1]
        if(is_tree(x,y)):
            count += 1
    
    print(count)
    slope_counts.append(count)

print(slope_counts[0] * slope_counts[1] * slope_counts[2] * slope_counts[3] * slope_counts[4])

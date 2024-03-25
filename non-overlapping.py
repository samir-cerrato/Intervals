def non_overlapping(intervals):
    intervals.sort(key=lambda x: (x[1], x[0]))

    count = 0
    last = float('-inf') 
    
    for interval in intervals:
        ai, bi = interval
        if ai > last:
            count += 1
            last = bi
    
    return count


n = int(input()) 
for _ in range(n):
    input_line = input().split()
    intervals = []
    for i in range(0, len(input_line), 2):
        a, b = int(input_line[i]), int(input_line[i+1])
        intervals.append((a, b))
    result = non_overlapping(intervals)
    print(result)
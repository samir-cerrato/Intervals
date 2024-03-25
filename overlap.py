def overlap(intervals):
    points = []
    
    for interval in intervals:
        a, b = interval
        points.append((a, "start"))
        points.append((b + 1, "end")) 
    
    points.sort() 
    
    max_overlap = 0
    current_overlap = 0
    
    for point in points:
        if point[1] == "start":
            current_overlap += 1
        else:
            current_overlap -= 1
        max_overlap = max(max_overlap, current_overlap)
    
    return max_overlap


n = int(input())
for _ in range(n):
    input_line = input().split()
    m = len(input_line) // 2
    intervals = []
    for i in range(0, len(input_line), 2):
        a, b = int(input_line[i]), int(input_line[i+1])
        intervals.append((a, b))
    result = overlap(intervals)
    print(result)


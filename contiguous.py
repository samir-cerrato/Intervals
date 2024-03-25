def contiguous_interval(intervals):
    intervals.sort() 
    
    merged = [intervals[0]]
    
    for i in range(1, len(intervals)):
        current_interval = intervals[i]
        prev_interval = merged[-1]
        
        if current_interval[0] <= prev_interval[1]:  
            merged[-1] = (prev_interval[0], max(current_interval[1], prev_interval[1]))
        else:
            merged.append(current_interval)
    
    max_length = 0
    for interval in merged:
        max_length = max(max_length, interval[1] - interval[0])
    
    return max_length

n = int(input())  
for _ in range(n):
    input_line = input().split()
    m = len(input_line) // 2
    intervals = []
    for i in range(0, len(input_line), 2):
        a, b = int(input_line[i]), int(input_line[i+1])
        intervals.append((a, b)) 
    result = contiguous_interval(intervals)
    print(result)


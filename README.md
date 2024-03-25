# Intervals
Write three efficient algorithms that processes intervals. At least two
of them should be implemented via some type of greedy algorithm.

All three programs have the same input and output format. The input will begin with an integer
n ≤1000 denoting how many test cases. This is followed by n lines of an even number 2m (m ≤2000)
of whitespace separated integers:

a1 b2 a2 b2 a3 b3 . . . a_m b_m

Each pairs [ai, bi] denotes a closed interval where it is guaranteed that ai ≤bi for 1 ≤i ≤m. The
output will be a single integer per line denoting the answer to the following questions.

Problem 1:

Determine the maximum number of non-overlapping intervals.

Problem 2:

Find the maximum number of intervals that overlap at a single point (on x-axis).

Problem 3:

Compute the largest contiguous interval obtained by taking a union of some of the input intervals.

Sample Input:

4

1 3 0 2 3 4

0 3 1 2 1 3 4 4

0 2 3 4 5 6 3 6 2 4

1 1 1 2 1 3 1 4 1 5


Output 1:

2

2

3

1

Output 2:

2

3

3

5

Output 3:

4

3

6

4

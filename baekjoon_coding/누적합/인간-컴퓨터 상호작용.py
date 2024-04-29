import sys
import bisect
from array import array

def main():
    input = sys.stdin.read
    data = input().split()
    
    S = data[0]
    q = int(data[1])
    queries = data[2:]
    
    index_lists = [array('I') for _ in range(26)]
    for i, char in enumerate(S):
        index_lists[ord(char) - ord('a')].append(i)
    
    output = []
    for i in range(q):
        alpha, l, r = queries[i * 3], int(queries[i * 3 + 1]), int(queries[i * 3 + 2])
        alpha_index = ord(alpha) - ord('a')
        left_index = bisect.bisect_left(index_lists[alpha_index], l)
        right_index = bisect.bisect_right(index_lists[alpha_index], r)
        output.append(str(right_index - left_index))
    
    sys.stdout.write("\n".join(output) + "\n")

if __name__ == "__main__":
    main()

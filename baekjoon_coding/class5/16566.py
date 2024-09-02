import sys
import bisect
input=sys.stdin.readline
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x]) 
            return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootX] = rootY
def main():
    N, M, K = map(int, input().split())
    minsu = list(map(int, input().split()))
    chulsu = list(map(int, input().split()))
    minsu.sort()
    uf = UnionFind(M)
    for chulsu_card in chulsu:
        idx = bisect.bisect_right(minsu, chulsu_card)
        idx = uf.find(idx)
        print(minsu[idx])
        if idx + 1 < M:
            uf.union(idx, idx + 1)
if __name__=="__main__":
    main()
import sys
input=sys.stdin.readline

class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def build_tree(info):
        nodes={chr(i): Node(chr(i))for i in range(ord('A'), ord('A') + len(info))}
        for key, left, right in info:
            if not left== '.':
                nodes[key].left=nodes[left]
            if not right== '.':
                nodes[key].right=nodes[right]
        
        return nodes['A']
def pre_Trav(node, result):
    if node:
        result.append(node.key)
        pre_Trav(node.left, result)
        pre_Trav(node.right, result)
def in_Trav(node, result):
    if node:
        in_Trav(node.left, result)
        result.append(node.key)
        in_Trav(node.right, result)
        
def post_Trav(node, result):
    if node:
        post_Trav(node.left, result)
        post_Trav(node.right, result)
        result.append(node.key)
    



n=int(input())
info=[input().rstrip().split() for _ in range(n)]

root=build_tree(info)

result_pre=[]
result_in=[]
result_post=[]

pre_Trav(root,result_pre)
in_Trav(root, result_in)
post_Trav(root, result_post)

print("".join(result_pre))
print("".join(result_in))
print("".join(result_post))

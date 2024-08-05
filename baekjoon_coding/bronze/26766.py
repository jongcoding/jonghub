def print_hearts(n):
    heart = [
        " @@@   @@@ ",
        "@   @ @   @",
        "@    @    @",
        "@         @",
        " @       @ ",
        "  @     @  ",
        "   @   @   ",
        "    @ @    ",
        "     @     "
    ]
    
  
    heart_str = "\n".join(heart)
    
    result = (heart_str + "\n") * n
    
   
    result = result.rstrip("\n")
    
    print(result)

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    n = int(input().strip())
    print_hearts(n)

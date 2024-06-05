def ctc(HH, MM):
    
    start_h = 9
    start_m = 0

    h = HH - start_h
    m = MM - start_m
    
    total_m = h * 60 +m
    return total_m

HH, MM = map(int, input().split())

time = ctc(HH, MM)

print(time)

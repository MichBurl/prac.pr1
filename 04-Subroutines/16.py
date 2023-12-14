def f(detector):
#    if detector.count("+")>3: return True
    count=0
    for i in range(len(detector)):
        if count==3: return True
        if detector[i]=="+": count+=1
        else: count=0
    return False
print(f("+-+-+-+-"))
n = int(input())
for a in range(2,n+1):
    for b in range(2,a+1):
        for c in range(b,a+1):
            for d in range(c,a+1):
                if a**3 == b**3 +c**3 +d**3:
                    print('Cube = '+str(a)+', Triple = ('+str(b)+','+str(c)+","+str(d)+')')
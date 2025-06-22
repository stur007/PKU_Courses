n = int(input())
triple = []
ans = []
for i in range(n+1):
    triple.append(i**3)
for b in range(2,n):
        for c in range(b,n):
            for d in range(c,n):
                if (a := triple[b]+triple[c]+triple[d]) in triple:
                    ans.append([triple.index(a),b,c,d])
ans.sort()
for i in ans:
    print(f'Cube = {i[0]}, Triple = ({i[1]},{i[2]},{i[3]})')
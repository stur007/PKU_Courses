n, m =map(int, input().split())
grades = list(map(int,input().split()))
grades.sort()
differs = []
for i in range(1,n):
    differ = grades[i]-grades[i-1]
    differs.append(differ)
differs.sort()
print(sum(differs[0:n-m]))

##数学题，还是挺有意思
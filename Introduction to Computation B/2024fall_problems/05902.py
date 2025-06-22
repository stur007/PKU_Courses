t = int(input())
for _ in range(t):
     n = int(input())
     queue = []
     for _ in range(n):
         type, num = map(int,input().split())
         if type == 1:
             queue.append(num)
         else:
             if num == 0:
                 queue.pop(0)
             else:
                 queue.pop(-1)
     if queue:
         print(*queue,sep = ' ')
     else:
         print('NULL')
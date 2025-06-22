import time

# 逐个输出
start_time = time.time()
for i in range(1000):
    print(i)
end_time = time.time()
print(f"逐个输出的时间: {end_time - start_time:.6f} 秒")

# 分隔输出，便于观察
print("\n" + "="*40 + "\n")

# 合并输出
start_time = time.time()
print(" ".join(str(i) for i in range(1000)))
end_time = time.time()
print(f"合并输出的时间: {end_time - start_time:.6f} 秒")

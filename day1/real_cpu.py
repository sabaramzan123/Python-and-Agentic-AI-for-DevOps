import psutil
# print(psutil.cpu_times())
# print(psutil.cpu_percent(interval=1))

# print(dir(psutil))
# print(psutil.cpu_count())

# print(psutil.subprocess.__doc__)

#loops

threshold = float(input("Enter threshold: "))
for i in range(5):
    if psutil.cpu_percent(interval=1) > threshold:
        print("CPU is unhealthy")
    else:
        print("CPU is healthy")
  



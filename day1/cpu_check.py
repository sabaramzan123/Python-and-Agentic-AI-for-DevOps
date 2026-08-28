cpu = int(input("Enter CPU:  "))
if cpu > 50:
    print("CPU usage is high")
elif cpu > 20 and cpu < 50:
    print("Alert")
else:
    print("CPU usage is normal")
    
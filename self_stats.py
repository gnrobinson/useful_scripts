# Testing self on statistics
# Guy Robinson

running_count = 0
running_sum = 0
running_max = None
running_min = None

num = input("Enter number or done: ")

while num != "done":
    num = float(num)
    running_count = running_count + 1
    running_sum = num + running_sum

    if running_max == None:
        running_max = num
    elif running_max < num:
        running_max = num
    else:
        running_max = running_max

    if running_min == None:
        running_min = num
    elif running_min > num:
        running_min = num
    else:
        running_min = running_min
    num = input("Enter number or done: ")

print(running_count)
print(running_sum)
print(running_max)
print(running_min)

num = list(map(int, input("Enter numbers separated by spaces: ").split()))
max_start = 0
max_length = 1
start = 0
length = 1
for i in range(1, len(num)):
    if num[i] == num[i - 1] + 1:
        length += 1
    else:
        if length > max_length:
            max_length = length
            max_start = start
        start = i
        length = 1
if length > max_length: 
    max_length = length
    max_start = start
print("The longest contiguous sequence is:", list(num)[max_start:max_start + max_length])   
print("The length of the longest contiguous sequence is:", max_length)
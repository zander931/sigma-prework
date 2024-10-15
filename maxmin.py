# maxmin.py returns the highest and lowest numbers in an array without using max() or min()
# L3_Challenge_3:_Task_2

def max_min(arr):
    min = arr[0]; max = arr[0]
    # Comparison 
    for num in arr:
        if num < min:
            min = num
        elif num > max:
            max = num
    return [min, max]


tests = [[2,4,1,0,2,-1], [20,50,12,6,14,8], [100,-100]]

for index, my_list in enumerate(tests):
    [min, max] = max_min(my_list)
    print(f"List {index+1}: min value: {min}, max value: {max}")
    
def not_string(str):

    if (str[:3] != "not"):
         str = "not " + str
    
    return str
         

print(not_string("not fortnite"))

def swap(lst):
    min = 10000000000000000
    max = 0
    min_pos = 0
    max_pos = 0
    for i in range (0,len(lst)):

        if (lst[i] > max):
            max = lst[i]
            max_pos = i

        if (lst[i] < min):
            min = lst[i]
            min_pos = i
    lst[min_pos] = max
    lst[max_pos] = min

    return lst

nums = [5,2,3,4,1]

print(swap(nums))

def count_spaces(string):

    space_num = 0
    for i in range (0,len(string)):
        if string[i] == " ":
            space_num += 1
    return space_num
print(count_spaces("Ba Ba Ba Boom hear me"))

def sum67(nums):
    i = 0
    sum = 0
    while i < len(nums):
        if nums[i] == 6:
            while i < len(nums) and nums[i] != 7:
                i+=1
            i+=1
        else:
            sum+=nums[i]
            i+=1
    return sum
nums3 = [5,3,4,6,70,70,7] # = 12

print(sum67(nums3))

def minmaxdiff(nums):
    min = 100000000000000000000000000
    max = 0
    for val in nums:

        if val<min:
            min = val
        if val>max:
            max = val
    return max-min
nums4 = [1,2,3,4,5]
print (minmaxdiff(nums4))
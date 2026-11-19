# Joseph O'Sullivan

def total_odds(nums):

    """
    Given a list for ints as an input and returns the 
    total of the ints in the list.
    """
    sum = 0
    for val in nums:
        if val%2!=0:
            sum+=val
    return sum

def is_equal (thing1, thing2):
    """
    Tests to see if two strings are the same and returns True if they are
    or false if they are not
    """
    
    return thing1 == thing2

  

print(total_odds([1,2,3,4,5,8,7,9])) # 25
print(total_odds([2,4,6,7,8,9,10,36])) # 16
print(total_odds([87,-42,3,-67,100])) # 23

print(is_equal("yes","yes")) # True
print(is_equal("yes","no")) # False
print(is_equal("Nay","Yay")) # False
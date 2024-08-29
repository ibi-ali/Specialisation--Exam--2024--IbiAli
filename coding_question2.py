#From the hint the number of squares is the sum of the current number(x) squared
#plus all the previous numbers squared e.g. 3x3 => 3**2 + 2**2 + 1**2
#so recursion can be used as follows x**2 + num_squares(x-1)

def num_squares(x):
    if x == 1:
        return 1
    else:

        return x**2 + num_squares(x-1)
    
#Test case
print(num_squares(5)) 
# With 5, the answer should be 55
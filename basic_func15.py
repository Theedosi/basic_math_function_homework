from math import floor
def main(a, b):
    '''Find the remainder when a is divided by b and return it.
    
    Args:
        a (int): a number
        b (int): a number
        
    Returns:
        int: the result.
    '''
    s = a%b
    return floor(s)
print(main(23,5))
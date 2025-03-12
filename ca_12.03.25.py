def is_narc(n):
    """Check if a number is narc."""
    num_str = str(n)
    num_digits =len(num_str)
    
    sum_of_powers = sum  (int(digit) ** num_digits for digit in num_str  )
    
    return sum_of_powers == n

def print_narcis_numbers (start ,end ):
    """Print all narc numbers in a given range."""
    for num in range(start, end + 1):
        if is_narc(num):
            print(num)

print_narcis_numbers(1000, 5000)

"""
GIVEN CODE FOR CHANGES :
1.def is_narc(n)
2.   "Check if a number is narc."
3.   num_str == str(n)
4.   num_digits == len(num_str)
5.   
6.  sum_of_powers = sum(int(digit) *** num_digits for digit in num_str)
7.  
8. return sum_of_powers == n

9.def print_narcis_numbers(start end)
10.   "Print all narc numbers in a given range."
11.  for num in range(start, end + 1)
12.     if is_narcissistic(num)
13.        print(num)

15.print_narc_numbers(1000, 5000)"""
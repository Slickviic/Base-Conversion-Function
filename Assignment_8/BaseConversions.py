
import sys
import stdio

def base_2(n):

    '''
    Description: 
        Calculates the Base 2 conversions for any positive integer n
    Parameters:
        n: A positive integer
    Returns:
        A string of the posisitve integer n in base 2 format
    '''

    base = 2

    if n <= 0:
        return '0b0'
    else:
        return str(base_2(n // base)) + str(n % base)

def base_8(n):

    '''
    Description: 
        Calculates the Base 2 conversions for any positive integer n
    Parameters:
        n: A positive integer
    Returns:
        A string of the posisitve integer n in base 2 format
    '''

    base = 8

    if n <= 0:
        return '0o0'
    else:
        return str(base_8(n // base)) + str(n % base)

def base_16(n):

    '''
    Description: 
        Calculates the Base 2 conversions for any positive integer n
    Parameters:
        n: A positive integer
    Returns:
        A string of the posisitve integer n in base 2 format
    '''

    base = 16

    if n <= 0:
        return '0x0'
    else:
        digit = n % base
        
        if digit == 10:
            digit = 'a'
        elif digit == 11:
            digit = 'b'
        elif digit == 12:
            digit = 'c'
        elif digit == 13:
            digit = 'd'
        elif digit == 14:
            digit = 'e'
        elif digit == 15:
            digit = 'f'

        return str(base_16(n // base)) + str(digit)

def main():
    for i in range(1, len(sys.argv)):
        n = int(sys.argv[i])

        print('Base 10: ' + str(n))
        print('Base 2: ' + base_2(n))
        print('Base 8: ' + base_8(n))
        print('Base 16: ' + base_16(n))
        print()



if __name__ == '__main__': main()
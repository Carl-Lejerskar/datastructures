from Stack import stack

def isPalindrome(string):
    '''
    Input: A string
    Output: True/False depending on if the supplied string is a palindrome.
    '''

    i = 0
    midpoint = len(string)//2
    my_stack = stack()

    while i < midpoint:       # push each letter of the first half of the string
        my_stack.push(string[i])
        i += 1

    if len(string) % 2 != 0:  # if there is an odd amount of letters, skip the middle letter
        i += 1 
    
    while i < len(string):    # iterate through the second half of the string and compare the values to the values on the stack
        
        if my_stack.pop() != string[i]:
            return False
        i += 1

    return True

if __name__ == "__main__":

    word = "racecar"

    print("This should return True:", isPalindrome(word))

    word = "foo"

    print("This should return False:", isPalindrome(word))

# Remember, all submissions are being checked for plagiarism.
# Your recruiter will be informed in case suspicious activity is detected.

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    equal_sum = list()
    numbers = dict()
    num = list()
    
    # For loop to breakdown A, add the individual digits appending them to a 
    # dictionary so they can be checked later.
    # Uses a temporary list to do this. 
    for n in A:
        digits = str(n)
        numbers[digits] = numbers.get(digits, 0)
        for digit in digits:
            num.append(int(digit))
        z = sum(num)
        num.clear()
        numbers[digits] = numbers.get(digits, 0) + z

        # Checks if sums of each digit matches z, if so allows the addition.
        # Only if digits does not match the key to prevent an interation 
        # adding itself. 
        for key, val in numbers.items():
            if val == z and key != digits:
                equal_sum.append(int(key) + int(digits))

    # Tries to return max function if there is not one it returns -1.    
    try:
        return (max(equal_sum))
    except:
        return -1
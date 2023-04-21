# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # Define variables for letter counts and total.
    count_b = 0
    count_a = 0
    count_n = 0
    count_total = 0
    
    # run for loop iterating through S, counting any "A", "B", "N" to be used later. 
    for n in S:
        if n == "A":
            count_a += 1
        elif n == "B":
            count_b += 1
        elif n == "N":
            count_n += 1
        else:
            continue
    # while loop for when "BANANA" can be counted/subtracted from S,
    # each iteration removes the number of letters from their respective count acting as a subtraction.
    # Once the rule is false the total times the iteration has completed is returned. 
    while count_a >= 3 and count_b >= 1 and count_n >= 2:
        count_total += 1
        count_n -= 2
        count_a -= 3
        count_b -= 1
    return count_total
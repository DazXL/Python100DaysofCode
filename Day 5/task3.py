#Task 3 is about For Loops with Range

range(1, 10) #example of range function, it does nothing!

for number in range(1, 10): # Prints numbers between 1 and 9, it never prints the last number of the range.
    print(number)

# The Gauss Challenge using the For Loop with Range

gaussChallenge = 0
for number in range(1, 101):
    gaussChallenge += number # It will Loop and add up each number in the range.

print(gaussChallenge)
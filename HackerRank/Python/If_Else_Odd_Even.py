"""Task
Given an integer, n, perform the following conditional actions:"""


n = int(input().strip())

num_odd = n % 2 != 0
num_even = n % 2 == 0

if num_odd:
    print("Weird")
elif num_even & (2 < n < 5):
    print("Not Weird")
elif num_even & (6 < n < 20):
    print("Weird")
else:
    print("Not Weird")

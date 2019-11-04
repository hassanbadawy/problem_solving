# %% [markdown]
# 
# # Left - Asterisks Printing
# Example: Let’s print a triangle made of asterisks (‘*’) separated by spaces. The triangle
# should consist of n rows, where n is a given positive integer, and consecutive rows should
# contain 1, 2, . . . , n asterisks. For example, for n = 4 the triangle should appear as follows:
# ```python
# *
# * *
# * * *
# * * * *
# ```

# %%
n = 4
for i in range(1,n+1):
    print('* '*i)
    print('')

# %% [markdown]
# # Centered - Asterisks Printing
# Example: Let’s print a triangle made of asterisks (‘*’) separated by spaces and consisting
# of n rows again, but this time upside down, and make it symmetrical. Consecutive rows should
# contain 2n − 1, 2n − 3, . . . , 3, 1 asterisks and should be indented by 0, 2, 4, . . . , 2(n − 1)
# spaces. For example, for n = 4 the triangle should appear as follows:
# ```python
# * * * * * * *
#   * * * * *
#     * * *
#       *
# ```

# %%
n = 4
j = 0
for i in range(n, 0, -1):
    if j>0:
        print(' '*(2*j), end = '')
    print('* '*(2*i-1))
    j+=1

# %% [markdown]
# # Accumilative Sum

# %%
n = 10
result = 0
for i in range(n,0, -1):
    result +=i
print(result)


# %%
# Solve it recursivly
def acc_sum(n):
    if n==1:
        return 1
    else:
        return n + acc_sum(n-1)
print(acc_sum(10))

# %% [markdown]
# # The Fibonacci numbers 
# Example: The Fibonacci numbers 4
# form a sequence of integers defined recursively in the following way. 
# The first two numbers in the Fibonacci sequence are 0 and 1, 
# and each subsequent number is the sum of the previous two. 
# The first few elements in this sequence are: 0,
# 1, 1, 2, 3, 5, 8, 13. Let’s write a program that prints all the Fibonacci numbers, 
# not exceeding a given integer n.

# %%



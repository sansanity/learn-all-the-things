# Exercise: Array DataStructure
# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this


expenses = [2200, 2350, 2600, 2130, 2190]
# Question 1
print("The difference is: ", expenses[1] - expenses[0])

# Question 2
q2 = expenses[0:3]
print("The total expense is:", sum(q2))

# Question 3

# for x in expenses:
#     if x == 2000:
#         print("True")
#     else:
#         print("False")

q3 = [x for x in expenses if x == 2000]
print(q3) # Empty list represents no matches

# Question 4
expenses.append(1980)
print(expenses)

# Question 5
apr_refund = expenses[3] + 200

new_expenses = [apr_refund if x == 2130 else x for x in expenses]
print(new_expenses)

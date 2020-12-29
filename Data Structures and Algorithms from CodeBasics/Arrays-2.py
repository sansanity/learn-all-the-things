# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)


heroes=['spider man','thor','hulk','iron man','captain america']

# Question 1
print("The answer is: ", len(heroes))

# Question 2
heroes.append("black panther")
print(heroes)

# Question 3
heroes.pop()
heroes.insert(3, "black panther")
print(heroes)

# Question 4
# heroes.remove("hulk", "thor").insert(3, "doctor strange")
# q4 = [i for j, i in enumerate(heroes) if j not in range(1, 3)]
# q4 = map(lambda x: x is "thor" or "hulk", heroes)
# heroes = heroes[4:].append("spider man").remove("hulk", "thor")
# print(heroes[4:].append("spider man").remove("hulk", "thor"))

heroes[1:3] = ["doctor strange"]
print(heroes)

# Question 5
q5 = sorted(heroes)
print(q5)

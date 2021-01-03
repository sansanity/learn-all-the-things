# Question 1: nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
# a): What was the average temperature in first week of Jan
# b): What was the maximum temperature in first 10 days of Jan
# c)Figure out the data structure that is best for this problem

import pandas as pd 

df = pd.read_csv("nyc_weather.csv")
print(df)
# Q1a)
print(df[0:7])
print("The average of the first week of Jan is " + str(df["temperature(F)"].iloc[0:7].mean()) + "C.")
# Q1b)
print("The maximum temperature of the first 10 days of Jan was " + str(df["temperature(F)"].max()) + "C.")
# Q1c)
# Array, because we only need the elements to answer the problems


# Question 2: nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
# a) What was the temperature on Jan 9?
# b) What was the temperature on Jan 4?
# c) Figure out the data structure that is best for this problem

my_dict = dict()

with open("nyc_weather.csv", "r") as f:
    for line in f:
        split = line.split(",")
        try:
            my_dict[split[0]] = int(split[1])
        except:
            print("This row is not an integer. Ignore")

    # Q2a) 
    print("The temperature on Jan 9 was " + str(my_dict["Jan 9"]) + "C.")

    # Q2b)
    print("The temperature on Jan 4 was " + str(my_dict["Jan 4"]) + "C.")

#Q2c)
# Hash maps, because we need to map the key (date) to the value (temperature)


# Question 3: poem.txt Contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in python and print every word and its count as show below. 
# Think about the best data structure that you can use to solve this problem and figure out why you selected that specific data structure.

with open("poem.txt", "r") as f:
    for line in f:
        print(line)


# The best data structure is hashmaps, because you have to pair the frequency of each word's appearance with the word itself.
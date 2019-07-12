# Creating Lists and Dictionaries
# Save each of the following lists and dictionaries into variables. You will use them throughout the assignment.

# Eg. fav_colours = ...

# Create a list for each item below that contains the given information:

# your favourite colours
# the age of you and your siblings/cousins/friends
# flip a coin 5 times and record whether or not the result was 'heads'
# your three favourite performing artists
# Create a dictionary for each item below that contains the given information:

# three words and their definitions
# your favourite movie names and their year of creation
# three cities of the world and their population
# the names of your siblings/cousins/friends and their ages
# After you've done that you should run your code to make sure there aren't any syntax errors. 
# You should get in the habit of running your code after each step in order to catch any mistakes as soon as they're introduced.


#LISTS
fav_colours = ['Blue', 'White', 'Black', 'Purple']
ages = [25, 22, 21, 18, 16]
coin_flip = ["Heads", "Heads", "Tails", "Tails", "Heads"]
fav_artist = ["The Arkells", "The Tragically Hip", "Frank Turner", "Tool", "The Zac Brown Band"]

#Dictionaries
fav_movies={
   "Avatar": 2009,
   "The Dark Knight" : 2008,
   "Avengers: Endgame": 2019,
   "Dude Where's My Car?": 2000,
}

fav_cities={
    'Toronto': 2930000,
    'Bari': 324198,
    'Vancouver': 675218,
}

relatives={
    'Matthew': 22,
    'Will': 21,
    'Rhys': 18,
}

#Exercise 2
# Print out the last element of the list of your favourite colours.
# Note: do this in a way that would still work for a list of any size!
print(fav_colours[(len(fav_colours)-1)])

# Add a new city to the dictionary of cities and population.
fav_cities["New York City"] = 8623000
#print(fav_cities)

# Reverse the list of coin flips and save it.
coin_flip.reverse()
#print(coin_flip)

# Print out the population of one of the cities.
print(fav_cities["Toronto"])

# Print out a sentence about each item in the list of performing artists.:
for artist in fav_artist:
    print("I think that {} is awesome".format(artist))

print("\n\n\n")
#Exercise 3


# Print out the first two performing artists in that list.
print(fav_artist[0], fav_artist[1])

# For each of your favourite movies, print out a sentence about when the movie was released.
for movie, year in fav_movies.items():
    print("{} is a great movie, it came out in {}".format(movie, year))

# Sort and reverse the list of ages of your family. Save it and print it to the screen.
# See if you can sort and reverse the list on one line!

(ages.sort(reverse=True))
print(ages)

# Add "Beauty and the Beast" movie to your dictionary of movies information, but with a twist: the movie was released both in 1991 and in 2017. Print it out.
fav_movies["Beauty and the Beast"] = [1991, 2017]
print(fav_movies)

print("\n\n\n")
#Exericise 4
#Print out all of the ages of your friends/family that are less than 30 (or any number where some ages will not be printed!).
for name, age in relatives.items():
    if age < 22:
        print(name)

# Find and output the age of the oldest person in your friends/family list.
print(max(ages))


# Count how many times you flipped 'heads' using the coin flips list.
heads = 0
for result in coin_flip:
    if result == "Heads":
        heads+=1

print(heads)

# You realize one of the performing artists in your list is no longer a favourite. Remove one of them from the list.
fav_artist.remove("The Zac Brown Band")
print(fav_artist)

# Pick a city in your city population dictionary and change its population.
fav_cities["Bari"]=350000
print(fav_cities)

print("\n\n\n")
# Find the sum total of the population in the dictionary of cities.
total_pop=0
for city, pop in fav_cities.items():
    total_pop += fav_cities[city]
print(total_pop)

# Using your dictionary containing the names of your family and friends with their ages, print out one of two messages for each depending on their age. For example:
# Martha is old.
# Stewart is young.
# Holly is young.

for name, age in relatives.items():
    if age > 21:
        print(f'{name} is allowed to drink in the USA')
    else:
        print(f'{name} cannot drink in the states')

# Print out the last two colours in your list of favourite colours.
print(fav_colours[(len(fav_colours)-1)], fav_colours[(len(fav_colours)-2)])

# Increase by 1 the age of everyone in your list of ages. Print it out.
for i in range(len(ages)):
    ages[i] +=1
print(ages)


# Add two new colours to your list of favourite colours.
fav_colours.append("Magenta")
fav_colours.append("Green")
print(fav_colours)

print("\n\n\n")

# Exercise 6
# Composing Lists and Dictionaries
# Make a new dictionary that contains a list of movies for each year. Each list of movies should be a list. Below is some data you can use.
movies_by_year = {
    1999: ['The Matrix', 'Star Wars: Episode 1', 'The Mummy'],
    2009: ['Avatar', 'Star Trek', 'District 9'],
    2019: ['How to Train Your Dragon 3', 'Toy Story 4', 'Star Wars: Episode 9']
}
print(movies_by_year)
# 1999: The Matrix, Star Wars: Episode 1, The Mummy
# 2009: Avatar, Star Trek, District 9
# 2019: How to Train Your Dragon 3, Toy Story 4, Star Wars: Episode 9


# Make a new list that contains each row of the buttons on a phone. Each row should be a list.
rows_on_phone = {
    1: [1,2,3],
    2: [4,5,6],
    3: [7,8,9],
    4: ['*',0,'#']
}
print(rows_on_phone)
# The rows on a phone are: 1 2 3, 4 5 6, 7 8 9, * 0 #


# Make a new list that contains information about three countries. Each country should be a dictionary that has a name, a continent, and whether or not it is an island.
countries_list = [{
    'name': 'Canada',
    'Continent': 'North America',
     'is_island': False
    },
    {'name': 'Australia',
     'Continent': 'Australia',
     'is_island': True
    },
    {'name': 'Italy',
     'Continent': 'Europe',
     'is_island': False
    }
]
print(countries_list)

print("\n\n\n")

# Exercise 7
# Output the message "I will not skateboard in the halls" 20 times.
# for i in range(20):
#     print("I will not skateboard in the halls")


# Create a list consisting of the above message. It should appear in the list 20 times.
skateboard= []

for i in range(20):
    skateboard.append("I will not skateboard in the halls")
# print(skateboard)
# print(len(skateboard))

# Create a list consisting of the numbers between 1 and 50.
nums = []
for i in range(1,51):
    nums.append(i)
print(nums)

# Use a for loop to find the sum of the numbers in the above list.
total_of_nums = 0
for i in nums:
    total_of_nums += i
print(total_of_nums)


# Create a new list which has three of each number up to 50.

# for i in range(1,50+1):
#     for x in range(1,4):
#         new_nums.append(i)
new_nums = [x for x in range(1,50+1) for y in range(3)]
print(new_nums)

# Ie. [1, 1, 1, 2, 2, 2, 3, 3, 3, ... , 50, 50, 50] and so on, up to 50.

# Make a new list out all of the countries from the dictionary in Exercise 6 that are not islands. Print out both lists.
new_countries_list = []
for entry in countries_list:
    if entry["is_island"] == False:
        new_countries_list.append(entry)
print(new_countries_list)

print("\n\n\n")

# Exercise 8
# You want to add up your expenses for the year. Create a list of numbers (integers or floats) that represents your expenses, eg:
# [250, 7.95, 30.95, 16.50]
# Add up the numbers and output the result.
# Put this code into a method. The method should take a list as an argument and return the sum of the expenses in the list. Call the method twice with different lists.

expenses1=[250, 7.95, 30.95, 16.50]
expenses2=[123,43,12,57.50, 129]

def exp_sum_calc(exp_list):
    total = 0
    for expence in exp_list:
        total += expence
    return(total)

print(exp_sum_calc(expenses1))
print(exp_sum_calc(expenses2))
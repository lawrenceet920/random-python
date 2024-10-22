# Ethan lawrence
# oct 22 2024
# random

# Part 1
import random
colors = ['Blue', 'Light Blue', 'Cyan', 'Sky Blue', 'Aqua']
print(colors[random.randrange(0, len(colors))])

# Part 2
animals = ['Cat', 'Lion', 'Tiger', 'Meerkat']
print(animals[random.randrange(0, len(animals))])
print(animals[random.randrange(0, len(animals))])
print(animals[random.randrange(0, len(animals))])

# part 3
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number_index = random.randrange(0,len(numbers))
print(f'{number_index} is the index for the number {numbers[number_index]}.')

print('\n ---------------------- \n')

# Part 4
fruits = ['apple', 'orange', 'cherry']
print(fruits[random.randrange(0, len(fruits)) - 1])

# Part 5
students = ['Ethan', 'Matthew', 'Trent', 'Dax', 'PJ']
len(students)
for x in students:
    print(f'{x} Scored a {random.randint(0, 100)}')

# Part 6

movies = ["Inception", "Titanic", "Avatar", "The Dark Knight", "Interstellar"]
movie_int = random.randint(0, len(movies) - 1)
print(f'{movie_int} is for {movies[movie_int]}')
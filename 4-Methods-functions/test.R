# Sample list
numbers <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Initialize an empty vector to store even numbers
even_numbers <- c()

# Iterate through the list with a for loop
for (number in numbers) {
  if (number %% 2 == 0) {
    even_numbers <- c(even_numbers, number)
  }
}

# Print the result
print(even_numbers)




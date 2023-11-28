#!/usr/bin/env ruby

# Extract the first command line argument
input_string = ARGV[0]

# Define the regular expression to match only capital letters
regex_pattern = /[A-Z]/

# Use scan method to find matches in the input string and join them
matches = input_string.scan(regex_pattern).join

# Print the matched portion
puts matches

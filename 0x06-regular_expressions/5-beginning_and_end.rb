#!/usr/bin/env ruby

# Extract the first command line argument
input_string = ARGV[0]

# Define the regular expression to match a string starting with 'h', ending with 'n',
# and having any single character in between
regex_pattern = /^h.n$/

# Use match method to find matches in the input string
match_result = input_string.match(regex_pattern)

# Print the matched portion if there is a match
puts match_result[0] if match_result

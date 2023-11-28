#!/usr/bin/env ruby

# Extract the first command line argument
input_string = ARGV[0]

# Define the regular expression to match a 10-digit phone number
regex_pattern = /^\d{10}$/

# Use match method to find matches in the input string
match_result = input_string.match(regex_pattern)

# Print the matched portion if there is a match
puts match_result[0] if match_result

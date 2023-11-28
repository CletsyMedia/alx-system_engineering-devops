#!/usr/bin/env ruby

# Extract the first command line argument
input_string = ARGV[0]

# Define the regular expression with a repetition token to match "hbt" with an optional 't'
regex_pattern = /hbt?n/

# Use the match method to find matches in the input string
match_result = input_string.match(regex_pattern)

# Print the matched portion
puts match_result ? match_result[0] : "No match"

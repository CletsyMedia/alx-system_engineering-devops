#!/usr/bin/env ruby

# Extract the first command line argument
input_string = ARGV[0]

# Define the regular expression with a repetition token to match "hbt" with an optional 't'
regex_pattern = /hbt{0,1}n/

# Use scan method to find matches in the input string
matches = input_string.scan(regex_pattern)

# Print the matches joined by a newline
puts matches.join

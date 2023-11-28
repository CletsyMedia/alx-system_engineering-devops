#!/usr/bin/env ruby

# Extract the first command line argument
input_string = ARGV[0]

# Define the regular expression to match "School"
regex_pattern = /School/

# Use scan method to find matches in the input string
matches = input_string.scan(regex_pattern)

# Print the matches joined by a newline
puts matches.join

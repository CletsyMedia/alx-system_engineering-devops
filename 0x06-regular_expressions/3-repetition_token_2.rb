#!/usr/bin/env ruby

# Extract the first command line argument
input_string = ARGV[0]

# Define the regular expression to match "hbtn" with 2 to 5 occurrences of 't' after 'b'
regex_pattern = /hbt+n/

# Use scan method to find matches in the input string
matches = input_string.scan(regex_pattern)

# Print the matches joined by a newline
puts matches.join

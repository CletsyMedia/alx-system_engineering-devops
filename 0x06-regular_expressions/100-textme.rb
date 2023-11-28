#!/usr/bin/env ruby

# Extract the first command line argument
input_string = ARGV[0]

# Define the regular expression to extract sender, receiver, and flags
regex_pattern = /\[from:(?<sender>[\w\+\-\:\s]+)\] \[to:(?<receiver>[\w\+\-\:\s]+)\] \[flags:(?<flags>[\d\:\-\s]+)\]/

# Use match method to find matches in the input string
match_result = input_string.match(regex_pattern)

# Print the extracted information
puts "#{match_result[:sender]},#{match_result[:receiver]},#{match_result[:flags]}" if match_result

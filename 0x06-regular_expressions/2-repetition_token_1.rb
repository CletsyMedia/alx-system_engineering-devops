#!/usr/bin/env ruby
# This Ruby script accepts a string as a command line argument and uses a regular expression
# to match instances of "hbtn" with an optional 't'. The script then prints the matched portions
# by joining the results. The regular expression uses the '?' quantifier to allow for zero or
# one occurrence of the character 't' after 'b'. This concise script efficiently handles the
# specified pattern, providing a clear and readable solution.
puts ARGV[0].scan(/hb?tn/).join

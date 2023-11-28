#!/usr/bin/env ruby
# Matches instances of "hbtn" with 2 to 5 occurrences of 't' after 'b'
puts ARGV[0].scan(/hbt+n/).join

#!/usr/bin/env ruby

# Check if the argument matches the regular expression /School/
def match_school(argument)
  regex = /School/
  if regex.match(argument)
    puts argument
  else
    puts "$"
  end
end

# Check if there is exactly one command-line argument
if ARGV.length == 1
  match_school(ARGV[0])
else
  puts "Usage: #{$PROGRAM_NAME} <string>"
end

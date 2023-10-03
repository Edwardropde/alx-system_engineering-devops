#!/usr/bin/env ruby

# Check if the argument matches the regular expression /h(b|t)+n/
def match_pattern(argument)
  regex = /h(b|t)+n/
  if regex.match(argument)
    puts argument
  else
    puts "$"
  end
end

# Check if there is exactly one command-line argument
if ARGV.length == 1
  match_pattern(ARGV[0])
else
  puts "Usage: #{$PROGRAM_NAME} <string>"
end

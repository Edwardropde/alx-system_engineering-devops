#!/usr/bin/env ruby

# Check if the argument matches the regular expression for a 10-digit phone
def match_phone_number(argument)
  regex = /^[0-9]{10}$/
  if regex.match(argument)
    puts "#{argument}$"
  else
    puts "$"
  end
end

# Check if there is exactly one command-line argument
if ARGV.length == 1
  match_phone_number(ARGV[0])
else
  puts "$"
end

#!/usr/bin/env ruby

# Check if the argument contains capital letters and print them
def match_capital_letters(argument)
  regex = /[A-Z]/
  capital_letters = argument.scan(regex).join
  puts capital_letters
end

# Check if there is exactly one command-line argument
if ARGV.length == 1
  match_capital_letters(ARGV[0])
else
  puts "$"
end

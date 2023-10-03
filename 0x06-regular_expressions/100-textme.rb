#!/usr/bin/env ruby

# Extract sender, receiver, and flags from the text message log
def extract_info(log)
  sender = log.match(/\[from:([^\]]+)\]/)
  receiver = log.match(/\[to:([^\]]+)\]/)
  flags = log.match(/\[flags:([^\]]+)\]/)

  if sender && receiver && flags
    puts "#{sender[1]},#{receiver[1]},#{flags[1]}"
  else
    puts "Invalid log format"
  end
end

# Check if there is exactly one command-line argument
if ARGV.length == 1
  extract_info(ARGV[0])
else
  puts "Usage: #{$PROGRAM_NAME} 'text_message_log'"
end

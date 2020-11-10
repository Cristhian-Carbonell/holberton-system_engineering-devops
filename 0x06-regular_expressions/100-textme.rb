#!/usr/bin/env ruby
print ("#{ARGV}").scan(/(?<=\[from:)(.*?)\]/).join + ','
print ("#{ARGV}").scan(/(?<=\[to:)(.*?)\]/).join + ','
puts ("#{ARGV}").scan(/(?<=\[flags:)(.*?)\]/).join

#!/usr/bin/env ruby
m1 = ("#{ARGV}").scan(/[H]olberton/)
m2 = m1.map(&:inspect).join('')
m2.gsub! /"/, ''
puts m2

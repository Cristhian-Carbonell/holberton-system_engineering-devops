#!/usr/bin/env ruby
m1 = ("#{ARGV[0]}").scan(/^\d{10,10}$/) #ARGV le los argumentos de la linea de comandos de bash
m2 = m1.map(&:inspect).join('') #lo convierte de matriz a string
m2.gsub! /"/, ''   #Quita las comillas dobles
puts m2
#!/usr/bin/env ruby
m1 = ("#{ARGV}").scan(/h(?>bt{1,}n|bn)/) #ARGV le los argumentos de la linea de comandos de bash
m2 = m1.map(&:inspect).join('') #lo convierte de matriz a string
m2.gsub! /"/, ''   #Quita las comillas dobles
puts m2
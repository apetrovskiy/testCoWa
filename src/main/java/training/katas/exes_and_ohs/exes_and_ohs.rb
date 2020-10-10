def XO(str)
    #your code here
    lower_cased = str.downcase
    lower_cased.split('').select { |chr| chr == 'x' }.length == lower_cased.split('').select { |chr| chr == 'o' }.length
end

puts XO('aaa')
puts XO('xo')
puts XO('XO')
puts XO('xo0')
puts XO('xxxoo')
puts XO("xxOo")

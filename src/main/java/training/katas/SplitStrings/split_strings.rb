def solution(str)
  if str.length == 0
    []
  end
  result = []
  (0..str.length - 1).step(2).each do |index|
    char1 = str[index]
    char2 = index + 1 < str.length ? str[index + 1] : '_'
    result.push(char1 + char2)
  end
  result
end

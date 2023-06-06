def convert_text(n):
  word = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
  text = []
  for num in str(n):
    # print(num)
    text.append(word[int(num)])
  return " ".join(text)
  
n = int(input())

print(convert_text(n))
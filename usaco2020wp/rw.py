_input = open('word.in', 'r')
output = open('word.out', 'w')

input_lines = []
textLength = 0


for line in _input:
    input_lines.append(line.rstrip())

nums = input_lines[0]
essayText = input_lines[1]
maxChars = int(nums.split()[1])
currentLineChars = 0



for i in essayText.split():
    currentLineChars = currentLineChars + len(i)
    if currentLineChars <= maxChars:
        output.write("%s " % i)
    elif currentLineChars > maxChars:
        output.write("\n%s " % i)
        currentLineChars = len(i)

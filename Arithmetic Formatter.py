import re

def arithmetic_arranger(problems, solve = False):
  if len(problems) > 5:
    return "Error: Too many problems."

  line1 = ""
  line2 = ""
  line3 = ""
  line4 = ""

  length = len(problems)
  i = 1
  for prob in problems:
    (operand1, operator, operand2) = prob.split(" ")
    if not re.search(r"^[+-]$", operator):
      return "Error: Operator must be '+' or '-'."
    if not (re.search(r"^\d+$", operand1) and re.search(r"^\d+$", operand2)):
      return "Error: Numbers must only contain digits."
    if len(operand1) > 4 or len(operand2) > 4:
      return "Error: Numbers cannot be more than four digits."

    result = None
    if operator == "+":
      result = str(int(operand1) + int(operand2))
    else:
      result = str(int(operand1) - int(operand2))

    max_length = max(len(operand1), len(operand2)) + 2

    spacing = "    "
    def space1(x):
      count = max_length - len(x)
      space = ""
      while count > 0:
        space += " "
        count -= 1
      return space

    def space2(x):
      count = max_length - 1 - len(x)
      space = ""
      while count > 0:
        space += " "
        count -= 1
      return space

    def dash(x):
      dash = ""
      while x > 0:
        dash += "-"
        x -= 1
      return dash

    if i != length:
      line1 += space1(operand1) + operand1 + spacing
      line2 += operator + space2(operand2) + operand2 + spacing
      line3 += dash(max_length) + spacing
      if solve:
        line4 += space1(result) + result + spacing
    else:
      line1 += space1(operand1) + operand1 + "\n"
      line2 += operator + space2(operand2) + operand2 + "\n"
      if not solve:
        line3 += dash(max_length)
      if solve:
        line3 += dash(max_length) + "\n"
        line4 += space1(result) + result
    i += 1

  if solve:
    return line1 + line2 + line3 + line4
  else:
    return line1 + line2 + line3

# Example
print(arithmetic_arranger(['3801 - 2', '123 + 49']))

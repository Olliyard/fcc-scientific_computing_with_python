def arithmetic_arranger(problems, answer=False):
  #Check if too many problems have been passed
  if(len(problems) > 5):
    return "Error: Too many problems."

  first_number = []
  second_number = []
  operator = []

  #Split the problem into first number, operator and second number
  for problem in problems:
    parts = problem.split()
    first_number.append(parts[0])
    operator.append(parts[1])
    second_number.append(parts[2])

  #Check for allowed operator
  if('*' in operator or '/' in operator):
    return "Error: Operator must be '+' or '-'."

  #Check if first_number and second_number only contain digits
  for i in range(len(first_number)):
    if not(first_number[i].isdigit() and second_number[i].isdigit()):
      return "Error: Numbers must only contain digits."

    elif (len(first_number[i]) > 4 or len(second_number[i]) > 4):
      return "Error: Numbers cannot be more than four digits."


  line1 = []
  line2 = []
  line3 = []
  line4 = []
  

  #Create first row (first_number)
  for i in range(len(first_number)):
    if(len(first_number[i]) > len(second_number[i])):
      line1.append(f"  {first_number[i]}")
    else:
      dif = (len(second_number[i]) - len(first_number[i]) + 2) + len(first_number[i])   #Check the difference between the biggest and smallest number and add 2 for formatting
      line1.append(f"{first_number[i]:>{dif}}")


  #Create second row (second_number)
  for i in range(len(second_number)):
    if(len(second_number[i]) > len(first_number[i])):
      line2.append(f"{operator[i]} {second_number[i]}")
      
    else:
      dif = (len(first_number[i]) - len(second_number[i]) + 1) + len(second_number[i])  #Check the difference between the biggest and smallest number and add 1 for formatting
      line2.append(f"{operator[i]}{second_number[i]:>{dif}}")  
      
  #Create third row (-)
  for i in range(len(first_number)):
    maxlen = (max(len(first_number[i]), len(second_number[i])) + 2)
    line3.append(f"{'':{'-'}>{maxlen}}")
  
  if answer:
    for i in range(len(first_number)):
      if operator[i] == "+":
        answer = str(int(first_number[i]) + int(second_number[i]))
      else:
        answer = str(int(first_number[i]) - int(second_number[i]))

      #Answer is longer than the other numbers length.
      if len(answer) > max(len(first_number[i]), len(second_number[i])):
        line4.append(f" {answer}")
      else:
        max_val = max(len(first_number[i]), len(second_number[i]))
        maxlen = 2*max_val - len(answer) + 2
        line4.append(f"{answer:>{maxlen}}")

        
    arranged_problems = "    ".join(line1) + "\n" + "    ".join(line2) + "\n" + "    ".join(line3) + "\n" + "    ".join(line4)
  else:
    arranged_problems = "    ".join(line1) + "\n" + "    ".join(line2) + "\n" + "    ".join(line3)
  
  return arranged_problems

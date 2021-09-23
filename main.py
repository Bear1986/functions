
# step 1: get the code working
print("*" * 17)
print("*", "Hello, World!", "*")
print("*" * 17)

print()

# step 2: make var for repeated values

length = 17
surround = "*"
text = "Hello, World!"

print(surround * length)
print(surround, text, surround)
print(surround * length)

print()

# step 3: write the functions. N.B remember to remove your var before you call your function

def header (text, surround):

  length = 17
  # surround = "*"
  # text = "Hello, World"

  print(surround * length)
  print(surround, text, surround)
  print(surround * length)

header("Hello, World!", "*")

print()

# step 4: make it able to take more paramotors 

def header (text, surround):

  length = len(text) + 4
  # surround = "*"
  # text = "Hello, World"

  print(surround * length)
  print(surround, text, surround)
  print(surround * length)

header("Hello, World!", "*")

print()

# example 1
header("Python Rocks", "!")
print()

# example 2
header("Coders 4 ever", "+")
print()

# when you have the desired output finnish your program with a main function
def main():
  header("Hello, World!", "*")
  print()
  header("Python Rocks", "!")
  print()
  header("Coders 4 ever", "+")
  print()
# then call the main
main()



##############################################################################

# Writing Your Own Functions Checklist:

#1 Understand what to implement: begin with an example test case.

#2Test the code: run the code to ensure the output matches the target example test case.

#3 Make variables for repeated values: any values in your code that repeat, replace with variables. 

#4 Identify the parameters: the variables that you expect to change when you call the function will become the parameters.

#5 Write the function signature,  or define the first line of the function.
#6 Substitute in parameters: finish implementing the function’s body by changing the variables over to parameters by identifying which variables should become which parameters and aligning the names to match. Don’t forget to indent!

#6 Test the function by calling it from main (or below the function definitions) with the same example test case from the first step.

#7 Test the function some more by using parameters other than the original test case. If the output doesn’t exactly match the example output for each test case, refine the implementation.

##############################################################################

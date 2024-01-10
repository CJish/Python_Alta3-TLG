import random

tlgstudents = ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Josey', 'Winton', 'Xiuxiang', 'Yaping']

wordbank = ["indentation", "spaces"]

wordbank.append(4)

num = int(input('Please enter a number between 0 and 20'))
        
student_name = tlgstudents[num]

print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent")

print("And now a randomly-chosen name")

num_max = len(tlgstudents)

num =  random.randrange(0 , num_max)

print(tlgstudents[num])

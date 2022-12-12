#oo scary
'''
Instructions:
We're now experts at classes, right?
Yeah?
mkay so do me a favor
Create the class student
every student has these traits:
name
student id (you can pick this number arbitrarily)
year (f/s/j/s)
major
gpa

create a function to see if the student is eligible for the honors program
to be eligible they need to have a gpa above 3.5
return true if they can and false if they cant, and print it out

create a function because this college is a wacky one- every day they generate a student id and if the student id matches a student, that student gets free food that day. 
1. generate a random number the length of however long you choose to make the id number
2. compare if the random number matches your student's id
3. if it matches print out "winner! student (name) gets free lunch!"
4. if not, print "Loser!"
(disclosure: obviously there's a very small chance of your generated number matching the student id number. I just want to see that you're generating and comparing properly)
'''

import random


class student:
    def __init__(self, name, student_id, year, major, gpa):
        self.name = name
        self.student_id = student_id
        self.year = year
        self.major = major
        self.gpa = gpa

    def is_eligible_for_honors(self):
        if self.gpa > 3.5:
            print("{self.name} is eligible for honors.")
        else:
            print({"{self.name} is not eligible for honors."})

    def get_free_food(self):
        random_id = random.randint(1, 100000)
        if random_id == self.student_id:
            print("Winner! Student {self.name} gets free lunch!")
        else:
            print("Loser!")


def main():
    # create three students and check if they get free lunch and if they qualify for honors
    s1 = student("Vhani", 11111, "Freshman", "Psychology", 3.7)
    s1.is_eligible_for_honors()
    s1.get_free_food()

    s2 = student("Olivia", 32993, "Senior", "Biomedical Science", 1.9)
    s2.is_eligible_for_honors()
    s2.get_free_food()

    s3 = student("Ava", 69420, "Sophomore", "Philosophy", 2.5)
    s3.is_eligible_for_honors()
    s3.get_free_food()

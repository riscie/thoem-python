class student:
    def __init__(self):
        self.name = "Mario"
        self.grade = 6

    def update(self, name, grade):
        self.name = name
        self.grade = grade

    def introduce_yourself(self):
        print(f'Hi, my name is {self.name}, my grade is {self.grade}')


# self?
# python decided to do methods in a way that makes the instance to which the method belongs be passed automatically, but not received automatically.
# the first parameter of methods is the instance the method is called on.
# That makes methods entirely the same as functions, and leaves the actual name to use up to you (although self is the convention, and people will generally frown at you when you use something else.)
# self is not special to the code, it's just another object.

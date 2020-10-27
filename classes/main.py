from student import student

if __name__ == '__main__':
    # create a new Student object
    student = student()
    # call introduce_yourself on that object
    student.introduce_yourself()

    # update the student object directly
    student.grade = 4
    # call introduce_yourself on that object
    student.introduce_yourself()

    # update the student object using our update function
    student.update("Luigi", 5.9)
    # call introduce_yourself on that object
    student.introduce_yourself()

    

# if __name__ == '__main__': ?
# Anything that comes after if __name__ == '__main__': will be run only when you explicitly run your file.
# python myfile.py
# However, if you import myfile.py elsewhere:
# import myfile
# Nothing under if __name__ == '__main__': will be called.

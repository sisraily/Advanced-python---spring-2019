"""
File main.py
-the user interface for the Student class.
This file was modfied to only test overloading methods within the class. The other code was commented out. 

"""
from student import Student

def main():
    # construct a Student object with name Aaron, and space for 5 test scores
    student1 = Student("Aaron", 5)

    # constructs a second object of type Student with space for 9 test scores.
    student2 = Student("Karen", 9)


    # Compares the two objects by using the overloading operators.
    # In this case the names of the students are compared.
    # Since the names are a string, the evaluation by comparing the strings
    # the ascii values, by checking if one name has a higher value than the other.
    print("student1 < student2: {}".format(student1 < student2))
    print("student1 <= student2: {}".format(student1 <= student2))
    print("student1 > student2: {}".format(student1 > student2))
    print("student1 <= student2: {}".format(student1 <= student2))
    print("student1 == student2: {}".format(student1 == student2))




    # set the scores for each test
    #student1.setScore(1, 100)
    #student1.setScore(2, 89)
    #student1.setScore(3, 95)
    #student1.setScore(4, 72)
    #student1.setScore(5, 85)

    # printing the student1 object displays a string representation of the object
    # Same as calling student1.__str__()
    #print("Student with test scores: ", student1)
    #print("")

    # Test the rest of the accessor functions in the Student class
    #print("Test summary for ", student1.getName(), ":")
    #print("High score: ", student1.getHighScore())
    #print("Average score: ", student1.getAverage())
    #print("Third test score: ", student1.getScore(3))



main()



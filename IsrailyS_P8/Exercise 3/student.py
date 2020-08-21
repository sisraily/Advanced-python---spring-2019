"""
File student.py
Manages a student's name and test scores.
Overload operators included and compare the ascii values of the names. 
"""

class Student():
    """Represents a student."""


    def __init__(self, name, number):
        """Constructor creates a Student with the given name
        and number of scores and sets all scores to 0."""
        self.__name = name
        self.__scores = []
        for count in range(number):
            self.__scores.append(0)



    def __lt__(self, student):
        """Returns True if the ascii value of the name to the left is
        less than the name to the right"""
        return (self.getName() < student.getName())
    def __le__(self, student):
        """Returns True if the ascii value of the name to the left is
        less than or equal to the name to the right"""
        return (self.getName() <= student.getName())
    def __gt__(self, student):
        """Returns True if the ascii value of the name to the left is
        more than the name to the right"""
        return (self.getName() > student.getName())
    def __ge__(self, student):
        return (self.getName() >= student.getName())
        """Returns True if the ascii value of the name to the left is
        more than or equal to the name to the right"""
    def __eq__(self, student):
        """Returns True if the ascii value of the name to the left is
        equal to name to the right"""
        return (self.getName() == student.getName())
        
        

    def getName(self):
        """Returns the student's name."""
        return self.__name

    def setScore(self, i, score):
        """Resets the nth score, counting from 1"""
        self.__scores[i-1] = score

    def getScore(self, i):
        """Returns the nth score, counting from 1"""
        return self.__scores[i-1]

    def getAverage(self):
        """Returns the average score"""
        return sum(self.__scores)/len(self.__scores)

    def getHighScore(self):
        """Returns the highest score"""
        return max(self.__scores)

    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.__name + "\nScores: " + " ".join(map(str, self.__scores))

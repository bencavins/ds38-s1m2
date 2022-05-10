import random


class Student:
    def __init__(self, id, age):
        self.id = id
        self.age = age
        self.assignments = []
        self.grades = []

    def turn_in_assignment(self, assignment):
        self.assignments.append(assignment)

    def calc_gpa(self):
        return sum(self.grades) / len(self.grades)


class BloomTechStudent(Student):
    def __init__(self, id, age, gca_score=0):
        super().__init__(id, age)
        self.gca_score = gca_score

    def flex(self):
        print('Student has flexed this class')
    
    def __repr__(self):
        return f'<BloomTechStudent id={self.id}, age={self.age}, gca={self.gca_score}>'


def student_generator():
    result = []
    for x in range(30):
        rand_id = random.randint(100000, 999999)
        rand_age = random.randint(18, 100)
        rand_gca_score = random.randint(300, 850)
        bs = BloomTechStudent(rand_id, rand_age, rand_gca_score)
        result.append(bs)
    return result

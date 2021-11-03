class GroupException(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def get_exception_message(self):
        return self.message


class Group:
    def __init__(self, students=None):
        if students is None:
            self.students = []
        else:
            self.students = students

    def add_student(self, student):
        try:
            if len(self.students) == 10:
                raise GroupException('There can be no more than 10 people in a group.')
        except GroupException as error:
            print(error.get_exception_message())
        else:
            self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def find_a_student(self, surname):
        for student in self.students:
            if student == surname:
                return f'{student}\n'

    def __str__(self):
        return "\n".join(self.students) + '\n'


harris = 'Harris Jessica'
ivanov = 'Ivanov Ivan'
adamson = 'Adamson Samuel'
evans = 'Evans Joseph'
smith = 'Smith Olivia'
walker = 'Walker Emily'
davies = 'Davies Thomas'
wilson = 'Wilson George'
king = 'King Lily'

group = [harris, ivanov, adamson, evans, smith, walker, davies, wilson, king]
group = Group(group)
print(group)
lewis = 'Lewis Isabella'
group.add_student(lewis)
print(group)
petrov = 'Petrov Petro'
group.add_student(petrov)
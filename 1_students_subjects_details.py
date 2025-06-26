class students:
    name = str
    roll_number = str
    marks = {'subject_name': 'marks'}

    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.marks = {}


    def add_marks(self, subject, mark):
        self.marks[subject] = mark

    def calculate_average(self):
        total = sum(self.marks.values())
        count = len(self.marks)
        average = total/count
        return average

    def display_details(self):
        print(self.name)
        print(self.roll_number)
        for subject, mark in self.marks.items():
            print(subject, mark)
        print("Average marks are = ",self.calculate_average())

      

student1 = students("Alice", "001")
student1.add_marks('Math', 98)
student1.add_marks('English', 92)

student1.display_details()


student2 = students("Apex", "002")
student2.add_marks('Math', 93)
student2.add_marks('English', 97)

student2.display_details()

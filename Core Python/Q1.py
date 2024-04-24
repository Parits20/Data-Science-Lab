import json

class StudentData;
    def __init__(self):
        self.students = self.data()

    def addstud(self , EnrollmentId , Contact):
        self.students[EnrollmentId] = {"Name" : name, "Contact" : contact}
        self.savedata()
        print("Added Successfully")

    def updatestud(self , EnrollmentId , name , contact):
        if EnrollmentId in self.students:
            self.students[EnrollmentId]["Name"] = name
            self.students[EnrollmentId]["Contact"] = contact
            self.savedata()
            print("Updated Successfully")
        else:
            print("Not found")

    def deletestud(self , EnrollmentId):
        if EnrollmentId in self.students:
            del self.students[EnrollmentId]
            self.savedata()
            print("Detailed Successfully")
        else:
            print("Not found")

    def displaystud(self):
        print("EnrollmentId\tName\tContact")
        for enrollmentId , details in self.students.items():
            print(f"{enrollmentId}\t{details['Name']}\t{details['Contact']}")

    def savedata(self):
        with open("")



import json

def add_student(dataset, enrollment_no, name, contact):
    dataset.append({"Enrollment No": enrollment_no, "Name": name, "Contact": contact})
    save_data(dataset)
    print("Student added successfully.")

def save_data(data):
    with open("students.json", "w") as fw:
        json.dump(data, fw)

def main():
    dataset = []

    # Load existing data if available
    try:
        with open("students.json", "r") as fr:
            dataset = json.load(fr)
    except FileNotFoundError:
        pass

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            enrollment_no = input("Enter Enrollment No: ")
            name = input("Enter Name: ")
            contact = input("Enter Contact No: ")
            add_student(dataset, enrollment_no, name, contact)

        elif choice == "2":
            print("Exiting program.")
            break

        else:
            print("Invalid choice! Please enter a valid option.")


if __name__ == "__main__":
    main()



import json

def add_student(enrollment_no, name, contact):
    student = {"Enrollment No": enrollment_no, "Name": name, "Contact": contact}
    students.append(student)
    save_data(students)
    print("Student added successfully.")

def save_data(data):
    with open("students.json", "w") as fw:
        json.dump(data, fw)

def load_data():
    try:
        with open("students.json", "r") as fr:
            return json.load(fr)
    except FileNotFoundError:
        return []

def main():
    global students
    students = load_data()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            enrollment_no = input("Enter Enrollment No: ")
            name = input("Enter Name: ")
            contact = input("Enter Contact No: ")
            add_student(enrollment_no, name, contact)

        elif choice == "2":
            print("Enrollment No\tName\tContact")
            for student in students:
                print(f"{student['Enrollment No']}\t{student['Name']}\t{student['Contact']}")

        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid choice! Please enter a valid option.")


if __name__ == "__main__":
    main()

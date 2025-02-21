def enroll_student(age):
    if 10 <= age <= 20:
        print("Student enrolled successfully!")
    else:
        print("Sorry, age must be between 10 and 20 years to enroll.")

# Example usage:
age = int(input("Enter student's age: "))
enroll_student(age)

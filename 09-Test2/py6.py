#Create a function f(years, course) that, for the data.json file, 
# returns the number of students who are at least the given number of years and have a grade average of at least 4 in the given course name. 
# Example:
#f(21, "statistics") 🡪 compare your result with other students

import json

def f(years, course):
    # Open and read the JSON file
    with open('E:\\GitHub\\pp1\\09-Test2\\data.json', 'r') as file:
        data = json.load(file)

        # Filter students based on criteria (age and grade)
        filtered_students = [student for student in data if student['age'] >= years and
                             any(course_data['name'] == course and min(course_data['grades']) >= 4
                                 for course_data in student['studies']['courses'])]

        # Count the number of filtered students
        count = len(filtered_students)
        
    return count

# Call the function with specified criteria
result = f(21, "statistics")
print(f"Number of students with at least 21 years and grade average >= 4 in 'statistics': {result}")
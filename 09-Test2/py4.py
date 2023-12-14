# The dictionary contains the names of subjects and the grades obtained. 
# Create a function f(subjects) that, for the given subjects and their grades, 
# returns the name of the subject for which the average grade is the highest. Example:
#f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}) 🡪 "comp"

def f(subjects):
    max_average = 0
    subject_with_highest_average = None

    for subject, grades in subjects.items():
        average_grade = sum(grades) / len(grades)
        
        if average_grade > max_average:
            max_average = average_grade
            subject_with_highest_average = subject

    return subject_with_highest_average

# Example usage:
result = f({"math": [3, 4, 4], "geo": [5, 4, 4, 4], "comp": [5, 4]})
print(result)  # Output will be "comp"

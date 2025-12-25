import pprint

def analyze_grades(students, passing_grade=60):
    # Your nested functions here
    grades = []

    passing = list(filter(lambda student: student['grade'] >= passing_grade, students))
    failing = list(filter(lambda student: student['grade'] < passing_grade, students))

    passing_students = [student['name'] for student in passing]
    failing_students = [student['name'] for student in failing]
    
    for student in students:
        grades.append(student['grade'])

    # Your main logic here
    def calculate_average():
        average = sum(grades)/len(grades)
        return average

    def count_passing():
        count = 0
        for student in students:
            if student['grade'] >= passing_grade:
                count += 1
        return count
    
    def get_top_student():
        top = max(students, key=lambda student: student['grade'])
        return top['name']

    calculate_average()
    count_passing()
    get_top_student()

    return {
        'average': calculate_average(),
        'passing_count': count_passing(),
        'failing_count': len(failing_students),
        'top_student': get_top_student(),
        'passing_students': passing_students,
        'failing_students': failing_students
    }


# Test cases
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 72},
    {'name': 'Charlie', 'grade': 55},
    {'name': 'Diana', 'grade': 90},
    {'name': 'Eve', 'grade': 45}
]

pprint.pprint(analyze_grades(students))
pprint.pprint(analyze_grades(students, passing_grade=70))
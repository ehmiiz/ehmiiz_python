"""
to return English 1010:
"""

def get_english_grade(student):
    return student['type']['student']['courses']['English_1010']['current_grade']

student = {
    "type": {
        "student": {
            "name": "Allan",
            "courses": {
                "math_1050": {
                    "current_grade": "B",
                },
                "English_1010": {
                    "current_grade": "A-",
                },
            },
        }
    }
}

get_english_grade(student)
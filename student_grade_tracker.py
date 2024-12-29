def get_grade_input():
    """Function to get grades from the user."""
    grades = []
    num_subjects = int(input("Enter the number of subjects or assignments: "))
    
    for i in range(num_subjects):
        grade = float(input(f"Enter grade for subject/assignment {i + 1}: "))
        grades.append(grade)
    
    return grades

def calculate_average(grades):
    """Function to calculate the average grade."""
    total = sum(grades)
    average = total / len(grades) if len(grades) > 0 else 0
    return average

def determine_letter_grade(average):
    """Function to determine the letter grade based on the average."""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def calculate_gpa(letter_grade):
    """Function to calculate the GPA based on the letter grade."""
    grade_to_gpa = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.0,
        'F': 0.0
    }
    return grade_to_gpa.get(letter_grade, 0.0)

def display_results(average, letter_grade, gpa):
    """Function to display the calculated results."""
    print(f"\nStudent Grade Summary:")
    print(f"Average grade: {average:.2f}")
    print(f"Letter grade: {letter_grade}")
    print(f"GPA: {gpa:.2f}")

def main():
    """Main function to drive the program."""
    print("Welcome to the Student Grade Tracker!")
    
    # Step 1: Get grades from the user
    grades = get_grade_input()
    
    # Step 2: Calculate average grade
    average = calculate_average(grades)
    
    # Step 3: Determine the letter grade
    letter_grade = determine_letter_grade(average)
    
    # Step 4: Calculate the GPA
    gpa = calculate_gpa(letter_grade)
    
    # Step 5: Display the results
    display_results(average, letter_grade, gpa)

# Run the program
if __name__ == "__main__":
    main()

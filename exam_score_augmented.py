# exam_score_augmented.py

def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else: # score < 60
        return "F"

def main():
    print("This program determines the letter grade from an exam score (0 - 100).\n")

    score = eval(input("Enter the exam score: "))

    letter_grade = grade(score)

    print(f"\nFor a score of {score}, the grade is {letter_grade}.")

main()
"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_subject_details(data)


def get_data():
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data.append(parts)
    print(data)
    return data
    input_file.close()


def display_subject_details(data):
    for subject_data in data:
        print(f"{subject_data[0]} is taught by {subject_data[1]:<12} and has {subject_data[2]:>3} students")


main()
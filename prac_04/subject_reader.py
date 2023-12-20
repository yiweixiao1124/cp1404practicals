"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    sunjects = get_sunjects()
    display_subject_details(sunjects)


def get_sunjects():
    sunjects = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)
        print(repr(line))
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        sunjects.append(parts)
    print(sunjects)
    input_file.close()
    return sunjects


def display_subject_details(sunjects):
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]:12} and has {subject[2]:4} students")


main()
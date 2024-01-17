from project import Project
import datetime


def main():
    MENU = "Menu:\n(L)oad projects \n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd  " \
           "project\n(U)pdate project\n(Q)uit"
    projects = get_file('projects.txt')

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Enter filename:")
            if filename != "":
                try:
                    projects = get_file(filename)
                    print(projects)
                except FileNotFoundError:
                    print('Invalid Filename')
            elif choice == "S":
                filename = input('Enter filename to be save: ')
                save_projects(projects, filename)
        elif choice == "D":
            complete_project, incomplete_project = check_project(projects)
            print('Incomplete projects: ')
            display_projects(incomplete_project)
            print("")
            print('Completed projects: ')
            display_projects(complete_project)
        elif choice == "F":
            is_valid = False
            while not is_valid:
                try:
                    date = input('Show projects that start after date (dd/mm/yyyy): ')
                    filtered_date_projects = filtered_projects(date, projects)
                    # print(filtered_date_projects)
                    projects = sort_projects(filtered_date_projects)
                    display_projects(projects)
                    is_valid = True
                except ValueError:
                    print("Incorrect date format, should be dd/mm/yy")
                    date = input('Show projects that start after date (dd/mm/yyyy): ')
        elif choice == "D":
            complete_project, incomplete_project = check_project(projects)
            print("Incomplete projects:")
            display_projects(incomplete_project)
        elif choice == "A":
            print('Lets add a new project')
            try:
                name = input('Name: ')
                start_date = input('Start date (dd/mm/yy): ')
                priority = int(input('Priority: '))
                estimate_cost = input('Cost estimate: ')
                estimate_cost = estimate_cost.replace('$', '')
                estimate_cost = int(estimate_cost)
                completion_percentage = input('Percent complete: ')
                project = Project(str(name), str(start_date), int(priority), int(estimate_cost), int(completion_percentage))
                projects.append(project)
            except ValueError:
                print('Invalid Input')
        elif choice == "U":
            projects = sort_projects(projects)
            display_projects(projects)
            projects_number = {}

            for number, project in enumerate(projects):
                projects_number[str(number + 1)] = project
                # print(projects_number)
            try:
                choice = input('Project choice: ')
                chosen_project = projects_number[choice]
                print (chosen_project)
                new_percentage = input('New Percentage: ')
                new_priority = input('New Priority: ')
                if new_percentage != '':
                    chosen_project.update_percentage(int(new_percentage))
                if new_priority != '':
                    chosen_project.update_priority(int(new_priority))
            except KeyError:
                print('Invalid Choice')
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def get_file(filename):
    projects = []# Open the file for reading
    in_file = open(filename, 'r')
    # print(in_file.read())
    # File format is like: Guitar, name, year, price
    # 'Consume' the first line (header) - we don't need its contents
    in_file.readline ()
    # All other lines are language data
    for line in in_file:
    # print(repr(line))
    # debugging
    # Strip newline from end and split it into parts by tab
        parts = line.strip().replace("\t", ",")
        parts = parts.split(",")
    # print(parts) # debugging# Construct a project object using the elements
        project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
    # Add the project we've just constructed to the list
        projects.append (project)
    # Close the file as soon as we've finished reading it
    in_file.close()
    return projects



def save_projects(filename,projects):
    with open(filename,'w') as out_file:

        for project in projects:
            print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.estimate_cost}\t{project.completion_percentage}")
    out_file.close()


def check_project(projects):
    """split the project into completed and incomplete projects"""
    complete_project = []
    incomplete_project = []
    for project in projects:
        if project.is_complete():
            complete_project.append(project)
            complete_project.sort()
        else:
            incomplete_project.append(project)
            incomplete_project.sort()
    return complete_project, incomplete_project


def display_projects(projects):
    for number, project in enumerate(projects):
        print(f"{number + 1} {project}")


def filtered_projects(date, projects):
    filtered_projects_date = []
    for project in projects:
        if project.compare_date(date):
            filtered_projects_date.append(project)
    return filtered_projects_date


def sort_projects(projects):
    date_list = []
    print(projects)
    for project in projects:
        if project.start_date not in date_list:
            date_list.append(project.start_date)
        print (date_list)
        date_list.sort()
        print (date_list)
        sorted_project = []
        for date in date_list:
            for project in projects:
                if project.start_date == date:
                    sorted_project.append(project)
                    print(sorted_project)
    return sorted_project


main()
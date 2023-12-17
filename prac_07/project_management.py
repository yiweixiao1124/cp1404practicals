from project import Project
import datetime
menu = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new " \
       "project\n- (U)pdate project\n- (Q)uit"


def main():
    projects = []

    choice = ''
    while choice != 'q':
        print(menu)
        choice = input(">>> ").strip().lower()
        if choice == 'l':
            filename = input("Enter filename to load projects from: ")
            load_projects(projects, filename)
        elif choice == 's':
            filename = input("Enter filename to save projects to: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_date = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, filter_date)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)

    print("Thank you for using custom-built project management software.")
    save_projects('projects.txt', projects)


def load_projects(projects, filename):
    in_file = open(filename, 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split('\t')
        name = parts[0]
        start_date = parts[1]
        priority = int(parts[2])
        estimate_cost = float(parts[3])
        completion_percentage = int(parts[4])
        project = Project(name, start_date, priority, estimate_cost, completion_percentage)
        projects.append(project)
    in_file.close()


def save_projects(projects):
    out_file = open('projects.txt', 'w')
    for project in projects:
        print(f"{project.name} {project.start_date} {project.priority} {project.estimate_cost} {project.completion_percentage}", file=out_file)
    out_file.close()


def display_projects(projects):
    incomplete_projects = [project for project in projects if not project.is_complete()]
    completed_projects = [project for project in projects if project.is_complete()]

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"{project}")

    print("Completed projects:")
    for project in completed_projects:
        print(f"{project}")


def filter_projects_by_date(projects, filter_date):
    filtered_projects = [project for project in projects if project.start_date > datetime.datetime.strptime(filter_date, "%d/%m/%Y").date()]
    filtered_projects.sort(key=lambda x: x.start_date)

    for project in filtered_projects:
        print(f"{project}")


def add_new_project(projects):
    name = input("Name: ")
    date_string = input("Start date (dd/mm/yyyy): ")
    start_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    print(f"That day is/was {start_date.strftime('%A')}")
    print(start_date.strftime("%d/%m/%Y"))
    priority = int(input("Priority: "))
    estimate_cost = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))

    new_project = Project(name, start_date, priority, estimate_cost, completion_percentage)
    projects.append(new_project)


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    choice = int(input("Project choice: "))
    new_completion_percentage = input("New Percentage: ")
    new_priority = input("New Priority: ")

    if new_completion_percentage:
        projects[choice].completion_percentage = int(new_completion_percentage)
    if new_priority:
        projects[choice].priority = int(new_priority)


main()

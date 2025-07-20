task = input("Enter a task for the day: ")
priority = input("Enter the priority of the task (high/medium/low): ")
time_bound = input("Is this task time-bound? (yes/no): ")
match (priority, time_bound):
    case ("high", "yes"):
        print("Reminder: 'Finish project report' is a high priority task that requires immediate attention today!.")
    case ("medium", "no"):
        print("This is a medium priority and non-time-bound task.")
    case ("low", "yes"):
        print("This is a low priority and time-bound task.")
    case _:
        print("Task priority not recognized.")
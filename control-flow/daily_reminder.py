task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ")
priority = input("Priority (high/medium/low): ")
match (priority, time_bound):
    case ("high", "yes"):
        print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!.")
    case ("medium", "no"):
        print(f"Reminder: '{task}' is a medium priority task that is not time-bound.")
    case ("low", "yes"):
        print(f"Reminder: '{task}' is a low priority task that is time-bound.")
    case _:
        print("Task priority not recognized.")
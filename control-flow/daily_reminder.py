Task = input("Enter a task for the day: ")
Time_Bound = input("Is it time-bound? (yes/no): ")
Priority = input("priority (high/medium/low): ")
match (Priority, Time_Bound):
    case ("high", "yes"):
        print(f"Reminder: '{Task}' is a high priority task that requires immediate attention today!.")
    case ("medium", "no"):
        print(f"Reminder: '{Task}' is a medium priority task that is not time-bound.")
    case ("low", "yes"):
        print(f"Reminder: '{Task}' is a low priority task that is time-bound.")
    case _:
        print("Task priority not recognized.")
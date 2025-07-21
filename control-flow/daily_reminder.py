task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ")
priority = input("Priority (high/medium/low): ")
match  priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!.")
        else:
            print(f"Reminder: '{task}' is a high priority task. Try to get it done soon.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that that requires attention today.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. plan to do it when possible.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task that is time-bound, so try not to forget")
        else:
            print(f"Reminder: '{task}' is a low priority task, consider completing it when you have free time")
    case _:
        print("Sorry, that's not a valid priority level. please use high, medium, or low.")
        
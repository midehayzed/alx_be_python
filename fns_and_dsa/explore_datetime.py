from datetime import datetime, timedelta
# Part 1: Display Current Date and Time
def display_current_datetime():
    current_date = datetime.now()  # Save current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format it
    print("Current date and time:", formatted_date)
# Part 2: Calculate Future Date
def calculate_future_date():
    days = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=days)  # Save future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print("Future date:", formatted_future_date)
# Main function to run both parts
def main():
    display_current_datetime()
    calculate_future_date()
if __name__ == "__main__":
    main()

import datetime
from application.salary import calculate_salary
from application.db.people import get_employees

def print_current_date():
    today = datetime.date.today()
    print(f"Текущая дата: {today}")

if __name__ == '__main__':
    print_current_date()
    calculate_salary()
    get_employees()
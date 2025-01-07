import argparse
from datetime import datetime

def parse_input():
    parser = argparse.ArgumentParser()

    def parse_date(date_str):
        return datetime.strptime(date_str, '%d/%m/%Y')

    parser.add_argument(
        '--bd',
        type=parse_date,
        required=True,
        help='Birthday of the user in format DD/MM/YYYY'
    )
    parser.add_argument(
        '--name',
        type=str,
        default='Ratchanont',
        help='Input the name of the person using the app'
    )

    args = parser.parse_args()
    return args

def printHello(who):
    print(f"Hello World, {who}!!")

def cal_todayVbd(bd):
    today = datetime.today()
    delta = bd - today
    return delta.days

if __name__ == "__main__":
    input_v = parse_input()
    print('This is my first .py file.')
    printHello(input_v.name)
    
    days_to_birthday = cal_todayVbd(input_v.bd)
    if days_to_birthday > 0:
        print(f'Your birthday is in {days_to_birthday} day(s) from today.')
    elif days_to_birthday == 0:
        print("Happy Birthday!")
    else:
        print(f'You have lived for {-days_to_birthday} day(s).')
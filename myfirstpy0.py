import argparse 
from datetime import datetime

def parse_input():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--bd',
        type=int,
        required=True,
        help='birthday of the user'
    )
    parser.add_argument(
        '--name',
        type=str,
        default='Ratchanont',
        # required=True,
        help='input the name of people who are using the app'
    )

    args = parser.parse_args()
    return args

def printHello(who):
    print(f"Hello World, {who}!!")

def cal_todayVbd(bd):
    td = datetime.today().strftime('%d')
    return bd-int(td)

if __name__== "__main__":
    input_v = parse_input()
    print('This is my first .py file.')
    printHello(input_v.name)
    print(f'your birthday is {cal_todayVbd(input_v.bd)} from today')

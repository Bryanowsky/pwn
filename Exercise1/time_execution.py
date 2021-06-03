from datetime import timedelta
from subprocess import call
import time
import argparse

# To execute this code in the console you need to run something like `python time_execution fibonacci.py` or another
# python file name in the same folder of this code.


def init_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('code', help='Python file path to execute it, needs to be in the same folder as this file.')
    return parser.parse_args()


def execute_code(code_file: str):
    try:
        call(['python', code_file])
    except OSError as e:
        print('Execution failed: ', e)


def get_execution_time(start_time: float):
    execution_time = time.time() - start_time
    print(f'Execution time: {timedelta(seconds=execution_time)}')


if __name__ == '__main__':
    args = init_args()
    start_time = time.time()
    execute_code(code_file=args.code)
    get_execution_time(start_time=start_time)


import sys

NOT_TRIANGLE_ERROR = 'не треугольник'

def validateArgs(args):
    if len(args) != 4:
        raise ValueError(NOT_TRIANGLE_ERROR)

try:
    validateArgs(sys.argv)
    print('Ok, maybe its triangle, man')
except Exception as error:
    print(error)
import sys

NOT_TRIANGLE_ERROR = 'не треугольник'

def validateArgs(args: list[str]) -> None:
    def checkArgsCount() -> None:
        if len(args) != 3:
            raise ValueError(NOT_TRIANGLE_ERROR)

    def checkArgsType() -> None:
        for element in args:
            if not element.isdigit():
                raise ValueError(NOT_TRIANGLE_ERROR)

    def checkArgsValue() -> None:
        for element in args:
            if element < 0:
                raise ValueError(NOT_TRIANGLE_ERROR)


    checkArgsCount()
    checkArgsType()
    args = [int(element) for element in args]
    checkArgsValue()


try:
    args = sys.argv.pop(0)
    validateArgs(sys.argv)
    print('Ok, maybe its triangle, man')
except Exception as error:
    print(error)
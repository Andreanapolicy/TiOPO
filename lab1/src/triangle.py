import sys

NOT_TRIANGLE_ERROR = 'не треугольник'
UNDEFINED_ERROR = 'неизвестная ошибка'
USUAL_TRIANGLE = 'обычный'
ISOSCELES_TRIANGLE = 'равнобедренный'
EQUILATERAL_TRIANGLE = 'равносторонний'

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
            if int(element) < 0:
                raise ValueError(NOT_TRIANGLE_ERROR)


    checkArgsCount()
    checkArgsType()
    args = [int(element) for element in args]
    checkArgsValue()


try:
    args = sys.argv
    args.pop(0)
    validateArgs(args)
    print('Ok, maybe its triangle, man')
except ValueError as error:
    print(error)
except Exception:
    print(UNDEFINED_ERROR)
import sys

NOT_TRIANGLE_ERROR = 'не треугольник'
UNDEFINED_ERROR = 'неизвестная ошибка'
USUAL_TRIANGLE = 'обычный'
ISOSCELES_TRIANGLE = 'равнобедренный'
EQUILATERAL_TRIANGLE = 'равносторонний'

def validateArgs(args: list[str]) -> None:
    def checkArgsCount() -> None:
        if len(args) != 3:
            raise ValueError(UNDEFINED_ERROR)

    def checkArgsType() -> None:
        for element in args:
            if not element.isdigit():
                raise ValueError(UNDEFINED_ERROR)

    def checkArgsValue() -> None:
        for element in args:
            if int(element) < 0:
                raise ValueError(UNDEFINED_ERROR)


    checkArgsCount()
    checkArgsType()
    args = [int(element) for element in args]
    checkArgsValue()


def getTriangleType(firstLine: int, secondLine: int, thirdLine: int) -> str:
    def isTriangle() -> bool:
        return firstLine + secondLine > thirdLine or thirdLine + secondLine > firstLine or firstLine + thirdLine > secondLine

    def isIsoscelesTriangle() -> bool:
        return firstLine == secondLine or thirdLine == secondLine or firstLine == thirdLine

    def isEquilateralTriangle() -> bool:
        return firstLine == secondLine and thirdLine == secondLine


    if not isTriangle():
        return NOT_TRIANGLE_ERROR

    if not isEquilateralTriangle():
        return EQUILATERAL_TRIANGLE

    if not isIsoscelesTriangle():
        return ISOSCELES_TRIANGLE

    return USUAL_TRIANGLE


try:
    args = sys.argv
    args.pop(0)
    validateArgs(args)
    print(getTriangleType(int(args[0]), int(args[1]), int(args[2])))
except ValueError as error:
    print(error)
except Exception:
    print(UNDEFINED_ERROR)
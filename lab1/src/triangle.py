import sys
import math

NOT_TRIANGLE_ERROR = 'не треугольник'
UNDEFINED_ERROR = 'неизвестная ошибка'
USUAL_TRIANGLE = 'обычный'
ISOSCELES_TRIANGLE = 'равнобедренный'
EQUILATERAL_TRIANGLE = 'равносторонний'

def validateArgs(args: list[str]) -> None:
    def isfloat(num):
        try:
            float(num)
            return True
        except ValueError:
            return False

    def checkArgsCount() -> None:
        if len(args) != 3:
            raise RuntimeError(UNDEFINED_ERROR)

    def checkArgsType() -> None:
        for element in args:
            if not isfloat(element):
                raise RuntimeError(UNDEFINED_ERROR)

    def checkArgsValue() -> None:
        for element in args:
            if element < 0:
                raise RuntimeError(UNDEFINED_ERROR)


    checkArgsCount()
    checkArgsType()
    args = [float(element) for element in args]
    checkArgsValue()


def getTriangleType(firstLine: float, secondLine: float, thirdLine: float) -> str:
    def isTriangle() -> bool:
        return firstLine + secondLine > thirdLine and thirdLine + secondLine > firstLine and firstLine + thirdLine > secondLine

    def isValidLinesValue() -> bool:
        MAX_VALID_LINE_VALUE = 2147483647
        MIN_VALID_LINE_VALUE = 0.001

        return (firstLine >= MIN_VALID_LINE_VALUE) and (firstLine <= MAX_VALID_LINE_VALUE) \
               and (secondLine >= MIN_VALID_LINE_VALUE) and (secondLine <= MAX_VALID_LINE_VALUE) \
               and (thirdLine >= MIN_VALID_LINE_VALUE) and (thirdLine <= MAX_VALID_LINE_VALUE)

    def isIsoscelesTriangle() -> bool:
        return math.isclose(firstLine, secondLine, rel_tol=1e-14, abs_tol=0.0) or math.isclose(thirdLine, secondLine, rel_tol=1e-14, abs_tol=0.0) or math.isclose(firstLine, thirdLine, rel_tol=1e-14, abs_tol=0.0)

    def isEquilateralTriangle() -> bool:
        return math.isclose(firstLine, secondLine, rel_tol=1e-14, abs_tol=0.0) and math.isclose(thirdLine, secondLine, rel_tol=1e-14, abs_tol=0.0)

    if not isValidLinesValue() or not isTriangle():
        return NOT_TRIANGLE_ERROR

    if isEquilateralTriangle():
        return EQUILATERAL_TRIANGLE

    if isIsoscelesTriangle():
        return ISOSCELES_TRIANGLE

    return USUAL_TRIANGLE


try:
    args = sys.argv
    args.pop(0)
    validateArgs(args)
    print(getTriangleType(float(args[0]), float(args[1]), float(args[2])))
except RuntimeError as error:
    print(error)
except Exception:
    print(UNDEFINED_ERROR)
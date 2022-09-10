import sys
import os.path
import subprocess

OUTPUT_PATH = '~output/result.txt'
SRC_PATH = '../src/triangle.py'
SUCCESS_MESSAGE = 'success'
ERROR_MESSAGE = 'error'

class TestCase:
    def __init__(self, params, result):
        self.params = params
        self.result = result

def validateArgs(args: list[str]) -> None:
    if (len(args) != 1):
        raise ValueError('Wrong call. Should be: py -3 run_tests.py <path to cases>')

    if not os.path.isfile(args[0]) or not os.path.exists(args[0]):
        raise ValueError('Wrong call. <path to cases> should be file')

def parseTestCases(filePath: str) -> list[TestCase]:
    with open(filePath, encoding='utf-8', mode='r') as file:
        testCases = []
        content = file.readlines()
        for line in content:
            separetedLine = line.replace('\n', '').split(' - ')
            testCase = TestCase(separetedLine[0], separetedLine[1])
            testCases.append(testCase)
        return testCases

def runTests(testCases: list[TestCase], outputPath: str) -> None:
    index = 1
    os.makedirs(os.path.dirname(outputPath), exist_ok=True)
    with open(outputPath, "w") as file:
        for testCase in testCases:
            process = subprocess.Popen(['py', '-3', SRC_PATH, *testCase.params.split()], stdout=subprocess.PIPE, shell=True)
            (binaryOutput, err) = process.communicate()
            output = binaryOutput.replace(b'\r', b'').decode('cp1251').replace('\n', '')
            file.write(str(index) + ' - ' + (SUCCESS_MESSAGE if output == testCase.result else ERROR_MESSAGE) + '\n')
            index += 1


try:
    args = sys.argv
    args.pop(0)
    validateArgs(args)
    runTests(parseTestCases(args[0]), OUTPUT_PATH)
except Exception as error:
    print(error)
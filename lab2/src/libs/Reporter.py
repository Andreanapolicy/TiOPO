import os.path
from datetime import datetime

SUCCESS_OUTPUT_PATH = '~output/success_result.txt'
FAILURE_OUTPUT_PATH = '~output/failure_result.txt'

def splitResults(results):
    successResponses = []
    failureResponses = []

    for response in results:
        if response.code < 400:
            successResponses.append(response)
        else:
            failureResponses.append(response)

    return [successResponses, failureResponses]


def writeUrlResponseReport(urlResponses):
    [successResponses, failureResponses] = splitResults(urlResponses)

    writeResponses(successResponses, SUCCESS_OUTPUT_PATH)
    writeResponses(failureResponses, FAILURE_OUTPUT_PATH)


def writeResponses(responses, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    index = 1
    with open(path, "w") as file:
        for response in responses:
            file.write(str(index) + '. ' + response.url + ' - ' + str(response.code) + '\n')
            index += 1
        file.write('Links count processed: ' + str(index - 1) + '\n')
        file.write('Precessed date: ' + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + '\n')
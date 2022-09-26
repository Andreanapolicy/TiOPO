SUCCESS_OUTPUT_PATH = '~output/success_result.txt'
FAILURE_OUTPUT_PATH = '~output/failure_result.txt'

def splitResults(results):
    successResponses = []
    failureResponses = []

    for response in results:
        if response.code == 200:
            successResponses.append(response)
        else:
            failureResponses.append(response)

    return [successResponses, failureResponses]


def writeUrlResponseReport(urlResponses):
    [successResponses, failureResponses] = splitResults(urlResponses)
    [print([response.code, response.url]) for response in successResponses]
    [print([response.code, response.url]) for response in failureResponses]



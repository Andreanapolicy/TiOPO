import datetime


def report(successFileName, failFileName, links):
    with open(failFileName, "w") as file:
        total = 0

        for link in links:
            if link.status > 400:
                file.write(link.PREVIOUS_URL + " --- " + link.url + " " + str(link.status))
                total += 1

        file.write("Total links: " + str(total))
        file.write("Precessed date: " + str(datetime.datetime.now()))

    with open(successFileName, "w") as file:
        total = 0

        for link in links:
            if link.status < 400:
                file.write(link.url + " " + str(link.status))
                total += 1

        file.write("Total links: " + str(total))
        file.write("Precessed date: " + str(datetime.datetime.now()))

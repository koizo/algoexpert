def validIPAddresses(string):
    # Write your code here.
    ips = []

    for i in range(1, min(len(string), 4)):
        currentip = ["", "", "", ""]
        currentip[0] = string[:i]

        if not isValid(currentip[0]):
            continue

        for j in range(i + 1, i + min(len(string) - 1, 4)):
            currentip[1] = string[i:j]

            if not isValid(currentip[1]):
                continue

            for k in range(j + 1, j + min(len(string) - j, 4)):
                currentip[2] = string[j:k]
                currentip[3] = string[k:]

                if isValid(currentip[2]) and isValid(currentip[3]):
                    ips.append(".".join(currentip))

    return ips


def isValid(ip):
    stringasint = int(ip)
    if stringasint > 255:
        return False

    return len(ip) == len(str(stringasint))

from definitions.filevars import PROXIES_PATH, ANALYSIS_OUTPUT
from definitions.settingsvars import REQUEST_TIMER
from utility.proxy import loadProxies
from handlers.jagexcheck import canCreateAccounts
from utility.exports import exportTribotFormat
import os, time

def main():
    proxyList = loadProxies(PROXIES_PATH)

    os.makedirs(os.path.dirname(ANALYSIS_OUTPUT), exist_ok=True)
    resultFile = open(ANALYSIS_OUTPUT, "w", encoding="utf-8")

    validList = []
    invalidList = []

    for proxy in proxyList:
        valid, message = canCreateAccounts(proxy)
        resultFile.write("["+str(proxy) + "] valid: " + str(valid) + ", message: " + str(message)+"\n")

        if(valid):
            validList.append(proxy)
        else:
            invalidList.append(proxy)

        time.sleep(REQUEST_TIMER)
        
    exportTribotFormat(validList)
    resultFile.write("\n\nValid Proxies:\n")
    for item in validList:
        resultFile.write(item+"\n")

    resultFile.write("\n\nInvalid Proxies:\n")
    for item in invalidList:
        resultFile.write(item+"\n")

    resultFile.close()

# I have main in its own method to make testing new things a bit faster.
# Since it's defined above, calling it here runs it.
main()
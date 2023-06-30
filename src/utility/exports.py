from definitions.filevars import PROXY_EXPORT_DIR
from definitions.settingsvars import TRIBOT_EXPORT_FILE
import os

def exportTribotFormat(validProxies):
    os.makedirs(os.path.dirname(PROXY_EXPORT_DIR+TRIBOT_EXPORT_FILE), exist_ok=True)
    exportFile = open(PROXY_EXPORT_DIR+TRIBOT_EXPORT_FILE, "w", encoding="utf-8")
    count = 1
    name = "Valid - "
    for proxy in validProxies:
        x = proxy.split("@")
        y = x[0].split(":")
        x = x[1].split(":")
        exportFile.write(name+str(count) + "," + x[0] + "," + x[1] + "," + y[0] + "," + y[1] + "\n")
        count += 1

    exportFile.close()
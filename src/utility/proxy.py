from definitions.settingsvars import PROXY_FORMAT

# path = file path.
def loadProxies(path):
    proxies = []
    file = None
    try:
        file = open(path, 'r')
    except (FileNotFoundError):
        # The executable builds to the projects root directory. Going to try to find the files dir at the same level as the executable would be.
        try:
            file = open('proxies.txt', 'r')
        except (FileNotFoundError):
            # Still didn't find the directory. Show error.
            raise FileNotFoundError('exe = Requires files in same dir\nterminal = Requires files in ../files dir')
    
    
    lines = file.readlines()
    count = 0

    
    for line in lines:
        if(line[0:1] == "#"):
            continue
        count += 1
        proxies.append(formatProxy(PROXY_FORMAT, line))

    return proxies


# inFormat is the layout your proxies were exported with.
# 0 = host:port:user:pass (allColonFormat)
def formatProxy(inFormat, proxy):
    match inFormat:
        case 0:
            return allColonFormat(proxy)
        case 1:
            return someOtherFormat(proxy)
        case _:
            return ""

def allColonFormat(proxy):
    x = proxy.split(":")
    return str(x[2].strip(' \t\n\r')+":"+x[3].strip(' \t\n\r')+"@"+x[0].strip(' \t\n\r')+":"+x[1].strip(' \t\n\r'))

# Define any other layouts you run into.
def someOtherFormat(proxy):
    return "Something"
import random

# Add as many user agents as you want for the program to cycle through.
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0",
]

def getRandomUserAgent():
    return USER_AGENTS[random.randint(0,len(USER_AGENTS)-1)]

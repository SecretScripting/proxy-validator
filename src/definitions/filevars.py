from definitions.settingsvars import INPUT_FILE_EXTENSION, INPUT_FILE_NAME

# Current directory
# Needs to be changed to ./ when building an exe.
BASE_DIR = "../"
FILE_DIR = BASE_DIR + "files/"

PROXIES_PATH = FILE_DIR + INPUT_FILE_NAME + INPUT_FILE_EXTENSION

ANALYSIS_OUTPUT = FILE_DIR + "proxy-analysis.txt"
PROXY_EXPORT_DIR = FILE_DIR

try:
    f = open(PROXIES_PATH)
except (FileNotFoundError):
    # doesn't exist.
    ANALYSIS_OUTPUT = "proxy-analysis.txt"
    PROXY_EXPORT_DIR = "./"
else:
    f.close()
# proxy-validator
 It's been a useful tool to help identify and separate the valid proxies in my pool. All I do is export the proxies from whatever provider I have at the time, copy them from the exported document to the proxies.txt file and run the program. 
 
 The first time I ran this, out of 20 proxies I had 11 good ones and 9 blocked. I rotated the 9 out, re-ran the list of 20 and had 19 good ones and 1 bad one. It took me 3-5 minutes to run 20, rotate my proxies out, re-run with the new proxies, and get a csv I could upload to Tribot with all 19 valid proxies ready to go.

This only works for **authenticated** proxies right now. It was developed and tested with **Python3**. I threw this together one afternoon while looking through some scraping documentation. I'm not very knowledgeable when it comes to Python, so the project / code formats might be a bit ugly.


# How to use
## Generates
This program generates a csv file that can be exported directly into the tribot proxy manager. It also generates an analysis file listing out which proxies are blocked by Jagex.

## General
You'll need to do a couple things to be able to use this. You'll need to follow the [Steps to build this manually](#steps-to-build-this-manually) section to be able to run the program. Then you'll need to copy your proxies (Formatted correctly) into the proxies.txt file located in the files directory. 

## uavars.py
In the src/definitions directory you'll find the uavars.py file. Each proxy that is checked will use a random user agent from that variable. If you decide to use this more frequently, I recommend googling some additional user agents and adding those to the USER_AGENTS array.

## settingsvars.py
* JAGEX_URL - The url used to validate the proxies against.
* REQUEST_TIMER - The amount of time the script waits in-between each request sent to jagex servers.
* PROXY_FORMAT - Variable to define how to read the proxies in the proxies.txt file. Currently only format is the one my proxy exports have had.
* INPUT_FILE_NAME & INPUT_FILE_EXTENSION - Defines the name and extension of the file that the proxies will be read from.
* TRIBOT_EXPORT_FILE - The csv file it exports every valid proxy to so I can quickly import them all into Tribot.

# Steps to build this manually
1) Download [Python3](https://www.python.org/downloads/), and take note of the install location which should be C:\ by default. Ensure you check the box to add Python to the path during install. 
    * https://www.python.org/downloads/

1) Install the [Pipenv](https://pipenv.pypa.io/en/latest/) package manager:
    * Run this command in a terminal:
        ```
        pip install pipenv
        ```
1) Add pipenv to your environment variables
    * The previous step added pipenv to the scripts directory. If you installed to the default C: directory, you would add this to your path environment variable:
        ```
        C:\Python311\Scripts
        ```
1) Open a Terminal in the root directory, and start a python virtual environment
    * Once the terminal is open in the project root directory, for example: C:\\git\\project\\proxy-validator, run this command:
        ```
        pipenv shell
        ```

1) Use pipenv to install required dependencies:
    * If you already have an environment that contains packages that are messing with this, may need to run this command first:
        ```
        pipenv uninstall --all
        ```
        It will uninstall all of the packages in the pipenv environment without modifying the pipfile, giving you a fresh environment.
    * Once you are ready to install the dependencies required for this project, just run this command in the terminal:
        ```
        pipenv install
        ```

1) Now that the dependencies are installed, you are a couple steps from using the tool:
    * You're going to switch into the src directory using the same terminal you ran the shell and install commands in:
        ```
        cd ./src
        ```
    * All that's left to do is run the main file, and wait for the output:
        ```
        py validateproxies.py
        ```

1) Enjoy the tool.

<br />
<details>
<summary>Expand this for steps to use a .venv directory</summary>
<p>
If you'd rather keep your projects virtual environment within the project directory itself, you can use these steps.

1) Follow the first three steps under the [VSCode setup](#vscode-setup) section.

1) Now instead of using pipenv to create a virtual environment, we'll create one in this directory using this command: 
    * If you have the VSCode python extension, you'll see a pop up telling you that it detected a new environment. If you click Yes to selecting it as the workspace folder, you'll only need to check that the interpreter is set to the correct environment (step 5 in VSCode setup).
    ```
    py -3 -m venv .venv
    ```

1) If you saw the pop up, and clicked 'Yes' to setting the workspace folder, you're done. You can skip to the last step of this section if you need further direction.

1) If you didn't see that pop up, clicked 'No', or it went away before you could click 'Yes', then you will need to set the interpreter to the '.venv':pipenv option. Follow step 5 in the [VSCode setup](#vscode-setup) section to find where to set that.


1) OPTIONAL: If you're a person who likes the peace of mind of knowing that your terminal is pointing to the right place, you can follow this step:
    * This command will give an error in the terminal if the .venv folder does not exist in the projects root directory. If it's not there, go back and run the command in step 2 of this section.
    ```
    .venv\scripts\activate
    ```
    When this command is finished running, you should see a (.venv) in the far left of the terminal. This means your terminal is pointing to the virtual python environment.

1) You can make your changes, and follow the last two steps in the [VSCode setup](#vscode-setup) section to switch into the directory and run the program. 


</p>
</details>
<br />

# VSCode setup

This will walk you through setting the Python Interpreter to the virtual environment. If you're using a virtual environment and don't do this, your workspace will not be able to resolve the dependencies in the project.

1) Follow the first three steps under the [Steps to build this manually](#steps-to-build-this-manually) section.

1) Open the project in VSCode.

1) At the top of the IDE click 'Terminal' > 'New Terminal'.
    * If you had your IDE open when you installed Python / added new environment variables, it won't work. Opening a new terminal off the bat avoids the potential issues that come with a stale terminal instance not having up-to-date variables.

1) Follow steps 4 and 5 under the [Steps to build this manually](#steps-to-build-this-manually) section.

1) You need to make sure the VSCode interpreter is set to the projects virtual environment:
    * First you need to bring up the command pallete. In VSCode press:
        ```
        Control + Shift + P
        ```
    * Search for 'Python: Select Interpreter', and select the one that says "PipEnv" on the far right. 
        * NOTE: You may need to click the little refresh button in the top right for it to pick up the virtual environment. You should also see the path on your system to the virtual environment, something like '~\\.virtualenvs\proxy-validator-...'

1) Switch into the src directory like so:
    ```
    cd ./src
    ```

1) When you're ready to run the project to test changes, just type:
    ```
    py validateproxies.py
    ```


Your workspace should now resolve the requests-html library and the dependencies that were downloaded with it like BeautifulSoup.
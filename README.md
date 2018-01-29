# Flask Web Application with IBM Watson Conversation

### Purpose 
This is a Python Flask web application with a simple _chat-friendly_ User Interface built as a demo for IBM Day @ Dtec in Dubai, United Arab Emirates. 

### How to run on local machine
1. Ensure Python is installed on your local environment (Both Python 2 and Python 3 are supported)
2. Install the requirements using the command `pip install -r requirements.txt` 
3. Edit the file `app.py` and add your Watson Conversation `username`, `password` and `workspace_ID`
4. Run the application as: `python app.py`
5. Point your web browser to the address `localhost:<port>`
6. Have a conversation with Watson!

### How to deploy on IBM Cloud
1. Ensure that the [IBM Cloud CLI](https://console.bluemix.net/docs/cli/reference/bluemix_cli/all_versions.html#ibm-cloud-cli-installer-all-versions) tool is installed
2. Clone this repository to a local directory 
3. Edit the file `app.py` and add your Watson Conversation `username`, `password` and `workspace_ID`
4. Open a terminal and run the commands: 
	- `bx login`
	- `bx target -o ORG -s SPACE`
	- `bx cf push` 

### Help
[Watson Conversation Python API Reference](https://www.ibm.com/watson/developercloud/conversation/api/v1/?python)
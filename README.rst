Intended to use as a forward proxy application performing conditional filtering on outgoing HTTP requests based HTTP body content.

Windows:
########

**Prerequisites:** pip + virtualenv

Download the source code.

Open Powershell, and change directory to your workspace.

Create an virtualenv by running "virtualenv <title>".

Change directory to the root of your new virtualenv, and run "./Script/activate".

Copy the downloaded folder to the root directory of the your virtualenv, og change directory to the pasted folder.

Now run "pip install -r requirements.txt".

To view the dependencies run "type requirements.txt".

In the same folder now run "waitress-serve --listen=127.0.0.1:8888 app:api", and you should se "Serving on http://127.0.0.1:8888".

Go to your browser and go to this address "http://http://127.0.0.1:8888/test_resource". 

If you see something like "SyntaxError: JSON.parse: unexpected character at line 1 column 1 of the JSON data" then the browser is trying to display the output as **json**. To view the content choose **raw** output in the browser.

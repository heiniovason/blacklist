This is a project that I started to test the Falcon web framework for myself. In this context I'm trying to build an application that serves as a forward proxy. 

Roughly explained the application will perform conditional filtering on 1..* value(s) from incoming requests' SOAP elements, and forward a respective request to an external web service if the conditional requirements are met.

Windows:
########

**Prerequisites:** python and pip are installed and added to system-, or user Path.

Open Powershell

Run "pip install virtualenv"

Change directory to your workspace.

Create an virtualenv by running "virtualenv <title>".

Change directory to the root of your new virtualenv, and run "./Script/activate".

Now download the project by running "git clone https://github.com/heiniovason/blacklist.git".

Change directory to the project folder, and run "pip install -r requirements.txt". To view the dependencies run "type requirements.txt".

In the project folder now run "waitress-serve --listen=127.0.0.1:8888 app:api", and you should se the following output "Serving on http://127.0.0.1:8888".

Now test by sending a GET request to "http://127.0.0.1:8888/test_resource". 

If you don't have REST client installed you can use your browser by you see something like "SyntaxError: JSON.parse: unexpected character at line 1 column 1 of the JSON data" then the browser is trying to display the output as **json**. To view the content choose **raw** output in the browser.

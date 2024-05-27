# rest_api1
You need to install Flask for creating the web server and googletrans for translation. Open your terminal or command prompt and run:
pip install Flask googletrans==4.0.0-rc1

Navigate to project directory in the terminal (if you're not already there) and run:
python app.py

This will start the Flask development server, and you should see output indicating the server is running:
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: xxx-xxx-xxx

Using Postman:
1. Open Postman
2. Set the Request Type to POST
3. Enter the URL http://127.0.0.1:5000/translate
	{
    		"text": "Hello, how are you?"
	}
4. Send the Request and check the response

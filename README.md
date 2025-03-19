# KCM Tool Back-end

This repo is the back-end part of KCM Tool. For front-end, please go to [KCM Tool Front-end repo](https://github.com/jiaqiwu66/KCM_tool_frontend)

## Introduction
Through investigation, we create a tool, which allow King County Metro to adjust parameters, get a simulation report, and compare the results within the team. 
We take several factors into account when designing and implementing the system, such as energy efficiency, battery capacity, depot capacity, etc.

## Local Test
We use **Python Flask** to build the back-end.
For more information, please refer to [Python Flask Tutorial](https://flask.palletsprojects.com/en/stable/tutorial/)

Please follow the next step to run the back-end in local:
- Clone the repo in local
```
git clone https://github.com/jiaqiwu66/KCM_tool_backend
```
- Install the required python package by `requirement.txt` file
```
# for Windows OS
pip install -r requirements.txt

# for Mac OS
pip3 install -r requirements.txt
```
- Run the `kcm.py` to start the back-end
```
# for Windows OS
python kcm.py

# for Mac OS
python3 kcm.py
```
If you can see the below info in the terminal, Congregations, back-end part is running in local.
```
* Serving Flask app 'kcm.py'
* Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
* Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

For front-end, please go to [KCM Tool Front-end repo](https://github.com/jiaqiwu66/KCM_tool_frontend)

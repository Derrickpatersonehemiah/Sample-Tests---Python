Pre Req:
To run these scripts, we need to have psutil and requests installed using pip
command: pip install psutil requests

System Health Monitoring Script:

1. Uses the psutil library to monitor CPU usage, memory usage, disk space, and running processes
2. Logs warnings if any of the metrics exceed predefined thresholds
3. Logs information about running processes and system health every 60 seconds.

Application Health Checker Script:

1. Uses the requests library to send HTTP GET requests to the application's health check endpoint
2. Logs the status of the application as 'UP' if the HTTP status code is 200, otherwise logs it as 'DOWN'
3. Logs errors if the application is unreachable or if there is a request exception
4. checks the application's health every 2 minutes.

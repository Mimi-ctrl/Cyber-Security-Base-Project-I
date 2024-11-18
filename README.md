# Cyber Security Base Project I

## Installation

1. Follow [these instructions](https://cybersecuritybase.mooc.fi/installation-guide) to install the necessary dependencies.
2. Clone the repository.
3. Run `python3 manage.py runserver`. This will start the server.
4. Open a browser and go to `localhost:8000` to access the website.

## List of the used flaws
! There is a fix for all of these in the code !

#### 1. A05:2021-Security Misconfiguration

https://owasp.org/Top10/A05_2021-Security_Misconfiguration/

In Django, you can configure that error messages are not exposed to users in production. This is done using a configuration file(settings.py).

Fix: Set the DEBUG variable to False in production. This prevents stack traces from being displayed and prevents the details of errors from being exposed.

Incorrect error handling can reveal too much information to the user, such as SQL requests, file paths, or other confidential information.

Fix: This can be fixed by handling errors correctly. In the code, replacing **empty_page_view** in the **views.py** file with the commented code in the try exception section will not reveal the error to the user.

#### 2. A07:2021-Identification and Authentication Failures

https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/

Authentication failures may occur if the application allows weak passwords (Password1 etc.) or displays the session ID in the URL.

Fix: When creating a user, check the password to see if it meets the criteria for a good password. Do not use the session ID in the URL.

#### 3. A09:2021-Security Logging and Monitoring Failures

https://owasp.org/Top10/A09_2021-Security_Logging_and_Monitoring_Failures/

By saving log data only to a local file.

Fix: Remove the LOGGING definition from **settings.py**. This will prevent log data from being saved only to a local file.

#### 4. A03:2021-Injection

https://owasp.org/Top10/A03_2021-Injection/

Raw SQL query was used without parameterization, which exposes to SQL injection.

Fix: Use parameterized queries or Django ORM, which prevents SQL injection and improves code security.

#### 5. A04:2021-Insecure Design

https://owasp.org/Top10/A04_2021-Insecure_Design/

description of flaw ...

how to fix it...

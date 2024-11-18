# Cyber Security Base Project I

## Installation

1. Follow [these instructions](https://cybersecuritybase.mooc.fi/installation-guide) to install the necessary dependencies.
2. Clone the repository.
3. Run `python3 manage.py runserver`. This will start the server.
4. Open a browser and go to `localhost:8000` to access the website.

## List of the used flaws

1. A05:2021-Security Misconfiguration

https://owasp.org/Top10/A05_2021-Security_Misconfiguration/

In Django, you can configure that error messages are not exposed to users in production. This is done using a configuration file (settings.py).

Fix: Set the DEBUG variable to False in production. This prevents stack traces from being displayed and prevents the details of errors from being exposed.

Incorrect error handling can reveal too much information to the user, such as SQL requests, file paths, or other confidential information.

Fix: This can be fixed by handling errors correctly. In the code, replacing empty_page_view in the views.py file with the commented code in the try exception section will not reveal the error to the user.

2. A07:2021-Identification and Authentication Failures

https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/

description of flaw 1...

how to fix it...

3. A09:2021-Security Logging and Monitoring Failures

https://owasp.org/Top10/A09_2021-Security_Logging_and_Monitoring_Failures/

description of flaw 1...

how to fix it...

4. A03:2021-Injection

https://owasp.org/Top10/A03_2021-Injection/

description of flaw 1...

how to fix it...

5. A04:2021-Insecure Design

https://owasp.org/Top10/A04_2021-Insecure_Design/

description of flaw 1...

how to fix it...

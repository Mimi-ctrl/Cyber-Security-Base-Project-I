# Cyber Security Base Project I

## Installation

1. Follow [these instructions](https://cybersecuritybase.mooc.fi/installation-guide) to install the necessary dependencies.
2. Clone the repository: Use the `git clone` command to create a local copy of the repository on your machine.
3. Run the server: Execute the command `python3 manage.py runserver`. This will start the Django development server on your local machine.
4. Access the application: Open a web browser and navigate to `http://localhost:8000`. This will display the website.

## List of the used flaws
! There is a fix for all of these in the code. Flaws can be found in the files **settings.py** and **views.py** !

#### 1. A05:2021-Security Misconfiguration

Link to the flaw: https://owasp.org/Top10/A05_2021-Security_Misconfiguration/

Security Misconfiguration refers to scenarios where the application's security settings are improperly configured.

In Django, error messages might unintentionally be exposed to users in the production environment if error handling is misconfigured in the **settings.py** file. This can reveal critical details such as file paths, or sensitive system information.

Fix: Set the DEBUG variable to False in the production environment. This ensures that detailed error messages are not displayed to end users

Incorrect error handling can expose application internals, such as SQL queries or API keys. 

Fix: Handle errors gracefully by logging them securely without leaking details to users.

#### 2. A07:2021-Identification and Authentication Failures

Link to the flaw: https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/

Identification and Authentication Failures addresses vulnerabilities in the identification or authentication mechanisms of an application.

Allowing weak passwords, such as **Password1** compromises user security. Including the session ID in the URL can expose it to attackers via browser history or URL sharing.

Fix: When creating a user, check the password to see if it meets the criteria for a good password. Avoid including sensitive information, such as session IDs, in URLs.

#### 3. A09:2021-Security Logging and Monitoring Failures

Link to the flaw: https://owasp.org/Top10/A09_2021-Security_Logging_and_Monitoring_Failures/

Security Logging and Monitoring Failures highlights insufficient logging and monitoring practices.

Saving log data only to a local file makes it harder to monitor events effectively. Additionally, sensitive logs could be lost or inaccessible in case of a server failure.

Fix: Avoid saving logs exclusively to local files by removing or modifying the LOGGING configuration in **settings.py**.

#### 4. A03:2021-Injection

Link to the flaw: https://owasp.org/Top10/A03_2021-Injection/

Injection encompasses vulnerabilities where untrusted input is executed as part of command or query, such as SQL injection.

Using raw SQL queries without parameterization in Django exposes application to SQL injection attacks, where attacker can manipulate query to gain unauthorized access to the database.

Fix: Use parameterized queries or Django ORM, which prevents SQL injection and improves code security.

#### 5. A04:2021-Insecure Design

Link to the flaw: https://owasp.org/Top10/A04_2021-Insecure_Design/

Insecure Design focuses on design flaws that lead to security vulnerabilities.

Allowing users to create unlimited number of resources, such as files or database entries, can lead to resource exhaustion and denial of service.

Fix: Implement resource limits per user or service to prevent abuse. For example set maximum number of notes per user.

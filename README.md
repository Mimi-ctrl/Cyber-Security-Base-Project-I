# Cyber Security Base Project I

## Installation instructions

1. Follow [these instructions](https://cybersecuritybase.mooc.fi/installation-guide) to install the necessary dependencies.
2. Clone the repository: Use the `git clone` command to create a local copy of the repository on your machine.
3. Run migrations and server: First, execute following commands to apply any pending database migrations: `python3 manage.py makemigrations` `python3 manage.py migrate`. After that, start the Django development server by running: `python3 manage.py runserver`. This will start the Django development server on your local machine.
4. Access the application: Open a web browser and navigate to `http://localhost:8000`. This will display the website.

## List of the used flaws in project
! There is a fix for all of these in the code. Flaws can be found in the files **index.html**, **settings.py** and **views.py**. Descriptions of flaws are written based on the text of the link that directs flaw. !

#### 1. A05:2021-Security Misconfiguration

Link to the flaw: https://owasp.org/Top10/A05_2021-Security_Misconfiguration/

Common vulnerabilities include issues like improper configuration of security settings or outdated components. Applications become vulnerable when security configurations are incomplete or incorrect. This includes situations such as leaving default accounts and passwords active, exposing overly detailed error messages, or failing to apply proper security headers. Misconfigurations can also occur if systems are not updated or if unnecessary features remain enabled, increasing the risk of exploitation.

Problem in the code: In Django, error messages might unintentionally be exposed to users in the production environment if error handling is misconfigured in the **settings.py** file. This can reveal critical details such as file paths, or sensitive system information.

Fix: Set the DEBUG variable to False in the production environment. This ensures that detailed error messages are not displayed to end users

Problem in the code: Incorrect error handling can expose application internals, such as SQL queries or API keys. 

Fix: Handle errors gracefully by logging them securely without leaking details to users. In my fix, I only send to the user error message "Something went wrong. ..." and nothing else.

#### 2. A07:2021-Identification and Authentication Failures

Link to the flaw: https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/

Common vulnerabilities include problems like not properly checking certificates, weak login systems, and poor session management. Applications are at risk if they allow automated attacks like credential stuffing or brute force, use weak or default passwords, or have insecure password recovery methods. Additional risks include reusing session IDs, showing them in URLs, or not ending sessions properly after logout or inacctivity.

Problem in the code: Allowing weak passwords, such as **Password1** compromises user security. Including the session ID in the URL can expose it to attackers via browser history or URL sharing.

Fix: When creating a user, check the password to see if it meets the criteria for a good password. Avoid including sensitive information, such as session IDs, in URLs.

#### 3. A09:2021-Security Logging and Monitoring Failures

Link to the flaw: https://owasp.org/Top10/A09_2021-Security_Logging_and_Monitoring_Failures/

Vulnerabilities occur when important events like logins or failed transactions aren’t logged, or when logs aren’t monitored for suspicious activity. Other issues include unclear log messages, logs stored only locally, or systems failing to alert on active attacks in real time. These failures leave breaches undetected and reduce visibility into security incidents.

Problem in the code: Saving log data only to a local file makes it harder to monitor events effectively. Additionally, sensitive logs could be lost or inaccessible in case of a server failure.

Fix: Avoid saving logs exclusively to local files by removing or modifying the LOGGING configuration in **settings.py**.

#### 4. A03:2021-Injection

Link to the flaw: https://owasp.org/Top10/A03_2021-Injection/

Injection vulnerabilities occur when applications fail to handle user input correctly. This allows attackers to exploit weakneses, such as using unvalidated or unsanitized input, to execute malicious commands or manipulate data, Common examples include SQL, NoSQL, OS command, and LDAP injections, all of which can compromise the integrity and confidentiality of systems. Applications are especially vulnerable if they use dynamic queries or non-parameterized calls, where malicious input is combined directly with commands.

Problem in the code: Using raw SQL queries without parameterization in Django exposes application to SQL injection attacks, where attacker can manipulate query to gain unauthorized access to the database.

Fix: Use parameterized queries or Django ORM, which prevents SQL injection and improves code security.

#### 5. Cross Site Request Forgery (CSRF)

Link to the flaw: https://owasp.org/www-community/attacks/csrf

CSRF happens when an attacker tricks a logged-in user into performing unintended actions on a website without their knowledge. For example, the attacker might make the user unknowingly create, update, or delete data. The server cannot tell whether the request is coming from the user or from an attacker.

Problem in the code: One part of the application allows users to create notes. However, it does not check if the request is coming from the user or an attacker. This means someone could trick a logged-in user into creating notes without their permission.

Fix: Solution is to make sure every action that changes data (like creating something) requires secret token, called a CSRF token. This token ensures that request is coming from the user and not from an attacker. Using this method makes it impossible for attackers to send fake requests.
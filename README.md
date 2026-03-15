# Secure Authentication System (SQL Injection Detection Lab)

## Overview

The Secure Authentication System is a defensive cybersecurity project designed to demonstrate secure login implementation and real-time detection of malicious authentication attempts.

This project simulates how modern applications protect user credentials by combining:

* Secure database interaction
* Input validation and attack pattern detection
* Logging of suspicious behavior
* Defensive software engineering practices

The system contrasts vulnerable and secure authentication logic to highlight how improper query handling can lead to serious security risks such as SQL Injection.

It represents a practical implementation of authentication hardening concepts used in real-world secure software systems.


## Key Features

* Secure user authentication using parameterized SQL queries
* Automatic local database setup using SQLite
* Real-time detection of suspicious login input patterns
* Logging of potential attack attempts for security analysis
* Demonstration of both vulnerable and secure login flows
* Command-line interactive authentication interface
* Lightweight and cross-platform implementation


## Security Concepts Demonstrated

This project applies multiple defensive cybersecurity principles:

* SQL Injection attack detection heuristics
* Secure query execution using prepared statements
* Secure credential validation workflow
* Security logging and incident tracking
* Input sanitization and validation mindset
* Comparison of secure vs insecure authentication design

These techniques simulate authentication protection mechanisms commonly deployed in secure enterprise systems.


## How the System Works

1. The application initializes a local SQLite database and creates a user table if it does not exist.
2. A default user record is inserted to simulate a production login environment.
3. During login:

    * User input is analyzed for suspicious SQL patterns.
    * Potential attack attempts are logged to a dedicated security log file.
4. The secure authentication module performs credential verification using parameterized queries.
5. The vulnerable module demonstrates how unsafe string-based queries can be exploited.

This workflow helps illustrate both attack methodology and defensive mitigation strategies.


## Project Structure
```
secure-auth-system/
│
├── app_secure.py        → Secure login implementation
├── app_vulnerable.py    → Demonstration of insecure authentication
├── users.db             → Local authentication database
├── attack_logs.txt      → Security event logging file
└── README.md
```


## Technologies Used

* Python
* SQLite Database
* Secure Query Parameterization
* Input Pattern Analysis
* Defensive Security Logging


## Example Usage

Run the secure version:
```
python app_secure.py
```
Run the vulnerable version (for learning demonstration):
```
python app_vulnerable.py
```

Try different login inputs to observe:

* Normal authentication behavior
* Detection of suspicious login attempts
* Differences between secure and insecure query execution


## Performance Characteristics

* Minimal resource usage
* Fast local database operations
* Efficient detection logic
* Suitable for educational lab environments


## Security & Ethical Use

This project is intended strictly for:

* Cybersecurity education
* Secure coding practice
* Authentication system research
* Defensive software engineering learning

It must not be used to conduct unauthorized intrusion or malicious testing against real systems.


## Learning Objectives

Through this project, the following competencies are demonstrated:

* Secure authentication workflow design
* Practical SQL Injection risk mitigation
* Security logging implementation
* Defensive programming mindset
* Database security fundamentals
* Real-world secure software architecture awareness


## Author

Developed as part of a hands-on cybersecurity project series focused on practical defensive engineering and secure system design.


## License

This project is provided for educational and research purposes.
Use responsibly and only in controlled or authorized environments.

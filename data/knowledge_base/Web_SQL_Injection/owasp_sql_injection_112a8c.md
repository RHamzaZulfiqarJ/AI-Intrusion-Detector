        ---
        title: OWASP SQL Injection
        category: Web_SQL_Injection
        source: OWASP
        url: https://owasp.org/www-community/attacks/SQL_Injection
        date: 2026-06-26
        ---

        # Overview

        SQL Injection
Overview
A SQL injection attack consists of insertion or “injection” of a SQL query via the input data from the client to the application. A successful SQL injection exploit can read sensitive data from the database, modify database data (Insert/Update/Delete), execute administration operations on the database (such as shutdown the DBMS), recover the content of a given file present on the DBMS file system and in some cases issue commands to the operating system. SQL injection attacks are a type of injection attack, in which SQL commands are injected into data-plane input in order to affect the execution of predefined SQL commands.
Threat Modeling
- SQL injection attacks allow attackers to spoof identity, tamper with existing data, cause repudiation issues such as voiding transactions or changing balances, allow the complete disclosure of all data on the system, destroy the data or make it otherwise unavailable, or become administrators of the database server.
- SQL Injection is very common with PHP and ASP applications due to the prevalence of older functional interfaces. Due to the nature of programmatic interfaces available, J2EE and ASP.NET applications are less likely to have easily exploited SQL injections.
- The severity of SQL Injection attacks is limited by the attacker’s skill and imagination, and to a lesser extent, defense in depth countermeasures, such as low privilege connections to the database server and so on. In general, consider SQL Injection a high impact severity.
Related Security Activities
How to Avoid SQL Injection Vulnerabilities
See the OWASP SQL Injection Prevention Cheat Sheet. See the OWASP Query Parameterization Cheat Sheet.
How to Review Code for SQL Injection Vulnerabilities
See the OWASP Code Review Guide article on how to Review Code for SQL Injection vulnerabilities.
How to Test for SQL Injection Vulnerabilities
See the OWASP Testing Guide for information on testing for SQL Injection vulnerabilities.
How to Bypass Web Application Firewalls with SQLi
See the OWASP Article on using SQL Injection to bypass a WAF
Description
SQL injection attack occurs when:
- An unintended data enters a program from an untrusted source.
- The data is used to dynamically construct a SQL query
The main consequences are:
- Confidentiality: Since SQL databases generally hold sensitive data, loss of confidentiality is a frequent problem with SQL Injection vulnerabilities.
- Authentication: If poor SQL commands are used to check user names and passwords, it may be possible to connect to a system as another user with no previous knowledge of the password.
- Authorization: If authorization information is held in a SQL database, it may be possible to change this information through the successful exploitation of a SQL Injection vulnerability.
- Integrity: Just as it may be possible to read sensitive information, it is also possible to make changes or even delete this information with a SQL Injection attack.
Risk Factors
The pla

*[Content truncated for brevity.]*

        # Technical Details

        _No specific information extracted._

        # Indicators

        _No specific information extracted._

        # Impact

        _No specific information extracted._

        # Detection

        _No specific information extracted._

        # Mitigation

        _No specific information extracted._

        # References

        - Source: [OWASP](https://owasp.org/www-community/attacks/SQL_Injection)
        - Category: Web_SQL_Injection
        - Generated: 2026-06-26

        _No specific information extracted._

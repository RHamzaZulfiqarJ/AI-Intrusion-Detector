        ---
        title: OWASP SQL Injection Prevention Cheat Sheet
        category: Web_SQL_Injection
        source: OWASP
        url: https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html
        date: 2026-06-26
        ---

        # Overview

        SQL Injection Prevention Cheat Sheet¶
Introduction¶
This cheat sheet will help you prevent SQL injection flaws in your applications. It will define what SQL injection is, explain where those flaws occur, and provide four options for defending against SQL injection attacks. SQL Injection attacks are common because:
- SQL Injection vulnerabilities are very common.
- The application's database is a frequent target for attackers because it typically contains sensitive or critical data.
What Is a SQL Injection Attack?¶
Attackers can use SQL injection on an application if it has dynamic database queries that use string concatenation and user-supplied input. To avoid SQL injection flaws, developers need to:
- Stop writing dynamic queries with string concatenation.
- Prevent malicious SQL input from being included in executed queries.
There are simple techniques for preventing SQL injection vulnerabilities, and they can be used with practically any kind of programming language and any type of database. While XML databases can have similar problems (e.g., XPath and XQuery injection), these techniques can be used to protect them as well.
Anatomy of a Typical SQL Injection Vulnerability¶
A common SQL injection flaw in Java is shown below. Because its unvalidated "customerName" parameter is simply appended to the query, an attacker can enter SQL code into that query and the application would take the attacker's code and execute it on the database.
String query = "SELECT account_balance FROM user_data WHERE user_name = "
 + request.getParameter("customerName");
try {
 Statement statement = connection.createStatement( ... );
 ResultSet results = statement.executeQuery( query );
}
...
Primary Defenses¶
- Option 1: Use of Prepared Statements (with Parameterized Queries)
- Option 2: Use of Properly Constructed Stored Procedures
- Option 3: Allow-list Input Validation
- Option 4: STRONGLY DISCOURAGED: Escaping All User Supplied Input
Defense Option 1: Prepared Statements (with Parameterized Queries)¶
When developers are taught how to write database queries, they should be told to use prepared statements with variable binding (aka parameterized queries). Prepared statements are simple to write and easier to understand than dynamic queries, and parameterized queries force the developer to define all SQL code first and pass in each parameter to the query later.
If database queries use this coding style, the database will always distinguish between code and data, regardless of what user input is supplied. Also, prepared statements ensure that an attacker cannot change the intent of a query, even if SQL commands are inserted by an attacker.
Safe Java Prepared Statement Example¶
In the safe Java example below, if an attacker were to enter the userID as tom' or '1'='1, the parameterized query would look for a username that literally matches the entire string tom' or '1'='1. Thus, the database would be protected against injections of malicious SQL code.
The following code

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

        - Source: [OWASP](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
        - Category: Web_SQL_Injection
        - Generated: 2026-06-26

        _No specific information extracted._

        ---
        title: OWASP Credential Stuffing
        category: FTP_Patator
        source: OWASP
        url: https://owasp.org/www-community/attacks/Credential_stuffing
        date: 2026-06-26
        ---

        # Overview

        Credential stuffing
Contributor(s): Jmanico, Dirk Wetter, kingthorin, Nick Malcolm , Jahanrajkar Singh
Description
Credential stuffing is the automated injection of stolen username and password pairs (“credentials”) in to website login forms, in order to fraudulently gain access to user accounts.
Since many users will re-use the same password and username/email, when those credentials are exposed (by a database breach or phishing attack, for example) submitting those sets of stolen credentials into dozens or hundreds of other sites can allow an attacker to compromise those accounts too.
Credential Stuffing is a subset of the brute force attack category. Brute forcing will attempt to try multiple passwords against one or multiple accounts; guessing a password, in other words. Credential Stuffing typically refers to specifically using known (breached) username / password pairs against other websites.
Attackers can also use information found in data leaks to reset passwords, particularly for business accounts. Since business information is often public, it is easier for attackers to obtain phone numbers, guess email addresses, and gather other relevant information. This method leverages security questions, recovery emails, or other personal information that might be included in the breach, allowing the attacker to take over accounts even if the passwords are not reused.
Likelihood & Severity
Credential stuffing is one of the most common techniques used to take-over user accounts.
Credential stuffing is dangerous to both consumers and enterprises because of the ripple effects of these breaches. For more information on this please reference the Examples section showing the connected chain of events from one breach to another through credential stuffing.
Anatomy of Attack
- The attacker acquires usernames and passwords from a website breach, phishing attack, password dump site.
- The attacker uses automated tools to test the stolen credentials against many websites (for instance, social media sites, online marketplaces, or web apps).
- If the login is successful, the attacker knows they have a set of valid credentials.
Now the attacker knows they have access to an account. Potential next steps include:
- Draining stolen accounts of stored value or making purchases.
- Accessing sensitive information such as credit card numbers, private messages, pictures, or documents.
- Using the account to send phishing messages or spam.
- Selling known-valid credentials to one or more of the compromised sites for other attackers to use.
Diagram
In the diagram above, acme.com’s database is compromised. An attacker takes the breached database and tries the credentials on three other websites, looking for successful logins. The attacker identifies two websites where the user “spongebob” is reusing their password, and one website where the user “sally” is reusing their password. The attacker can now get access to those three accounts.
Defense
Defenses against Credential 

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

        - Source: [OWASP](https://owasp.org/www-community/attacks/Credential_stuffing)
        - Category: FTP_Patator
        - Generated: 2026-06-26

        _No specific information extracted._

        ---
        title: OWASP Credential Stuffing Prevention Cheat Sheet
        category: Web_Brute_Force
        source: OWASP
        url: https://cheatsheetseries.owasp.org/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html
        date: 2026-06-26
        ---

        # Overview

        Credential Stuffing Prevention Cheat Sheet¶
Introduction¶
This cheatsheet covers defences against two common types of authentication-related attacks: credential stuffing and password spraying. Although these are separate, distinct attacks, in many cases the defences that would be implemented to protect against them are the same, and they would also be effective at protecting against brute-force attacks. A summary of these different attacks is listed below:
| Attack Type | Description | 
|---|---|
| Brute Force | Testing multiple passwords from dictionary or other source against a single account. | 
| Credential Stuffing | Testing username/password pairs obtained from the breach of another site. | 
| Password Spraying | Testing a single weak password against a large number of different accounts. | 
Multi-Factor Authentication¶
Multi-factor authentication (MFA) is by far the best defense against the majority of password-related attacks, including credential stuffing and password spraying, with analysis by Microsoft suggesting that it would have stopped 99.9% of account compromises. As such, it should be implemented wherever possible. Historically, depending on the audience of the application, it may not have been practical or feasible to enforce the use of MFA, however with modern browsers and mobile devices now supporting FIDO2 Passkeys and other forms of MFA, it is attainable for most use cases.
In order to balance security and usability, multi-factor authentication can be combined with other techniques to require the 2nd factor only in specific circumstances where there is reason to suspect that the login attempt may not be legitimate, such as a login from:
- A new browser/device or IP address.
- An unusual country or location.
- Specific countries that are considered untrusted or typically do not contain users of a service.
- An IP address that appears on known denylists or is associated with anonymization services, such as proxy or VPN services.
- An IP address that has tried to login to multiple accounts.
- A login attempt that appears to be scripted or from a bot rather than a human (i.e. large login volume sourced from a single IP or subnet).
Or an organization may choose to require MFA in the form of a "step-up" authentication for the above scenarios during a session combined with a request for a high risk activity such as:
- Large currency transactions
- Privileged or Administrative configuration changes
Additionally, for enterprise applications, known trusted IP ranges could be added to an allowlist so that MFA is not required when users connect from these ranges.
Alternative Defenses¶
Where it is not possible to implement MFA, there are many alternative defenses that can be used to protect against credential stuffing and password spraying. In isolation none of these are as effective as MFA, however multiple, layered defenses can provide a reasonable degree of protection. In many cases, these mechanisms will also protect against brute-fo

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

        - Source: [OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html)
        - Category: Web_Brute_Force
        - Generated: 2026-06-26

        _No specific information extracted._

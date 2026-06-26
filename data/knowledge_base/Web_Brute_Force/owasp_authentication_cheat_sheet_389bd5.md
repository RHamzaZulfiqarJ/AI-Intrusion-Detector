        ---
        title: OWASP Authentication Cheat Sheet
        category: Web_Brute_Force
        source: OWASP
        url: https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html
        date: 2026-06-26
        ---

        # Overview

        Authentication Cheat Sheet¶
Introduction¶
Authentication (AuthN) is the process of verifying that an individual, entity, or website is who or what it claims to be by determining the validity of one or more authenticators (like passwords, fingerprints, or security tokens) that are used to back up this claim.
Digital Identity is the unique representation of a subject engaged in an online transaction. A digital identity is always unique in the context of a digital service but does not necessarily need to be traceable back to a specific real-life subject.
Identity Proofing establishes that a subject is actually who they claim to be. This concept is related to KYC concepts and it aims to bind a digital identity with a real person.
Session Management is a process by which a server maintains the state of an entity interacting with it. This is required for a server to remember how to react to subsequent requests throughout a transaction. Sessions are maintained on the server by a session identifier which can be passed back and forth between the client and server when transmitting and receiving requests. Sessions should be unique per user and computationally very difficult to predict. The Session Management Cheat Sheet contains further guidance on the best practices in this area.
Authentication General Guidelines¶
User IDs¶
The primary function of a User ID is to uniquely identify a user within a system. Ideally, User IDs should be randomly generated to prevent the creation of predictable or sequential IDs, which could pose a security risk, especially in systems where User IDs might be exposed or inferred from external sources.
Usernames¶
Usernames are easy-to-remember identifiers chosen by the user and used for identifying themselves when logging into a system or service. The terms User ID and username might be used interchangeably if the username chosen by the user also serves as their unique identifier within the system.
Users should be permitted to use their email address as a username, provided the email is verified during sign-up. Additionally, they should have the option to choose a username other than an email address. For information on validating email addresses, please visit the input validation cheat sheet email discussion.
Authentication Solution and Sensitive Accounts¶
- Do NOT allow login with sensitive accounts (i.e. accounts that can be used internally within the solution such as to a backend / middleware / database) to any front-end user interface
- Do NOT use the same authentication solution (e.g. IDP / AD) used internally for unsecured access (e.g., public access / DMZ)
Implement Proper Password Strength Controls¶
A key concern when using passwords for authentication is password strength. A "strong" password policy makes it difficult or even improbable for one to guess the password through either manual or automated means. The following characteristics define a strong password:
- Password Length- Minimum length for passwords should be 

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

        - Source: [OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
        - Category: Web_Brute_Force
        - Generated: 2026-06-26

        _No specific information extracted._

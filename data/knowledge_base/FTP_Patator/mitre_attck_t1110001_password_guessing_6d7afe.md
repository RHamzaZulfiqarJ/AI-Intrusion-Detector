        ---
        title: MITRE ATT&CK T1110.001 - Password Guessing
        category: FTP_Patator
        source: MITRE ATT&CK
        url: https://attack.mitre.org/techniques/T1110/001/
        date: 2026-06-26
        ---

        # Overview

        | ID | Name | 
|---|---|
| T1110.001 | Password Guessing | 
| T1110.002 | Password Cracking | 
| T1110.003 | Password Spraying | 
| T1110.004 | Credential Stuffing | 
Adversaries with no prior knowledge of legitimate credentials within the system or environment may guess passwords to attempt access to accounts. Without knowledge of the password for an account, an adversary may opt to systematically guess the password using a repetitive or iterative mechanism. An adversary may guess login credentials without prior knowledge of system or environment passwords during an operation by using a list of common passwords. Password guessing may or may not take into account the target's policies on password complexity or use policies that may lock accounts out after a number of failed attempts.
Guessing passwords can be a risky option because it could cause numerous authentication failures and account lockouts, depending on the organization's login failure policies. [1]
Typically, management services over commonly used ports are used when guessing passwords. Commonly targeted services include the following:
In addition to management services, adversaries may "target single sign-on (SSO) and cloud-based applications utilizing federated authentication protocols," as well as externally facing email applications, such as Office 365.[2]. Further, adversaries may abuse network device interfaces (such as wlanAPI) to brute force accessible wifi-router(s) via wireless authentication protocols.[3]
In default environments, LDAP and Kerberos connection attempts are less likely to trigger events over SMB, which creates Windows "logon failure" event ID 4625.
| ID | Name | Description | 
|---|---|---|
| G0007 | APT28 | APT28 has used a brute-force/password-spray tooling that operated in two modes: in brute-force mode it typically sent over 300 authentication attempts per hour per targeted account over the course of several hours or days.[4] APT28 has also used a Kubernetes cluster to conduct distributed, large-scale password guessing attacks.[5] | 
| G0016 | APT29 | APT29 has successfully conducted password guessing attacks against a list of mailboxes.[6] | 
| S0020 | China Chopper | China Chopper's server component can perform brute force password guessing against authentication portals.[7] | 
| S0488 | CrackMapExec | CrackMapExec can brute force passwords for a specified user on a single target system or across an entire network.[8] | 
| S0367 | Emotet | Emotet has been observed using a hard coded list of passwords to brute force user accounts. [9][10][11][12][13][14] | 
| S0698 | HermeticWizard | HermeticWizard can use a list of hardcoded credentials in attempt to authenticate to SMB shares.[15] | 
| S0532 | Lucifer | Lucifer has attempted to brute force TCP ports 135 (RPC) and 1433 (MSSQL) with the default username or list of usernames and passwords.[16] | 
| S0598 | P.A.S. Webshell | P.A.S. Webshell can use predefined users and passwords to execute brute force attack

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

        - Source: [MITRE ATT&CK](https://attack.mitre.org/techniques/T1110/001/)
        - Category: FTP_Patator
        - Generated: 2026-06-26

        _No specific information extracted._

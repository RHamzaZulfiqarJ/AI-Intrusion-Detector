        ---
        title: MITRE ATT&CK T1110.003 - Password Spraying
        category: SSH_Patator
        source: MITRE ATT&CK
        url: https://attack.mitre.org/techniques/T1110/003/
        date: 2026-06-26
        ---

        # Overview

        | ID | Name | 
|---|---|
| T1110.001 | Password Guessing | 
| T1110.002 | Password Cracking | 
| T1110.003 | Password Spraying | 
| T1110.004 | Credential Stuffing | 
Adversaries may use a single or small list of commonly used passwords against many different accounts to attempt to acquire valid account credentials. Password spraying uses one password (e.g. 'Password01'), or a small list of commonly used passwords, that may match the complexity policy of the domain. Logins are attempted with that password against many different accounts on a network to avoid account lockouts that would normally occur when brute forcing a single account with many passwords. [1]
Typically, management services over commonly used ports are used when password spraying. Commonly targeted services include the following:
In addition to management services, adversaries may "target single sign-on (SSO) and cloud-based applications utilizing federated authentication protocols," as well as externally facing email applications, such as Office 365.[2]
In order to avoid detection thresholds, adversaries may deliberately throttle password spraying attempts to avoid triggering security alerting. Additionally, adversaries may leverage LDAP and Kerberos authentication attempts, which are less likely to trigger high-visibility events such as Windows "logon failure" event ID 4625 that is commonly triggered by failed SMB connection attempts.[3]
| ID | Name | Description | 
|---|---|---|
| G1030 | Agrius | Agrius engaged in password spraying via SMB in victim environments.[4] | 
| G0007 | APT28 | APT28 has used a brute-force/password-spray tooling that operated in two modes: in password-spraying mode it conducted approximately four authentication attempts per hour per targeted account over the course of several days or weeks.[5][6] APT28 has also used a Kubernetes cluster to conduct distributed, large-scale password spray attacks.[7] | 
| C0051 | APT28 Nearest Neighbor Campaign | During APT28 Nearest Neighbor Campaign, APT28 performed password-spray attacks against public facing services to validate credentials.[8] | 
| G0016 | APT29 | APT29 has conducted brute force password spray attacks.[9][10][11] | 
| G0064 | APT33 | APT33 has used password spraying to gain access to target systems.[12][13] | 
| S0606 | Bad Rabbit | Bad Rabbit’s | 
| G0114 | Chimera | Chimera has used multiple password spraying attacks against victim's remote services to obtain valid user and administrator accounts.[15] | 
| S0488 | CrackMapExec | CrackMapExec can brute force credential authentication by using a supplied list of usernames and a single password.[16] | 
| G1003 | Ember Bear | Ember Bear has conducted password spraying against Outlook Web Access (OWA) infrastructure to identify valid user names and passwords.[17] | 
| G0125 | HAFNIUM | HAFNIUM has gained initial access through password spray attacks.[18] | 
| G1001 | HEXANE | HEXANE has used password spraying attacks to obtain valid credentials.[19] 

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

        - Source: [MITRE ATT&CK](https://attack.mitre.org/techniques/T1110/003/)
        - Category: SSH_Patator
        - Generated: 2026-06-26

        _No specific information extracted._

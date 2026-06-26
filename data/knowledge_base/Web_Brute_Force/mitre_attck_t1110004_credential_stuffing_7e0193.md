        ---
        title: MITRE ATT&CK T1110.004 - Credential Stuffing
        category: Web_Brute_Force
        source: MITRE ATT&CK
        url: https://attack.mitre.org/techniques/T1110/004/
        date: 2026-06-26
        ---

        # Overview

        | ID | Name | 
|---|---|
| T1110.001 | Password Guessing | 
| T1110.002 | Password Cracking | 
| T1110.003 | Password Spraying | 
| T1110.004 | Credential Stuffing | 
Adversaries may use credentials obtained from breach dumps of unrelated accounts to gain access to target accounts through credential overlap. Occasionally, large numbers of username and password pairs are dumped online when a website or service is compromised and the user account credentials accessed. The information may be useful to an adversary attempting to compromise accounts by taking advantage of the tendency for users to use the same passwords across personal and business accounts.
Credential stuffing is a risky option because it could cause numerous authentication failures and account lockouts, depending on the organization's login failure policies.
Typically, management services over commonly used ports are used when stuffing credentials. Commonly targeted services include the following:
In addition to management services, adversaries may "target single sign-on (SSO) and cloud-based applications utilizing federated authentication protocols," as well as externally facing email applications, such as Office 365.[1]
| ID | Name | Description | 
|---|---|---|
| G0114 | Chimera | Chimera has used credential stuffing against victim's remote services to obtain valid accounts.[2] | 
| S0266 | TrickBot | TrickBot uses brute-force attack against RDP with rdpscanDll module.[3][4] | 
| G1055 | VOID MANTICORE | VOID MANTICORE has utilized credential stuffing attacks to obtain initial access to victim environments.[5] | 
| ID | Mitigation | Description | 
|---|---|---|
| M1036 | Account Use Policies | Set account lockout policies after a certain number of failed login attempts to prevent passwords from being guessed. Too strict a policy may create a denial of service condition and render environments un-usable, with all accounts used in the brute force being locked-out. Use conditional access policies to block logins from non-compliant devices or from outside defined organization IP ranges.[6] Consider blocking risky authentication requests, such as those originating from anonymizing services/proxies.[7] | 
| M1032 | Multi-factor Authentication | Use multi-factor authentication. Where possible, also enable multi-factor authentication on externally facing services. | 
| M1027 | Password Policies | Refer to NIST guidelines when creating password policies. [8] | 
| M1018 | User Account Management | Proactively reset accounts that are known to be part of breached credentials either immediately, or after detecting bruteforce attempts. | 
| ID | Name | Analytic ID | Analytic Description | 
|---|---|---|---|
| DET0460 | Credential Stuffing Detection via Reused Breached Credentials Across Services | AN1262 | Multiple failed authentication attempts using distinct username/password pairs from a single IP address or session within a short time window, targeting common services like RDP or SMB | 
| 

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

        - Source: [MITRE ATT&CK](https://attack.mitre.org/techniques/T1110/004/)
        - Category: Web_Brute_Force
        - Generated: 2026-06-26

        _No specific information extracted._

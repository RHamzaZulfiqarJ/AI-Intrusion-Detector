        ---
        title: MITRE ATT&CK T1110 - Brute Force
        category: FTP_Patator
        source: MITRE ATT&CK
        url: https://attack.mitre.org/techniques/T1110/
        date: 2026-06-26
        ---

        # Overview

        Adversaries may use brute force techniques to gain access to accounts when passwords are unknown or when password hashes are obtained.[1] Without knowledge of the password for an account or set of accounts, an adversary may systematically guess the password using a repetitive or iterative mechanism.[2] Brute forcing passwords can take place via interaction with a service that will check the validity of those credentials or offline against previously acquired credential data, such as password hashes.
Brute forcing credentials may take place at various points during a breach. For example, adversaries may attempt to brute force access to Valid Accounts within a victim environment leveraging knowledge gathered from other post-compromise behaviors such as OS Credential Dumping, Account Discovery, or Password Policy Discovery. Adversaries may also combine brute forcing activity with behaviors such as External Remote Services as part of Initial Access.
If an adversary guesses the correct password but fails to login to a compromised account due to location-based conditional access policies, they may change their infrastructure until they match the victim’s location and therefore bypass those policies.[3]
| ID | Name | Description | 
|---|---|---|
| C0025 | 2016 Ukraine Electric Power Attack | During the 2016 Ukraine Electric Power Attack, Sandworm Team used a script to attempt RPC authentication against a number of hosts.[2] | 
| G1030 | Agrius | Agrius engaged in various brute forcing activities via SMB in victim environments.[4] | 
| G0007 | APT28 | APT28 can perform brute force attacks to obtain credentials.[5][1][6] | 
| G0082 | APT38 | APT38 has used brute force techniques to attempt account access when passwords are unknown or when password hashes are unavailable.[7] | 
| G0087 | APT39 | |
| G0096 | APT41 | APT41 performed password brute-force attacks on the local admin account.[9] | 
| S0572 | Caterpillar WebShell | Caterpillar WebShell has a module to perform brute force attacks on a system.[10] | 
| S0220 | Chaos | Chaos conducts brute force attacks against SSH services to gain initial access.[11] | 
| S0488 | CrackMapExec | CrackMapExec can brute force supplied user credentials across a network range.[12] | 
| G0105 | DarkVishnya | DarkVishnya used brute-force attack to obtain login data.[13] | 
| G0035 | Dragonfly | Dragonfly has attempted to brute force credentials to gain access.[14] | 
| G1003 | Ember Bear | Ember Bear used the | 
| G0053 | FIN5 | FIN5 has has used the tool GET2 Penetrator to look for remote login and hard-coded credentials.[16][17] | 
| G0117 | Fox Kitten | Fox Kitten has brute forced RDP credentials.[18] | 
| G1001 | HEXANE | HEXANE has used brute force attacks to compromise valid credentials.[19] | 
| S0599 | Kinsing | |
| G0049 | OilRig | OilRig has used brute force techniques to obtain credentials.[21][22] | 
| C0022 | Operation Dream Job | During Operation Dream Job, Lazarus Group performed brute force attacks against

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

        - Source: [MITRE ATT&CK](https://attack.mitre.org/techniques/T1110/)
        - Category: FTP_Patator
        - Generated: 2026-06-26

        _No specific information extracted._

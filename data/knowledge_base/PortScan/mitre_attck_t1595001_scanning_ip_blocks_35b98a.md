        ---
        title: MITRE ATT&CK T1595.001 - Scanning IP Blocks
        category: PortScan
        source: MITRE ATT&CK
        url: https://attack.mitre.org/techniques/T1595/001/
        date: 2026-06-26
        ---

        # Overview

        | ID | Name | 
|---|---|
| T1595.001 | Scanning IP Blocks | 
| T1595.002 | Vulnerability Scanning | 
| T1595.003 | Wordlist Scanning | 
Adversaries may scan victim IP blocks to gather information that can be used during targeting. Public IP addresses may be allocated to organizations by block, or a range of sequential addresses.
Adversaries may scan IP blocks in order to Gather Victim Network Information, such as which IP addresses are actively in use as well as more detailed information about hosts assigned these addresses. Scans may range from simple pings (ICMP requests and responses) to more nuanced scans that may reveal host software/versions via server banners or other network artifacts.[1] Information from these scans may reveal opportunities for other forms of reconnaissance (ex: Search Open Websites/Domains or Search Open Technical Databases), establishing operational resources (ex: Develop Capabilities or Obtain Capabilities), and/or initial access (ex: External Remote Services).
| ID | Name | Description | 
|---|---|---|
| C0062 | Anthropic AI-orchestrated Campaign | During the Anthropic AI-orchestrated Campaign, the adversary used Claude Code to scan infrastructure across IP ranges associated with the target organization.[2] | 
| G1003 | Ember Bear | Ember Bear has targeted IP ranges for vulnerability scanning related to government and critical infrastructure organizations.[3] | 
| G0139 | TeamTNT | TeamTNT has scanned specific lists of target IP addresses.[4] | 
| ID | Mitigation | Description | 
|---|---|---|
| M1056 | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. Efforts should focus on minimizing the amount and sensitivity of data available to external parties. | 
| ID | Name | Analytic ID | Analytic Description | 
|---|---|---|---|
| DET0817 | Detection of Scanning IP Blocks | AN1949 | Monitoring the content of network traffic can help detect patterns associated with active scanning activities. This can include identifying repeated connection attempts, unusual scanning behaviors, or probing activity targeting multiple IP addresses across a network. |

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

        - Source: [MITRE ATT&CK](https://attack.mitre.org/techniques/T1595/001/)
        - Category: PortScan
        - Generated: 2026-06-26

        _No specific information extracted._

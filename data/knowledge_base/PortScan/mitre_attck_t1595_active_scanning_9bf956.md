        ---
        title: MITRE ATT&CK T1595 - Active Scanning
        category: PortScan
        source: MITRE ATT&CK
        url: https://attack.mitre.org/techniques/T1595/
        date: 2026-06-26
        ---

        # Overview

        Adversaries may execute active reconnaissance scans to gather information that can be used during targeting. Active scans are those where the adversary probes victim infrastructure via network traffic, as opposed to other forms of reconnaissance that do not involve direct interaction.
Adversaries may perform different forms of active scanning depending on what information they seek to gather. These scans can also be performed in various ways, including using native features of network protocols such as ICMP.[1][2] Information from these scans may reveal opportunities for other forms of reconnaissance (ex: Search Open Websites/Domains or Search Open Technical Databases), establishing operational resources (ex: Develop Capabilities or Obtain Capabilities), and/or initial access (ex: External Remote Services or Exploit Public-Facing Application).
| ID | Name | Description | 
|---|---|---|
| C0030 | Triton Safety Instrumented System Attack | In the Triton Safety Instrumented System Attack, TEMP.Veles engaged in network reconnaissance against targets of interest.[3] | 
| ID | Mitigation | Description | 
|---|---|---|
| M1056 | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. Efforts should focus on minimizing the amount and sensitivity of data available to external parties. | 
| ID | Name | Analytic ID | Analytic Description | 
|---|---|---|---|
| DET0830 | Detection of Active Scanning | AN1962 | Monitor network data for uncommon data flows. Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. |

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

        - Source: [MITRE ATT&CK](https://attack.mitre.org/techniques/T1595/)
        - Category: PortScan
        - Generated: 2026-06-26

        _No specific information extracted._

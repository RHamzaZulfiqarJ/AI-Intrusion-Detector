        ---
        title: MITRE ATT&CK T1499.001 - OS Exhaustion Flood (Slowloris)
        category: DoS_Slowloris
        source: MITRE ATT&CK
        url: https://attack.mitre.org/techniques/T1499/001/
        date: 2026-06-26
        ---

        # Overview

        | ID | Name | 
|---|---|
| T1499.001 | OS Exhaustion Flood | 
| T1499.002 | Service Exhaustion Flood | 
| T1499.003 | Application Exhaustion Flood | 
| T1499.004 | Application or System Exploitation | 
Adversaries may launch a denial of service (DoS) attack targeting an endpoint's operating system (OS). A system's OS is responsible for managing the finite resources as well as preventing the entire system from being overwhelmed by excessive demands on its capacity. These attacks do not need to exhaust the actual resources on a system; the attacks may simply exhaust the limits and available resources that an OS self-imposes.
Different ways to achieve this exist, including TCP state-exhaustion attacks such as SYN floods and ACK floods.[1] With SYN floods, excessive amounts of SYN packets are sent, but the 3-way TCP handshake is never completed. Because each OS has a maximum number of concurrent TCP connections that it will allow, this can quickly exhaust the ability of the system to receive new requests for TCP connections, thus preventing access to any TCP service provided by the server.[2]
ACK floods leverage the stateful nature of the TCP protocol. A flood of ACK packets are sent to the target. This forces the OS to search its state table for a related TCP connection that has already been established. Because the ACK packets are for connections that do not exist, the OS will have to search the entire state table to confirm that no match exists. When it is necessary to do this for a large flood of packets, the computational requirements can cause the server to become sluggish and/or unresponsive, due to the work it must do to eliminate the rogue ACK packets. This greatly reduces the resources available for providing the targeted service.[3]
| ID | Mitigation | Description | 
|---|---|---|
| M1037 | Filter Network Traffic | Leverage services provided by Content Delivery Networks (CDN) or providers specializing in DoS mitigations to filter traffic upstream from services.[4] Filter boundary traffic by blocking source addresses sourcing the attack, blocking ports that are being targeted, or blocking protocols being used for transport. To defend against SYN floods, enable SYN Cookies. | 
| ID | Name | Analytic ID | Analytic Description | 
|---|---|---|---|
| DET0356 | Endpoint DoS via OS Exhaustion Flood Detection Strategy | AN1012 | Burst of incomplete TCP handshakes (e.g., SYN floods) or uncorrelated ACK packets targeting the state table resulting in OS resource exhaustion. | 
| AN1013 | Flood of spoofed SYN or ACK packets causing exhaustion of OS TCP state table, potentially via user-space utilities or kernel-level DoS agents. | ||
| AN1014 | Adversary tool/script issuing mass SYN/ACK floods that degrade OS responsiveness and interrupt service response on macOS endpoints. |

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

        - Source: [MITRE ATT&CK](https://attack.mitre.org/techniques/T1499/001/)
        - Category: DoS_Slowloris
        - Generated: 2026-06-26

        _No specific information extracted._

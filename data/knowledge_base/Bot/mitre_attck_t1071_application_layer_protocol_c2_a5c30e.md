        ---
        title: MITRE ATT&CK T1071 - Application Layer Protocol (C2)
        category: Bot
        source: MITRE ATT&CK
        url: https://attack.mitre.org/techniques/T1071/
        date: 2026-06-26
        ---

        # Overview

        Adversaries may communicate using OSI application layer protocols to avoid detection/network filtering by blending in with existing traffic. Commands to the remote system, and often the results of those commands, will be embedded within the protocol traffic between the client and server.
Adversaries may utilize many different protocols, including those used for web browsing, transferring files, electronic mail, DNS, or publishing/subscribing. For connections that occur internally within an enclave (such as those between a proxy or pivot node and other nodes), commonly used protocols are SMB, SSH, or RDP.[1]
| ID | Name | Description | 
|---|---|---|
| S0660 | Clambling | Clambling has the ability to use Telnet for communication.[2] | 
| S0038 | Duqu | Duqu uses a custom command and control protocol that communicates over commonly used ports, and is frequently encapsulated by application layer protocols.[3] | 
| C0041 | FrostyGoop Incident | During FrostyGoop Incident, the adversary initiated Layer Two Tunnelling Protocol (L2TP) connections to Moscow-based IP addresses.[4] | 
| S0601 | Hildegard | |
| G1032 | INC Ransom | INC Ransom has used valid accounts over RDP to connect to targeted systems.[6] | 
| S0532 | Lucifer | Lucifer can use the Stratum protocol on port 10001 for communication between the cryptojacking bot and the mining server.[7] | 
| G0059 | Magic Hound | Magic Hound malware has used IRC for C2.[8][9] | 
| S0034 | NETEAGLE | Adversaries can also use NETEAGLE to establish an RDP connection with a controller over TCP/7519. | 
| S1147 | Nightdoor | Nightdoor uses TCP and UDP communication for command and control traffic.[10][11] | 
| S1084 | QUIETEXIT | QUIETEXIT can use an inverse negotiated SSH connection as part of its C2.[1] | 
| S1130 | Raspberry Robin | Raspberry Robin is capable of contacting the TOR network for delivering second-stage payloads.[12][13][14] | 
| G0106 | Rocke | Rocke issued wget requests from infected systems to the C2.[15] | 
| S0623 | Siloscape | |
| S0633 | Sliver | Sliver can utilize the Wireguard VPN protocol for command and control.[17] | 
| G0139 | TeamTNT | |
| G1047 | Velvet Ant | Velvet Ant has used reverse SSH tunnels to communicate to victim devices.[19] | 
| ID | Mitigation | Description | 
|---|---|---|
| M1037 | Filter Network Traffic | Use network appliances to filter ingress or egress traffic and perform protocol-based filtering. Configure software on endpoints to filter network traffic. | 
| M1031 | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. | 
| ID | Name | Analytic ID | Analytic Description | 
|---|---|---|---|
| DET0444 | Detection of Command and Control Over Application Layer Protocols | AN1225 | Detects suspicious usage of common application-layer protocols (e.g., HTTP, HTTPS, DNS, SMB) by abnormal processes, with high

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

        - Source: [MITRE ATT&CK](https://attack.mitre.org/techniques/T1071/)
        - Category: Bot
        - Generated: 2026-06-26

        _No specific information extracted._

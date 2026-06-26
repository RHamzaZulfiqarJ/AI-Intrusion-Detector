        ---
        title: MITRE ATT&CK T1499 - Endpoint Denial of Service (Hulk)
        category: DoS_Hulk
        source: MITRE ATT&CK
        url: https://attack.mitre.org/techniques/T1499/002/
        date: 2026-06-26
        ---

        # Overview

        | ID | Name | 
|---|---|
| T1499.001 | OS Exhaustion Flood | 
| T1499.002 | Service Exhaustion Flood | 
| T1499.003 | Application Exhaustion Flood | 
| T1499.004 | Application or System Exploitation | 
Adversaries may target the different network services provided by systems to conduct a denial of service (DoS). Adversaries often target the availability of DNS and web services, however others have been targeted as well.[1] Web server software can be attacked through a variety of means, some of which apply generally while others are specific to the software being used to provide the service.
One example of this type of attack is known as a simple HTTP flood, where an adversary sends a large number of HTTP requests to a web server to overwhelm it and/or an application that runs on top of it. This flood relies on raw volume to accomplish the objective, exhausting any of the various resources required by the victim software to provide the service.[2]
Another variation, known as a SSL renegotiation attack, takes advantage of a protocol feature in SSL/TLS. The SSL/TLS protocol suite includes mechanisms for the client and server to agree on an encryption algorithm to use for subsequent secure connections. If SSL renegotiation is enabled, a request can be made for renegotiation of the crypto algorithm. In a renegotiation attack, the adversary establishes a SSL/TLS connection and then proceeds to make a series of renegotiation requests. Because the cryptographic renegotiation has a meaningful cost in computation cycles, this can cause an impact to the availability of the service when done in volume.[3]
| ID | Mitigation | Description | 
|---|---|---|
| M1037 | Filter Network Traffic | Leverage services provided by Content Delivery Networks (CDN) or providers specializing in DoS mitigations to filter traffic upstream from services.[4] Filter boundary traffic by blocking source addresses sourcing the attack, blocking ports that are being targeted, or blocking protocols being used for transport. | 
| ID | Name | Analytic ID | Analytic Description | 
|---|---|---|---|
| DET0173 | Detection Strategy for Endpoint DoS via Service Exhaustion Flood | AN0489 | High-frequency, repetitive service requests (e.g., HTTP, TLS renegotiation) originating from a single or small set of source IPs targeting endpoint web services or application ports, leading to exhaustion of CPU or memory on targeted Windows services. | 
| AN0490 | Excessive inbound HTTP or TLS connections to services such as Apache or Nginx, causing worker thread exhaustion or segmentation faults. | ||
| AN0491 | Flood of incoming TLS or HTTP(S) connections to macOS-hosted services (e.g., MAMP, Apache), causing high CPU usage and system unresponsiveness. | ||
| AN0492 | Automated or scripted HTTP/TLS flooding from one VM or cloud instance against another service, exploiting compute-based billing or exhaustion of service infrastructure. |

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

        - Source: [MITRE ATT&CK](https://attack.mitre.org/techniques/T1499/002/)
        - Category: DoS_Hulk
        - Generated: 2026-06-26

        _No specific information extracted._

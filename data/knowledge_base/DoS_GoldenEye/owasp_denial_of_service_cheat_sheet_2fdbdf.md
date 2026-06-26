        ---
        title: OWASP Denial of Service Cheat Sheet
        category: DoS_GoldenEye
        source: OWASP
        url: https://cheatsheetseries.owasp.org/cheatsheets/Denial_of_Service_Cheat_Sheet.html
        date: 2026-06-26
        ---

        # Overview

        Denial of Service Cheat Sheet¶
Introduction¶
This cheat sheet describes a methodology for handling denial of service (DoS) attacks on different layers. It also serves as a platform for further discussion and analysis, since there are many different ways to perform DoS attacks.
Fundamentals¶
Because anti-DoS methods cannot be one-step solutions, your developers and application/infrastructure architects must develop DoS solutions carefully. They must keep in mind that "availability" is a basic part of the CIA triad.
Remember that if every part of the computing system within the interoperability flow does not function correctly, your infrastructure suffers. A successful DoS attack hinders the availability of instances or objects to a system and can eventually render the entire system inaccessible.
To ensure systems can be resilient and resist a DoS attack, we strongly suggest a thorough analysis on components within your inventory based on functionality, architecture and performance (i.e. application-wise, infrastructure and network related).
This DoS system inventory should look for potential places where DoS attacks can cause problems and highlight any single points of system failures, which can range from programming related errors to resource exhaustion. It should give you a clear picture of what issues are at stake (e.g. bottlenecks, etc.). To resolve problems, a solid understanding of your environment is essential to develop suitable defence mechanisms. These could be aligned with:
- Scaling options (up = inner hardware components, out = the number of complete components).
- Existing conceptual / logical techniques (such as applying redundancy measurements, bulk-heading, etc. - which expands your in-house capabilities).
- A cost analysis applied to your situation.
This document adopts a specific guidance structure from CERT-EU to analyze this subject, which you may need to change depending on your situation. It is not a complete approach but it will help you create fundamental blocks which should be utilized to assist you in constructing anti-DoS concepts fitting your needs.
Analyzing DoS attack surfaces¶
In this cheat sheet, we will use the DDOS classification as documented by CERT-EU to examine DoS system vulnerabilities. It uses the seven OSI model and focuses three main attack surfaces, namely Application, Session and Network.
1) Overview of potential DoS weaknesses¶
It is important to understand that each of these three attack categories needs to be considered when designing a DoS-resilient solution:
Application attacks focus on rendering applications unavailable by exhausting resources or by making it unusable in a functional way.
Session (or protocol) attacks focus on consuming server resources, or resources of intermediary equipment like firewalls and load-balancers.
Network (or volumetric) attacks focus on saturating the bandwidth of the network resource.
Note that OSI model layers 1 and 2 are not included in this categorization, so w

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

        - Source: [OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Denial_of_Service_Cheat_Sheet.html)
        - Category: DoS_GoldenEye
        - Generated: 2026-06-26

        _No specific information extracted._

        ---
        title: NIST SP 800-189 Resilient Interdomain Traffic Exchange
        category: DDoS
        source: NIST
        url: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-189.pdf
        date: 2026-06-26
        ---

        # Overview

        NIST Special Publication 800-189 

Resilient Interdomain Traffic Exchange: 
BGP Security and DDoS Mitigation 

Kotikalapudi Sriram 
Doug Montgomery 





This publication is available free of charge from: 
https://doi.org/10.6028/NIST.SP.800-189 




C O M P U T E R S E C U R I T Y

NIST Special Publication 800-189 

Resilient Interdomain Traffic Exchange: 
BGP Security and DDoS Mitigation 

Kotikalapudi Sriram 
Doug Montgomery 
Advanced Network Technology Division 
Information Technology Laboratory 







This publication is available free of charge from: 
https://doi.org/10.6028/NIST.SP.800-189 


December 2019 




U.S. Department of Commerce 
Wilbur L. Ross, Jr., Secretary 

National Institute of Standards and Technology 
Walter Copan, NIST Director and Under Secretary of Commerce for Standards and Technology

[... content truncated ...]

        # Technical Details

        NIST SP 800-189 RESILIENT INTERDOMAIN TRAFFIC EXCHANGE: 
 BGP SECURITY & DDOS MITIGATION 
iv 
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-189 
Reports on Computer Systems Technology 
The Information Technology Laboratory (ITL) at the National Institute of Standards and 
Technology (NIST) promotes the U.S. economy and public welfare by providing technical 
leadership for the Nation’s measurement and standards infrastructure. ITL develops tests, test 
methods, reference data, proof of concept implementations, and technical analyses to advance the 
development and productive use of information technology. ITL’s responsibilities in clude the 
development of management, administrative, technical, and physical standards and guidelines for 
the cost-effective security and privacy of other than national security-related information in federal 
information systems. The Special Publication 800-series reports on ITL’s research, guidelines, and 
outreach efforts in information system security, and its collaborative activities with industry, 
government, and academic organizations.

Abstract 
In recent years, numerous routing control plane anomalies, such as Border Gateway Protocol 
(BGP) prefix hijacking and route leaks, have resulted in denial-of-service (DoS), unwanted data 
traffic detours, and performance degradation. Large-scale distributed denial-of-service (DDoS) 
attacks on servers using spoofed internet protocol (IP) addresses and reflection-amplification in 
the data plane have also been frequent, resulting in significant disruption of services and 
damages. This special publication on Resilient Interdomain Traffic Exchange (RITE) includes 
initial guidance on securing the interdomain routing control traffic, preventing IP address 
spoofing, and certain aspects of DoS/DDoS detection and mitigation. 
Many of the recommendations in this publication focus on the Border Gateway Protocol (BGP). 
BGP is the control protocol used to distribute and compute paths between the tens of thousands 
of autonomous networks that comprise the internet. Technologies recommended in this 
document for securing the interdomain routing control traffic include Resource Public Key 
Infrastructure (RPKI), BGP origin validation (BGP-OV), and prefix filtering. Additionally, 
technologies recommended for mitigating DoS/DDoS attacks focus on prevention of IP address 
spoofing using source address validation (SAV) with access control lists (ACLs) and unicast 
Reverse Path Forwarding (uRPF). Other technologies (including some application plane 
methods) such as remotely triggered black hole (RTBH) filtering, flow specification (Flowspec), 
and response rate limiting (RRL) are also recommended as part of the overall security 
mechanisms. 
 Keywords 
Routing security and robustness; Internet infrastructure security; Border Gateway Protocol 
(BGP) security; prefix hijacks; IP address spoofing; distributed denial-of-service (DDoS); 
Resourc

*[Content truncated for brevity.]*

        # Indicators

        _No specific information extracted._

        # Impact

        _No specific information extracted._

        # Detection

        NIST SP 800-189 RESILIENT INTERDOMAIN TRAFFIC EXCHANGE: 
 BGP SECURITY & DDOS MITIGATION 
 4 
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-189 
The various types of unauthorized prefix originations described above are called prefix hijacks or 
false origin announcements. The unauthorized announcement of a prefix longer than the 
legitimate announcement is called a sub-prefix hijack. The consequences of such adverse actions 
can be serious and include denial-of-service, eavesdropping, misdirection to imposter servers (to 
steal login credentials or inject malware), or defeat of IP reputation systems to launch spam 
email. There have been numerous incidents involving prefix hijacks in recent years. There are 
several commercial services and research projects that track and log anomalies in the global BGP 
routing system [BGPmon] [ThousandEyes] [BGPStream] [ARTEMIS]. Many of these sites 
provide detailed forensic analyses of observed attack scenarios. 
2.2 AS Path Modification 
BGP messages carry a sequence of AS numbers that indicates the “path” of interconnected 
networks over which data will flow. This “AS_PATH” [RFC4271] data is often used to 
implement routing policies that reflect the business agreements and peering policies that have 
been negotiated between networks. BGP is also vulnerable to modification of the AS_PATH 
information that it conveys. As an example, a malicious AS which receives a BGP update may 
illegitimately remove some of the preceding ASes in the AS_PATH attribute of the update to 
make the path length seem shorter. When the update modified in this manner is propagated, the 
ASes upstream can be deceived to believe that the path to the advertised prefix via the adversary 
AS is shorter. By doing this, the adversary AS may seek to illegitimately increase its revenue 
from its customers, or may be able to eavesdrop on traffic that would otherwise not transit 
through their AS. 
Another example of maliciously modifying a BGP update is when an adversary AS replaces a 
prefix in a received update with a more-specific prefix (subsumed by the prefix) and then 
forwards the update to neighbors. This attack is known as a Kapela-Pilosov attack [Kapela-
Pilosov]. Only the prefix is replaced by a more-specific prefix, but the AS path is not altered. In 
BGP path selection, a more-specific prefix advertisement wins over a less-specific prefix 
advertisement. This means that ASes on the internet would widely accept and use the adversary 
AS’s advertisement for the more-specific prefix. The exceptions are the ASes that are in the AS 
path from the adversary to the prefix. These exception ASes reject any advertisements that they 
may receive for the more-specific prefix because they detect their own AS number in the AS 
path. This is called avoidance of loop detection and is a standard practice in BGP. Thus, the data 
path from the adversary AS to the prefix (i.e., the network in consideration) r

*[Content truncated for brevity.]*

        # Mitigation

        NIST SP 800-189 RESILIENT INTERDOMAIN TRAFFIC EXCHANGE: 
 BGP SECURITY & DDOS MITIGATION 
 13 
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-189 

Figure 6: RPKI data retrieval, caching, and propagation to routers 
A BGP router can use the ROA information retrieved from an RPKI cache server to mitigate the 
risk of prefix hijacks and some forms of route leaks in advertised routes. A BGP router would 
typically receive a validated list of {prefix, maxlength, origin AS} tuples (derived from valid 
ROAs) from one or more RPKI cache servers. This list may be called a white list. The router 
makes use of this list with the BGP origin validation (BGP-OV) process depicted in Figure 7 to 
determine the validation state of an advertised route [RFC6811]. A BGP route is deemed to have 
a “Valid” origin if the {prefix, origin AS} pair in the advertised route can be corroborated with 
the list (i.e., the pair is permissible in accordance with at least one ROA; see Figure 7 for the 
details). A route is considered “Invalid” if there is a mismatch with the list (i.e., AS number does 
not match, or the prefix length exceeds maxlength; see Figure 7 for additional details). Further, a 
route is deemed “NotFound” if the prefix announced is not covered by any prefix in the white list 
(i.e., there is no ROA that contains a prefix that equals or subsumes the announced prefix). When 
an AS_SET [RFC4271] is present in a BGP update, it is not possible to clearly determine the 
origin AS from the AS_PATH [RFC6811]. Thus, an update containing an AS_SET in its 
AS_PATH can never receive an assessment of “Valid” in the origin validation process (see 
Figure 7). The use of AS_SET in BGP updates is discouraged in BCP 172 [RFC6472]. The 
RPKI-based origin validation may be supplemented by validation based on IRR data (see Section 
4.1).

        # References

        - Source: [NIST](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-189.pdf)
        - Category: DDoS
        - Generated: 2026-06-26

        Authority 
This publication has been developed by NIST in accordance with its statutory responsibilities under the 
Federal Information Security Modernization Act (FISMA) of 2014, 44 U.S.C. § 3551 et seq., Public Law 
(P.L.) 113-283. NIST is responsible for developing information security standards and guidelines, including 
minimum requirements for federal information systems, but such standards and guidelines shall not apply 
to national security systems without the express approval of appropriate federal officials exercising policy 
authority over such systems. This guideline is consistent with the requirements of the Office of Management 
and Budget (OMB) Circular A-130. 
Nothing in this publication should be taken to contradict the standards and guidelines made mandatory and 
binding on f ederal agencies by the Secreta ry of Commerce under statutory authority. Nor should these 
guidelines be interpreted as altering or superseding the existing authorities of the Secretary of Commer

*[Content truncated for brevity.]*

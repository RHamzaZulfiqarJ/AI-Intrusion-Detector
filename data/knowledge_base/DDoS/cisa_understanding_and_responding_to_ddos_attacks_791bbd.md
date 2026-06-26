        ---
        title: CISA - Understanding and Responding to DDoS Attacks
        category: DDoS
        source: CISA
        url: https://www.cisa.gov/sites/default/files/2024-03/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf
        date: 2026-06-26
        ---

        # Overview

        Disclaimer: This document is marked TLP:CLEAR. Disclosure is not limited. Sources may use TLP:CLEAR when information carries minimal or 
no foreseeable risk of misuse, in accordance with applicable rules and procedures for public release. Subject to standard copyright rules, 
TLP:CLEAR information may be distributed without restriction. For more information on the Traffic Light Protocol, see 
http://www.cisa.gov/tlp/. 
TLP:CLEAR 





























Publication: March 21, 2024 
UNDERSTANDING AND 
RESPONDING TO DISTRIBUTED 
DENIAL-OF-SERVICE ATTACKS

2 CISA | FBI | MS-ISAC 
TLP:CLEAR 
TLP:CLEAR 
Change Record 
Version Date Revision/Change Description Section/Page Affected 
1.0 October 2022 Initial Version 
2.0 March 2024 
• Categorizes DDoS and DoS 
techniques into three types: 
Volumetric, Protocol, and 
Application. 
• Added DDoS technical 
definitions and nine visual aids. 
• Added mitigations for 
defending against the types of 
DDoS techniques outlined in 
the guide 
• p.4 through p.15

        # Technical Details

        6 CISA | FBI | MS-ISAC 
TLP:CLEAR 
TLP:CLEAR 
2. Protocol-Based Attacks: These attacks exploit vulnerabilities in network protocols or 
services to disrupt the target. By focusing on weak protocol implementations, the 
malicious actor can degrade the target’s performance or cause it to malfunction. 
Protocol-based DDoS attacks typically target Layers 3 (network layer) and 4 
(transport layer) of the Open Systems Interconnection (OSI) model. 

Figure 4: Protocol-Based Attacks 

Figure 3: Volumetric-Based Attack Example

        # Indicators

        _No specific information extracted._

        # Impact

        10 CISA | FBI | MS-ISAC 
TLP:CLEAR 
TLP:CLEAR 
10. Patch and Update Systems: Regularly update and patch all software, operating 
systems, and network devices to address known vulnerabilities. Vulnerable systems 
can be exploited to amplify the impact of a DDoS attack. 
11. Web Application Security: Implement secure coding practices and conduct regular 
security assessments of your web applications. Vulnerable applications can be 
targeted to exhaust server resources during an attack. 
12. Redundancy and Failover: Implement redundant network infrastructure and ensure 
failover mechanisms are in place. This will help maintain service availability during an 
attack by quickly redirecting traffic to alternative resources. 
13. Employee Awareness and Training: Educate employees about DDoS attacks, their 
impact, and how to recognize and report suspicious activities. This will help minimize 
the risk of falling victim to social engineering attacks that can aid in launching a 
DDoS attack. 
14. Communication Plan: Develop a communication plan to keep stakeholders informed 
during an attack. This includes internal teams, customers, and third-party service 
providers. Clear communication helps manage expectations and coordinates 
response efforts. 
15. Backup and Recovery: Regularly back up critical data and ensure you have a tested 
and updated disaster recovery plan. This will help you recover quickly after an attack 
and minimize potential data loss. 
Note: These steps can help mitigate the impact of a DDoS attack, it's crucial for organizations to 
remain vigilant to these types of attacks and remain in constant communication with their 
organization cybersecurity professionals and stay updated on the latest security practices to 
effectively defend against evolving threats.

        # Detection

        9 CISA | FBI | MS-ISAC 
TLP:CLEAR 
TLP:CLEAR 
What Steps Should Your Organization Take Before Experiencing a 
DDoS Attack? 
No organization can predict when a DDoS attack will occur. However, malicious actors often 
look for gaps in security systems to launch a DDoS attack; therefore, it is imperative that an 
organization’s network defenders implement best practices to minimize the potential 
damage of a DDoS attack. The following is a list of proactive DDoS steps to consider: 
1. Risk Assessment: Conduct a thorough and proactive risk assessment to determine 
your organizations vulnerability to DDoS attacks. Risk assessments can identify 
potential vulnerabilities in your network infrastructure, systems, and applications. 
Such an assessment will also help your organization understand the potential impact 
of a DDoS attack and aid in prioritizing and implementing appropriate security 
measures. 
2. Network Monitoring: Implement robust network monitoring tools and intrusion 
detection systems (IDS) to identify any unusual or suspicious traffic patterns. This 
can heighten your organization’s ability to detect and respond to DDoS attacks. 
3. Traffic Analysis: Regularly analyze your network traffic to establish a baseline of 
normal traffic patterns. This helps you identify any significant deviations during an 
attack. 
4. Implement Captcha: Integrating a Captcha challenge into a website or online service 
to help differentiate between human users and automated bots, which helps prevent 
DDoS attacks. By requiring human interaction to access or interact with websites, 
Captcha acts as preventive barrier against DDoS attacks. 
5. Incident Response Plan: Develop a comprehensive incident response plan that 
outlines the steps to be taken in the event of a DDoS attack. The plan should include 
roles and responsibilities, communication channels, and predefined mitigation 
strategies. 
6. DDoS Mitigation Service: Consider employing the services of a DDoS mitigation 
provider. They possess the expertise and specialized infrastructure to handle large-
scale attacks and can help filter out malicious traffic before it reaches your network. 
7. Bandwidth Capacity Planning: Evaluate your current bandwidth capacity and consider 
increasing it to handle sudden spikes in traffic during an attack. This can help 
minimize the impact on legitimate users. 
8. Load Balancing: Implement load balancing solutions to distribute traffic across 
multiple servers or data centers. This can help distribute the load and prevent a 
single point of failure during an attack. 
9. Firewall Configuration: Configure your firewalls to filter out suspicious traffic patterns 
and/or block traffic from known malicious IP addresses. Keep the firewall rules 
updated and consider implementing rate limitations to prevent overwhelming traffic.

11 CISA | FBI | MS-ISAC 
TLP:CLEAR 
TLP:CLEAR 
How Does Your Organization Know If It’s Experiencing a DDoS 
Attack? 
Identifying whether your organiza

*[Content truncated for brevity.]*

        # Mitigation

        12 CISA | FBI | MS-ISAC 
TLP:CLEAR 
TLP:CLEAR 
10. Communication Disruptions: DDoS attacks can target communication channels, such 
as Voice over Internet Protocol (VoIP) services or messaging platforms. If there are 
disruptions or quality degradation in network communication services, it may be an 
indication of an attack. 
How Organizations Can Respond to a DDoS Incident 
Organizations experiencing a DDoS attack, are encouraged to initiate incident response 
plans, contact DDoS protection service provider (if applicable), and engage with your 
network security team to mitigate the attack and restore normal operations. The following is 
a list of steps to consider: 
1. 
Identify the Attack: Recognize the signs of a DDoS attack, such as a sudden surge in 
traffic, increased network latency, or unavailability of services. Use network 
monitoring tools and traffic analysis to confirm the attack. 
2. Activate Incident Response Plan: Implement your organization’s documented and 
approved incident response plan immediately. This plan should outline the roles and 
responsibilities of key personnel, communication channels, and the steps to be taken 
during a DDoS attack. 
3. Notify Service Providers: Contact internet service providers (ISP) or hosting providers 
to inform them about the attack. They may have mitigation measures in place or be 
able to reroute traffic to help mitigate the impact. 
4. Gather Evidence: Document and collect as much information as possible about the 
attack, including timestamps, IP addresses, packet captures, and any logs or alerts 
generated by your network infrastructure. This evidence can be useful for reporting 
the incident to law enforcement agencies or for future analysis. 
5. Implement Traffic Filtering: Configure network infrastructure, firewalls, or intrusion 
prevention systems to filter out malicious traffic. Use rate-limitation or access control 
lists to block traffic from suspicious IP addresses or specific protocols commonly 
used in DDoS attacks. 
6. Enable DDoS Mitigation Services: If available, activate DDoS mitigation services 
provided by your ISP or third-party vendors specializing in DDoS protection. These 
services can help filter and divert malicious traffic, allowing legitimate traffic to reach 
your network. 
7. Scale Up Bandwidth and Resources: If your organization has the capacity, consider 
scaling up your network bandwidth and resources to absorb the attack traffic. This 
may involve adding additional servers or increasing your network capacity 
temporarily. 
8. Enable Content Delivery Network (CDN): Utilize a CDN service to distribute content 
across multiple servers and data centers geographically. CDNs can help mitigate 
DDoS attacks by absorbing and distributing traffic, minimizing the impact on your 
infrastructure.

13 CISA | FBI | MS-ISAC 
TLP:CLEAR 
TLP:CLEAR 
9. Communicate Internally and Externally: Maintain clear and regular communication 
with key stakeholders, including employees

*[Content truncated for brevity.]*

        # References

        - Source: [CISA](https://www.cisa.gov/sites/default/files/2024-03/understanding-and-responding-to-distributed-denial-of-service-attacks_508c.pdf)
        - Category: DDoS
        - Generated: 2026-06-26

        3 CISA | FBI | MS-ISAC 
TLP:CLEAR 
TLP:CLEAR 
Table of Contents 
Change Record ........................................................................................................................... 2 
Table of Contents ....................................................................................................................... 2 
Overview ..................................................................................................................................... 4 
DoS and DDoS ............................................................................................................................ 4 
DoS and DDoS Attacks Categorized Into Three Technique Types ......................................... 5 
What Steps Should Your Organization Take Before Experiencing a DDoS Attack? ............ 9 
How Does Your Organization Know If It’s Experiencing a DDoS Attack? ............................ 11 
How Organizations Can Respond to a DDoS Incident ...................

*[Content truncated for brevity.]*

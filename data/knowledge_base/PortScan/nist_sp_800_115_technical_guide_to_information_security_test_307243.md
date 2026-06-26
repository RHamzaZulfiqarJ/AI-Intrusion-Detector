        ---
        title: NIST SP 800-115 Technical Guide to Information Security Testing
        category: PortScan
        source: NIST
        url: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-115.pdf
        date: 2026-06-26
        ---

        # Overview

        Special Publication 800-115 
Technical Guide to 
Information Security Testing 
and Assessment 
Recommendations of the National Institute 
of Standards and Technology 
Karen Scarfone 
Murugiah Souppaya 
Amanda Cody 
Angela Orebaugh

Technical Guide to Information Security 
Testing and Assessment 
Recommendations of the National 
Institute of Standards and Technology 
Karen Scarfone 
Murugiah Souppaya 
Amanda Cody 
Angela Orebaugh 
NIST Special Publication 800-115 
C O M P U T E R S E C U R I T Y
Computer Security Division 
Information Technology Laboratory 
National Institute of Standa rds and Technology 
Gaithersburg, MD 20899-8930 
September 2008 
U.S. Department of Commerce 
Carlos M. Gutierrez, Secretary 
National Institute of Standards and Technology 
Dr. Patrick D. Gallagher, Deputy Director

[... content truncated ...]

        # Technical Details

        TECHNICAL GUIDE TO INFORMATION SECURITY TESTING AND ASSESSMENT 

Reports on Computer Systems Technology 

The Information Technology Laboratory (ITL) at the National Institute of Standards and Technology 
(NIST) promotes the U.S. economy and public welfare by providing technical leadership for the nation’s 
measurement and standards infrastructure. ITL develops tests, test methods, reference data, proof of 
concept implementations, and technical analysis to advance the development and productive use of 
information technology (IT). ITL’s responsibilities include the development of technical, physical, 
administrative, and management standards and guidelines for the cost-effective security and privacy of 
sensitive unclassified information in Federal computer systems. This Special Publication 800-series 
reports on ITL’s research, guidance, and outreach efforts in computer security and its collaborative 
activities with industry, government, and academic organizations. 













Certain commercial entities, equipment, or materials may be identified in this 
document in order to describe an experimental procedure or concept adequately. 
Such identification is not intended to imply recommendation or endorsement by the 
National Institute of Standards and Technology, nor is it intended to imply that the 
entities, materials, or equipment are necessarily the best available for the purpose. 
National Institute of Standards and Technology Special Publication 800-115 
Natl. Inst. Stand. Technol. Spec. Publ. 800-115, 80 pages (Sep. 2008) 


















 ii

TECHNICAL GUIDE TO INFORMATION SECURITY TESTING AND ASSESSMENT 
Table of Contents 
Executive Summary..............................................................................................................ES-1 
1. Introduction ......................................................................................................................1-1 
1.1 Authority...................................................................................................................1-1 
1.2 Purpose and Scope .................................................................................................1-1 
1.3 Audience ..................................................................................................................1-1 
1.4 Document Structure .................................................................................................1-2 
2. Security Testing and Examination Overview ................................................................2-1 
2.1 Information Security Assessment Methodology.......................................................2-1 
2.2 Technical Assessment Techniques .........................................................................2-2 
2.3 Comparing Tests and Examinations ........................................................................2-3 
2.4 Testing Viewpoints............................................

*[Content truncated for brevity.]*

        # Indicators

        _No specific information extracted._

        # Impact

        TECHNICAL GUIDE TO INFORMATION SECURITY TESTING AND ASSESSMENT 
individuals to ensure assessments are conducted in accordance with these requirements. Topics 
that an assessment policy should address include the organizational requirements with which 
assessments must comply, roles and responsibilities, adherence to an established assessment 
methodology, assessment frequency, and documentation requirements. 
 Implement a repeatable and documented assessment methodology. This provides 
consistency and structure to assessments, expedites the transition of new assessment staff, and 
addresses resource constraints associated with assessments. Using such a methodology enables 
organizations to maximize the value of assessments while minimizing possible risks introduced 
by certain technical assessment techniques. These risks can range from not gathering sufficient 
information on the organization’s security posture for fear of impacting system functionality to 
affecting the system or network availability by executing techniques without the proper 
safeguards in place. Processes that minimize risk caused by certain assessment techniques 
include using skilled assessors, developing comprehensive assessment plans, logging assessor 
activities, performing testing off-hours, and conducting tests on duplicates of production systems 
(e.g., development systems). Organizations need to determine the level of risk they are willing to 
accept for each assessment, and tailor their approaches accordingly. 
 Determine the objectives of each security assessment, and tailor the approach accordingly. 
Security assessments have specific objectives, acceptable levels of risk, and available resources. 
Because no individual technique provides a comprehensive picture of an organization’s security 
when executed alone, organizations should use a combination of techniques. This also helps 
organizations to limit risk and resource usage. 
 Analyze findings, and develop risk mitigation techniques to address weaknesses. To ensure 
that security assessments provide their ultimate value, organizations should conduct root cause 
analysis upon completion of an assessment to enable the translation of findings into actionable 
mitigation techniques. These results may indicate that organizations should address not only 
technical weaknesses, but weaknesses in organizational processes and procedures as well. 


ES-2

TECHNICAL GUIDE TO INFORMATION SECURITY TESTING AND ASSESSMENT 
(POP). Servers that are externally accessible are tested for vulnerabilities that might allow access to 
internal servers and private information. External security testing also concentrates on discovering access 
method vulnerabilities, such as wireless access points, modems, and portals to internal servers. 
For internal security testing, assessors work from the internal network and assume the identity of a trusted 
insider or an attacker who has penetrated the perimeter defenses. This kind of testing c

*[Content truncated for brevity.]*

        # Detection

        TECHNICAL GUIDE TO INFORMATION SECURITY TESTING AND ASSESSMENT 
Examples of log information that may be useful when conducting technical security assessments include: 
 Authentication server or system logs may include successful and failed authentication attempts. 
 System logs may include system and service startup and shutdown information, installation of 
unauthorized software, file accesses, security policy changes, account changes (e.g., account 
creation and deletion, account privilege assignment), and privilege use. 
 Intrusion detection and prevention system logs may include malicious activity and inappropriate 
use. 
 Firewall and router logs may include outbound connections that indicate compromised internal 
devices (e.g., rootkits, bots, Trojan horses, spyware). 
 Firewall logs may include unauthorized connection attempts and inappropriate use. 
 Application logs may include unauthorized connection attempts, account changes, use of 
privileges, and application or database usage information. 
 Antivirus logs may include update failures and other indications of outdated signatures and 
software. 
 Security logs, in particular patch management and some IDS and intrusion prevention system 
(IPS) products, may record information on known vulnerable services and applications. 
Manually reviewing logs can be extremely time-consuming and cumbersome. Automated audit tools are 
available that can significantly reduce review time and generate predefined and customized reports that 
summarize log contents and track them to a set of specific activities. Assessors can also use these 
automated tools to facilitate log analysis by converting logs in different formats to a single, standard 
format for analysis. In addition, if assessors are reviewing a specific action—such as the number of failed 
logon attempts in an organization—they can use th ese tools to filter logs based on the activity being 
checked. 
3.3 Ruleset Review 
A ruleset is a collection of rules or signatures that network traffic or system activity is compared against 
to determine what action to take—for example, forw arding or rejecting a packet, creating an alert, or 
allowing a system event. Review of these rulesets is done to ensure comprehensiveness and identify gaps 
and weaknesses on security devices and throughout layered defenses such as network vulnerabilities, 
policy violations, and unintended or vulnerable communication paths. A review can also uncover 
inefficiencies that negatively impact a ruleset’s performance. 
Rulesets to review include network- and host-based firewall and IDS/IPS rulesets, and router access 
control lists. The following list provides examples of the types of checks most commonly performed in 
ruleset reviews: 
 For router access control lists 
– Each rule is still required (for example, rules that were added for temporary purposes are 
removed as soon as they are no longer needed) 
– Only traffic that is authorized per policy is permitted, and al

*[Content truncated for brevity.]*

        # Mitigation

        TECHNICAL GUIDE TO INFORMATION SECURITY TESTING AND ASSESSMENT 
6.4 Assessment Logistics ..............................................................................................6-4 
6.4.1 Assessor Selection and Skills.......................................................................6-5 
6.4.2 Location Selection ........................................................................................6-6 
6.4.3 Technical Tools and Resources Selection ...................................................6-8 
6.5 Assessment Plan Development .............................................................................6-10 
6.6 Legal Considerations .............................................................................................6-12 
6.7 Summary................................................................................................................6-12 
7. Security Assessment Execution.....................................................................................7-1 
7.1 Coordination.............................................................................................................7-1 
7.2 Assessing.................................................................................................................7-2 
7.3 Analysis....................................................................................................................7-3 
7.4 Data Handling ..........................................................................................................7-4 
7.4.1 Data Collection .............................................................................................7-5 
7.4.2 Data Storage ................................................................................................7-5 
7.4.3 Data Transmission........................................................................................7-6 
7.4.4 Data Destruction...........................................................................................7-7 
8. Post-Testing Activities ....................................................................................................8-1 
8.1 Mitigation Recommendations...................................................................................8-1 
8.2 Reporting .................................................................................................................8-1 
8.3 Remediation/Mitigation ............................................................................................8-2 

List of Appendices 
Appendix A— Live CD Distributions for Security Testing .................................................. A-1 
Appendix B— Rules of Engagement Template.................................................................... B-1 
Appendix C— Application Security Testing and Examination ........................................... C-1 
Appendix D— Remote Access Testing ................................................................................. D-1 
Appendix E— Re

*[Content truncated for brevity.]*

        # References

        - Source: [NIST](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-115.pdf)
        - Category: PortScan
        - Generated: 2026-06-26

        TECHNICAL GUIDE TO INFORMATION SECURITY TESTING AND ASSESSMENT 
Acknowledgements 

The authors, Karen Scarfone and Murugiah Souppaya of the National Institute of Standards and 
Technology (NIST) and Amanda Cody and Angela Orebaugh of Booz Allen Hamilton, wish to thank 
their colleagues who reviewed drafts of this document and contributed to its technical content. The 
authors would like to acknowledge John Connor, Tim Grance, Blair Heiserman, Arnold Johnson, Richard 
Kissel, Ron Ross, Matt Scholl, and Pat Toth of NIST and Steve Allison, Derrick Dicoi, Daniel Owens, 
Victoria Thompson, Selena Tonti, Theodore Winograd, and Gregg Zepp of Booz Allen Hamilton for their 
keen and insightful assistance throughout the development of the document. The authors appreciate all 
the feedback provided during the public comment period, especially by Marshall Abrams, Karen Quigg, 
and others from MITRE Corporation; William Mills of SphereCom Enterprises; and representatives from 
the Financial Manage

*[Content truncated for brevity.]*

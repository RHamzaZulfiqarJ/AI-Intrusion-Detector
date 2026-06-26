        ---
        title: NIST Intrusion Detection Systems Guide
        category: BENIGN
        source: NIST
        url: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-94.pdf
        date: 2026-06-26
        ---

        # Overview

        Special Publication 800-94 
Guide to Intrusion Detection 
and Prevention Systems 
(IDPS) 
Recommendations of the National Institute 
of Standards and Technology 

Karen Scarfone 
Peter Mell

Guide to Intrusion Detection and 
Prevention Systems (IDPS) 

Recommendations of the National 
Institute of Standards and Technology 

Karen Scarfone 
Peter Mell 


NIST Special Publication 800-94 
C O M P U T E R S E C U R I T Y
Computer Security Division 
Information Technology Laboratory 
National Institute of Standards and Technology 
Gaithersburg, MD 20899-8930 

February 2007 





U.S. Department of Commerce 
Carlos M. Gutierrez, Secretary 
Technology Administration 
Robert C. Cresanti, Under Secretary of Commerce for 
Technology 
National Institute of Standards and Technology 
William Jeffrey, Director

[... content truncated ...]

        # Technical Details

        GUIDE TO INTRUSION DETECTION AND PREVENTION SYSTEMS (IDPS) 
Reports on Computer Systems Technology 

The Information Technology Laboratory (ITL) at the National Institute of Standards and Technology 
(NIST) promotes the U.S. economy and public welfare by providing technical leadership for the nation’s 
measurement and standards infrastructure. ITL develops tests, test methods, reference data, proof of 
concept implementations, and technical analysis to advance the development and productive use of 
information technology. ITL’s responsibilities include the development of technical, physical, 
administrative, and management standards and guidelines for the cost-effective security and privacy of 
sensitive unclassified information in Federal computer systems. This Special Publication 800-series 
reports on ITL’s research, guidance, and outreach efforts in computer security and its collaborative 
activities with industry, government, and academic organizations. 













Certain commercial entities, equipment, or materials may be identified in this 
document in order to describe an experimental procedure or concept adequately. 
Such identification is not intended to imply recommendation or endorsement by the 
National Institute of Standards and Technology, nor is it intended to imply that the 
entities, materials, or equipment are necessarily the best available for the purpose. 
National Institute of Standards and Technology Special Publication 800-94 
Natl. Inst. Stand. Technol. Spec. Publ. 800-94, 127 pages (February 2007) 


















 iii

GUIDE TO INTRUSION DETECTION AND PREVENTION SYSTEMS (IDPS) 
Stateful protocol analysis can identify unexpected sequences of commands, such as issuing the same 
command repeatedly or issuing a command without first issuing a command upon which it is dependent. 
Another state tracking feature of stateful protocol analysis is that for protocols that perform 
authentication, the IDPS can keep track of the authenticator used for each session, and record the 
authenticator used for suspicious activity. This is helpful when investigating an incident. Some IDPSs 
can also use the authenticator information to define acceptable activity differently for multiple classes of 
users or specific users. 
The “protocol analysis” performed by stateful protocol analysis methods usually includes reasonableness 
checks for individual commands, such as minimum and maximum lengths for arguments. If a command 
typically has a username argument, and usernames have a maximum length of 20 characters, then an 
argument with a length of 1000 characters is suspicious. If the large argument contains binary data, then 
it is even more suspicious. 
Stateful protocol analysis methods use protocol models, which are typically based primarily on protocol 
standards from software vendors and standards bodies (e.g., Internet Engineering Task Force [IETF] 
Request for Comments [RFC]). The protocol models als

*[Content truncated for brevity.]*

        # Indicators

        _No specific information extracted._

        # Impact

        _No specific information extracted._

        # Detection

        GUIDE TO INTRUSION DETECTION AND PREVENTION SYSTEMS (IDPS) 
Acknowledgements 

The authors, Karen Scarfone and Peter Mell of the National Institute of Standards and Technology 
(NIST), wish to thank their colleagues who reviewed drafts of this document and contributed to its 
technical content. The authors would like to acknowledge John Connor, Tim Grance, Anoop Singhal, and 
Murugiah Souppaya of NIST; Michael Gerdes, Ralph Martins, Angela Orebaugh, and Mike Zeberlein of 
Booz Allen Hamilton; and Steve Sharma of Project Performance Corporation for their keen and insightful 
assistance throughout the development of the document. The authors particularly want to thank Rebecca 
Bace of KSR for her careful review of the publication and for her work on the predecessor publication, 
NIST Special Publication 800-31, Intrusion Detection Systems. The authors would also like to express 
their thanks to security experts Andrew Balinsky (Cisco Systems), Anton Chuvakin (LogLogic), Jay 
Ennis (Network Chemistry), John Jerrim (Lancope), and Kerry Long (Center for Intrusion Monitoring 
and Protection, Army Research Laboratory), as well as representatives from the Department of State and 
Gartner, for their particularly valuable comments and suggestions. Additional acknowledgements will be 
added to the final version of the publication. 


Trademarks 
All product names are registered trademarks or trademarks of their respective companies. 

 iv

GUIDE TO INTRUSION DETECTION AND PREVENTION SYSTEMS (IDPS) 
Table of Contents 
Executive Summary..............................................................................................................ES-1 
1. Introduction ......................................................................................................................1-1 
1.1 Authority...................................................................................................................1-1 
1.2 Purpose and Scope .................................................................................................1-1 
1.3 Audience ..................................................................................................................1-1 
1.4 Document Structure .................................................................................................1-1 
2. Intrusion Detection and Prevention Principles .............................................................2-1 
2.1 Uses of IDPS Technologies .....................................................................................2-1 
2.2 Key Functions of IDPS Technologies ......................................................................2-2 
2.3 Common Detection Methodologies..........................................................................2-3 
2.3.1 Signature-Based Detection...........................................................................2-4 
2.3.2 Anomaly-Based Detection ...........................................................................

*[Content truncated for brevity.]*

        # Mitigation

        _No specific information extracted._

        # References

        - Source: [NIST](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-94.pdf)
        - Category: BENIGN
        - Generated: 2026-06-26

        GUIDE TO INTRUSION DETECTION AND PREVENTION SYSTEMS (IDPS) 
or review by another organization. If so, they should determine if that oversight authority requires IDPSs 
or other specific system security resources. Resource constraints should also be taken into consideration 
by evaluators. Evaluators also need to define specialized sets of requirements for the following: 
 Security capabilities, including information gathering, logging, detection, and prevention 
 Performance, including maximum capacity and performance features 
 Management, including design and implementation (e.g., reliability, interoperability, scalability, 
product security), operation and maintenance (including software updates), and training, 
documentation, and technical support 
 Life cycle costs, both initial and maintenance costs. 
When evaluating IDPS products, organizations should consider using a combination of several 
sources of data on the products’ characteristics and capabilities. 
Common product data 

*[Content truncated for brevity.]*

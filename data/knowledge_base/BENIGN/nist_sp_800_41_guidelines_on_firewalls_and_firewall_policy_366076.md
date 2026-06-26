        ---
        title: NIST SP 800-41 Guidelines on Firewalls and Firewall Policy
        category: BENIGN
        source: NIST
        url: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-41r1.pdf
        date: 2026-06-26
        ---

        # Overview

        Special Publication 800-41 
Revision 1 
Guidelines on Firewalls and 
Firewall Policy 
Recommendations of the National Institute 
of Standards and Technology 

Karen Scarfone 
Paul Hoffman

Guidelines on Firewalls and Firewall 
Policy 

Recommendations of the National 
Institute of Standards and Technology 

Karen Scarfone 
Paul Hoffman 
NIST Special Publication 800-41 
Revision 1 
C O M P U T E R S E C U R I T Y
Computer Security Division 
Information Technology Laboratory 
National Institute of Standards and Technology 
Gaithersburg, MD 20899-8930 

September 2009 





U.S. Department of Commerce 
Gary Locke, Secretary 
National Institute of Standards and Technology 
Patrick D. Gallagher, Deputy Director

GUIDELINES ON FIREWALLS AND FIREWALL POLICY 
 If an edge firewall has a DMZ, consider which outward-facing services should be run from the DMZ 
and which should remain on the inside network. 
 Do not rely on NATs to provide the benefits of firewalls. 
 In some environments, putting one firewall behind another may lead to a desired security goal, but in 
general such multiple layers of firewalls can be troublesome. 
 3-5

[... content truncated ...]

        # Technical Details

        GUIDELINES ON FIREWALLS AND FIREWALL POLICY 

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
National Institute of Standards and Technology Special Publication 800-41 Revision 1 
Natl. Inst. Stand. Technol. Spec. Publ. 800-41 rev1, 48 pages (Sep. 2009) 


 iii

GUIDELINES ON FIREWALLS AND FIREWALL POLICY 
Table of Contents 
Executive Summary..............................................................................................................ES-1 
1. Introduction ......................................................................................................................1-1 
1.1 Authority...................................................................................................................1-1 
1.2 Purpose and Scope .................................................................................................1-1 
1.3 Audience ..................................................................................................................1-1 
1.4 Document Structure .................................................................................................1-1 
2. Overview of Firewall Technologies ................................................................................2-1 
2.1 Firewall Technologies ..............................................................................................2-2 
2.1.1 Packet Filtering.............................................................................................2-2 
2.1.2 Stateful Inspection ........................................................................................2-4 
2.1.3 Application Firewalls..................................................................

*[Content truncated for brevity.]*

        # Indicators

        _No specific information extracted._

        # Impact

        GUIDELINES ON FIREWALLS AND FIREWALL POLICY 
3. Firewalls and Network Architectures 
Firewalls are used to separate networks with differing security requirements, such as the Internet and an 
internal network that houses servers with sensitive data. Organizations should use firewalls wherever their 
internal networks and systems interface with external networks and systems, and where security 
requirements vary among their internal networks. This section is intended to help organizations determine 
where firewalls should be placed, and where other networks and systems should be located in relation to 
the firewalls. 
Since one of the primary functions of a firewall is to prevent unwanted traffic from entering a network 
(and, in some cases, from exiting it), firewalls should be placed at the edge of logical network 
boundaries.14 This normally means that firewalls are positioned either as a node where the network splits 
into multiple paths, or inline along a single path. In routed networks, the firewall usually resides just on 
the network at the location immediately before traffic enters the router (the ingress point), and is 
sometimes co-resident with the router. It is rare to place the firewall for a multi-path node after the router 
because the firewall device would need to watch each of the multiple exit paths that typically exist in such 
situations. The vast majority of hardware firewall devices contain router capabilities, and in switched 
networks, a firewall is often part of the switch itself to enable it to protect as many of the switched 
segments as possible. 
Firewall vendors often vary in their terminology for the logical flow of firewall traffic. A firewall takes 
traffic that has not been checked, checks it against the firewall's policy, and then acts accordingly (e.g., 
passes the traffic, blocks it, passes it with some modification). Because all traffic on a network has a 
direction, policies are based on the direction that the traffic is moving. For the purposes of this document, 
traffic that has not yet been checked is coming from the “unprotected side” of the firewall and is moving 
towards the “protected side.” Some firewalls check traffic in both directions—for example, if they are set 
up to prevent specific traffic from an organization's local area network (LAN) from escaping to the 
Internet.
15 In these cases, the protected side of the firewall is the one facing the outside network. 
Section 2 lists many different types of firewall technologies. Network firewalls are almost always 
hardware devices with multiple network interfaces; host-based and personal firewalls involve software 
that resides on a single computer and protects only that computer; and personal firewall appliances are 
designed to protect a single PC or a small office/home office network. This section focuses on network 
firewalls because the other types are usually unrelated to network topology issues. 
3.1 Network Layouts with Firewalls 
Figure 3-

*[Content truncated for brevity.]*

        # Detection

        GUIDELINES ON FIREWALLS AND FIREWALL POLICY 
5.2.2 Policy Configuration......................................................................................5-4 
5.2.3 Logging and Alerts Configuration .................................................................5-5 
5.3 Test ..........................................................................................................................5-6 
5.4 Deploy......................................................................................................................5-6 
5.5 Manage ....................................................................................................................5-7 

List of Appendices 
Appendix A— Glossary .......................................................................................................... A-1 
Appendix B— Acronyms and Abbreviations ....................................................................... B-1 
Appendix C— Resources ....................................................................................................... C-1 

List of Figures 
Figure 2-1. TCP/IP Layers .........................................................................................................2-1 
Figure 2-2. Application Proxy Configuration ..............................................................................2-7 
Figure 3-1. Simple Routed Network with Firewall Device ..........................................................3-2 
Figure 3-2. Firewall with a DMZ .................................................................................................3-2 

List of Tables 
Table 2-1. State Table Example ................................................................................................2-4 


 vi

GUIDELINES ON FIREWALLS AND FIREWALL POLICY 
Identify all requirements that should be considered when determining which firewall to implement. 
There are many considerations that organizations should include in their firewall selection and planning 
processes. Organizations need to determine which network areas need to be protected, and which types of 
firewall technologies will be most effective for the types of traffic that require protection. Several 
important performance considerations also exist, as well as concerns regarding the integration of the 
firewall into existing network and security infrastructures. Additionally, firewall solution design involves 
requirements relating to physical environment and personnel as well as consideration of possible future 
needs, such as plans to adopt new IPv6 technologies or virtual private networks (VPN). 
Create rulesets that implement the organization’s firewall policy while supporting firewall 
performance. 
Firewall rulesets should be as specific as possible with regards to the network traffic they control. To 
create a ruleset involves determining what types of traffic are required, including protocols the firewall 
may need to use for management purposes. The de

*[Content truncated for brevity.]*

        # Mitigation

        _No specific information extracted._

        # References

        - Source: [NIST](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-41r1.pdf)
        - Category: BENIGN
        - Generated: 2026-06-26

        GUIDELINES ON FIREWALLS AND FIREWALL POLICY 
Acknowledgments 

The authors, Karen Scarfone of the National Institute of Standards and Technology (NIST) and Paul 
Hoffman of the Virtual Private Network Consortium, wish to thank their colleagues who reviewed drafts 
of this document and contributed to its technical content. The authors would like to acknowledge Tim 
Grance, Murugiah Souppaya, Sheila Frankel, and Gale Richter of NIST, and Matthew Goche, David 
Klug, Logan Lodge, John Pearce, Noel Richards, Anne Roudabush, and Steven Sharma of Booz Allen 
Hamilton, for their keen and insightful assistance throughout the development of the document. Special 
thanks go to Brahim Asfahani of Booz Allen Hamilton for his contributions to early drafts of the 
document. The authors also thank all the reviewers who provided feedback during the public comment 
period, particularly Joel Snyder (Opus One), Ron Colvin (National Aeronautics and Space Administration 
[NASA]), Dean Farrington (Wells Far

*[Content truncated for brevity.]*

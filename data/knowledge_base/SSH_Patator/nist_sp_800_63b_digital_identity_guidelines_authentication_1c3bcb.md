        ---
        title: NIST SP 800-63B Digital Identity Guidelines (Authentication)
        category: SSH_Patator
        source: NIST
        url: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63b.pdf
        date: 2026-06-26
        ---

        # Overview

        Date updated: July 24, 2025 
Withdrawn NIST Technical Series Publication 
Warning Notice 
The attached publication has been withdrawn (archived), and is provided solely for historical purposes. 
It may have been superseded by another publication (indicated below). 
Withdrawn Publication 
Series/Number NIST Special Publication 800-63B 
Title Digital Identity Guidelines: Authentication and Lifecycle Management 
Publication Date(s) June 2017 (includes updates as of 03-02-2020) 
Withdrawal Date August 1, 2025 
Withdrawal Note NIST SP 800-63B is withdrawn and superseded in its entirety by NIST SP 800-
63B-4. 
Superseding Publication(s) (if applicable) 
The attached publication has been superseded by the following publication(s): 
Series/Number NIST SP 800-63B-4 
Title Digital Identity Guidelines: Authentication and Authenticator Management 
Author(s) David Temoshok, et al. 
Publication Date(s) July 2025 
URL/DOI https://doi.org/10.6028/NIST.SP.800-63B-4 
Additional Information (if applicable) 
Contact Applied Cybersecurity Division (Information Technology Laboratory) 
Latest revision of the 
attached publication 
Related Information https://csrc.nist.gov/pubs/sp/800/63/b/4/final 
https://www.nist.gov/identity-access-management/nist-special-publication-
800-63-digital-identity-guidelines
Withdrawal 
Announcement Link

NIST Special Publication 800-63B 
Digital Identity Guidelines 
Authentication and Lifecycle Management 

Paul A. Grassi 
James L. Fenton 
Elaine M. Newton 
Ray A. Perlner 
Andrew R. Regenscheid 
William E. Burr 
Justin P. Richer 
Privacy Authors: 
Naomi B. Lefkovitz 
Jamie M. Danker 
Usability Authors: 
Yee-Yin Choong 
Kristen K. Greene 
Mary F. Theofanos 

This publication is available free of charge from: 
https://doi.org/10.6028/NIST.SP.800-63b

[... content truncated ...]

        # Technical Details

        NIST SP 800-63B DIGITAL IDENTITY GUIDELINES: 
 AUTHENTICATION & LIFECYCLE MANAGEMENT 
ii 
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-63b 

Reports on Computer Systems Technology 
The Information Technology Laboratory (ITL) at the National Institute of Standards and 
Technology (NIST) promotes the U.S. economy and public welfare by providing technical 
leadership for the Nation’s measurement and standards infrastructure. ITL develops tests, test 
methods, reference data, proof of concept implementations, and technical analyses to advance the 
development and productive use of information technology. ITL’s responsibilities include the 
development of management, administrative, technical, and physical standards and guidelines for 
the cost-effective security and privacy of other than national security-related information in federal 
information systems. The Special Publication 800-series reports on ITL’s research, guidelines, and 
outreach efforts in information system security, and its collaborative activities with industry, 
government, and academic organizations. 
Abstract 
These guidelines provide technical requirements for federal agencies implementing digital identity 
services and are not intended to constrain the development or use of standards outside of this 
purpose. These guidelines focus on the authentication of subjects interacting with government 
systems over open networks, establishing that a given claimant is a subscriber who has been 
previously authenticated. The result of the authentication process may be used locally by the 
system performing the authentication or may be asserted elsewhere in a federated identity system. 
This document defines technical requirements for each of the three authenticator assurance levels. 
This publication supersedes corresponding sections of NIST Special Publication (SP) 800-63-2. 
Keywords 
authentication; credential service provider; digital authentication; digital credentials; electr onic 
authentication; electronic credentials, federation.

NIST SP 800-63B DIGITAL IDENTITY GUIDELINES: 
 AUTHENTICATION & LIFECYCLE MANAGEMENT 
1 
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-63b 

1 Purpose 
This section is informative. 
This document and its companion documents, Special Publication (SP) 800-63, SP 800-63A, 
and SP 800-63C, provide technical guidelines to agencies for the implementation of digital 
authentication.

NIST SP 800-63B DIGITAL IDENTITY GUIDELINES: 
 AUTHENTICATION & LIFECYCLE MANAGEMENT 
2 
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-63b 

2 Introduction 
This section is informative. 
Digital identity is the unique representation of a subject engaged in an online transaction. A 
digital identity is always unique in the context of a digital service, but does not necessarily need 
to be traceable back to a specific real-life subject. In other words, acces

*[Content truncated for brevity.]*

        # Indicators

        _No specific information extracted._

        # Impact

        NIST SP 800-63B DIGITAL IDENTITY GUIDELINES: 
 AUTHENTICATION & LIFECYCLE MANAGEMENT 
6 
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-63b 

4.1.2 Authenticator and Verifier Requirements 
Cryptographic authenticators used at AAL1 SHALL use approved cryptography. Software-based 
authenticators that operate within the context of an operating system MAY, where applicable, 
attempt to detect compromise (e.g., by malware) of the user endpoint in which they are running 
and SHOULD NOT complete the operation when such a compromise is detected. 
Communication between the claimant and verifier (using the primary channel in the case of an 
out-of-band authenticator) SHALL be via an authenticated protected channel to provide 
confidentiality of the authenticator output and resistance to man-in-the-middle (MitM) attacks. 
Verifiers operated by government agencies at AAL1 SHALL be validated to meet the 
requirements of FIPS 140 Level 1. 
4.1.3 Reauthentication 
Periodic reauthentication of subscriber sessions SHALL be performed as described in Section 
7.2. At AAL1, reauthentication of the subscriber SHOULD be repeated at least once per 30 days 
during an extended usage session, regardless of user activity. The session SHOULD be 
terminated (i.e., logged out) when this time limit is reached. 
4.1.4 Security Controls 
The CSP SHALL employ appropriately-tailored security controls from the low baseline of 
security controls defined in SP 800-53 or equivalent federal (e.g., FEDRAMP) or industry 
standard. The CSP SHALL ensure that the minimum assurance-related controls for low-
impact systems, or equivalent, are satisfied. 
4.1.5 Records Retention Policy 
The CSP shall comply with its respective records retention policies in accordance with 
applicable laws, regulations, and policies, including any National Archives and Records 
Administration (NARA) records retention schedules that may apply. If the CSP opts to retain 
records in the absence of any mandatory requirements, the CSP SHALL conduct a risk 
management process, including assessments of privacy and security risks, to determine how long 
records should be retained and SHALL inform the subscriber of that retention policy. 
 Authenticator Assurance Level 2 
This section is normative. 
AAL2 provides high confidence that the claimant controls authenticator(s) bound to the 
subscriber’s account. Proof of possession and control of two distinct authentication factors is 
required through secure authentication protocol(s). Approved cryptographic techniques are 
required at AAL2 and above.

NIST SP 800-63B DIGITAL IDENTITY GUIDELINES: 
 AUTHENTICATION & LIFECYCLE MANAGEMENT 
8 
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-63b 

When a device such as a smartphone is used in the authentication process, the unlocking of that 
device (typically done using a PIN or biometric) SHALL NOT be considered one of the 
authentication factors.

*[Content truncated for brevity.]*

        # Detection

        NIST SP 800-63B DIGITAL IDENTITY GUIDELINES: 
 AUTHENTICATION & LIFECYCLE MANAGEMENT 
7 
This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-63b 

4.2.1 Permitted Authenticator Types 
At AAL2, authentication SHALL occur by the use of either a multi-factor authenticator or a 
combination of two single-factor authenticators. A multi-factor authenticator requires two factors 
to execute a single authentication event, such as a cryptographically-secure device with an 
integrated biometric sensor that is required to activate the device. Authenticator requirements are 
specified in Section 5. 
When a multi-factor authenticator is used, any of the following MAY be used: 
• Multi-Factor OTP Device (Section 5.1.5) 
• Multi-Factor Cryptographic Software (Section 5.1.8) 
• Multi-Factor Cryptographic Device (Section 5.1.9) 
When a combination of two single-factor authenticators is used, it SHALL include a Memorized 
Secret authenticator (Section 5.1.1) and one possession-based (i.e., “something you have”) 
authenticator from the following list: 
• Look-Up Secret (Section 5.1.2) 
• Out-of-Band Device (Section 5.1.3) 
• Single-Factor OTP Device (Section 5.1.4) 
• Single-Factor Cryptographic Software (Section 5.1.6) 
• Single-Factor Cryptographic Device (Section 5.1.7) 
Note: When biometric authentication meets the requirements in Section 5.2.3, the device 
has to be authenticated in addition to the biometric — a biometric is recognized as a factor, 
but not recognized as an authenticator by itself. Therefore, when conducting authentication 
with a biometric, it is unnecessary to use two authenticators because the associated device 
serves as “something you have,” while the biometric serves as “something you are.” 
4.2.2 Authenticator and Verifier Requirements 
Cryptographic authenticators used at AAL2 SHALL use approved cryptography. Authenticators 
procured by government agencies SHALL be validated to meet the requirements of FIPS 
140 Level 1. Software-based authenticators that operate within the context of an operating 
system MAY, where applicable, attempt to detect compromise of the platform in which they are 
running (e.g., by malware) and SHOULD NOT complete the operation when such a compromise 
is detected. At least one authenticator used at AAL2 SHALL be replay resistant as described 
in Section 5.2.8. Authentication at AAL2 SHOULD demonstrate authentication intent from at 
least one authenticator as discussed in Section 5.2.9. 
Communication between the claimant and verifier (the primary channel in the case of an out-of-
band authenticator) SHALL be via an authenticated protected channel to provide confidentiality 
of the authenticator output and resistance to MitM attacks. 
Verifiers operated by government agencies at AAL2 SHALL be validated to meet the 
requirements of FIPS 140 Level 1.

NIST SP 800-63B DIGITAL IDENTITY GUIDELINES: 
 AUTHENTICATION & LIFECYCLE MANAGEMENT 
12 
This publication is available free of

*[Content truncated for brevity.]*

        # Mitigation

        _No specific information extracted._

        # References

        - Source: [NIST](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63b.pdf)
        - Category: SSH_Patator
        - Generated: 2026-06-26

        NIST Special Publication 800-63B 
Digital Identity Guidelines 
Authentication and Lifecycle Management 
Paul A. Grassi 
Elaine M. Newton 
Applied Cybersecurity Division 
Information Technology Laboratory 

Ray A. Perlner 
Andrew R. Regenscheid 
Computer Security Division 
Information Technology Laboratory 

James L. Fenton 
Altmode Networks 
Los Altos, Calif. 

William E. Burr 
Dakota Consulting, Inc. 
Silver Spring, Md. 
 Justin P. Richer 
Bespoke Engineering 
Billerica, Mass. 

Privacy Authors: 
Naomi B. Lefkovitz 
Applied Cybersecurity Division 
Information Technology Laboratory 

Usability Authors: 
Yee-Yin Choong 
Kristen K. Greene 
Information Access Division 
Information Technology Laboratory 

Jamie M. Danker 
National Protection and Programs Directorate 
Department of Homeland Security 
Mary F. Theofanos 
Office of Data and Informatics 
Material Measurement Laboratory 

This publication is available free of charge from: 
https://doi.org/10.6028/NIST.SP.800-63b 
June 201

*[Content truncated for brevity.]*

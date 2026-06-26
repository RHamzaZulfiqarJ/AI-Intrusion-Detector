        ---
        title: CISA Brute Force Attack Techniques
        category: SSH_Patator
        source: CISA
        url: https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-008a
        date: 2026-06-26
        ---

        # Overview

        Archived Content
In an effort to keep CISA.gov current, the archive contains outdated information that may not reflect current policy or programs.Detecting Post-Compromise Threat Activity in Microsoft Cloud Environments
Summary
This Advisory uses the MITRE Adversarial Tactics, Techniques, and Common Knowledge (ATT&CK®) framework. See the ATT&CK for Enterprise for all referenced threat actor tactics and techniques.
Updated April 15, 2021: The U.S. Government attributes this activity to the Russian Foreign Intelligence Service (SVR). Additional information may be found in a statement from the White House. For more information on SolarWinds-related activity, go to https://us-cert.cisa.gov/remediating-apt-compromised-networks and https://www.cisa.gov/supply-chain-compromise.
This Alert is a companion alert to AA20-352A: Advanced Persistent Threat Compromise of Government Agencies, Critical Infrastructure, and Private Sector Organizations. AA20-352A primarily focuses on an advanced persistent threat (APT) actor’s compromise of SolarWinds Orion products as an initial access vector into networks of U.S. Government agencies, critical infrastructure entities, and private network organizations. As noted in AA20-352A, the Cybersecurity and Infrastructure Security Agency (CISA) has evidence of initial access vectors in addition to the compromised SolarWinds Orion products.
This Alert also addresses activity—irrespective of the initial access vector leveraged—that CISA attributes to an APT actor. Specifically, CISA has seen an APT actor using compromised applications in a victim’s Microsoft 365 (M365)/Azure environment. CISA has also seen this APT actor utilizing additional credentials and Application Programming Interface (API) access to cloud resources of private and public sector organizations. These tactics, techniques, and procedures (TTPs) feature three key components:
- Compromising or bypassing federated identity solutions;
- Using forged authentication tokens to move laterally to Microsoft cloud environments; and
- Using privileged access to a victim’s cloud environment to establish difficult-to-detect persistence mechanisms for Application Programming Interface (API)-based access.
This Alert describes these TTPs and offers an overview of, and guidance on, available open-source tools—including a CISA-developed tool, Sparrow—for network defenders to analyze their Microsoft Azure Active Directory (AD), Office 365 (O365), and M365 environments to detect potentially malicious activity.
Note: this Alert describes artifacts—presented by these attacks—from which CISA has identified detectable evidence of the threat actor’s initial objectives. CISA continues to analyze the threat actor’s follow-on objectives.
Technical Details
Frequently, CISA has observed the APT actor gaining Initial Access [TA0001] to victims’ enterprise networks via compromised SolarWinds Orion products (e.g., Solorigate, Sunburst).[1] However, CISA is investigating instances in which th

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

        - Source: [CISA](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-008a)
        - Category: SSH_Patator
        - Generated: 2026-06-26

        _No specific information extracted._

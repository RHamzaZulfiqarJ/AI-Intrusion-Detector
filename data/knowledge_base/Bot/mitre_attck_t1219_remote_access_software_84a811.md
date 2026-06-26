        ---
        title: MITRE ATT&CK T1219 - Remote Access Software
        category: Bot
        source: MITRE ATT&CK
        url: https://attack.mitre.org/techniques/T1219/
        date: 2026-06-26
        ---

        # Overview

        An adversary may use legitimate remote access tools to establish an interactive command and control channel within a network. Remote access tools create a session between two trusted hosts through a graphical interface, a command line interaction, a protocol tunnel via development or management software, or hardware-level access such as KVM (Keyboard, Video, Mouse) over IP solutions. Desktop support software (usually graphical interface) and remote management software (typically command line interface) allow a user to control a computer remotely as if they are a local user inheriting the user or software permissions. This software is commonly used for troubleshooting, software installation, and system management.[1][2][3] Adversaries may similarly abuse response features included in EDR and other defensive tools that enable remote access.
Remote access tools may be installed and used post-compromise as an alternate communications channel for redundant access or to establish an interactive remote desktop session with the target system. It may also be used as a malware component to establish a reverse connection or back-connect to a service or adversary-controlled system.
Installation of many remote access tools may also include persistence (e.g., the software's installation routine creates a Windows Service). Remote access modules/features may also exist as part of otherwise existing software (e.g., Google Chrome’s Remote Desktop).[4][5]
| ID | Name | Description | 
|---|---|---|
| G1024 | Akira | Akira uses legitimate utilities such as AnyDesk and PuTTy for maintaining remote access to victim environments.[6][7] | 
| G1043 | BlackByte | BlackByte has used tools such as AnyDesk in victim environments.[8][9] | 
| S0030 | Carbanak | |
| G0008 | Carbanak | Carbanak used legitimate programs such as AmmyyAdmin and Team Viewer for remote interactive C2 to target systems.[11] | 
| G0080 | Cobalt Group | Cobalt Group used the Ammyy Admin tool as well as TeamViewer for remote access, including to preserve remote access if a Cobalt Strike module was lost.[12][13][14] | 
| G0105 | DarkVishnya | DarkVishnya used DameWare Mini Remote Control for lateral movement.[15] | 
| S0384 | Dridex | |
| S0554 | Egregor | Egregor has checked for the LogMein event log in an attempt to encrypt files in remote machines.[17] | 
| G0046 | FIN7 | FIN7 has utilized the remote management tool Atera to download malware to a compromised system.[18] | 
| G0115 | GOLD SOUTHFIELD | GOLD SOUTHFIELD has used the cloud-based remote management and monitoring tool "ConnectWise Control" to deploy REvil.[19] | 
| S0601 | Hildegard | Hildegard has established tmate sessions for C2 communications.[20] | 
| G1032 | INC Ransom | INC Ransom has used AnyDesk and PuTTY on compromised systems.[21][22][23][24] | 
| S1245 | InvisibleFerret | InvisibleFerret has utilized remote access software including AnyDesk client through the "adc" module.[25][26][27] InvisibleFerret has also downloaded the AnyDesk

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

        - Source: [MITRE ATT&CK](https://attack.mitre.org/techniques/T1219/)
        - Category: Bot
        - Generated: 2026-06-26

        _No specific information extracted._

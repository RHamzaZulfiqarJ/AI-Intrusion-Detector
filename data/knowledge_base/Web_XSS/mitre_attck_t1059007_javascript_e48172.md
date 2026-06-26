        ---
        title: MITRE ATT&CK T1059.007 - JavaScript
        category: Web_XSS
        source: MITRE ATT&CK
        url: https://attack.mitre.org/techniques/T1059/007/
        date: 2026-06-26
        ---

        # Overview

        Adversaries may abuse various implementations of JavaScript for execution. JavaScript (JS) is a platform-independent scripting language (compiled just-in-time at runtime) commonly associated with scripts in webpages, though JS can be executed in runtime environments outside the browser.[1]
JScript is the Microsoft implementation of the same scripting standard. JScript is interpreted via the Windows Script engine and thus integrated with many components of Windows such as the Component Object Model and Internet Explorer HTML Application (HTA) pages.[2][3][4]
JavaScript for Automation (JXA) is a macOS scripting language based on JavaScript, included as part of Apple’s Open Scripting Architecture (OSA), that was introduced in OSX 10.10. Apple’s OSA provides scripting capabilities to control applications, interface with the operating system, and bridge access into the rest of Apple’s internal APIs. As of OSX 10.10, OSA only supports two languages, JXA and AppleScript. Scripts can be executed via the command line utility osascript, they can be compiled into applications or script files via osacompile, and they can be compiled and executed in memory of other programs by leveraging the OSAKit Framework.[5][6][7][8][9]
Adversaries may abuse various implementations of JavaScript to execute various behaviors. Common uses include hosting malicious scripts on websites as part of a Drive-by Compromise or downloading and executing these script files as secondary payloads. Since these payloads are text-based, it is also very common for adversaries to obfuscate their content as part of Obfuscated Files or Information.
| ID | Name | Description | 
|---|---|---|
| S0622 | AppleSeed | AppleSeed has the ability to use JavaScript to execute PowerShell.[10] | 
| G0099 | APT-C-36 | APT-C-36 has used a fileless attack chain composed of three JavaScript code snippets to execute subsequent payloads.[11] | 
| G0050 | APT32 | APT32 has used JavaScript for drive-by downloads and C2 communications.[12][13] | 
| S9031 | AshTag | AshTag can use JSON files to deliver payloads and configuration files.[14] | 
| S0373 | Astaroth | Astaroth uses JavaScript to perform its core functionalities. [15][16] | 
| S0640 | Avaddon | Avaddon has been executed through a malicious JScript downloader.[17][18] | 
| S1246 | BeaverTail | BeaverTail has executed malicious JavaScript code.[19][20][21][22][23] BeaverTail has also been compiled with the Qt framework to execute in both Windows and macOS.[24] | 
| S1180 | BlackByte Ransomware | BlackByte Ransomware is distributed as a JavaScript launcher file.[25] | 
| S0482 | Bundlore | Bundlore can execute JavaScript by injecting it into the victim's browser.[26] | 
| C0015 | C0015 | During C0015, the threat actors used a malicious HTA file that contained a mix of encoded HTML and JavaScript/VBScript code.[27] | 
| C0017 | C0017 | During C0017, APT41 deployed JScript web shells on compromised systems.[28] | 
| S0631 | Chaes | Chaes has used JavaScript 

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

        - Source: [MITRE ATT&CK](https://attack.mitre.org/techniques/T1059/007/)
        - Category: Web_XSS
        - Generated: 2026-06-26

        _No specific information extracted._

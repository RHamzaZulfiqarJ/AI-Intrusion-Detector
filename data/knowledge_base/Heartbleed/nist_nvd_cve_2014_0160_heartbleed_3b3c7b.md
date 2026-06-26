        ---
        title: NIST NVD CVE-2014-0160 (Heartbleed)
        category: Heartbleed
        source: NIST NVD
        url: https://nvd.nist.gov/vuln/detail/CVE-2014-0160
        date: 2026-06-26
        ---

        # Overview

        You are viewing this page in an unauthorized frame window.
This is a potential security issue, you are being redirected to
https://nvd.nist.gov
An official website of the United States government
Official websites use .gov
A .gov website belongs to an official government organization in the United States.
Secure .gov websites use HTTPS
A lock () or https:// means you've safely connected to the .gov website. Share sensitive information only on official, secure websites.
The (1) TLS and (2) DTLS implementations in OpenSSL 1.0.1 before 1.0.1g do not properly handle Heartbeat Extension packets, which allows remote attackers to obtain sensitive information from process memory via crafted packets that trigger a buffer over-read, as demonstrated by reading private keys, related to d1_both.c and t1_lib.c, aka the Heartbleed bug.
Metrics
NVD enrichment efforts reference publicly available information to associate
vector strings. CVSS information contributed by other sources is also
displayed.
CVSS V2 scoring evaluates the impact of the vulnerability on the host where the vulnerability is located. When evaluating the impact of this vulnerability to your organization, take into account the nature of the data that is being protected and act according to your organization’s risk acceptance. While CVE-2014-0160 does not allow unrestricted access to memory on the targeted host, a successful exploit does leak information from memory locations which have the potential to contain particularly sensitive information, e.g., cryptographic keys and passwords. Theft of this information could enable other attacks on the information system, the impact of which would depend on the sensitivity of the data and functions of that system.
References to Advisories, Solutions, and Tools
By selecting these links, you will be leaving NIST webspace.
We have provided these links to other web sites because they
may have information that would be of interest to you. No
inferences should be drawn on account of other sites being
referenced, or not, from this page. There may be other web
sites that are more appropriate for your purpose. NIST does
not necessarily endorse the views expressed, or concur with
the facts presented on these sites. Further, NIST does not
endorse any commercial products that may be mentioned on
these sites. Please address comments about this page to [email protected].
https://gist.github.com/chapmajs/10473815 Third Party Advisory
https://gist.github.com/chapmajs/10473815 Exploit
Changed
Reference Type
https://lists.apache.org/thread.html/ba661b0edd913b39ff129a32d855620dd861883ade05fd88a8ce517d%40%3Cdev.tomcat.apache.org%3E No Types Assigned
https://lists.apache.org/thread.html/ba661b0edd913b39ff129a32d855620dd861883ade05fd88a8ce517d%40%3Cdev.tomcat.apache.org%3E Mailing List, Patch, Third Party Advisory
Changed
Reference Type
https://lists.apache.org/thread.html/f8e0814e11c7f21f42224b6de111cb3f5e5ab5c15b78924c516d4ec2%40%3Cdev.tomcat.apache.org%3E No Types Assigne

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

        - Source: [NIST NVD](https://nvd.nist.gov/vuln/detail/CVE-2014-0160)
        - Category: Heartbleed
        - Generated: 2026-06-26

        _No specific information extracted._

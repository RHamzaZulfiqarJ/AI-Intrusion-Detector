        ---
        title: OWASP Cross Site Scripting (XSS)
        category: Web_XSS
        source: OWASP
        url: https://owasp.org/www-community/attacks/xss/
        date: 2026-06-26
        ---

        # Overview

        Cross Site Scripting (XSS)
Contributor(s): Jim Manico, Jeff Williams, Dave Wichers, Adar Weidman, Roman, Alan Jex, Andrew Smith, Jeff Knutson, Imifos, Erez Yalon, kingthorin, Vikas Khanna. Grant Ongers
Overview
Cross-Site Scripting (XSS) attacks are a type of injection, in which malicious scripts are injected into otherwise benign and trusted websites. XSS attacks occur when an attacker uses a web application to send malicious code, generally in the form of a browser side script, to a different end user. Flaws that allow these attacks to succeed are quite widespread and occur anywhere a web application uses input from a user within the output it generates without validating or encoding it.
An attacker can use XSS to send a malicious script to an unsuspecting user. The end user’s browser has no way to know that the script should not be trusted, and will execute the script. Because it thinks the script came from a trusted source, the malicious script can access any cookies, session tokens, or other sensitive information retained by the browser and used with that site. These scripts can even rewrite the content of the HTML page. For more details on the different types of XSS flaws, see: Types of Cross-Site Scripting.
Related Security Activities
How to Avoid Cross-site scripting Vulnerabilities
- XSS (Cross Site Scripting) Prevention Cheat Sheet
- DOM based XSS Prevention Cheat Sheet
- OWASP Development Guide article on Data Validation
- OWASP Development Guide article on Phishing
How to Review Code for Cross-site scripting Vulnerabilities
See the OWASP Code Review Guide.
How to Test for Cross-site scripting Vulnerabilities
See the latest OWASP Testing Guide article on how to test for the various kinds of XSS vulnerabilities.
- Testing_for_Reflected_Cross_site_scripting
- Testing_for_Stored_Cross_site_scripting
- Testing_for_DOM-based_Cross_site_scripting
Description
Cross-Site Scripting (XSS) attacks occur when:
- Data enters a Web application through an untrusted source, most frequently a web request.
- The data is included in dynamic content that is sent to a web user without being validated for malicious content.
The malicious content sent to the web browser often takes the form of a segment of JavaScript, but may also include HTML, Flash, or any other type of code that the browser may execute. The variety of attacks based on XSS is almost limitless, but they commonly include transmitting private data, like cookies or other session information, to the attacker, redirecting the victim to web content controlled by the attacker, or performing other malicious operations on the user’s machine under the guise of the vulnerable site.
Reflected and Stored XSS Attacks
XSS attacks can generally be categorized into two categories: reflected and stored. There is a third, much less well-known type of XSS attack called DOM Based XSS that is discussed separately here.
Reflected XSS Attacks
Reflected attacks are those where the injected script is reflected off t

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

        - Source: [OWASP](https://owasp.org/www-community/attacks/xss/)
        - Category: Web_XSS
        - Generated: 2026-06-26

        _No specific information extracted._

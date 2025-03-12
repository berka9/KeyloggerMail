# Keylogger Script

##  Overview
This script implements a **keylogger** using the `pynput` library to capture keyboard input and periodically send the logged keystrokes via email. It runs in the background and continuously logs user keystrokes.

##  Features
- **Records keystrokes** in real time.
- **Handles special characters and spaces**.
- **Sends logged keystrokes via email** at regular intervals.
- Uses **multithreading** for periodic email dispatching.

##  How It Works
1. **Keyboard Logging:**
   - The script uses `pynput.keyboard.Listener` to listen for keyboard events.
   - Captured keystrokes are stored in a global variable `log`.

2. **Data Transmission:**
   - Every **30 seconds**, the logged keystrokes are sent to a specified email.
   - Uses `smtplib` to send the email via Gmail SMTP.

3. **Threading for Continuous Execution:**
   - The script runs a **timer-based thread** to send logs at intervals.
   - After each email is sent, the log is cleared to avoid redundant data.

##  Security & Ethical Considerations
This script is a **keylogger**, which can be used for **malicious purposes** if deployed without consent. Some key risks include:
- **Unauthorized data collection** without user permission.
- **Email credentials exposure**, making the sender vulnerable to hacking.
- **Legal implications**, as unauthorized keylogging is illegal in many jurisdictions.

⚠ **Warning:** Unauthorized use of keyloggers is a violation of privacy laws. Only use this script for ethical and educational purposes, such as testing security defenses or monitoring personal devices with consent.

##  Possible Use Cases
- **Cybersecurity Research:** Understanding how keyloggers operate.
- **Parental Control:** Monitoring child activity (with consent).
- **Personal Security Auditing:** Checking for vulnerabilities on personal systems.

##  Legal Disclaimer
This script is provided for **educational and research purposes only**. Any misuse for unauthorized surveillance or illegal activities is strictly prohibited.

---

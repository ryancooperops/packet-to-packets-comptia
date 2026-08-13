# CompTIA IT & Security Lab Journal 🛠️🔐

Hey! Welcome to my hands-on learning lab for CompTIA certifications. 

I’m an IT student building out my personal homelab while prepping for CompTIA exams. Rather than treating these certifications as purely theoretical multiple-choice tests, I use this repository to bridge the gap between exam objectives and actual command-line troubleshooting, packet captures, and system hardening.

---

## 💡 A Student's Perspective: Building Real Tech Skills

When you first dive into CompTIA material, the alphabet soup of acronyms (DNS, DHCP, SIEM, CIA, NAT, VLAN...) can feel like a completely different language. The secret I discovered? **If you can inspect it in Wireshark or configure it in a VM, you'll never forget it.**

### My Core Learning Tactics:
* **CLI Over Memorization**: Don't just memorize what `traceroute` or `netstat` does—run them on your terminal, break your home local network on purpose, and analyze the output!
* **Think Like a Defender**: For Security+, understanding *how* a threat actor carries out a Credential Stuffing or ARP Poisoning attack makes configuring the defensive control (MFA, Dynamic ARP Inspection) logical and intuitive.
* **Master the Trifecta Synergies**: A+ gives you hardware/OS foundations, Network+ teaches how packets move, and Security+ teaches how to lock those packets down. They build on top of each other seamlessly.

---

## 🎯 Key Technical Domains & Practical Breakdowns

### 1. Network Infrastructure & Troubleshooting (Network+ Focus)
* **OSI Model Layer Isolation**: Pinpointing connectivity issues layer-by-layer (Physical cable checks -> IP routing issues -> Firewall port blocking).
* **Essential Networking Toolkit**:
  * `ping` / `traceroute`: Testing ICMP reachability and hop latency.
  * `nslookup` / `dig`: Querying DNS record types (A, AAAA, CNAME, MX, TXT).
  * `ipconfig` / `ifconfig` / `ip addr`: Checking interface bindings and subnet masks.

### 2. Cybersecurity Controls & Threat Vectors (Security+ Focus)
* **Identity & Access Management (IAM)**: Implementing Zero Trust architecture, Multi-Factor Authentication (MFA), and Least Privilege enforcement.
* **Cryptographic Frameworks**: Public Key Infrastructure (PKI), Symmetric vs. Asymmetric encryption, and TLS 1.3 handshake dynamics.
* **Incident Response & Forensics**: Log aggregation using SIEM tools, memory capture preservation, and chain of custody tracking.

### 3. Systems Hardware & OS Management (A+ Focus)
* **Storage Technologies**: RAID array configurations (RAID 0, 1, 5, 10) balancing performance against fault tolerance.
* **Virtualization & Cloud Fundamentals**: Hypervisor Type 1 (bare-metal) vs. Type 2 (hosted) resource allocation.

---

## 📁 Repository Structure

* `README.md` - Overall hands-on study framework and homelab notes.
* `Security-Plus-SY0-701-Notes.md` - (In Progress) Domain-by-domain breakdown, threat vector analysis, and PBQ practice tips.
* `Network-Plus-N10-008-Notes.md` - (In Progress) Subnetting cheat sheets, routing protocols, and command-line diagnostics.

---

## ⏱️ My Learning & Lab Roadmap

- [x] Set up a VirtualBox sandbox with Kali Linux and Ubuntu Server
- [x] Practice packet inspection using Wireshark display filters (`ip.addr == ...`, `tcp.flags.syn == 1`)
- [ ] Complete 50+ Performance-Based Questions (PBQs) for Security+
- [ ] Document custom firewall rulesets using `iptables` and Windows Defender Firewall

*Thanks for swinging by! Feel free to star ⭐️ this repo if you're also grinding through CompTIA exams or building your IT skills.*

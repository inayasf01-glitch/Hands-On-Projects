https://1drv.ms/w/c/44cea5c90db5facc/IQA8koHHVjRDTqjlkwFYRpN2AY3SHnH1OL10cjIK5mf6c3s?e=5L0Odo

Project Title: Network Intrusion Detection (IDS) Lab Report

Course Subject: CSC 273 — Network Security

Student Name: Inaya Shahid

Student ID: 1262799

Institution: Middlesex Community College, New Jersey

Submission Date: 4/3/2026


Acknowledgement

I completed this project through independent learning, hands-on practice, and continuous effort to develop technical skills in network security, Linux administration, and intrusion detection system configuration. I did this to strengthen practical knowledge in monitoring, traffic analysis, and enterprise security implementation. Guidance and mentorship provided during the learning process supported the successful completion of this project and helped build confidence in applying network security concepts in a real-world lab environment.

Abstract

This project focused on the design and implementation of a network intrusion detection system IDS) using Snort within a virtualized lab environment. The system monitored network traffic between a Windows Server and a client machine, generating alerts for suspicious activity such as multiple ICMP requests or port scans. The lab provided hands-on experience in Linux administration, IDS configuration, network traffic analysis, and security alert management. The successful deployment of the IDS demonstrated the importance of real-time monitoring, custom rule creation, and alert verification in maintaining secure enterprise networks.

Introduction

Modern organizations face constant threats from malicious actors attempting to access network resources or disrupt services. Network intrusion detection systems IDS) are essential tools that monitor and analyze network traffic for signs of suspicious or unauthorized activity. These systems play a critical role in an organization's defense-in-depth strategy, providing early warnings of potential security incidents.
This project simulated a small enterprise network environment in a virtual lab, with a Linux-based Snort sensor monitoring traffic between a Windows Server and a client system. By deploying an IDS in this controlled environment, the project provided practical experience in network security monitoring, traffic analysis, and alert management. These are all essential skills for cybersecurity professionals and system administrators operating in today's complex threat landscape. The hands-on nature of this lab allowed for a deeper understanding of how IDS functions in a real-world context.

Problem Statement

Small and medium-sized organizations often lack the ability to monitor network traffic effectively due to resource constraints or a lack of specialized expertise. Without real-time intrusion detection capabilities, malicious activity such as port scanning, brute-force attacks, or unauthorized access attempts can go undetected for extended periods. This lack of visibility can lead to significant security breaches, data loss, and operational disruption, ultimately impacting business continuity and reputation.
This project addresses these critical challenges by deploying a Snort-based IDS in a virtual environment. The solution provides centralized monitoring, automated alert generation, and visualization of potential network threats. 
By implementing such a system, organizations can gain better insight into their network's security posture and respond proactively to emerging threats, thereby mitigating potential risks effectively.

Objectives

The primary objectives of this project were to gain practical experience in deploying and managing an IDS within a simulated network environment. This involved several key steps to ensure comprehensive learning and successful implementation.
 

<img width="1532" height="1064" alt="image" src="https://github.com/user-attachments/assets/5c59c225-0ad0-4e4a-b0c5-5d1ec54d0a88" />
 
Tools and Technologies
The successful implementation of this network intrusion detection system relied on a combination of industry-standard tools and technologies. These selections were made to provide a realistic and effective learning environment.

<img width="1474" height="1172" alt="image" src="https://github.com/user-attachments/assets/b44606c3-1178-4091-a673-28095dd39f64" />


System Requirements

To ensure the virtualized lab environment operated efficiently and effectively, specific hardware and software requirements were established. Adhering to these specifications was crucial for the seamless performance of the IDS and the simulated network.
 
Hardware Requirements (Host System)

•	Minimum 8 GB RAM: Essential for running multiple virtual machines concurrently without performance degradation.

•	Dual-Core Processor or Higher: Provides sufficient processing power for virtualization tasks and Snort's real-time analysis.

•	Minimum 100 GB Available Storage: Required for installing operating systems, virtual machine files, and Snort logs.

•	Internet Connectivity: Necessary for downloading software, updates, and research.

Virtual Machine Configuration

•	Linux VM Snort Sensor):

•	4 GB RAM

•	2 CPU cores

•	40 GB virtual hard disk

•	Windows Server VM Target/Client):

•	Previously configured with 4 GB RAM

•	2 CPU cores

•	50 GB virtual disk

Network Adapter Configuration

•	Network Adapter 1 NAT:Configured for internet access, allowing VMs to download updates and communicate with external resources.

•	Network Adapter 2 Internal Network): Established for private communication between the VMs, isolating the lab network from the host's external network.

Software Requirements

•	Linux Operating System Ubuntu/Kali)

•	Oracle VM VirtualBox

•	Windows Server 2022

•	Snort IDS

•	Traffic analysis and logging tools (e.g., Snorby, ELK Stack for dashboards - optional, but recommended for advanced analysis 

•	Draw.io for network diagrams

Environment Setup

The virtual lab environment was meticulously created using Oracle VirtualBox on a personal computer system. This setup allowed for a controlled and isolated space to deploy and test the network intrusion detection system without affecting the host machine's integrity.
The IDS sensor, a Linux virtual machine, was strategically configured to monitor traffic between the Windows Server lab and client systems within the internal network. This placement is critical for effective intrusion detection, as it allows Snort to inspect all relevant traffic flows.

Key configuration steps included:

1.	Network Adapter 1 Configuration: Set as NAT Network Address Translation) to provide the virtual machines with internet access for updates and software downloads.
2.	Network Adapter 2 Configuration: Configured as an Internal Network, creating a private, isolated segment for communication solely between the virtual machines. This ensures that the simulated attacks and monitoring occur within a contained environment.
3.	Linux VM IP Addressing: The Linux VM was allocated a static IP address to ensure consistent network identification and reliable monitoring by Snort.
4.	Snort Installation and Integration: Snort was installed on the Linux VM and integrated with the designated network interfaces for efficient packet capturing.
5.	Custom Snort Rules: Specific rules were defined to generate alerts for suspicious traffic patterns, such as multiple ICMP requests (ping floods) and port scans.
6.	Network Diagram: A visual representation of the network topology was created using Draw.io, illustrating the traffic flow and the strategic placement of the IDS sensor.

          +------------------+        +------------------+
          |  Windows Server  |        |   Client VM      |
          |   (Target)       |        |  (Simulated User)|
          +--------+---------+        +---------+--------+
                   \                       /
                    \                     /
                     \                   /
                      \                 /
                       \               /
                        \             /
                         \           /
                      +------------------+
                      |   Linux VM IDS   |
                      |   (Snort Sensor) |
                      +------------------+
                               |
                               |
                         Internal Network
                               |
                               |
                       +------------------+
                       | Host Machine /   |
                       | Oracle VirtualBox|
                       +------------------+

Network diagram
<img width="890" height="386" alt="image" src="https://github.com/user-attachments/assets/b9dbf1a6-8840-414f-ad00-a881d4a8766a" />

 
Figure 1 Figure 1 Linux System Configuration Window for Virtual Machine Setup

Methodology / Procedure

The project followed a structured methodology to ensure the systematic deployment, configuration, and testing of the Network Intrusion Detection System. Each step was carefully executed to achieve the stated objectives and gather relevant evidence.

1.	Deployment of Linux Virtual Machine:
•	A Linux virtual machine Ubuntu/Kali Linux) was deployed within Oracle VirtualBox.

•	The VM was configured with 4 GB RAM, 2 CPU cores, and a 40 GB virtual hard disk to meet system requirements.

 
2.	Snort Installation:
•	Snort was installed on the Linux VM using the command: sudo apt install snort. This command ensures all necessary dependencies are met for a proper installation.
3.	Network Interface Configuration:
    •	Network interfaces on the Linux VM were configured to monitor the internal network segment established between the Windows Server and client VMs. This involved ensuring Snort could listen on the correct interface.
4.	  Custom Snort Rule Creation:
•	Custom Snort rules were created to detect specific suspicious activities. An example rule for detecting ICMP ping floods was implemented:
"alert icmp any any -> 192.168.1.10 any (msg:"Potential ICMP Scan Detected"; threshold: type both, track by_src, count 5, seconds 60;)".
This rule alerts when a source sends more than 5 ICMP packets to the target IP  192.168.1.10 within a 60-second window.
5.	Simulated Network Activity:
•	Network activity, including ping floods and port scans, was simulated from the client VM towards the Windows Server. This step was crucial for testing the effectiveness of the deployed Snort rules.
6.	Alert Log Verification:
•	Snort logs were thoroughly reviewed to capture and verify the detection of suspicious behavior corresponding to the simulated attacks. This confirmed that the IDS was functioning as intended.
7.	Network Diagram Creation:
•	A comprehensive network diagram was created using Draw.io, visually representing the placement of the IDS sensor and the traffic flow within the virtualized lab environment.
8.	Documentation:
•	All setup procedures, configurations, observed alerts, and test results were meticulously documented to provide a complete record of the project.
 
Evidence

The following images serve as visual evidence of the successful environment setup, Snort installation, custom rule implementation, and alert verification.

Virtual Machine Configuration — Oracle VirtualBox

This image illustrates the initial configuration of the Linux virtual machine, detailing the allocated resources such as RAM, CPU cores, and storage, which are crucial for the efficient operation of the Snort IDS.
<img width="691" height="435" alt="image" src="https://github.com/user-attachments/assets/7aee0bbc-6900-497f-927f-8e7b618b7a87" />

 
Figure 2 Virtual Machine Setup with Snort showing network interface configuration

Snort Installation and Configuration

The screenshot below confirms the successful installation of Snort and its configuration to monitor the designated network interface. This step is vital for ensuring Snort can capture and analyze network traffic effectively.
<img width="807" height="470" alt="image" src="https://github.com/user-attachments/assets/1c9db2fc-a127-4d2d-9a31-53070107bc8a" />
 
Figure 3 Snort Configuration Interface displaying ICMP rules
 
Custom Rule Implementation

This image demonstrates the implementation of custom Snort rules, specifically designed to detect ping floods. The rule definition is shown, highlighting how specific thresholds and alert messages are configured.
<img width="747" height="478" alt="image" src="https://github.com/user-attachments/assets/cd417ae0-ac4e-4035-87c0-abe15af6fe04" />

 
Figure 4 Custom rule Demonstrating the Custom snort rules designed to detect ping floods

Alert Log Verification

The network monitoring console displays real-time alerts generated by Snort in response to simulated attacks. This evidence confirms that the custom rules are effective in identifying and logging suspicious activities such as ICMP and TCP port scans.
<img width="691" height="470" alt="image" src="https://github.com/user-attachments/assets/1293f800-3b4b-4897-b3dd-88528acdff57" />
 
Figure 5 Network Monitoring Console showing detected ICMP and TCP port scan alerts 

Network Diagram

A network diagram, created using Draw.io, would visually represent the virtualized lab environment. It would illustrate the Windows Server, client machine, and the Linux VM acting as the Snort IDS sensor, all connected via an internal network. The diagram would also depict the traffic flow and the strategic placement of the IDS for optimal monitoring.

Results

The network intrusion detection system was successfully deployed and configured within the virtual lab environment. The Snort sensor effectively monitored traffic between the Windows Server and the client machine, demonstrating its capability to detect and alert on suspicious network activity in real-time.

Key findings include:

•	Successful Deployment: The Linux-based Snort sensor was installed and integrated into the virtual network without significant issues.

•	Traffic Monitoring: Snort successfully captured and analyzed network traffic flowing between the designated virtual machines.

•	Custom Rule Efficacy: The custom rules configured for detecting ping floods and port scans proved effective. During simulated attacks, Snort generated the expected alerts, which were logged for further analysis.

•	Alert Verification: Verification of the Snort logs confirmed that the IDS accurately identified and reported suspicious behavior, demonstrating proper alerting and monitoring functionality.

•	Threat Detection Capabilities: The project successfully showcased the real-time threat detection capabilities of an IDS and underscored the importance of strategic IDS placement within an enterprise network for comprehensive monitoring.

Overall, the project achieved its objectives, validating the practical application of Snort as an intrusion detection system in a controlled virtual environment.
 
Skills Gained

This project provided invaluable hands-on experience and significantly enhanced a range of technical and analytical skills critical for a career in cybersecurity and IT.

Linux System Administration

Proficiency in managing and configuring Linux operating systems, including command-line operations, package management, and file system navigation.

Snort IDS Installation and Configuration

Expertise in deploying, configuring, and maintaining Snort, a leading intrusion detection system, including understanding its architecture and operational modes.

Network Traffic Monitoring and Analysis

Ability to capture, analyze, and interpret network packets and traffic patterns to identify anomalies and potential security threats.

Custom Rule Creation and Alert Verification

Skill in writing and testing custom Snort rules to detect specific attack signatures and effectively verify the accuracy of generated alerts.

Virtual Machine Deployment and Networking

Competence in setting up and configuring virtualized environments using Oracle VirtualBox, including network adapter configuration and inter-VM communication.

Threat Detection and Incident Documentation

Understanding of threat detection methodologies and the importance of thorough documentation for security incidents and system configurations.

Cybersecurity Reporting and Visualization

Ability to effectively communicate technical findings through structured reports and visual aids like network diagrams.

Troubleshooting and System Security Management

Enhanced skills in identifying and resolving issues within network security systems and overall security management practices.
 
Conclusion

This project successfully demonstrated the deployment and configuration of a network intrusion detection system using Snort within a virtualized lab environment. The implementation provided invaluable practical experience in Linux administration, network monitoring, and threat detection. By successfully configuring custom rules and verifying alerts for simulated attacks, the project underscored the critical role of IDS in maintaining network security.
The project strengthened technical skills required for real-world cybersecurity and IT roles, highlighting the importance of proactive traffic monitoring, alert management, and custom IDS rule creation in maintaining secure organizational networks. The hands-on nature of this lab reinforced theoretical knowledge with practical application, preparing the student for real-world security challenges.

Future Scope

Building upon the foundational work established in this project, several avenues for future improvements and expansions can be explored to further enhance the capabilities and realism of the IDS lab environment.

•	Adding Multiple Client Machines: Expand the monitored network to include multiple client machines, simulating a more complex enterprise environment and increasing the diversity of traffic to be analyzed.

•	Advanced Snort Rules: Develop and implement more sophisticated Snort rules to detect complex attack patterns, including application-layer attacks, zero-day exploits, and sophisticated malware communication.

•	Integration with Visualization Dashboards: Integrate Snort with visualization dashboards such as the ELK Stack Elasticsearch, Logstash, Kibana) or Snorby. This would provide acentralized, graphical interface for log analysis, alert management, and real-time security monitoring, significantly improving operational efficiency.

•	Automated Alert Notifications: Implement automated alert notification systems via email or SMS. This would ensure that security personnel are immediately informed of critical incidents, enabling faster response times.

•	Performance Testing and Benchmarking: Conduct performance testing and benchmarking of the IDS efficiency under varying network loads. This would help understand the system's limitations and optimize its deployment in high-traffic environments.

•	Expanding Detection to Application Layer and Internal Threats: Extend the IDS capabilities to detect application layer attacks (e.g., SQL injection, XSS) and internal threats, such as insider misuse or lateral movement attempts, which are often overlooked by perimeter defenses.
 
References

•	Snort.org. Snort User Manual and Documentation. Available at: https://www.snort.org/

•	Cisco Systems. Introduction to Intrusion Detection Systems. Available at: https://www.cisco.com/c/en/us/products/security/intrusion-prevention-systems/what-is-ips-ids.html

•	NIST National Institute of Standards and Technology). Cybersecurity Best Practices Guidelines. Available at: https://www.nist.gov/cybersecurity

•	Oracle Corporation. Oracle VM VirtualBox User Guide. Available at: https://www.virtualbox.org/manual/UserManual.html

•	Ubuntu Documentation. Installing and Configuring Snort on Ubuntu. Available at: https://ubuntu.com/tutorials/install-snort-on-ubuntu

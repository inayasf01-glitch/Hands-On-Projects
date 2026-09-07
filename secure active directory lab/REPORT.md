https://1drv.ms/w/c/44cea5c90db5facc/IQAJ8l4sB9rqQoJWNVdMmw7CAXMrTBHS6hKF5BtoDESExyA?e=3QBqRe


















Project Title: Secure Active Directory Home Lab Report



Course Subject: CSC 270 — Windows System Administration

Student Name: Inaya Sahid Student ID: 1262799

Institution: Middlesex Community College, New Jersey Submission Date: 4/3/2026 


Acknowledgement

This project was completed through independent learning, hands-on practice, and continuous effort to develop technical skills in Windows Server administration, Active Directory configuration, and enterprise security management. The project was undertaken to strengthen practical knowledge in virtualization, centralized user management, and Group Policy-based security implementation. Guidance and mentorship provided during the learning process supported the successful completion of this project and helped build confidence in applying system administration concepts in a real-world lab environment.

Abstract

This project focused on the design and implementation of a secure Active Directory environment using Windows Server 2022 within a virtualized lab environment. The system simulated a small enterprise network by configuring a Domain Controller, creating user accounts, and applying Group Policy security settings to enforce restrictions such as disabling Command Prompt access for standard users. The lab provided hands-on experience in Windows Server administration, Active Directory Domain Services (AD DS), Group Policy configuration, and basic enterprise security hardening. The successful deployment of the domain environment demonstrated the importance of centralized authentication, user management, and policy enforcement in maintaining secure and manageable organizational networks.

Introduction

Modern organizations rely heavily on centralized directory services to manage users, computers, and security policies across their networks. Active Directory Domain Services (AD DS) is a core Microsoft technology that provides authentication, authorization, and centralized management of resources within a Windows-based domain environment. Without such centralized control, managing users and enforcing consistent security policies becomes complex, error-prone, and insecure.

This project simulated a small enterprise network environment in a virtual lab, with a Windows Server 2022 system configured as a Domain Controller for the domain lab.local. By deploying Active Directory in this controlled environment, the project provided practical experience in domain configuration, user account management, and Group Policy-based security enforcement. These are essential skills for system administrators and cybersecurity professionals responsible for maintaining secure and efficient enterprise infrastructures. The hands-on nature of this lab allowed for a deeper understanding of how Active Directory functions in a real-world context.

Problem Statement

Small and medium-sized organizations often struggle to manage user accounts, permissions, and security configurations effectively when relying on local accounts and manual configuration. Without centralized directory services, administrators must configure each system individually, which can lead to inconsistent security settings, weak access control, and increased administrative overhead. This lack of centralized management can result in security vulnerabilities, misconfigurations, and difficulty enforcing organizational policies.

This project addresses these challenges by deploying a Windows Server 2022-based Active Directory domain in a virtual environment. The solution provides centralized user management, Group Policy-based security  

enforcement, and a structured domain architecture that simulates a secure enterprise network. By implementing such a system, organizations can gain better control over user access, standardize security configurations, and improve operational efficiency.


Objectives

The primary objectives of this project were to gain practical experience in deploying and managing a secure Active Directory environment within a simulated network. This involved several key steps to ensure comprehensive learning and successful implementation.


<img width="1232" height="1036" alt="image" src="https://github.com/user-attachments/assets/cd3b051c-bc1a-4e2a-aad3-218a53b0a1e6" />
 


Tools and Technologies

The successful implementation of this secure Active Directory environment relied on a combination of industry-standard tools and technologies. These selections were made to provide a realistic and effective learning environment.

<img width="1486" height="832" alt="image" src="https://github.com/user-attachments/assets/91954dee-cb17-42a0-9005-291b2417a2ea" />

 
System Requirements

To ensure the virtualized lab environment operated efficiently and effectively, specific hardware and software

requirements were established. Adhering to these specifications was crucial for the seamless performance of the Domain Controller and the simulated network.

Hardware Requirements (Host System)

•	Minimum 8 GB RAM: Essential for running multiple virtual machines concurrently without performance degradation.

•	Dual-Core Processor or Higher: Provides sufficient processing power for virtualization tasks and domain services.

•	Minimum 100 GB Available Storage: Required for installing operating systems, virtual machine files, and logs. 

•	Internet Connectivity: Necessary for downloading software, updates, and documentation


Virtual Machine Configuration

Windows Server 2022 VM (Domain Controller):

•	4 GB RAM

•	2 CPU cores

•	50 GB virtual hard disk

(Optional) Windows Client VM:

•	2–4 GB RAM

•	1–2 CPU cores

•	40–50 GB virtual disk

Network Adapter Configuration

•	Network Adapter 1 (NAT): Configured for internet access, allowing the server to download updates and communicate with external resources.

•	Network Adapter 2 (Internal Network): Established for private communication between the virtual machines, isolating the lab network from the host's external network.



Software Requirements

•	Windows Server 2022 Operating System

•	Oracle VM VirtualBox

•	Windows Client Operating System

•	Active Directory Domain Services (AD DS)

•	Group Policy Management Console (GPMC)

•	Draw.io for network diagrams


Environment Setup

The virtual lab environment was created using Oracle VirtualBox on a personal computer system. This setup allowed for a controlled and isolated space to deploy and test the Active Directory domain without affecting the host machine's integrity.

The Windows Server 2022 virtual machine was configured as the Domain Controller for the domain lab.local, providing centralized authentication and directory services. A client system (optional) was connected to the same internal network to simulate domain-joined user activity.

Key configuration steps included: 


•	Network Adapter 1 Configuration: Set as NAT (Network Address Translation) to provide the virtual machines with internet access for updates and software downloads.

•	Network Adapter 2 Configuration: Configured as an Internal Network, creating a private, isolated segment for communication solely between the virtual machines.

•	Static IP Addressing: The Windows Server VM was assigned a static IP address to ensure consistent network identification and reliable domain services.

•	Domain Configuration: The server was configured as a Domain Controller for the domain lab.local, enabling centralized management of users and policies.

•	Group Policy Integration: Group Policy Objects were created and linked to the domain to enforce security setting 
Methodology / Procedure

The project followed a structured methodology to ensure the systematic deployment, configuration, and testing of the secure Active Directory environment. Each step was carefully executed to achieve the stated objectives and gather relevant evidence.

1.	Deployment of Windows Server Virtual Machine:
A Windows Server 2022 virtual machine was deployed within Oracle VirtualBox.
The VM was configured with 4 GB RAM, 2 CPU cores, and a 50 GB virtual hard disk to meet system requirements.
2.	Static IP Configuration:
A static IP address was assigned to the Windows Server VM on the internal network interface to ensure consistent connectivity for domain services.
3.	Installation of Active Directory Domain Services:
Active Directory Domain Services (AD DS) was installed using Server Manager.
The AD DS role was added, and the server was prepared for promotion to a Domain Controller.
4.	Domain Controller Promotion:
The server was promoted to a Domain Controller for the new forest and domain lab.local.
DNS services were installed as part of the promotion process to support domain name resolution.
5.	User Account Creation:
A standard user account named studentuser was created in Active Directory Users and Computers.
This account was used to simulate a typical domain user and to test authentication and policy enforcement.
6.	Group Policy Object Creation:
A Group Policy Object (GPO) named Security Policy was created using the Group Policy Management Console (GPMC).
Within this GPO, a security setting was configured to disable Command Prompt access for standard users, enhancing security by limiting access to system-level commands.
7.	Policy Application and Testing:
The Security Policy GPO was linked to the appropriate domain or organizational unit (OU).
A client system (or the server itself using the studentuser account) was used to log in and verify that the Command Prompt restriction was successfully applied.
Additional tests were performed to confirm domain authentication and policy propagation.
8.	Documentation:
All setup procedures, configurations, and test results were documented to provide a complete record of the project.




Evidence

The following images serve as visual evidence of the successful environment setup, Active Directory configuration, user account creation, and Group Policy enforcement.
 
Virtual Machine Configuration — Oracle VirtualBox

This image illustrates the configuration of the Windows Server 2022 virtual machine, detailing the allocated resources such as RAM, CPU cores, storage, and network adapters, which are crucial for the efficient operation of the Domain Controller.
<img width="991" height="694" alt="image" src="https://github.com/user-attachments/assets/77f6f9e8-ebcb-459e-8904-bdc5c4054dcc" />

 
Figure 1: Virtual Machine Setup showing Windows Server 2022 configuration and network adapter settings.


Active Directory Domain Services Installation  

The screenshot confirms the successful installation of Active Directory Domain Services through Server Manager and the completion of the server promotion to a Domain Controller for lab.local.
<img width="627" height="448" alt="image" src="https://github.com/user-attachments/assets/69da3e1d-1bcf-4525-83a7-f96d01cbb466" />

Figure 2: AD DS Installation and Domain Controller Promotion Wizard.

User Account Creation

This image demonstrates the creation of the student user account within Active Directory Users and Computers, representing a standard domain user.
<img width="759" height="543" alt="image" src="https://github.com/user-attachments/assets/6b41a9ae-cf96-45e7-9ec4-3fe2f1428904" />

 
Figure 3: Active Directory Users and Computers console displaying the studentuser account.


Group Policy Configuration

The screenshot shows the Security Policy GPO configuration, including the setting used to disable Command Prompt access for standard users.
<img width="741" height="513" alt="image" src="https://github.com/user-attachments/assets/58f46f84-af2c-47ce-8597-f5a56b6b6692" />
 
Figure 4: Group Policy Management Console displaying the configured Command Prompt restriction policy.

Results

The secure Active Directory environment was successfully deployed and configured within the virtual lab environment. The Domain Controller effectively managed authentication and user accounts, and Group Policy security settings were enforced as intended.

Key findings include:

•	Successful Deployment: The Windows Server 2022-based Domain Controller was installed and integrated into the virtual network without significant issues.

•	Centralized Authentication: Domain logons using the studentuser account functioned correctly, demonstrating proper Active Directory authentication.

•	Group Policy Efficacy: The custom Security Policy GPO configured to disable Command Prompt access for standard users proved effective. Testing confirmed that the policy was applied and enforced.

•	Policy Propagation: Group Policy settings were successfully propagated to the target user environment, validating the domain’s ability to centrally manage security configurations.

•	Enterprise Simulation: The project successfully simulated a small enterprise environment with centralized management and security enforcement.


Overall, the project achieved its objectives, validating the practical application of Active Directory as a centralized directory and security management solution in a controlled virtual environment.

Skills Gained

This project provided invaluable hands-on experience and significantly enhanced a range of technical and administrative skills critical for a career in IT and cybersecurity.

•	Windows Server Administration

Proficiency in managing and configuring Windows Server 2022, including role installation and server promotion.

•	Active Directory Configuration
Expertise in deploying, configuring, and maintaining Active Directory Domain Services, including domain creation and management.

•	User Account Management
Ability to create, manage, and organize user accounts within a domain environment.

•	Group Policy Implementation
Skill in creating and applying Group Policy Objects to enforce security settings and standardize configurations across users and systems.

•	Virtual Machine Deployment and Networking
Competence in setting up and configuring virtualized environments using Oracle VirtualBox, including network adapter configuration and internal network design.

•	System Security Management
Understanding of security hardening techniques using Group Policy to restrict user capabilities and reduce attack surface.

•	Technical Documentation and Visualization
Ability to effectively communicate technical configurations and results through structured reports and visual aids like network diagrams.

•	Troubleshooting and Policy Verification
Enhanced skills in identifying and resolving issues related to domain services, authentication, and policy enforcement.
 
Conclusion

This project successfully demonstrated the deployment and configuration of a secure Active Directory environment using Windows Server 2022 within a virtualized lab environment. The implementation provided practical experience in Windows Server administration, domain configuration, user management, and Group Policy-based security enforcement.
By successfully configuring a Domain Controller, creating user accounts, and applying security policies such as disabling Command Prompt access for standard users, the project underscored the critical role of Active Directory in maintaining secure and manageable organizational networks. The hands-on nature of this lab reinforced theoretical knowledge with practical application, preparing the student for real-world system administration and cybersecurity challenges.

Future Scope

Building upon the foundational work established in this project, several avenues for future improvements and expansions can be explored to further enhance the capabilities and realism of the Active Directory lab environment.

•	Adding Multiple Client Machines: Expand the domain to include multiple client computers, simulating a more complex enterprise environment and increasing the diversity of user scenarios.

•	Advanced Group Policy Settings: Develop and implement more sophisticated Group Policy configurations, including password policies, software restriction policies, and login banners.

•	File Sharing and Access Control: Configure shared folders with NTFS and share permissions, implementing role-based access control for different user groups.

•	Integration with Network Monitoring Tools: Integrate the environment with monitoring tools to track logon activity, policy changes, and security events.

•	Backup and Disaster Recovery: Implement backup strategies for Active Directory, including System State backups and Domain Controller recovery procedures.

•	Additional Security Controls: Deploy firewall policies, account lockout policies, and auditing configurations to further harden the environment.










References

•	Microsoft Corporation. Windows Server 2022 Documentation. Available at: Windows Server documentation | Microsoft Learn

•	Microsoft Learn. Active Directory Domain Services Overview. Available at: Microsoft Learn: Build with answers in reach

•	Oracle Corporation. Oracle VM VirtualBox User Guide. Available at: Oracle VM VirtualBox User Guide for Release 7.0

• NIST (National Institute of Standards and Technology). Cybersecurity Best Practices Guidelines. Available at Cybersecurity and privacy | NIST

https://1drv.ms/w/c/44cea5c90db5facc/IQA1XSoXpArmS5JU9P7yO8bzAY2fODQdeTWmgjyMnnbK06I?e=MhJhdu

Project Title: Post Attack Digital Forensic Investigation Lab Report

Course Subject: CSC 258 — Computer Forensics

Student Name: Inaya Shahid

Student ID: 1262799

Institution: Middlesex Community College, New Jersey

Submission Date: 4/3/2026


Acknowledgement

This project was completed through independent learning, hands on practice, and persistent effort to develop technical skills in digital forensics and incident response. The project was undertaken to strengthen practical knowledge in forensic analysis, evidence preservation, and post attack investigation methodologies. Guidance and mentorship provided during the learning process supported the successful completion of this project and helped build confidence in applying technical and procedural concepts in a controlled lab environment.

Abstract

This project focused on performing a post attack digital forensic investigation using industry standard tools, including FTK Imager and Autopsy, within a virtualized lab environment. The system simulated a compromised virtual machine, allowing the capture and analysis of digital evidence such as deleted files, system logs, and browser history. The project provided hands on experience in forensic imaging, artifact extraction, timeline reconstruction, and incident response procedures. The successful investigation demonstrated the importance of preserving data integrity, reconstructing attacker activity, and documenting findings for professional reporting and cybersecurity applications.

Introduction

Modern organizations face increasing threats from cyberattacks that compromise systems, disrupt operations, and expose sensitive data. Digital forensics plays a critical role in identifying how attacks occur, what damage was done, and how systems can be secured moving forward. It involves the systematic collection, preservation, and analysis of electronic evidence to support incident response and legal or organizational reporting.
This project simulated a real world post attack scenario in which a virtual machine was compromised during a prior penetration testing exercise. By performing a forensic investigation in a controlled lab environment, the project provided practical experience in capturing forensic images, analyzing system artifacts, and reconstructing attacker timelines. These skills are essential for cybersecurity professionals responsible for responding to incidents and ensuring the integrity of digital evidence.

Problem Statement

Organizations often struggle to effectively respond to cybersecurity incidents due to a lack of forensic readiness, inadequate evidence preservation, or insufficient investigative procedures. Without proper forensic workflows, critical evidence may be altered or lost, making it difficult to determine the cause of an attack, identify the attacker’s actions, or implement effective remediation.
This project addresses these challenges by demonstrating a structured digital forensic investigation workflow. It emphasizes the importance of forensic imaging, artifact extraction, timeline reconstruction, and chain of custody procedures to ensure that evidence remains intact and actionable throughout the investigation.


Objectives

The primary objectives of this project were to gain practical experience in conducting a digital forensic investigation within a simulated environment. This involved several key steps to ensure comprehensive learning and successful implementation.
 

Capture and Preserve Digital Evidence 
Use FTK Imager to create a forensic image of the compromised system while maintaining data integrity. 
Analyze Forensic Images Using Autopsy
Import the forensic image into Autopsy to extract relevant artifacts. 
Recover System Artifacts
Identify deleted files, browser history, system logs, and recently executed programs. 
Reconstruct Attacker Timeline
Use Autopsy’s Timeline feature to document attacker activity chronologically 
Verify Evidence Integrity
Perform hash verification to maintain chain of custody compliance. 
Prepare a Professional Forensic Report
Document findings, vulnerabilities, and remediation recommendations. 

Tools and Technologies
<img width="1536" height="618" alt="image" src="https://github.com/user-attachments/assets/717391c9-586b-45c6-a41d-28edcfae4a0f" />

The successful execution of this digital forensic investigation relied on a combination of industry standard tools and technologies. These selections were made to provide a realistic and effective learning environment.


Category	Tool / Technology	Description

<img width="1490" height="642" alt="image" src="https://github.com/user-attachments/assets/be5fb8fb-029f-4e33-9c52-a363bba7bbbf" />


System Requirements

To ensure the virtualized lab environment operated efficiently and effectively, specific hardware and software requirements were established. Adhering to these specifications was crucial for the seamless performance of the forensic tools and the compromised system.
 
Hardware Requirements (Host System)

•	Minimum 8 GB RAM

•	Dual Core Processor or Higher

•	Minimum 100 GB Available Storage

•	Internet Connectivity

Virtual Machine Configuration

•	4 GB RAM allocated to the virtual machine

•	2 CPU cores assigned

•	50 GB virtual hard disk

Software Requirements

•	FTK Imager

•	Autopsy

•	Oracle VM VirtualBox

•	Ubuntu / Windows Operating System (Compromised VM)

•	Kali Linux (Optional)

•	Draw.io for network diagrams

Environment Setup

The virtual lab environment was created using Oracle VirtualBox on a personal computer system. The system simulated a compromised network scenario with the following configuration:

•	Network Adapter 1: NAT for internet access

•	Network Adapter 2: Internal Network for isolated communication

•	Compromised VM: Configured as the target system for forensic investigation

•	Forensic Workstations: Configured to run FTK Imager and Autopsy for evidence acquisition and analysis

This setup allowed the capture of digital evidence without affecting the original compromised system, maintaining the integrity of forensic investigations.


Methodology / Procedure

The project followed a structured methodology to ensure the systematic execution of the digital forensic investigation. Each step was carefully executed to achieve the stated objectives and gather relevant evidence.

1. Forensic Image Creation
FTK Imager was used to create a forensic image (.E01) of the compromised virtual machine. This ensured that the original evidence remained unaltered throughout the investigation.
2. Autopsy Case Setup
A new case was created in Autopsy, and the forensic image was imported for analysis. Autopsy’s ingest modules were configured to extract relevant artifacts.
3. Artifact Extraction
Autopsy was used to identify key artifacts, including:

•	Browser history

•	Recently executed programs

•	System logs

•	Deleted files

These artifacts provided insight into attacker activity and attempts to conceal evidence.

5. Timeline Analysis
Autopsy’s Timeline feature was used to reconstruct attacker activity in chronological order. This allowed the identification of:

•	Initial compromise

•	Execution of malicious programs

•	File modifications

•	Evidence deletion attempts

7. Hash Verification
Hash values were generated and compared to verify the integrity of the forensic image and extracted artifacts, ensuring compliance with chain of custody standards.
8. Reporting
A professional forensic report was compiled, documenting:

•	Attack vectors

•	Extracted artifacts

•	Timeline reconstruction

•	Risk assessment

•	Remediation recommendations
 
Evidence
The following images serve as visual evidence of the successful forensic acquisition, analysis, and timeline reconstruction.

FTK Imager — Forensic Image Creation
This screenshot shows the creation of the forensic image (.E01), confirming proper evidence acquisition.
<img width="764" height="344" alt="image" src="https://github.com/user-attachments/assets/2459bedb-83da-4773-9191-8c174338cf9c" />
 
Figure 1 shows the creation of the forensic image

Autopsy Case Setup
This image displays the Autopsy interface with the newly created case and imported forensic image.
<img width="783" height="384" alt="image" src="https://github.com/user-attachments/assets/abf19700-5af9-4575-bebb-9090a8d4e624" />
 
Figure 2 shows the autopsy interface with a new case 

Artifact Extraction — Browser History / Deleted Files
This image displays the extracted browser history, recovered deleted files, and system logs.
<img width="773" height="411" alt="image" src="https://github.com/user-attachments/assets/c9230549-db09-475b-9ff8-80e2aa4b3064" />
 
Figure 3 shows the browser history

Timeline Reconstruction
This image demonstrates Autopsy’s Timeline view, showing attacker activity in chronological order.
<img width="643" height="366" alt="image" src="https://github.com/user-attachments/assets/9e407d42-2f30-47fa-b0ea-f841a172c4d5" />
 
Figure 4 shows the autopsy’s timeline view


Results

The digital forensic investigation successfully reconstructed the actions of the attacker within the compromised virtual machine. Key artifacts were recovered, including deleted files, browser history, and system logs. The timeline analysis provided a clear sequence of events, confirming how the system was exploited. Hash verification confirmed that all evidence remained unaltered during analysis. The project demonstrated proper forensic workflow and the ability to document findings in a professional report suitable for academic, legal, and professional review.
 
Skills Gained

This project provided invaluable hands on experience and significantly enhanced a range of technical and analytical skills critical for a career in digital forensics and incident response.

•	Forensic Image Acquisition and Preservation

Proficiency in using FTK Imager to capture and preserve digital evidence.

•	Artifact Extraction and Analysis

Experience using Autopsy to analyze browser history, logs, and deleted files.

•	Timeline Reconstruction

Ability to reconstruct attacker activity using forensic timelines.

•	Chain of Custody Maintenance

Understanding of evidence handling and integrity verification.

•	Incident Response Procedures

Skill in analyzing compromised systems and documenting findings.

•	Professional Forensic Reporting

Ability to communicate technical findings through structured reports.

•	Virtual Machine Configuration

Competence in setting up forensic workstations and compromised systems.

•	Data Integrity Verification

Experience using hash functions to validate evidence authenticity.
 
Conclusion

This project successfully demonstrated a complete post attack digital forensic investigation within a virtualized lab environment. By capturing and analyzing a forensic image, recovering system artifacts, and reconstructing attack timelines, the project provided valuable hands on experience in computer forensics and incident response. The implementation reinforced the importance of evidence preservation, professional reporting, and structured investigative procedures in cybersecurity practice. The skills developed in this project are directly applicable to real world IT security, incident response, and forensic analysis roles.

Future Scope

Building upon the foundational work established in this project, several avenues for future improvements and expansions can be explored to further enhance the capabilities and realism of the forensic investigation environment.

•	Integrating automated forensic tools to accelerate analysis

•	Performing network forensics to complement host based investigations

•	Investigating multiple compromised systems in a single incident

•	Implementing advanced artifact analysis techniques such as memory forensics

•	Simulating attacks with multiple vectors for complex investigations

•	Creating standardized forensic reports for legal or professional submission
 
References

•	Basis Technology. FTK Imager Documentation. Available at: FTKImager_UG.book

•	Sleuth Kit. Autopsy Digital Forensics Platform User Guide. Available at: Index of /autopsy/docs/user-docs

•	Oracle VM VirtualBox User Guide. Available at: Oracle VM VirtualBox User Guide for Release 7.0

•	NIST Computer Forensics Guidelines. Available at: SP 800-86, Guide to Integrating Forensic Techniques into Incident Response | CSRC

•	Casey, E. Digital Evidence and Computer Crime: Forensic Science, Computers, and the Internet. 

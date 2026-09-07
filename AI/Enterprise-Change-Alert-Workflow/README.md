\# Enterprise Change Alert Workflow



A Python-based enterprise architecture enablement prototype that detects architecture artifact changes, validates required metadata against governance rules, classifies change priority, and uses generative AI to assist with architecture review.



\## Overview



Enterprise architecture teams need reliable ways to identify changes, maintain consistent architecture information, and prioritize items that require human review.



This project prototypes that workflow locally using Python, deterministic governance rules, Google Gemini, JSON-based audit data, and an HTML dashboard.



The system is designed around a simple principle:



> \*\*Deterministic rules establish governance status; AI provides advisory analysis; humans make the final architecture decision.\*\*



\## Workflow



```text

Architecture Artifact

&#x20;       |

&#x20;       v

Change Detection

&#x20;       |

&#x20;       v

Metadata Parsing

&#x20;       |

&#x20;       v

Standards Validation

&#x20;       |

&#x20;       v

Change Classification

&#x20;       |

&#x20;       v

AI-Assisted Architecture Review

&#x20;       |

&#x20;       v

Review Queue / Audit Log

&#x20;       |

&#x20;       v

HTML Dashboard

Key Features

Detects new or modified architecture artifacts

Parses structured architecture metadata from text-based proposals

Validates required architecture fields

Identifies governance metadata gaps

Classifies changes by business-impact priority

Determines whether architecture review is required

Generates AI-assisted architecture summaries

Identifies potential technical, security, operational, integration, scalability, and governance risks

Generates architecture review questions

Suggests areas for human review

Maintains structured audit information

Generates an HTML dashboard for change visibility and review tracking

Technology Stack

Python 3

Google Gemini API

python-dotenv

JSON

HTML/CSS

PowerShell / Windows

Git / GitHub

Project Structure

Enterprise-Change-Alert-Workflow/

Γöé

Γö£ΓöÇΓöÇ alerts/

Γöé   ΓööΓöÇΓöÇ dashboard.html

Γöé

Γö£ΓöÇΓöÇ monitored\_files/

Γöé   Γö£ΓöÇΓöÇ api\_gateway\_v3.txt

Γöé   Γö£ΓöÇΓöÇ customer\_platform\_v2.txt

Γöé   ΓööΓöÇΓöÇ legacy\_reporting\_v1.txt

Γöé

Γö£ΓöÇΓöÇ src/

Γöé   Γö£ΓöÇΓöÇ ai\_architecture\_review.py

Γöé   Γö£ΓöÇΓöÇ change\_alert.py

Γöé   Γö£ΓöÇΓöÇ change\_classifier.py

Γöé   Γö£ΓöÇΓöÇ dashboard.py

Γöé   Γö£ΓöÇΓöÇ metadata\_parser.py

Γöé   ΓööΓöÇΓöÇ standards\_validator.py

Γöé

Γö£ΓöÇΓöÇ .gitignore

ΓööΓöÇΓöÇ README.md

Architecture Review Pipeline

1\. Change Detection



The monitoring workflow compares architecture artifacts against previously recorded file state and identifies new or modified artifacts.



2\. Metadata Parsing



Architecture proposals are parsed into structured metadata including:



System

Version

Change Type

Description

Owner

Business Impact

Environment

Review Required

3\. Standards Validation



Required metadata fields are checked using deterministic validation rules.



A complete artifact passes validation.



An artifact with missing required metadata fails validation and receives elevated governance risk.



4\. Change Classification



Changes are classified according to business impact:



High

Medium

Low



Validation failures also increase the governance risk classification.



5\. AI-Assisted Architecture Review



Google Gemini provides advisory analysis based only on the architecture proposal.



The AI produces:



Architecture Summary

Potential Risks

Review Questions

Suggested Review Focus



The AI does not make the final architecture approval decision.



6\. Dashboard



The workflow generates an HTML dashboard containing:



Total changes

Systems affected

New artifacts

Modified artifacts

Validation results

High-priority changes

High-governance-risk changes

Review queue

Architecture change details

AI-assisted review information

Example Scenarios



The prototype includes three architecture artifacts representing different governance conditions.



Internal API Gateway

Production environment

High business impact

Complete required metadata

Architecture review required

Customer Data Platform

Production environment

Medium business impact

Complete required metadata

Architecture review required

Legacy Reporting Platform

Production environment

Missing required metadata

Validation failure

Elevated governance risk

Architecture review required



These examples demonstrate how the workflow distinguishes between complete architecture information and governance gaps.



AI Governance Approach



The project intentionally separates deterministic governance logic from generative AI.



Deterministic Logic



Used for:



Required-field validation

Governance status

Business-impact classification

Review requirement determination

Generative AI



Used for:



Architecture summarization

Risk identification

Review-question generation

Suggested review focus



This separation reduces the risk of allowing an LLM to independently determine governance approval.



The intended operating model is:



Rules ΓåÆ AI Assistance ΓåÆ Human Architecture Review



Security Considerations



The Gemini API key is stored locally in a .env file and is excluded from version control through .gitignore.



The repository does not contain the API credential.



Do not commit .env or other secrets to source control.



Running the Project

1\. Create a virtual environment

python -m venv .venv

2\. Activate the environment

.\\.venv\\Scripts\\Activate.ps1

3\. Install dependencies

pip install google-genai python-dotenv

4\. Configure the Gemini API key



Create a local .env file:



GEMINI\_API\_KEY=your\_api\_key\_here



Do not commit this file.



5\. Run change detection

python -m src.change\_alert

6\. Generate the dashboard

python -m src.dashboard



The resulting dashboard is generated at:



alerts/dashboard.html

Current Scope



This implementation is a local Python prototype designed to demonstrate enterprise architecture workflow concepts.



It does not currently implement live integrations with:



Microsoft SharePoint

Microsoft Teams

Power Automate

SAP LeanIX



Those platforms represent potential future integration points rather than technologies currently implemented by this project.



Future Enhancements



Potential future development includes:



SharePoint-based architecture artifact ingestion

Power Automate workflow integration

Microsoft Teams review notifications

Enterprise architecture repository integration

SAP LeanIX integration

Automated metadata extraction from richer document formats

Role-based review workflows

Persistent architecture repositories

More sophisticated change-diff analysis

Additional governance and architecture standards

AI-assisted knowledge discovery

Architecture documentation reuse

Automated workflow notifications

Why This Project Matters



This project explores how software automation and generative AI can support enterprise architecture teams without replacing human governance decisions.



It demonstrates practical experience with:



Python automation

Structured data processing

Governance validation

Workflow design

Generative AI integration

AI-assisted decision support

Auditability

Dashboard development

Enterprise architecture concepts

Responsible AI boundaries

Author



Inaya Shahid



Information Technology Student

AI, Cybersecurity, Software Development \& Emerging Technologies


Video Evidence:

[Enterprise_Change_Alert_Workflow_Demo_Final.zip](https://github.com/user-attachments/files/31927209/Enterprise_Change_Alert_Workflow_Demo_Final.zip)


# 🛡️ ArchiGuard AI

## 🤖 Automated Enterprise Architecture Compliance Auditor

ArchiGuard AI is a Python-based proof-of-concept that uses generative AI to evaluate unstructured technology architecture proposals against defined enterprise technology standards.

The system transforms an architecture proposal into a structured compliance assessment containing an overall compliance decision, standard-by-standard evaluation, supporting evidence, identified violations, remediation recommendations, and review limitations.

The project demonstrates how AI and automation can reduce repetitive manual effort in enterprise architecture review while producing consistent and documented results.

---

# 📋 Project Overview

Enterprise architecture proposals often contain large amounts of unstructured technical information that must be reviewed against organizational technology and security standards.

Manually performing these reviews can require significant time and can result in inconsistent documentation.

ArchiGuard AI explores an automated approach:

Architecture Proposal → Python Compliance Engine → Enterprise Technology Standards → Gemini AI → Compliance Evaluation → Markdown Compliance Report

The prototype reads architecture proposals, evaluates them against a defined set of enterprise technology standards, and automatically generates a structured compliance report.

The goal is not to replace enterprise architects or governance professionals.

Instead, the project demonstrates how generative AI can assist with repetitive architecture-review and documentation activities while keeping the evaluation structured and reviewable.

---

# 🎯 Project Objectives

The project was developed to explore how generative AI and Python automation could support enterprise architecture governance workflows.

The primary objectives were to:

1. Process unstructured technology architecture proposals.
2. Evaluate proposals against defined enterprise technology standards.
3. Use generative AI to assist with architecture compliance analysis.
4. Extract supporting evidence from architecture proposals.
5. Identify potential standards violations.
6. Generate remediation recommendations.
7. Identify areas requiring additional human review.
8. Produce structured compliance reports automatically.
9. Create a repeatable architecture review workflow.
10. Demonstrate AI-assisted documentation automation.

---

# 🏗️ Architecture

Architecture Proposal
        ↓
Python Compliance Engine
        ↓
Enterprise Technology Standards
        ↓
Gemini AI
        ↓
Compliance Evaluation
        ↓
Markdown Compliance Report

The Python compliance engine manages the workflow, loads the defined enterprise standards, processes architecture proposals, sends the relevant analysis to Gemini, and generates structured Markdown compliance reports.

---

# 🔄 Project Workflow

ArchiGuard AI follows a repeatable architecture-review pipeline.

## Stage 1 — Architecture Proposal

The system receives an unstructured technology architecture proposal.

The proposal contains technical information that must be evaluated against the organization's defined standards.

The prototype includes multiple test proposals representing different compliance conditions.

---

## Stage 2 — Standards Loading

The compliance engine loads a defined set of enterprise technology standards.

These standards establish the criteria used during the architecture evaluation.

The current prototype evaluates five standards:

- Customer data encryption
- Legacy database integration
- Business continuity and disaster recovery
- Centralized identity and access management
- Security audit logging

---

## Stage 3 — Automated Processing

The Python application processes the architecture proposal and prepares the information for AI-assisted analysis.

This creates a repeatable processing pipeline rather than requiring each proposal to be manually reviewed and documented.

---

## Stage 4 — Generative-AI Analysis

Gemini AI analyzes the architecture proposal against the defined enterprise standards.

The AI-assisted analysis identifies:

- Evidence supporting compliance
- Potential violations
- Areas requiring additional review
- Relevant architecture considerations

The project uses generative AI as an analytical assistant within a structured workflow.

---

## Stage 5 — Compliance Evaluation

Each enterprise technology standard receives an individual assessment.

The system evaluates whether the proposal:

- Satisfies the standard
- Violates the standard
- Requires additional review

The resulting assessments are combined into an overall compliance status.

---

## Stage 6 — Compliance Decision

The system produces an overall architecture compliance status.

The supported outcomes are:

- PASSED
- FAILED
- NEEDS REVIEW

This provides a concise summary of the architecture proposal's overall compliance state.

---

## Stage 7 — Automated Documentation

The results are automatically written into a structured Markdown compliance report.

Each report contains:

- Overall Status
- Executive Summary
- Standards Evaluation
- Evidence
- Assessment
- Violations
- Remediation
- Review Limitations

This demonstrates how AI-assisted analysis can be combined with documentation automation.

---

# ⚙️ Core Components

## 1. Architecture Proposal Processing

Processes unstructured technology architecture proposals as the input to the compliance workflow.

Purpose:

- Provide architecture information for evaluation
- Support repeatable processing
- Allow different architecture scenarios to be tested

---

## 2. Enterprise Technology Standards

Provides the defined standards against which architecture proposals are evaluated.

The current standards cover:

- Customer data encryption
- Legacy database integration
- Business continuity and disaster recovery
- Centralized identity and access management
- Security audit logging

These standards provide a consistent evaluation framework for the prototype.

---

## 3. Python Compliance Engine

The Python application coordinates the compliance-review workflow.

It:

- Loads architecture proposals
- Loads enterprise technology standards
- Sends analysis requests to Gemini
- Processes AI-generated evaluations
- Generates compliance reports
- Stores the resulting documentation

This creates the automation layer connecting the architecture proposal, AI analysis, and final report.

---

## 4. Generative-AI Analysis

Gemini provides the generative-AI component used to analyze architecture proposals.

The AI-assisted workflow is designed to evaluate technical information against defined standards and return structured findings.

This demonstrates a practical application of generative AI beyond conversational use cases.

---

## 5. Compliance Evaluation

The system organizes the AI-assisted analysis into standard-by-standard evaluations.

Each evaluation includes:

- Compliance status
- Evidence
- Assessment

This provides greater transparency than relying only on a single overall AI-generated conclusion.

---

## 6. Remediation Recommendations

When standards are not satisfied, the generated report identifies violations and provides remediation recommendations.

This allows the output to move beyond simply identifying a problem and toward documenting possible next steps.

---

## 7. Review Limitations

The system also records areas where additional information or human review may be required.

This is important because architecture governance decisions can depend on information that may not be present in an unstructured proposal.

The prototype therefore explicitly documents review limitations rather than presenting every AI-generated conclusion as definitive.

---

# 📊 Compliance Report Structure

Each generated report follows a consistent structure.

## Overall Status

Provides the final compliance decision:

- PASSED
- FAILED
- NEEDS REVIEW

## Executive Summary

Provides a concise explanation of the architecture's overall compliance condition.

## Standards Evaluation

Provides an individual assessment for each defined enterprise technology standard.

Each standard includes:

- Status
- Evidence
- Assessment

## Violations

Documents standards that were not satisfied.

## Remediation

Provides recommended actions for addressing identified violations.

## Review Limitations

Documents information gaps, assumptions, or areas where additional review may be required.

---

# 🧪 Test Cases

The project includes test architecture proposals designed to demonstrate different compliance outcomes.

## Proposal 01 — Compliant Architecture

Expected result:

PASSED

The proposal satisfies all five defined enterprise technology standards.

The resulting compliance report documents the supporting evidence and provides a standard-by-standard assessment.

---

## Proposal 02 — Non-Compliant Architecture

Expected result:

FAILED

The proposal contains multiple standards violations and an area requiring additional review.

The generated report identifies the violations and provides remediation recommendations.

This test case demonstrates that the system can distinguish between compliant and non-compliant architecture scenarios.

---

# 🔍 Example Standards

ArchiGuard AI currently evaluates the following five enterprise technology standards.

## 1. Customer Data Encryption

Evaluates whether customer data is appropriately protected through encryption.

## 2. Legacy Database Integration

Evaluates how legacy database systems are integrated with newer architecture components.

## 3. Business Continuity and Disaster Recovery

Evaluates whether the proposed architecture addresses resilience and recovery requirements.

## 4. Centralized Identity and Access Management

Evaluates whether identity and access management are handled through centralized mechanisms.

## 5. Security Audit Logging

Evaluates whether security-relevant activity is appropriately logged and available for review.

---

# 🖥️ Interactive Demonstration

The project includes a Streamlit-based interface for demonstrating the automated compliance-review process.

The interface allows an architecture proposal to be processed through the compliance workflow and displays the resulting assessment.

The demonstration presents:

- Overall compliance status
- Executive summary
- Standard-by-standard evaluation
- Compliance findings
- Violations
- Remediation recommendations
- Review limitations
- Compliance report output

The interface provides a visual representation of the AI-assisted architecture compliance workflow.

---

# 📁 Project Structure

ArchiGuard-AI
│
├── inputs/
│   ├── proposal_01_compliant.txt
│   └── proposal_02_non_compliant.txt
│
├── outputs/
│   ├── proposal_01_compliant_compliance_*.md
│   └── proposal_02_non_compliant_compliance_*.md
│
├── standards/
│   └── enterprise_tech_standards.md
│
├── src/
│   └── compliance_engine.py
│
├── app.py
├── requirements.txt
├── .env.example
└── README.md

---

# 🛠️ Technology Stack

## Programming

- Python

## Artificial Intelligence

- Google Gemini API
- google-genai
- Generative AI

## Application Interface

- Streamlit

## Configuration

- python-dotenv

## Documentation & Data

- Markdown
- Structured compliance reports
- Text-based architecture proposals

## Development & Version Control

- PyCharm
- Git
- GitHub

---

# 🏢 Enterprise Architecture Concepts

The project demonstrates several concepts relevant to enterprise architecture and technology governance.

## Architecture Standards Assessment

Architecture proposals are evaluated against a defined set of technology standards.

## Compliance Evaluation

The system produces structured compliance decisions instead of relying solely on unstructured AI output.

## Evidence-Based Analysis

The compliance assessment incorporates evidence from the architecture proposal to support each standard evaluation.

## Exception and Review Handling

The system can identify areas where the available information is insufficient for a definitive assessment.

## Remediation Recommendations

Identified violations are accompanied by recommended remediation actions.

## Documentation Automation

The system automatically converts the analysis into a structured compliance report.

## Repeatable Architecture Review

The same evaluation process can be applied to multiple architecture proposals.

---

# 🤖 AI Governance Approach

AI is used as an assistive analytical component rather than an autonomous enterprise governance authority.

The system combines:

- Defined technology standards
- Structured processing
- Generative-AI analysis
- Standard-by-standard evaluation
- Explicit review limitations
- Automated documentation

This approach is important because enterprise architecture decisions can have security, operational, and business consequences.

The prototype therefore emphasizes structured evaluation and transparent reporting rather than treating an AI-generated response as an unquestionable decision.

---

# 🔐 Security & Responsible AI Considerations

The project was designed with the principle that AI-generated architecture analysis should remain reviewable.

Important considerations include:

- Architecture standards are explicitly defined.
- Compliance results are broken down by individual standard.
- Evidence is included in the generated report.
- Violations are documented separately.
- Remediation recommendations are separated from compliance findings.
- Review limitations are explicitly recorded.
- The system is positioned as a proof of concept rather than a production governance authority.

These design choices help make the generated results easier for a human reviewer to inspect.

---

# 📈 Automation Value

Traditional architecture compliance review can involve a repetitive process:

Read Proposal
↓
Review Standards
↓
Evaluate Compliance
↓
Document Evidence
↓
Identify Violations
↓
Recommend Remediation
↓
Create Review Report

ArchiGuard AI demonstrates how these activities can be combined into an automated workflow:

Architecture Proposal
↓
Automated Processing
↓
AI-Assisted Analysis
↓
Compliance Evaluation
↓
Structured Findings
↓
Automated Compliance Report

The result is a repeatable approach to architecture compliance analysis and documentation.

---

# 🧠 Engineering Skills Demonstrated

This project provided practical experience with:

- Python application development
- Generative-AI integration
- Google Gemini API integration
- API-based application workflows
- Prompt engineering
- Structured AI outputs
- Compliance evaluation
- Enterprise technology standards
- Architecture governance concepts
- Automated documentation
- Markdown report generation
- File processing
- Error and retry handling
- Streamlit application development
- Git/GitHub project organization

---

# 🎓 Learning Outcomes

Through this project, I developed a stronger understanding of how artificial intelligence can be applied to enterprise technology workflows.

## 1. Integrating Generative AI into Applications

The project provided practical experience connecting a Python application to a generative-AI API and incorporating the resulting analysis into an automated workflow.

## 2. Designing Structured AI Workflows

Rather than treating generative AI as an isolated chatbot, the project uses AI as one component within a larger processing pipeline.

## 3. Applying AI to Enterprise Technology Problems

The project explores how generative AI can assist with architecture review, compliance analysis, and documentation.

## 4. Working with Technology Standards

Defining explicit standards creates a repeatable framework for evaluating architecture proposals.

## 5. Automating Technical Documentation

The project demonstrates how analysis results can be automatically transformed into consistent compliance reports.

## 6. Recognizing AI Limitations

Including review limitations reinforces the importance of human oversight when AI is used for governance-oriented analysis.

---

# 🔮 Future Enhancements

The current implementation is a Python-based proof of concept. Future development could expand the system into a broader enterprise architecture governance workflow.

Potential enhancements include:

- Integration with enterprise architecture repositories
- SharePoint-based document workflows
- Microsoft Teams notifications
- Microsoft Power Automate integration
- SAP LeanIX integration
- Additional enterprise technology standards
- Persistent compliance history
- Role-based access controls
- Architecture-review approval workflows
- More advanced evidence extraction
- Human-in-the-loop review
- Enterprise dashboards
- Production-grade deployment

These integrations are future enhancements and are not part of the current prototype implementation.

---

# 📌 Current Scope

ArchiGuard AI is a student-built proof of concept demonstrating AI-assisted enterprise architecture compliance analysis and automated documentation.

The current prototype operates on architecture proposal files and defined enterprise technology standards.

It is intended to demonstrate the underlying technical and architectural concepts rather than function as a production enterprise governance platform.

The compliance results should therefore be treated as AI-assisted analysis requiring appropriate human review.

---

# 💼 Why This Project Matters

Enterprise architecture teams must evaluate technology proposals against security, integration, resilience, identity, and governance requirements.

This project explores how generative AI and automation can assist with that process.

The broader concept is:

Analyze → Evaluate → Document → Review

ArchiGuard AI connects:

- Artificial intelligence
- Python development
- Enterprise architecture
- Technology governance
- Compliance analysis
- Automation
- Technical documentation

into a single practical project.

The project demonstrates how generative AI can be applied to a concrete enterprise technology problem rather than being used only for general-purpose question answering.

---

# 👩‍💻 Author

Inaya Shahid

Information Technology Student | AI & Cybersecurity Enthusiast

Interested in:

- Artificial Intelligence
- Enterprise Technology
- Cybersecurity
- Software Engineering
- Secure Computing
- Emerging Technologies

---

# 🙏 Acknowledgements

This project was developed as part of my independent technical portfolio development and exploration of AI-assisted enterprise technology workflows.

The project combines concepts from software development, artificial intelligence, cybersecurity, enterprise architecture, technology governance, and workflow automation.

🔗 Project Resources

Live Application:
https://inayasf01-glitch-hands-on-projects-aiarchiguard-aiapp-dctb0e.streamlit.app/


Video Evidence:

https://github.com/user-attachments/assets/5e7d0b8c-6fee-4f71-a44b-edcad4083b6a

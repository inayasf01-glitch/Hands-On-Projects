# ArchiGuard AI

## Automated Enterprise Architecture Compliance Auditor

ArchiGuard AI is a Python-based proof-of-concept that uses generative AI to evaluate unstructured technology architecture proposals against defined enterprise technology standards.

The system produces structured compliance reports containing:

- Overall compliance status
- Standard-by-standard evaluation
- Evidence from the architecture proposal
- Compliance assessments
- Identified violations
- Remediation recommendations
- Review limitations

## Architecture

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

## Technology

- Python
- Google Gemini API
- google-genai
- python-dotenv
- Markdown
- Git/GitHub

## Enterprise Architecture Concepts

The project demonstrates:

- Architecture standards assessment
- Compliance evaluation
- Evidence-based analysis
- Exception / review handling
- Remediation recommendations
- Documentation automation
- Repeatable architecture review workflows

## Test Cases

### Proposal 01 — Compliant Architecture

Expected result:

PASSED

The proposal satisfies all five defined standards.

### Proposal 02 — Non-Compliant Architecture

Expected result:

FAILED

The proposal contains multiple violations and one area requiring additional review.

## Example Standards

The prototype evaluates:

1. Customer data encryption
2. Legacy database integration
3. Business continuity and disaster recovery
4. Centralized identity and access management
5. Security audit logging

## Project Purpose

This project demonstrates how AI and automation can reduce manual effort in architecture review by transforming unstructured proposals into consistent, documented compliance assessments.

It is a student-built proof of concept and does not represent a production enterprise governance system.


Video Evidence:

[ArchiGuard_AI_Demo_Final.zip](https://github.com/user-attachments/files/31927187/ArchiGuard_AI_Demo_Final.zip)

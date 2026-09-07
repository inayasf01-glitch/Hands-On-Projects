# Enterprise Technology Standards

## Purpose

These standards define baseline enterprise architecture controls used by ArchiGuard AI to evaluate technology proposals.

## Standard 1 — Customer Data Encryption

Customer data must be encrypted using AES-256 or an equivalent strong encryption standard when stored at rest.

**Control:** Encryption at rest  
**Required technology:** AES-256 or equivalent

## Standard 2 — Legacy Database Integration

Applications integrating with legacy databases must use secure REST APIs or an approved service-based integration layer.

Direct database connections from application systems are not permitted.

**Control:** API-based integration  
**Required approach:** Secure REST API or approved service layer

## Standard 3 — Business Continuity and Disaster Recovery

Critical cloud applications must support multi-region recovery to reduce the impact of regional infrastructure failures.

**Control:** Multi-region resilience  
**Required capability:** Multi-region recovery

## Standard 4 — Centralized Identity and Access Management

Enterprise applications must use centralized identity management with role-based access control (RBAC).

Local application accounts should not be used as the primary enterprise authentication mechanism.

**Control:** Centralized IAM  
**Required capability:** Centralized identity + RBAC

## Standard 5 — Security Audit Logging

Applications handling sensitive or customer data must maintain centralized audit logs for security-relevant activity.

**Control:** Security audit logging  
**Required capability:** Centralized audit logging
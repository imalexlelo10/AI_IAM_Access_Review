# AI + IAM Access Review

## Project Overview

I built this project to explore the integration of artificial intelligence with Identity and Access Management (IAM) by analyzing employee identity and access data within an organizational environment. The current Python-based audit engine verifies approved security group assignments, checks employee and account statuses, and identifies potential IAM issues without automatically making changes to user accounts.

The next phase of the project will integrate AI to analyze the structured audit findings, explain identified risks, and recommend appropriate remediation actions for review.

## Problem

Manually reviewing each user's role-based access and account status can become time-consuming as an organization grows. Administrators may need to verify whether employees have the appropriate security group assignments, whether their accounts match their current employment status, and whether any access issues require further investigation.

This project simplifies that process by analyzing employee identity and access data and providing administrators with visibility into the current IAM environment. Instead of individually reviewing every user, the tool identifies access violations, unknown roles, account lifecycle violations, and accounts requiring additional review. This allows administrators to focus their attention on potential IAM risks while keeping remediation decisions under human control.

## Technologies & Concepts

* **Python** — Used to build the access review and account lifecycle audit logic.
* **CSV** — Stores simulated employee identity, role, security group, employment, and account data.
* **Identity and Access Management (IAM)** — Provides the overall framework for reviewing identities and access.
* **Role-Based Access Control (RBAC)** — Compares employee job roles against approved security group assignments.
* **Joiner-Mover-Leaver (JML)** — Used to evaluate identity lifecycle conditions, including terminated and on-leave employees.
* **Git & GitHub** — Used for version control, project documentation, and maintaining the project repository.
* **Artificial Intelligence (AI) — In Progress** — Planned to analyze structured IAM findings, explain security risks, and recommend remediation actions while leaving final decisions to an administrator.

## Current Features

* Reviews employee account and employment status to identify potential identity lifecycle issues.
* Compares employee security group assignments against approved role-based access policies.
* Detects employees whose assigned security group does not match the access required for their job role.
* Identifies job roles that do not currently have an approved access policy defined.
* Flags terminated employees whose accounts remain active.
* Identifies account conditions that require additional review, such as employees who are on leave.
* Categorizes detected issues as **Access Violations, Account Violations, Account Reviews, or Unknown Roles**.
* Tracks the total number of access violations, unknown roles, account violations, and accounts requiring review.
* Stores identified issues as structured findings for future AI-assisted analysis and reporting.

## How It Works

1. **Load Employee Data** — The program reads employee identity and access information from a CSV file, including job role, security group, employment status, and account status.

2. **Evaluate Role-Based Access** — The employee's job role is compared against the approved access policy to determine which security group the employee should be assigned to. The approved group is then compared with the employee's actual security group.

3. **Identify Access Issues** — If the assigned security group does not match the approved group for the employee's role, the program flags the employee with an **Access Violation**. If no access policy exists for the job role, the employee is categorized as an **Unknown Role**.

## How It Works

1. **Load Employee Data** — The program reads employee identity and access information from a CSV file, including job role, security group, employment status, and account status.

2. **Evaluate Role-Based Access** — The employee's job role is compared against the approved access policy to determine which security group the employee should be assigned to. The approved group is then compared with the employee's actual security group.

3. **Identify Access Issues** — If the assigned security group does not match the approved group for the employee's role, the program flags the employee with an **Access Violation**. If no access policy exists for the job role, the employee is categorized as an **Unknown Role**.

4. **Evaluate Account Lifecycle Status** — After reviewing role-based access, the program compares the employee's employment status with their account status to identify potential identity lifecycle issues.

   * **Terminated + Active:** A terminated employee still has an active account. This is treated as an **Account Violation** because access may remain available after the employee has left the organization.
   * **Active + Disabled:** The employee is still actively employed, but the account is disabled. This is marked for **Account Review** because the condition may be intentional or may indicate an account provisioning or administrative issue.
   * **On Leave:** An employee on leave is marked for **Account Review** because their required level of access may depend on the organization's access and leave policies.

5. **Categorize the Findings** — The program separates findings into categories rather than assuming every unusual condition represents the same security problem. This provides administrators with more context when investigating potential access-control and identity lifecycle issues.

6. **Preserve Human Review** — The program identifies and categorizes potential issues without automatically changing account permissions or statuses. The findings provide information that an administrator can use to investigate the situation and determine the appropriate remediation.

## Example Findings

The audit engine produces structured findings that help distinguish between role-based access issues and identity lifecycle issues.

### Daniel Carter — Account Violation

* **Employment Status:** Terminated
* **Account Status:** Active
* **RBAC Check:** Pass
* **Finding:** Account Violation

Daniel's assigned security group correctly matches the approved access for his job role, allowing him to pass the RBAC check. However, his employment status is recorded as terminated while his account remains active. This creates a potential identity lifecycle security risk because an account may remain accessible after an employee has left the organization.

Before taking action, an IAM administrator should verify Daniel's employment status against the organization's authoritative identity or HR records and determine whether there is an approved reason for the account to remain active. If the active account is not authorized, the administrator could then follow the organization's offboarding procedures.

### Maya Johnson — Account Review

* **Employment Status:** On Leave
* **Account Status:** Disabled
* **RBAC Check:** Pass
* **Finding:** Account Review

Maya's assigned security group correctly matches the approved access for her role. However, her employment status indicates that she is currently on leave while her account is disabled.

This condition is categorized as an **Account Review** rather than an Account Violation because the disabled account may be intentional based on organizational policy. Before making changes, an IAM administrator should verify Maya's official leave status, review the organization's access policies for employees on leave, and determine whether the disabled account is appropriate for her current status.

### Sheryl Brown — Access Violation

* **Job Role:** HR Specialist
* **Expected Group:** GG_HR_Specialists
* **Actual Group:** GG_Finance_Analysts
* **Finding:** Access Violation

Sheryl is identified as an Access Violation because her assigned security group does not match the approved security group defined for her job role. As an HR Specialist, the current access policy expects her to belong to `GG_HR_Specialists`, while her actual assignment is `GG_Finance_Analysts`.

This mismatch could indicate unnecessary or unauthorized access and potentially conflict with the principle of least privilege. However, the finding should be investigated before access is changed. An IAM administrator should verify Sheryl's current responsibilities and approved access requirements to determine whether the Finance access is unauthorized or whether the organization's access policy needs to account for an approved exception.


## Project Structure

```text
AI-IAM-Access-Review/
│
├── data/
│   └── employees.csv
│
├── src/
│   ├── access_review.py
│   └── ai_analyzer.py        # Planned AI analysis component
│
├── reports/                  # Future generated audit reports
│
├── screenshots/              # Project output and demonstration images
│
├── README.md
└── .gitignore
```

### Component Responsibilities

* **`employees.csv`** — Stores simulated employee identity and access data, including job roles, security groups, employment statuses, and account statuses.
* **`access_review.py`** — Serves as the rules-based IAM audit engine. It reads employee data, compares assigned access against approved RBAC policies, evaluates account lifecycle conditions, and produces structured findings.
* **`ai_analyzer.py`** — Planned AI analysis component that will receive structured findings from the audit engine and provide additional risk explanations and remediation recommendations.
* **`reports/`** — Will contain generated access review and audit reports.
* **`screenshots/`** — Contains visual evidence of project execution and audit results.

Separating the audit engine from the AI analysis component keeps each part of the application focused on a specific responsibility. The Python audit engine determines what conditions were detected based on defined rules, while the AI component will provide additional context and analysis of those findings.

## Future Development

The next phase of this project will integrate an AI analysis component that evaluates the structured findings produced by the rules-based IAM audit engine.

The AI component is planned to:

* Explain why a detected IAM finding may represent a security or access-management risk.
* Recommend what an IAM administrator should investigate based on the available evidence.
* Provide contextual feedback for access violations, account lifecycle issues, unknown roles, and accounts requiring review.
* Suggest possible remediation steps while keeping the final decision with the administrator.
* Convert technical findings into clearer information that can support security auditing and access reviews.

The AI component will not automatically modify employee accounts, security groups, or permissions. Its purpose is to assist the administrator with understanding and investigating findings before any access changes are made.

A future reporting component will organize the audit findings and AI-generated analysis into a readable access review report.

## What I Learned

Building this project helped me better understand both Python programming and Identity and Access Management concepts. One of the biggest programming lessons I learned was the importance of proper indentation. During development, incorrect indentation caused some of my account lifecycle checks to execute incorrectly, which helped me understand how indentation determines the scope and execution flow of Python code.

I also gained more experience with Python syntax, variable naming, dictionaries, lists, conditional statements, and working with data from CSV files. Debugging errors throughout the project helped me become more comfortable identifying where a problem is occurring instead of only focusing on the final output.

From an IAM perspective, I developed a better understanding of how **Role-Based Access Control (RBAC)** and **Joiner-Mover-Leaver (JML)** processes apply to real access-management situations. I learned that having the correct security group does not necessarily mean an identity is completely secure. An employee can pass an RBAC check while still having an account lifecycle issue, such as a terminated employee retaining an active account.

Most importantly, I learned that an IAM finding should provide evidence for further investigation rather than automatically lead to an access change. Understanding the context surrounding an identity is important before making changes to accounts or permissions.

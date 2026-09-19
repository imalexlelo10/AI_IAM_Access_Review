import csv
from pathlib import Path

approved_access = {
    "IT Support Specialist": "GG_IT_Support",
    "HR Specialist": "GG_HR_Specialists",
    "HR Lead": "GG_HR_Specialists",
    "Financial Analyst": "GG_Finance_Analysts"
}

project_folder = Path(__file__).resolve().parent.parent
csv_file = project_folder / "data" / "employees.csv"

print("Project folder:", project_folder)
print("CSV path:", csv_file)
print("CSV exists:", csv_file.exists())

with open(csv_file, newline="") as file:
    reader = csv.DictReader(file)

    flagged_employees = 0
    unknown_roles = 0
    account_violations = 0
    review_needed = 0
    findings = []
    

    for employee in reader:
        job_role = employee["job_role"]
        actual_group = employee["security_groups"]
        employment_status = employee["employment_status"]
        account_status = employee["account_status"]
        print("Employment status:", employee["employment_status"])
        print("Account status:", employee["account_status"])

        expected_group = approved_access.get(job_role)

        print(employee["name"])

        if expected_group is None:
            print("Expected: No policy defined")
            print("Actual:", actual_group)
            print("Status: UNKNOWN ROLE")
            unknown_roles = unknown_roles + 1

            finding = {
                "employee": employee["name"],
                "finding_type": "Unknown Role",
                "actual_group": actual_group
            }

            findings.append(finding)

        elif actual_group == expected_group:
            print("Expected:", expected_group)
            print("Actual:", actual_group)
            print("Status: PASS")

        else:
            print("Status: FLAGGED")
            print("Reason: Role requires", expected_group, "but found", actual_group)
            flagged_employees = flagged_employees + 1

            finding = {
                "employee": employee["name"],
                "finding_type": "Access Violation",
                "expected_group": expected_group,
                "actual_group": actual_group
            }

            findings.append(finding)
            
        if employment_status == "Terminated" and account_status == "Active":
                print("Account Status: FLAGGED")
                print("Reason: Terminated employee still has an active account")
                account_violations = account_violations + 1

                finding = {
                    "employee": employee["name"],
                    "finding_type": "Account Violation",
                    "employment_status": "Terminated",
                    "account_status": "Active"
                }

                findings.append(finding)

        elif employment_status == "Active" and account_status == "Disabled":
                print("Account Status: REVIEW NEEDED")
                print("Reason: Active employee has a disabled account")
                review_needed = review_needed + 1

                finding = {
                    "employee": employee["name"],
                    "finding_type": "Account Review",
                    "employment_status": "Active",
                    "account_status": "Disabled"
                }

                findings.append(finding)

        elif employment_status == "On Leave":
                print("Account Status: REVIEW NEEDED")
                print("Reason: Employee is assigned as ON LEAVE")
                review_needed = review_needed + 1

                finding = {
                    "employee": employee["name"],
                    "finding_type": "Account Review",
                    "employment_status": employment_status,
                    "account_status": account_status
                }

                findings.append(finding)

        else:
                print("Account Status: PASS")

print("Access Violations: ",flagged_employees)
print("Unknown roles: ",unknown_roles)
print("Account violations: ",account_violations)
print("Accounts needing review: ",review_needed)
print(findings)

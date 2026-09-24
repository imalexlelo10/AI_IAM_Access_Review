
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


def run_access_review():

    flagged_employees = 0
    unknown_roles = 0
    account_violations = 0
    review_needed = 0
    findings = []

    print("\n" + "=" * 60)
    print("AI + IAM ACCESS REVIEW")
    print("=" * 60)

    print("\nProject Information")
    print("-" * 60)
    print("Project folder:", project_folder)
    print("CSV path:", csv_file)
    print("CSV exists:", csv_file.exists())

    print("\n" + "=" * 60)
    print("[1] EMPLOYEE ACCESS AUDIT")
    print("=" * 60)

    with open(csv_file, newline="") as file:
        reader = csv.DictReader(file)

        for employee in reader:
            job_role = employee["job_role"]
            actual_group = employee["security_groups"]
            employment_status = employee["employment_status"]
            account_status = employee["account_status"]

            expected_group = approved_access.get(job_role)

            print("\n" + "-" * 60)
            print(f"Employee: {employee['name']}")
            print("-" * 60)

            print(f"Job Role: {job_role}")
            print(f"Employment Status: {employment_status}")
            print(f"Account Status: {account_status}")

            # RBAC ACCESS REVIEW
            print("\nAccess Review:")

            if expected_group is None:
                print("Expected Group: No policy defined")
                print(f"Actual Group: {actual_group}")
                print("Access Status: UNKNOWN ROLE")

                unknown_roles = unknown_roles + 1

                finding = {
                    "employee": employee["name"],
                    "finding_type": "Unknown Role",
                    "actual_group": actual_group
                }

                findings.append(finding)

            elif actual_group == expected_group:
                print(f"Expected Group: {expected_group}")
                print(f"Actual Group: {actual_group}")
                print("Access Status: PASS")

            else:
                print(f"Expected Group: {expected_group}")
                print(f"Actual Group: {actual_group}")
                print("Access Status: FLAGGED")
                print(
                    f"Reason: Role requires {expected_group} "
                    f"but found {actual_group}"
                )

                flagged_employees = flagged_employees + 1

                finding = {
                    "employee": employee["name"],
                    "finding_type": "Access Violation",
                    "expected_group": expected_group,
                    "actual_group": actual_group
                }

                findings.append(finding)

            # ACCOUNT LIFECYCLE REVIEW
            print("\nAccount Lifecycle Review:")

            if employment_status == "Terminated" and account_status == "Active":
                print("Lifecycle Status: FLAGGED")
                print(
                    "Reason: Terminated employee still has an active account"
                )

                account_violations = account_violations + 1

                finding = {
                    "employee": employee["name"],
                    "finding_type": "Account Violation",
                    "employment_status": employment_status,
                    "account_status": account_status
                }

                findings.append(finding)

            elif employment_status == "Active" and account_status == "Disabled":
                print("Lifecycle Status: REVIEW NEEDED")
                print(
                    "Reason: Active employee has a disabled account"
                )

                review_needed = review_needed + 1

                finding = {
                    "employee": employee["name"],
                    "finding_type": "Account Review",
                    "employment_status": employment_status,
                    "account_status": account_status
                }

                findings.append(finding)

            elif employment_status == "On Leave":
                print("Lifecycle Status: REVIEW NEEDED")
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
                print("Lifecycle Status: PASS")

    print("\n" + "=" * 60)
    print("[2] AUDIT SUMMARY")
    print("=" * 60)

    print(f"Access Violations:        {flagged_employees}")
    print(f"Unknown Roles:            {unknown_roles}")
    print(f"Account Violations:       {account_violations}")
    print(f"Accounts Needing Review:  {review_needed}")
    print(f"Total Findings:           {len(findings)}")

    return findings

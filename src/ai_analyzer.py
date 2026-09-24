from access_review import run_access_review


def analyze_finding(finding):
    finding_type = finding["finding_type"]
    employee = finding["employee"]

    print(f"Employee: {employee}")
    print(f"Finding Type: {finding_type}")

    if finding_type == "Account Violation":
        employment_status = finding["employment_status"]
        account_status = finding["account_status"]

        print(f"Employment Status: {employment_status}")
        print(f"Account Status: {account_status}")

        risk_level = "HIGH"
        print(f"Risk Level: {risk_level}")

        investigation = (
            "Verify the employee's employment status and account status."
        )
        print(f"Investigation: {investigation}")

        recommended_action = (
            "If termination is confirmed and no approved exception exists, "
            "disable the account and revoke access."
        )
        print(f"Recommended Action: {recommended_action}")

    elif finding_type == "Access Violation":
        expected_group = finding["expected_group"]
        actual_group = finding["actual_group"]

        print(f"Expected Group: {expected_group}")
        print(f"Actual Group: {actual_group}")

        risk_level = "MEDIUM"
        print(f"Risk Level: {risk_level}")

        investigation = (
            "Verify if the employee has approved access to the different "
            "security group."
        )
        print(f"Investigation: {investigation}")

        recommended_action = (
            "If the employee's access to the different security group is "
            "not approved, remove the employee from the unauthorized group."
        )
        print(f"Recommended Action: {recommended_action}")

    elif finding_type == "Account Review":
        employment_status = finding["employment_status"]
        account_status = finding["account_status"]

        print(f"Employment Status: {employment_status}")
        print(f"Account Status: {account_status}")

        risk_level = "LOW"
        print(f"Risk Level: {risk_level}")

        investigation = (
            "Verify the employee's employment status and account status."
        )
        print(f"Investigation: {investigation}")

        recommended_action = (
            "If the employee's On Leave status is confirmed, keep the "
            "account disabled according to organizational policy. If the "
            "status is incorrect, verify the employee's current employment "
            "status before changing account access."
        )
        print(f"Recommended Action: {recommended_action}")

    elif finding_type == "Unknown Role":
        actual_group = finding["actual_group"]

        print(f"Actual Group: {actual_group}")

        risk_level = "MEDIUM"
        print(f"Risk Level: {risk_level}")

        investigation = (
            "Verify the employee's official job role and whether the "
            "assigned security group is authorized for that role."
        )
        print(f"Investigation: {investigation}")

        recommended_action = (
            "If the employee's job role is confirmed, verify the approved "
            "access policy and assign the appropriate security group. "
            "Remove unauthorized access only after verification."
        )
        print(f"Recommended Action: {recommended_action}")


findings = run_access_review()


print("\n" + "=" * 60)
print("[3] RISK ANALYSIS REPORT")
print("=" * 60)


for finding in findings:
    print("\n" + "-" * 60)
    analyze_finding(finding)


print("\n" + "=" * 60)
print("ACCESS REVIEW COMPLETE")
print("=" * 60)
print(f"Total Findings Analyzed: {len(findings)}")

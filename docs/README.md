```md id="jxm442"
# PDEO Cost Calculators

**Last Updated:** May 13, 2026

The PDEO Cost Calculators are a set of static HTML/CSS/JavaScript tools designed to support SHIP counselors in calculating the Original PDP/MA-PD Cost for specific enrollment scenarios.

The calculators align with STARS Manual guidance and are intended to reduce manual calculation effort by guiding users through scenario-specific cost calculations.

---

# Included Calculators

## 1. New to Medicare PDP/MA-PD  
### Prescriptions on a Consistent Non-30-Day Refill Schedule

Calculates Original PDP/MA-PD Cost using:
- Monthly Total
- Refill Frequency
- Coverage Months

---

## 2. New to Medicare PDP/MA-PD  
### Prescriptions on a Mixed Non-30-Day Refill Schedule

Calculates Original PDP/MA-PD Cost using:
- Multiple medications
- Individual retail costs
- Individual refill frequencies
- Aggregated totals

---

## 3. New to Medicare PDP/MA-PD (this year) and Switching PDP/MA-PD (next year)  
### Prescriptions on a 30-Day Refill Schedule

Calculates Original PDP/MA-PD Cost using:
- New to Medicare PDP/MA-PD Plan Details (current year)
- Current PDP/MA-PD Plan Details for Next Year
- Combined cost calculations

---

# Design Approach

These calculators are designed as guided tools rather than full instructional resources.

Current design goals include:
- Reducing cognitive load
- Using consistent layouts and interaction patterns
- Supporting mobile-friendly use
- Providing clear cost breakdowns after calculation
- Supporting scenario-based workflows

Scenario applicability guidance is provided on the calculator index page.

---

# Implemented Features

Current implemented features include:
- Branded headers and navigation
- Tooltip guidance for Plan Details usage
- “Back to Calculators” navigation
- “Start Over” reset functionality
- Cost breakdown sections
- Input validation and error messaging
- Consistent UI/UX patterns across calculators

---

# Technical Structure

- Static HTML/CSS/JavaScript implementation
- No backend or server-side processing
- Tailwind CSS used for styling
- Standalone calculator pages
- Responsive layouts for desktop and mobile use

---

# Accessibility Work

Current accessibility considerations include:
- Proper heading structure
- Labels associated with form inputs
- Keyboard-accessible interactive elements
- Responsive layouts and zoom support
- Validation messaging
- Color contrast considerations
- Screen reader support through live regions and descriptive labeling

---

# Workflow

Typical workflow:

1. Edit and test calculators in VS Code
2. Commit changes through Git
3. Push updates to GitHub
4. Review functionality and usability in the development environment

---

# Development Notes

Current development priorities include:
1. Accessibility review and testing
2. Calculator accuracy validation
3. Mobile usability testing
4. Branding consistency review
5. Stakeholder review and feedback

Feedback and enhancement notes are tracked separately within the repository.

---

# Deployment Notes

The calculators are currently hosted in a development/testing environment using GitHub Pages.

Future deployment considerations include:
- URL structure
- Hosting approach
- Accessibility from work environments
- Organizational review requirements
- Ongoing maintenance processes

---

# Disclaimer

This project is supported by the Administration for Community Living (ACL), U.S. Department of Health and Human Services (HHS) as part of a financial assistance award totaling $3,000,000 with 100% funding by ACL/HHS. The contents are those of the author(s) and do not necessarily represent the official views of, nor an endorsement, by ACL/HHS or the U.S. government.
```

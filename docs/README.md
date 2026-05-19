# SHIP Interactive Tools

**Last Updated:** May 19, 2026

SHIP Interactive Tools is a collection of static HTML/CSS/JavaScript web apps designed to support common SHIP and STARS workflows through guided, task-focused interactive resources.

The current project includes PDEO cost calculation web apps, STARS troubleshooting tools, and interactive STARS reference tools.

---

# Current Web Apps

## PDEO Cost Calculators

A collection of guided web apps that support SHIP counselors in calculating Original PDP/MA-PD Cost for specific enrollment scenarios.

### Included PDEO Calculators

#### 1. New to Medicare PDP/MA-PD  
##### Prescriptions on a Consistent Non-30-Day Refill Schedule

Calculates Original PDP/MA-PD Cost using:
- Monthly Total
- Refill Frequency
- Coverage Months

#### 2. New to Medicare PDP/MA-PD  
##### Prescriptions on a Mixed Non-30-Day Refill Schedule

Calculates Original PDP/MA-PD Cost using:
- Multiple medications
- Individual retail costs
- Individual refill frequencies
- Aggregated totals

#### 3. New to Medicare PDP/MA-PD (this year) and Switching PDP/MA-PD (next year)  
##### Prescriptions on a 30-Day Refill Schedule

Calculates Original PDP/MA-PD Cost using:
- New to Medicare PDP/MA-PD Plan Details (current year)
- Current PDP/MA-PD Plan Details for Next Year
- Combined cost calculations

---

## STARS Login Troubleshooter

An interactive troubleshooting web app that helps users identify and resolve common STARS login, account setup, and access issues through guided questions and scenario-based troubleshooting paths.

---

## STARS User Role Explorer

An interactive reference web app that helps users understand STARS user roles, permissions, and hierarchy visibility through searchable and guided role exploration.

---

# Design Approach

These web apps are designed as guided tools rather than full instructional resources.

Current design goals include:
- Reducing cognitive load
- Using consistent layouts and interaction patterns
- Supporting mobile-friendly use
- Providing guided workflows
- Supporting scenario-based tasks
- Maintaining consistent branding and navigation patterns

---

# Technical Structure

- Static HTML/CSS/JavaScript implementation
- No backend or server-side processing
- No stored user data
- Tailwind CSS used for styling
- Standalone responsive web apps
- Shared branding/assets across tools

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

1. Edit and test web apps in VS Code
2. Commit changes through Git
3. Push updates to GitHub
4. Review functionality and usability in the development environment

---

# Development Notes

Current development priorities include:
1. Accessibility review and testing
2. Mobile usability testing
3. Branding consistency review
4. Stakeholder review and feedback
5. Deployment and rollout planning

Feedback and enhancement notes are tracked separately within the repository.

---

# Deployment Notes

The web apps are currently hosted in a development/testing environment using GitHub Pages.

Current deployment planning includes:
- SHIP-owned subdomain routing
- Resource Library and Toolbox access points
- Partial rollout testing with selected SHIP networks
- ACL review and approval processes
- Ongoing maintenance and update workflows

---

# Disclaimer

This project is supported by the Administration for Community Living (ACL), U.S. Department of Health and Human Services (HHS) as part of a financial assistance award totaling $3,000,000 with 100% funding by ACL/HHS. The contents are those of the author(s) and do not necessarily represent the official views of, nor an endorsement, by ACL/HHS or the U.S. government.
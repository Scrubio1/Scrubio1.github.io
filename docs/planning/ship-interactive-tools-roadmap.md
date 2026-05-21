# SHIP Interactive User Tools Roadmap

## Overview

The SHIP Interactive User Tools project is a growing collection of lightweight static web applications designed to support SHIP counselors, leaders, and staff with common workflows, calculations, and STARS-related tasks.

The tools are designed to:
- Reduce cognitive load
- Improve usability for common tasks
- Support mobile-friendly access
- Provide focused, task-oriented interactions
- Reduce manual calculations and repetitive troubleshooting steps
- Support rapid updates as ACL/STARS guidance evolves

The tools are maintained as static HTML/CSS/JavaScript applications hosted through GitHub Pages.

---

# Current Web Apps

## PDEO Tools

The PDEO Tools currently include calculators that support Original PDP/MA-PD Cost calculations for specific enrollment scenarios aligned with the STARS Manual.

Current calculators include:

### 1. New to Medicare PDP/MA-PD  
#### Prescriptions on a Consistent Non-30-Day Refill Schedule

Calculates Original PDP/MA-PD Cost using:
- Monthly Total
- Refill Frequency
- Coverage Months

---

### 2. New to Medicare PDP/MA-PD  
#### Prescriptions on a Mixed Non-30-Day Refill Schedule

Calculates Original PDP/MA-PD Cost using:
- Multiple medications
- Individual retail costs
- Individual refill frequencies
- Aggregated totals

---

### 3. New to Medicare PDP/MA-PD (this year) and Switching PDP/MA-PD (next year)  
#### Prescriptions on a 30-Day Refill Schedule

Calculates Original PDP/MA-PD Cost using:
- New to Medicare PDP/MA-PD Plan Details (current year)
- Current PDP/MA-PD Plan Details for next year
- Combined cost calculations

Future PDEO tools may also include:
- Scenario explainers
- Workflow support tools
- Reference utilities

---

## STARS Login Troubleshooter

An interactive troubleshooting tool that guides users through common STARS login and access issues including:
- Username problems
- Password issues
- Account lockouts
- MFA verification issues

The tool is designed to reduce confusion and help users identify the appropriate next step before escalating issues.

---

## STARS User Role Explorer

An interactive reference tool showing:
- STARS role capabilities
- Menu visibility
- Access limitations
- Hierarchy relationships

The tool simulates portions of the STARS navigation experience while simplifying role comparison and explanation.

---

# Design and UX Principles

The web apps are designed as focused utility tools rather than full instructional resources.

Current design principles include:
- Reduce cognitive load
- Minimize unnecessary navigation
- Use consistent layouts and interaction patterns
- Support responsive/mobile-friendly use
- Use clear and concise language
- Support older adult users and varied technical comfort levels
- Maintain visual consistency across apps
- Keep interactions task-oriented and easy to complete

---

# Technical Architecture

## Hosting

- Static HTML/CSS/JavaScript implementation
- Hosted through GitHub Pages
- No backend or server-side processing
- No database or stored user data

## Repository Structure

The apps are maintained within the `SHIP-Tools` repository.

Current structure includes:
- Shared assets/images
- Shared snippets/templates
- Planning and architecture documentation
- Individual application folders

## Shared Components

Shared standards currently include:
- Branding
- Logo behavior
- Disclaimer language
- Accessibility considerations
- Responsive layout patterns

---

# Accessibility and QA

Accessibility and usability considerations include:

## Accessibility

- Proper heading structure
- Labels associated with form inputs
- Keyboard-accessible interactions
- Visible focus indicators
- Responsive layouts and zoom support
- WCAG color contrast considerations
- Descriptive alt text
- Screen-reader-friendly structure

## QA and Testing

Current testing methods include:
- Lighthouse testing
- Manual keyboard testing
- Manual mobile testing
- Responsive layout testing
- Link/path validation
- Functional workflow testing

Testing currently includes:
- Desktop browsers
- Android mobile devices
- Additional Apple/iOS testing as available

---

# Deployment Model

The current deployment model is:

- Tools hosted externally through GitHub Pages
- Discovery and role-based visibility managed through the SHIP TA portal
- Tools opened in new browser tabs rather than embedded portal views
- Planned use of a custom subdomain for production access
- Portal links removable independently from the hosted applications

This model supports:
- Rapid updates
- Independent tool expansion
- Lightweight maintenance
- Reduced portal deployment dependencies

---

# Analytics and Evaluation

The project currently uses Plausible Analytics for lightweight, privacy-friendly usage tracking.

Current goals include understanding:
- Landing page visits
- Most-used tools
- Mobile vs. desktop usage
- General usage trends
- Repeat visits and adoption patterns

The analytics implementation:
- Does not collect beneficiary information
- Does not require user accounts
- Uses minimal tracking infrastructure

Analytics may help support:
- Future project planning
- Prioritization decisions
- Usage evaluation
- Grant reporting discussions

---

# Governance and Maintenance

The tools are intended to support ongoing updates as ACL/STARS guidance changes.

Current maintenance principles include:
- Stable URL structures when possible
- Shared branding standards
- Consistent disclaimer language
- Centralized asset management
- Version-controlled updates through GitHub

Updates can be deployed independently without requiring full portal release cycles.

---

# Future Expansion

Future development may include:
- Additional PDEO utilities
- Additional STARS support tools
- Workflow support web apps
- Expanded interactive references
- Additional mobile-focused utilities

The project structure is intended to support gradual expansion over time while maintaining consistency across apps.

---

# Disclaimer

This project is supported by the Administration for Community Living (ACL), U.S. Department of Health and Human Services (HHS) as part of a financial assistance award totaling $1,500,000 with 100% funding by ACL/HHS. The contents are those of the author(s) and do not necessarily represent the official views of, nor an endorsement, by ACL/HHS or the U.S. government.
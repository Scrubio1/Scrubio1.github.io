# PDEO Calculators Roadmap

## Overview

The PDEO Calculators are a set of lightweight, static tools designed to support SHIP counselors in calculating the Original PDP/MA-PD Cost for specific enrollment scenarios.

Each calculator aligns with the STARS Manual and is designed to reduce cognitive load by guiding users through the calculation process without requiring manual math.

---

## Calculators Included

### 1. New to Medicare PDP/MA-PD  
**Prescriptions on a Consistent Non-30-Day Refill Schedule**  
- Calculates Original PDP/MA-PD Cost using:
  - Monthly Total
  - Refill Frequency
  - Coverage Months

---

### 2. New to Medicare PDP/MA-PD  
**Prescriptions on a Mixed Non-30-Day Refill Schedule**  
- Calculates Original PDP/MA-PD Cost using:
  - Multiple medications
  - Individual retail costs
  - Individual refill frequencies
  - Aggregated total

---

### 3. New to Medicare PDP/MA-PD (this year) and Switching PDP/MA-PD (next year)  
**Prescriptions on a 30-Day Refill Schedule**  
- Calculates Original PDP/MA-PD Cost using:
  - New to Medicare PDP/MA-PD Plan Details (this year)
  - Current PDP/MA-PD Plan Details for Next Year
  - Combined cost calculation

---

## Design Approach

These calculators are designed as **guided tools**, not full instructional resources.

- Scenario applicability guidance is provided on the index page
- Users are expected to reference Plan Details from the Medicare Plan Finder (MPF)
- Each calculator performs a single calculation: **Original PDP/MA-PD Cost**
- Calculations follow the steps outlined in the STARS Manual

### UX Principles

- Minimize cognitive load
- Reduce unnecessary text
- Use consistent layout and interaction patterns
- Provide clear cost breakdowns after calculation
- Support mobile-friendly use

---

## Current State

- All calculators are implemented as static HTML/CSS/JavaScript tools
- No backend or server-side processing is required
- Tools are accessible as standalone pages in a development environment

### Implemented Features

- Branded headers (title + subtitle)
- Tooltip guidance for Plan Details usage
- “Back to Calculators” navigation
- “Start Over” reset functionality
- Cost breakdown revealed after calculation
- Input validation and error messaging
- Consistent UI/UX across all calculators

### Structure

Each calculator includes:
- Coverage Period section (where applicable)
- Input fields specific to the scenario
- Calculate button
- Cost breakdown output section

---

## Accessibility / Section 508 Work

### Structure
- Use proper heading order
- Ensure all instructions are real HTML text
- Group related form fields logically
- Use labels for all inputs

### Keyboard Access
- All elements must be keyboard accessible
- Logical focus order
- Interactive elements must support keyboard use

### Screen Reader Support
- Associate labels with inputs
- Announce calculation results
- Provide clear, descriptive error messaging

### Visual Accessibility
- Ensure sufficient color contrast
- Avoid relying on color alone for meaning
- Support zoom and responsive layouts

### Forms and Validation
- Clearly identify required fields
- Provide understandable validation messages
- Avoid ambiguous field names

---

## Content Decisions

- Scenario explanation is handled on the index page, not within each calculator
- Plan Details naming follows STARS Manual language exactly
- Calculators do not replicate full workflow instructions
- Focus remains on completing the Original PDP/MA-PD Cost calculation step

---

## Next Development Priorities

1. Conduct accessibility (Section 508) review  
2. Test calculators for accuracy using sample Plan Details  
3. Validate mobile usability and layout  
4. Confirm branding consistency across index and calculator pages  
5. Prepare for stakeholder review and feedback  

---

## Deployment and Hosting Considerations

The calculators are currently hosted in a development/testing environment (GitHub Pages).

Final deployment will require coordination with developers and IT.

### Key Decisions

- Hosting approach:
  - Standalone URL (e.g., dedicated tool access)
  - Subdomain (e.g., `pdeo.shiphelp.org`)
  - Integration within shiphelp.com

- Domain and URL structure
- Accessibility from work environments and external networks
- Alignment with organizational standards for:
  - Disclaimers
  - Copyright
- Ongoing maintenance and update process

These decisions will determine how the calculators are made available to SHIP counselors.

---

## Required Disclaimer Text

This project is supported by the Administration for Community Living (ACL), U.S. Department of Health and Human Services (HHS) as part of a financial assistance award totaling $3,000,000 with 100% funding by ACL/HHS. The contents are those of the author(s) and do not necessarily represent the official views of, nor an endorsement, by ACL/HHS or the U.S. government.

---

## Notes

The PDEO Calculators are designed to function as a cohesive set of tools that align with the STARS Manual while improving usability and reducing manual calculation effort for SHIP counselors.
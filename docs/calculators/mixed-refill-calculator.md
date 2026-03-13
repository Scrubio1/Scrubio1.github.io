# Calculator Roadmap

## Tool
**Name:** PDEO New to Medicare PDP/MA-PD (Prescriptions on a Mixed Refill Schedule) Original PDP/MA-PD Cost Calculator



## Purpose
This calculator helps users quickly calculate the Original PDP/MA-PD Cost for a New to Medicare PDP/MA-PD enrollment scenario when all prescriptions follow a mixed refill schedule and that schedule is not 30 days.

## Current State
- Calculator logic exists in `index.html`
- Tool can be opened as a standalone HTML page
- Supporting context and usage guidance currently live on the library/resource page rather than fully inside the tool
- Accessibility/508 review is still needed

## Standalone Content Still Needed
The calculator should be understandable and usable without relying on the Resource Library page.

### Add scenario explanation
Include a section that explains when this calculator applies:
- The person has no previous PDP/MA-PD coverage
- The person has previous non-Medicare drug coverage
- The beneficiary's plan is no longer available on the Medicare Plan Finder due to plan terminations, sanction, or moving to a new area/state

### Add "You will need" information
Include a section that explains required information:
- Plan Details for the plan the beneficiary is enrolling in

### Add built-in instructions
Include clear step-by-step instructions in the calculator itself:
1. Select the First Coverage Month
2. Find the monthly totals in the Retail Cost column on the Plan Details for the beneficiary's preferred pharmacy
3. Enter the monthly total amount in the Monthly Total field
4. Select the Refill Frequency
5. Review the autofilled Number of Refills field
6. Click the calculate button to see the total

### Add tips or follow-up guidance
Consider including brief guidance such as:
- Transfer the total to the BCF/BAS
- Use the related STARS Manual guidance for the full PDEO process
- Refresh the browser window to clear the calculator if needed

## Accessibility / Section 508 Work
### Structure
- Use proper heading order
- Ensure instructions are real text in HTML, not only visual design elements
- Group related form fields logically
- Use labels for all inputs
- Do not rely on placeholder text as the only label

### Keyboard access
- All fields and buttons must be reachable by keyboard only
- Focus order should be logical
- Any expandable or collapsible help content must work with keyboard controls

### Screen reader support
- Associate labels with inputs
- Make calculation results available to screen readers
- Use clear error messaging tied to the relevant field
- Ensure any helper text is programmatically associated where needed

### Visual accessibility
- Check color contrast
- Avoid conveying meaning by color alone
- Ensure text remains readable at zoom
- Make sure layout works well on different screen sizes

### Forms and error handling
- Clearly identify required fields
- Provide understandable validation messages
- Prevent ambiguous field names

## Content Questions / Decisions
- Decide whether tips should appear directly on the page or in a collapsible help section
- Decide whether result guidance should include a reminder about where to transfer the total
- Decide whether related resource links should be included in the tool or kept outside it

## Next Development Priorities
1. Add built-in scenario and instruction text to the page
2. Add semantic HTML labels and field grouping
3. Add accessible result and error messaging
4. Review keyboard-only use
5. Review color contrast and zoom behavior

### Required Disclaimer Text


This project is supported by the Administration for Community Living (ACL), U.S. Department of Health and Human Services (HHS) as part of a financial assistance award totaling $3,000,000 with 100% funding by ACL/HHS.  The contents are those of the author(s) and do not necessarily represent the official views of, nor an endorsement, by ACL/HHS or the U.S. government.


## Notes
This calculator is being revised so it can function as a true standalone tool rather than depending on explanatory text on the library page.
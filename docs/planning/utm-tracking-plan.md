# SHIP Interactive User Tools UTM Tracking Plan

## Purpose

This document outlines the planned use of UTM-tagged links for tracking adoption and usage patterns of the SHIP Interactive User Tools web apps using Plausible Analytics.

These links are intended to help identify:
- Which communication methods drive traffic to the tools
- Which outreach methods are most effective
- General adoption and usage trends over time

The tracking approach is intended to remain lightweight and privacy-friendly.

---

## URL Usage

The UTM text examples below are intended to be appended to the end of the landing page URL or individual web app URL being shared.

Example:

```text
https://tools.shiptacenter.org/pdeo-tools/?utm_source=toolbox&utm_medium=portal

---

## Deployment Timing

These UTM-tagged links should NOT be used until:
- Informatics confirms the final production URL/subdomain
- Full deployment is ready
- SHIP-facing outreach and promotion begin

Until then, standard development/testing URLs should continue to be used internally.

---

# Analytics Platform

Current analytics platform:
- Plausible Analytics

Purpose of analytics:
- Lightweight usage tracking
- Adoption monitoring
- Communication effectiveness tracking
- General project evaluation

The analytics implementation:
- Does not collect beneficiary information
- Does not require user accounts
- Uses privacy-friendly tracking methods

---

# Planned UTM Use Cases

Potential tracked communication/use cases include:
- Resource Library page entries
- Toolbox entries
- News Bulletins
- Constant Contact emails



---

# UTM Naming Standards

The following naming patterns are proposed to maintain consistent reporting within Plausible Analytics.

---

## Resource Library

```text
?utm_source=resource_library&utm_medium=portal
```

---

## Toolbox Entry

```text
?utm_source=toolbox&utm_medium=portal
```

---

## Constant Contact Email

```text
?utm_source=constant_contact&utm_medium=email
```

---

## Post Webinar

```text
?utm_source=post_webinar&utm_medium=email
```

---

## News Bulletin

```text
?utm_source=news_bulletin&utm_medium=email
```

---

## Other

```text
?utm_source=other&utm_medium=email
```

---

# Goals of UTM Tracking

Potential reporting and evaluation uses include:
- Understanding which outreach methods generate the most visits
- Monitoring adoption after communications or trainings
- Identifying which tools are most frequently accessed
- Supporting future planning and prioritization decisions
- Supporting grant/project reporting discussions

---

# Maintenance Notes

To maintain clean analytics reporting:
- UTM naming should remain consistent
- Existing naming conventions should be reused when possible
- New campaign names should avoid duplicate variations (example: `Toolbox` vs `toolbox`)

Tracked links can be prepared internally and provided to staff creating:
- Resource Library entries
- Toolbox pages
- Emails
- News Bulletins
- Other communications

This avoids requiring all staff to understand UTM formatting or analytics configuration.

---

# Future Considerations

Potential future additions may include:
- Tool-specific UTM links
- Campaign-specific tracking
- Event/training-specific links
- QR codes tied to tracked URLs
- Shared analytics dashboards for internal review
# Analytics Standards

## Purpose

This document defines the UTM naming conventions used for SHIP Interactive Tools.

Consistent UTM usage allows the SHIP Technical Assistance Center to understand how users discover and access interactive tools hosted at https://tools.shiptacenter.org.

---

# Webinar Resources

Used when links are provided through:

- Zoom Resource Panel
- Webinar Chat
- Webinar Q&A responses

Parameters:

```text
utm_source=zoom
utm_medium=webinar_resources
utm_campaign=[webinar_name]
```

Example:

```text
https://tools.shiptacenter.org/tool-name?utm_source=zoom&utm_medium=webinar_resources&utm_campaign=medicare_basics
```

---

# SHIPhelp Resource Library

Used when linking from Resource Library entries.

Parameters:

```text
utm_source=shiphelp
utm_medium=resource_library
utm_campaign=evergreen
```

Example:

```text
https://tools.shiptacenter.org/tool-name?utm_source=shiphelp&utm_medium=resource_library&utm_campaign=evergreen
```

---

# What's New Newsletter

Used when a direct tool link is included in the newsletter.

Parameters:

```text
utm_source=whatsnew
utm_medium=onlinenewsletter
utm_campaign=[article_purpose]
```

Example:

```text
https://tools.shiptacenter.org/tool-name?utm_source=whatsnew&utm_medium=onlinenewsletter&utm_campaign=pdeo_tools
```

---

# Constant Contact

Used when linking directly from email communications.

Parameters:

```text
utm_source=constantcontact
utm_medium=email
utm_campaign=evergreen
```

Example:

```text
https://tools.shiptacenter.org/tool-name?utm_source=constantcontact&utm_medium=email&utm_campaign=evergreen
```

---

# Naming Rules

- Use lowercase values.
- Use underscores instead of spaces.
- Use consistent campaign names when reporting across multiple communications.
- Avoid creating new source values unless necessary.
- Update this document whenever a new distribution channel is introduced.
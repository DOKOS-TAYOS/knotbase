# GitHub repository About settings

These values are intended for the **right-hand “About” panel** on the public [Knotbase repository](https://github.com/DOKOS-TAYOS/knotbase). This Markdown file documents the proposed settings but **does not itself change GitHub repository metadata**.

## Repository description

Copy this into **About → Edit → Description**:

> Portable, GitHub-backed knowledge and AI workflow instructions for ChatGPT Projects: private bootstrap, research, coding and writing.

The description is concise and makes it clear that the project distributes **instructions**, not a standalone model or a hosted AI service.

## Website

Suggested website/homepage URL (public getting-started guide):

```text
https://github.com/DOKOS-TAYOS/knotbase/blob/main/docs/GETTING_STARTED.md
```

Use this after the documentation PR is merged into `main`.

## Topics

Copy these **space-separated** topics into **About → Edit → Topics**:

```text
chatgpt chatgpt-projects ai-workflows knowledge-base personal-knowledge-management github-integration prompt-engineering ai-agents research-tools developer-tools markdown open-source
```

These describe the actual public instruction package without implying a guaranteed runtime, trained custom model, memory synchronization or a standalone SaaS platform.

## Apply in GitHub

1. Open the [Knotbase repository's main page](https://github.com/DOKOS-TAYOS/knotbase).
2. In the right-hand **About** panel, click the **gear icon / Edit**.
3. Paste the **description**, website and individual **topics** above.
4. Save and verify the values on the repository page.

GitHub metadata requires repository administration access and a supported write action. If the connected ChatGPT GitHub tool cannot edit these fields, a repository administrator must apply them in GitHub's interface.

## Quality checklist

- [ ] Description is short, accurate and distinct from the private DIK project
- [ ] Topics correspond to published functionality
- [ ] Website points to the **actual onboarding guide** on the default branch
- [ ] Public README links prominently to the same guide
- [ ] No personal/private information is embedded in the public description

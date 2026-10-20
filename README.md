# Knotbase

**Portable, indexed AI workflows for ChatGPT Projects.** Knotbase organizes research, writing, coding, GitHub and personal-knowledge tasks into documented instructions that a compatible ChatGPT client can follow.

[![Public router validation](https://img.shields.io/github/actions/workflow/status/DOKOS-TAYOS/knotbase/validate-public-router.yml?branch=main&label=validation)](https://github.com/DOKOS-TAYOS/knotbase/actions/workflows/validate-public-router.yml)
[![MIT License](https://img.shields.io/github/license/DOKOS-TAYOS/knotbase)](LICENSE)

> **[Get started: set up your Knotbase Project](docs/GETTING_STARTED.md)** — choose a public or private copy, connect GitHub, and configure ChatGPT.
>
> **[Open the ChatGPT Project instructions](PROJECT_INSTRUCTIONS.md)** — before pasting them into a Project, replace `YOUR_GITHUB_OWNER/YOUR_KNOTBASE_REPO` with the exact `owner/repository` of your own Knotbase instance.

## What Knotbase provides

Knotbase is a public, modular instruction package—not a standalone application, hosted AI service, or custom model. Its indexed workflows help a compatible ChatGPT client select relevant guidance and preserve each workflow's scope, evidence requirements, approvals, and permissions.

The public registry includes 64 commands. For example:

- `#EXPL <topic...>` creates an audience-aware explanation.
- `#DEEP <topic...>` routes a research task through its indexed workflow.
- `#BLOG <topic...>` starts the staged blog-writing workflow.
- `#TEST <repo>` begins an inventory-only test review.
- `#SHIP <repo>; [branch]` routes integration through its repository and GitHub safeguards.
- `#HELP` lists the registered commands and their syntax.

These examples describe instruction routes; the connected client still needs the tools, access, and evidence required by a particular task. The public router and command registry define the current scope.

## Getting started in five steps

1. **Choose your copy.** Use a public fork for public material, or create an independent private copy if you plan to keep personal records in the repository.
2. **Make it your repository.** Clone or download Knotbase, then place it in the repository you control. Keep personal information out of the upstream and public forks.
3. **Connect GitHub to ChatGPT.** Grant access to only the repository or repositories you intend to use, and confirm the integration works in your chosen ChatGPT interface.
4. **Configure a ChatGPT Project.** Paste [the Project instructions](PROJECT_INSTRUCTIONS.md) into the Project settings after replacing `YOUR_GITHUB_OWNER/YOUR_KNOTBASE_REPO` with your copy's exact `owner/repo`.
5. **Bootstrap and verify.** Start a new Project chat, follow [`BOOTSTRAP.md`](BOOTSTRAP.md) when setting up an instance, and review every proposed write. You can run the structural validator locally with `python maintenance_for_ai/validation/validate.py`.

For detailed steps and privacy choices, follow the **[Getting started guide](docs/GETTING_STARTED.md)**.

## How the instruction files fit together

- **`PROJECT_INSTRUCTIONS.md`** points a ChatGPT Project at the user's own repository and requires the client to read its current `AGENTS.md` before routing a new task.
- **`AGENTS.md`** is the public instruction router. It resolves compact commands through the canonical command lookup and registry, or selects a relevant public domain for a natural-language request.
- **Indexed workflows** in `info_for_ai/` and `maintenance_for_ai/` supply the task-specific steps, evidence requirements, phase gates, and limits. The router loads only the files indexed for the selected task.
- **`BOOTSTRAP.md`** applies when a user explicitly sets up their own Knotbase instance. It defines owner selection, privacy, permissions, and fail-closed checks before owner-specific workflows can be used.

Together these files describe how a capable client can use the repository's instructions. They do not install or continuously run an agent.

## Privacy: public fork or private copy

A fork of this public repository remains public. Use it for public material and configuration only. If Knotbase will contain your CV, personal history, private source records, repository inventory, or maintenance logs, create an **independent private copy** and verify that it is the authorized destination before saving anything. A public fork can be paired with a separate private knowledge repository only when the workflow and client can verify access to that destination.

Never commit credentials, tokens, or private personal information to the public upstream or a public fork. See the [Getting started privacy guidance](docs/GETTING_STARTED.md#2-requirements-and-privacy-decisions) and [bootstrap contract](BOOTSTRAP.md).

## Documentation

| Guide | Purpose |
| --- | --- |
| [Getting started](docs/GETTING_STARTED.md) | Installation choices, ChatGPT Project setup, privacy, and first use |
| [Project instructions](PROJECT_INSTRUCTIONS.md) | Copy-ready Project prompt; replace the repository placeholder before use |
| [Bootstrap contract](BOOTSTRAP.md) | Owner-specific setup and permission requirements |
| [Public router scope](docs/PUBLIC_ROUTER_SCOPE.md) | What the public instruction router includes and excludes |
| [HTML public scope](docs/HTML_PUBLIC_SCOPE.md) | Scope of the public HTML workflows |
| [Public asset scope](docs/PUBLIC_ASSETS_SCOPE.md) | Availability of generic HTML runtime resources |
| [Privacy adaptations](docs/PRIVACY_ADAPTATIONS.md) | Documented privacy-related source changes |
| [Editorial exclusions](docs/EDITORIAL_EXCLUSIONS.md) | Documented editorial exclusions |
| [Authorized CV deviations](docs/AUTHORIZED_CV_DEVIATIONS.md) | Scope of the public CV workflow adaptations |
| [Migration continuity](docs/MIGRATION_CONTINUITY.md) | Verified migration checkpoints and remaining work |
| [Source parity manifest](manifests/source_parity.csv) | Published source records and their adaptation status |
| [GitHub About settings](docs/GITHUB_ABOUT.md) | Proposed repository description and discoverability topics |

## Public pilot status

The repository publishes selected, indexed instruction workflows and an unconfigured onboarding scaffold. It does not include personal records or configure a user's GitHub account. Owner-specific operations require the user's own instance, verified permissions, and any workflow-specific evidence and approval.

The validation workflow checks repository structure and selected contracts. A passing check does **not** demonstrate end-to-end ChatGPT behavior, remote permissions, or successful generation of every workflow's output. See [the public router scope](docs/PUBLIC_ROUTER_SCOPE.md) for the precise limitations.

## Project links

- [Repository](https://github.com/DOKOS-TAYOS/knotbase)
- [Issues](https://github.com/DOKOS-TAYOS/knotbase/issues)
- [Pull requests](https://github.com/DOKOS-TAYOS/knotbase/pulls)
- [Validation workflow](https://github.com/DOKOS-TAYOS/knotbase/actions/workflows/validate-public-router.yml)
- [MIT License](LICENSE)

# Getting started with Knotbase

**From an empty GitHub account and a new ChatGPT Project to a user-controlled knowledge workspace.** No software installation is necessary to read the instructions in ChatGPT, but you need a GitHub repository that the available ChatGPT GitHub integration can read.

> **Choose the right repository type first.** A fork of this **public** repository is also **public** and cannot independently be made private. If you want to store your CV, professional history or other personal records in your Knotbase repository, create an **independent private copy** instead. Never commit secrets or sensitive personal information to the public upstream or a public fork.

## Contents

1. [What Knotbase is](#1-what-knotbase-is)
2. [Requirements and privacy decisions](#2-requirements-and-privacy-decisions)
3. [Download, fork or make a private copy](#3-download-fork-or-make-a-private-copy)
4. [Connect GitHub to ChatGPT](#4-connect-github-to-chatgpt)
5. [Create the ChatGPT Project and paste its instructions](#5-create-the-chatgpt-project-and-paste-its-instructions)
6. [Start the bootstrap conversation](#6-start-the-bootstrap-conversation)
7. [Supply your personal information and evidence](#7-supply-your-personal-information-and-evidence)
8. [Authorize configuration and verify the installation](#8-authorize-configuration-and-verify-the-installation)
9. [Use Knotbase day to day](#9-use-knotbase-day-to-day)
10. [Write permissions, confirmations and approvals](#10-write-permissions-confirmations-and-approvals)
11. [Troubleshooting, security warnings and limitations](#11-troubleshooting-security-warnings-and-limitations)
12. [Updates, maintenance and checklist](#12-updates-maintenance-and-checklist)

## 1. What Knotbase is

Knotbase is a repository of modular, indexed instructions that helps ChatGPT route research, writing, coding, GitHub and professional-document tasks through documented workflows. It is **not** a standalone executable, a special AI model, a memory service or a replacement for ChatGPT's own tools.

The main entry point is **[`AGENTS.md`](../AGENTS.md)**. Your ChatGPT Project instructions tell the model which repository to open; `AGENTS.md` defines routing, workflow selection and safeguards. The **[`BOOTSTRAP.md`](../BOOTSTRAP.md)** contract controls first-time owner setup.

The upstream distribution is a **public pilot**. Indexed commands exist, but availability of connected GitHub actions, local execution, content generation and end-to-end behavior varies with the user's plan and tools. A command being listed does not prove that every corresponding operation can be performed in a given chat.

## 2. Requirements and privacy decisions

You will need:

- A GitHub account and permission to create a repository under your account or organization.
- A ChatGPT account that supports **Projects** and a usable **GitHub connection** in the intended interface.
- Access to your own copy of this repository, with `AGENTS.md`, `BOOTSTRAP.md` and `PROJECT_INSTRUCTIONS.md` present.
- Optional: Git installed locally, if you choose the command-line copy method; Python if you want to run the included structural validator.

**Privacy options:**

| Setup | Appropriate for |
| --- | --- |
| Independent **private** repository | Recommended if Knotbase will store your personal knowledge, CV, source records, inventory or maintenance history |
| **Public fork** + separate **private** knowledge repository | Publicly sharing the instruction framework while keeping personal records elsewhere, provided workflows have verified access to the correct private destination |
| Public fork only, no personal data stored | Trying generic read-only workflows and adapting public instructions |

A public fork is not a private data vault. If you are unsure, create an independent **private** repository from the outset.

## 3. Download, fork or make a private copy

### Recommended: create an independent private repository

1. Open [the Knotbase repository](https://github.com/DOKOS-TAYOS/knotbase).
2. Download it using **Code → Download ZIP** or clone it:

   ```bash
   git clone https://github.com/DOKOS-TAYOS/knotbase.git
   cd knotbase
   ```

3. In your GitHub account, create a **new, empty private repository**, for example `YOUR_GITHUB_OWNER/my-knotbase`. Do not initialize it with another README or licence when you intend to push a cloned history.
4. If you cloned Knotbase, point your local `origin` to **your own new repository** and preserve the public upstream separately:

   ```bash
   git remote rename origin upstream
   git remote add origin https://github.com/YOUR_GITHUB_OWNER/my-knotbase.git
   git push -u origin main
   ```

5. If you downloaded the ZIP instead, extract it and upload the extracted repository files into your new private repository. Preserve the directory structure, especially `AGENTS.md`, `BOOTSTRAP.md`, `info_for_ai/`, `maintenance_for_ai/` and `config/`. ZIP installation does not preserve Git history.
6. Open **your own** repository URL and verify that it contains `AGENTS.md` and `PROJECT_INSTRUCTIONS.md`.

Replace `YOUR_GITHUB_OWNER` and `my-knotbase` with the actual names. Git authentication or permissions may be requested by GitHub when pushing.

### Alternative: a public fork

Click **Fork** in the public Knotbase repository, choose your account and create the fork. The result is a **public** repository. Use it only for public configuration and public material; arrange a separate private knowledge destination if you want personal records.

### Which URL matters?

In every subsequent step, use the exact `owner/repo` of **your own** instance, such as `maria/my-knotbase`. Do **not** point your ChatGPT Project at `DOKOS-TAYOS/knotbase`: that is the shared upstream and not your private instance.

## 4. Connect GitHub to ChatGPT

1. Open ChatGPT **Settings → Plugins** or **Apps / Connectors**, whichever appears in your interface.
2. Find **GitHub**, connect it and authenticate using **your own GitHub account**.
3. Follow GitHub's authorization screen and grant access to **at least your Knotbase repository**. If you chose a separate private knowledge repository, grant only the necessary additional access to that repository.
4. Back in ChatGPT, confirm that you can use GitHub in the **same chat mode/interface** in which you plan to use Knotbase. Support can vary by account, plan and product surface.
5. Check access with a read-only request such as: *“Read `AGENTS.md` from `YOUR_GITHUB_OWNER/my-knotbase` and tell me only whether it was found.”*

Grant the least access you need; do not make every repository accessible just to try Knotbase. Connecting GitHub does not automatically grant writing capabilities in all ChatGPT modes.

Official documentation: [Connecting GitHub to ChatGPT](https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt).

## 5. Create the ChatGPT Project and paste its instructions

1. In ChatGPT, choose **New project** and create one named, for example, **Knotbase**.
2. Open **Project settings → Project instructions** (often available from the project's **•••** menu).
3. Open **[`PROJECT_INSTRUCTIONS.md`](../PROJECT_INSTRUCTIONS.md) in your own GitHub repository**.
4. Copy **the complete content** of that file.
5. **Before pasting**, replace every occurrence of **`YOUR_GITHUB_OWNER/YOUR_KNOTBASE_REPO`** with your real `owner/repo`; for example, `maria/my-knotbase`. The resulting prompt must identify **your instance**, not the shared upstream.
6. Paste the modified text into your new ChatGPT Project's instructions and save it.
7. Start a **new chat inside that project**.

**Example replacement:**

```text
Before: YOUR_GITHUB_OWNER/YOUR_KNOTBASE_REPO
After:  maria/my-knotbase
```

This placeholder is in the instruction *text*, not a GitHub link to click. A mismatched owner or repository name will cause bootstrap to fail; fix the Project instructions if that happens.

Official documentation: [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt).

## 6. Start the bootstrap conversation

In a **new chat in that Project**, send:

> Quiero configurar mi instancia de Knotbase. Lee `AGENTS.md` y `BOOTSTRAP.md` de **mi repositorio configurado** y sigue su proceso de inicialización. Mi repositorio es `YOUR_GITHUB_OWNER/my-knotbase`. Voy a proporcionarte la información que conozco sobre mí; pídeme los datos que falten, uno por uno, y no inventes nada. Confirma el destino privado y los permisos antes de guardar información.

Replace the example repository name. The assistant should first verify its ability to **read the actual repository** and determine whether first-time setup is still needed. If GitHub access fails, fix the connection or project instructions before asking it to edit anything.

Typical initial configuration in [`config/instance.csv`](../config/instance.csv) is:

| Key | Meaning |
| --- | --- |
| `instance_repository` | Full `owner/repo` of your Knotbase installation |
| `github_owner` | Verified GitHub account or organization whose repositories are in scope |
| `knowledge_repository` | Your chosen **private** repository for personal knowledge |
| `knowledge_storage` | Description of the actual storage arrangement |
| `onboarding_state` | State of verified onboarding, initially `unconfigured` |

The assistant must verify real targets and permissions. An empty value is a question to resolve, not an instruction to copy the original author's data.

## 7. Supply your personal information and evidence

Provide **what you already have**, and let the assistant ask for missing information when a workflow genuinely needs it. It is reasonable to do this across several chats or sessions; do not require a complete biography on day one.

Useful optional inputs include:

- Identity and preferred public name, professional role and short profile.
- CVs and records of education, employment, projects and skills.
- Publication identifiers (DOIs, ORCID, scholarly profiles), papers and portfolio links.
- GitHub account, repositories, which ones are active, archived or frozen, and the intended scope of maintenance.
- Writing/language preferences, citation standards and preferred deliverables.
- Documents containing traceable evidence for claims that you want the system to reuse.

Example follow-up:

> Te adjunto mi CV y estas publicaciones. Extrae solamente hechos respaldados por las fuentes, identifica contradicciones o información incompleta y pregúntame antes de incorporar datos a la base privada.

**Data safety:** Supply only information you are comfortable sharing with your ChatGPT account. Decide what is **public**, **restricted** or **private** before publishing anything. Do not paste passwords, API keys, GitHub tokens or other secrets into chat or Git. Do not let the assistant copy all accessible emails, drives or repositories merely because a connection exists.

## 8. Authorize configuration and verify the installation

When the assistant proposes changes, inspect the **exact repository**, affected files, evidence and visibility. Approve only the writes you intend. In particular:

1. Check that configuration points to your own GitHub account and copy, never the public upstream or the original author's private DIK.
2. Check that personal knowledge is destined for an **authorized private repository**.
3. Authorize only requested personal records, inventory rows and configuration changes.
4. Verify that files actually appear on the intended branch/repository after a successful write. A prepared draft or a proposed PR is not a completed write.
5. Optionally validate a locally cloned installation:

   ```bash
   python maintenance_for_ai/validation/validate.py
   ```

The validator checks repository-level structural contracts; it cannot by itself prove that ChatGPT can execute all workflows or that remote write permissions are available. If your plan supports only read access, the assistant can still explain, draft changes or generate patches, but must not claim that GitHub was updated.

The complete onboarding contract and acceptance tests are in [`BOOTSTRAP.md`](../BOOTSTRAP.md).

## 9. Use Knotbase day to day

After installation, **use normal ChatGPT conversation**. Ask about a concept, a paper, a CV, a coding task or a repository. Knotbase routes supported workflows through its own instructions. You can also use its registered compact commands.

Examples using the current public registry:

```text
#HELP
#EXPL Explícame qué es la entropía de Shannon desde cero
#BLOG Una introducción a los métodos de compresión
#CV <paste a job offer or describe the target role>
```

Run `#HELP` for the complete installed command catalogue and each command's syntax. Some workflows deliberately work in **phases**, requiring an explicit `OK` before proceeding. Others are read-only. Do not infer a command's meaning solely from its name.

A new independent task triggers a fresh read of the configured repository's `AGENTS.md`, as described in `PROJECT_INSTRUCTIONS.md`. This keeps the Project aligned with updates to the user's own repository.

## 10. Write permissions, confirmations and approvals

There are two distinct questions: **Can this ChatGPT interface write to your GitHub repository?** and **Did you authorize this particular change?** Both must be satisfied. Even if a connection has broad permissions, certain workflows require explicit confirmation.

- If you see a write-approval dialog, read the destination and diff, and approve only when correct.
- If the interface cannot write, ask for a reviewed patch, commit instructions or a PR where supported.
- Do not grant blanket access merely to avoid approval dialogs. Use the minimum scopes needed for the operation.
- Remote operations may require CI, branch protection, review or other acceptance checks. A connected account does not override them.

## 11. Troubleshooting, security warnings and limitations

| Symptom | What to check |
| --- | --- |
| “AGENTS.md not found” | Project prompt has the **correct `owner/repo`**, GitHub connection authorizes the repo, and the current ChatGPT mode can access GitHub |
| ChatGPT reads the **public upstream** | Replace the Project instructions placeholder with **your own** repository; start a new chat in the correct Project |
| Private repo is inaccessible | GitHub app installation and selected-repository permissions; whether GitHub is supported in the current interface |
| Bot can read but cannot write | The available ChatGPT GitHub workflow may be read-only, or the account/branch lacks write permission; prepare changes for manual review instead |
| Missing user facts or empty CV | The public distribution intentionally ships no personal biography; supply evidence and finish the relevant private onboarding |
| `#NAME` is unavailable | Read `#HELP`; only registered commands are enabled |
| A phased task does not proceed | Check whether that specific workflow requires an explicit approval, often an isolated `OK` |
| Validator passes but a task still fails | Structural validation is not an end-to-end ChatGPT runtime test |

**Cybersecurity and safety notices:** Some legitimate defensive or repository-security tasks may trigger warnings or restrictions. First clarify the **authorized defensive purpose, repository ownership and exact scope** and request a compliant alternative or an explanation. Do not assume every refusal is a false positive, and do not use a new chat to bypass a safety restriction. A new chat is appropriate when restoring missing context, not for evading safeguards.

**No hidden automation:** Knotbase's Markdown instructions do not run continuously in the background. Recurring tasks, webhooks, notifications and remote GitHub actions require separately available tools and explicit setup.

## 12. Updates, maintenance and checklist

If you use an independent private copy that preserves the public upstream remote, consider updates carefully: review upstream changes and avoid overwriting configured personal records. If you use a fork, review suggested upstream synchronizations before merging. Never open a public upstream PR that contains your personal data.

**Installation checklist**

- [ ] My own repository exists; its visibility matches my privacy requirements.
- [ ] GitHub is connected in the ChatGPT interface I will use, with access to my repository.
- [ ] My ChatGPT Project instructions contain **my exact `owner/repo`**.
- [ ] ChatGPT can read `AGENTS.md` and `BOOTSTRAP.md` from that repository.
- [ ] My instance, GitHub owner and private knowledge destination are correctly identified.
- [ ] Only authorized, source-backed personal facts are stored in the appropriate private location.
- [ ] Read-only workflows run; any write action is separately verified.
- [ ] I understand that this is a public pilot, not a guaranteed full consumer-runtime installation.

## Further reading

- [ChatGPT Project prompt](../PROJECT_INSTRUCTIONS.md)
- [Bootstrap contract](../BOOTSTRAP.md)
- [Public workflow scope](PUBLIC_ROUTER_SCOPE.md)
- [Privacy adaptations](PRIVACY_ADAPTATIONS.md)
- [Source parity manifest](../manifests/source_parity.csv)
- [GitHub's documentation on forks](https://docs.github.com/en/pull-requests/reference/forks)

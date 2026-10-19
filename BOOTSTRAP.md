# Knotbase user bootstrap

This file describes the **consumer's own installation**. The upstream public Knotbase repository is a template, never a destination for a user's personal records or routine maintenance changes.

## Bootstrap trigger

At the start of a newly adopted Knotbase instance, inspect `config/instance.csv`. If `instance_repository` or `github_owner` is empty, perform this bootstrap before selecting owner-specific GitHub commands, reading user facts as verified, or making repository mutations. Ask for the missing values conversationally, one decision at a time; do not guess from the original author's repository or from the currently connected GitHub account.

1. Ask which **user-owned fork or private instance repository** is the maintained Knotbase (`owner/repo`). It must be a repository the user is authorized to edit. Never default to `DOKOS-TAYOS/knotbase` or `DOKOS-TAYOS/dokos-instructions-knowledge`.
2. Ask which GitHub owner(s) and actual repositories are in scope. For multi-repository operations, populate and verify the inventory at `info_for_ai/info_user/repositorios_github.csv`, including archived and frozen status. An empty inventory never means “all repositories”.
3. Ask where the user wants their **private knowledge** to live. Recommended: a private fork or private knowledge repository accessible only to them. The `knowledge_repository` may equal `instance_repository` only if the instance is private. Personal data must never be pushed to the public upstream repository.
4. Offer optional self-description, CV, publications and professional profile records. Accept sources only when the user supplies or authorizes them. Empty tables remain empty, not fabricated. The user may defer personal setup and still use generic read-only educational/research workflows.
5. Record the configuration in the user's own private instance, only with their permission, and confirm that the repository and access rights actually exist. No credentials, tokens, passwords or sensitive material belong in the configuration or the chat transcript.
6. Check `info_for_ai/indice_dominios.csv`, `info_for_ai/info_user/indice_info_user.csv` and `maintenance_for_ai/indice_mantenimiento.csv` before declaring relevant owner workflows ready. Do not announce functional readiness for missing modules or validators.

## Safe operation

- If the configured instance is not writable, offer read-only guidance and report the blocker.
- For omitted explicit repository arguments, resolve only from the verified private inventory; ask when selection is ambiguous or incomplete.
- The canonical repository owner, publication catalog, knowledge-store location and command targets belong to the current user, **not** to the original DIK author.
- Changing the instance or owners is a scope change: reconfirm authorization and revalidate inventory.
- Distinguish onboarding templates from documented evidence: a blank CSV or Markdown profile is never proof of any personal fact.
- Public upstream updates should be integrated separately from user private data. Never propose a pull request that copies private instance files into upstream.

## Minimal completion criteria

`instance_repository` and `github_owner` have verified, nonempty values in the user's own instance; private knowledge storage has been chosen or explicitly deferred; no user secrets have been stored. Additional features require their own indexed dependencies and acceptance tests.

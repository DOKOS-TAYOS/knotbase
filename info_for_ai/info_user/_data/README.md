# Traceable user data

The four CSV tables are canonical, empty schema templates. Use stable SRC-, FACT-, CAP- and REL- identifiers, ISO 8601 dates, source-backed claims, `visibility` and `review_status`. A blank field is not a verified fact. Never publish private or restricted records to upstream.

- `fuentes.csv`: source provenance and verification
- `hechos.csv`: canonical factual assertions
- `capacidades.csv`: individually evidenced capabilities
- `relaciones.csv`: nonredundant relationships between entities

Preserve the original column contract and evidence links when populating these tables in a user-controlled private store.

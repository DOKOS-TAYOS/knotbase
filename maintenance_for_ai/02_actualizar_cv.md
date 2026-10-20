# Actualizar desde CV

Usa este procedimiento cuando el usuario proporcione una nueva versión de uno o varios CV.

**Invariant:** Write personal source records only to the configured authorized private knowledge store; never to upstream. Do not proceed without a verified writable target.

## Objetivo

Detectar información realmente nueva o modificada y propagar solo los cambios necesarios a la capa trazable y a las vistas editoriales afectadas.

## Procedimiento

1. Identifica el CV como una fuente nueva o una nueva versión de una fuente existente.
2. Compara sus afirmaciones con `info_for_ai/info_user/_data/fuentes.csv`, `hechos.csv` y `capacidades.csv` antes de editar vistas Markdown. Consulta `relaciones.csv` únicamente cuando el CV introduzca o modifique un enlace transversal que no esté ya representado como hecho, de acuerdo con `_data/README.md`.
3. Registra trayectoria, educación, roles, proyectos, supervisión, eventos y demás afirmaciones personales en `hechos.csv`; no materialices una segunda fila equivalente en `relaciones.csv`.
4. Clasifica cada diferencia como nueva, modificada, ya documentada, contradictoria o insuficientemente precisa.
5. Añade o modifica únicamente registros respaldados por el CV y respeta las reglas de `confidence`, `visibility` y `review_status` del esquema trazable.
6. Si un dato anterior queda reemplazado, conserva trazabilidad histórica mediante `valid_to`, `superseded` o notas cuando corresponda; no borres historia útil para simplificar.
7. Actualiza solo las vistas Markdown que utilicen los hechos o capacidades modificados. No regeneres todos los perfiles si el cambio afecta a una sección concreta.
8. No conviertas una frase promocional del CV en un hecho probado. Mantén la distinción entre `declared_claim`, `observed_fact`, `project_objective` y `proven_result`.
9. Si dos CV discrepan y no hay regla de precedencia suficiente, conserva la discrepancia como `needs_review` en lugar de elegir arbitrariamente.
10. Ejecuta validadores y tests, en especial las comprobaciones de privacidad de vistas públicas.

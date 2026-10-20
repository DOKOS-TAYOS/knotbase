# Actualizar información general de usuario

Usa este procedimiento para incorporar o corregir información profesional o personal de the configured user en `info_user` cuando la actualización no pertenezca de forma más específica a papers, CV o inventario de repositorios GitHub. Si la tarea encaja en `01_actualizar_papers.md`, `02_actualizar_cv.md` o `03_actualizar_repositorios_github.md`, usa ese procedimiento especializado.

**Invariant:** Before mutation, verify the selected private knowledge repository and user authorization. A blank upstream profile does not identify a user or confer permission to store personal data.

## Objetivo

Mantener sincronizadas la evidencia trazable y las vistas derivadas de `InfoUser` con el menor número de lecturas y cambios posible, usando `indice_info_user.csv` como inventario y mapa de dependencias.

## Procedimiento

1. Abre `info_for_ai/info_user/00_core.md` y `info_for_ai/info_user/indice_info_user.csv`. No recorras la carpeta completa.
2. Identifica la fuente canónica responsable del dato. Abre `info_user/_data/README.md` solo si necesitas consultar el esquema de `fuentes.csv`, `hechos.csv`, `capacidades.csv` o `relaciones.csv`.
3. Si la evidencia todavía no está registrada, añádela primero a `_data/fuentes.csv`. Una declaración directa de the configured user puede ser una fuente válida, pero debe conservar procedencia, fecha, visibilidad, confianza y estado de revisión según el esquema.
4. Registra después la afirmación en su propietario canónico: hechos y trayectoria en `hechos.csv`, capacidades personales respaldadas en `capacidades.csv`, y únicamente enlaces transversales no redundantes en `relaciones.csv`. No materialices la misma afirmación en varias capas.
5. Para cada recurso canónico modificado, filtra `indice_info_user.csv` por filas `authority=derived` cuyo `source_of_truth` incluya ese recurso. Revisa solo esas vistas candidatas y actualiza únicamente las que hayan quedado materialmente desfasadas.
6. Una vista derivada puede resumir o reorganizar información canónica, pero no aumentar ni reducir de forma material el alcance de una capacidad o afirmación, ni eliminar calificadores relevantes de confianza, revisión, visibilidad, incertidumbre o límites explícitos. Si una vista empieza a utilizar materialmente una fuente canónica nueva o deja de usarla, actualiza su `source_of_truth` en `indice_info_user.csv` en la misma tarea.
7. No introduzcas una afirmación personal nueva únicamente en una vista derivada. Si la evidencia no permite registrarla canónicamente con el estado adecuado, omítela o conserva la incertidumbre en la capa trazable correspondiente.
8. Ejecuta `python maintenance_for_ai/validation/validate.py` y revisa el diff final. Si el índice no permite localizar de forma suficiente una dependencia, declara esa inconsistencia y usa solo el fallback de búsqueda mínimo necesario para resolverla.

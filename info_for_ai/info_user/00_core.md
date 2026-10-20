# Núcleo de uso de información de usuario

Carga este archivo siempre que el routing seleccione `info_user`. Después abre `indice_info_user.csv` y únicamente los recursos necesarios para la petición.

## Selección de información

1. Usa el índice como inventario canónico del dominio. No recorras `info_user/` ni cargues varias vistas por proximidad temática.
2. Para síntesis o redacción, prefiere una vista derivada específica cuando cubra suficientemente la petición. Abre datos canónicos solo cuando hagan falta precisión, trazabilidad, resolución de discrepancias, actualización o comprobación de límites.
3. `authority=canonical` prevalece sobre una vista `derived` para el dato que controla. Un recurso `snapshot` solo describe el estado observado en su fecha y no debe convertirse en estado actual sin verificación.
4. No abras `README.md`, `_data/README.md`, fuentes, taxonomía, hechos atómicos o discrepancias por defecto. Úsalos únicamente cuando su responsabilidad sea necesaria para la tarea.
5. `12_discrepancias_y_limitaciones.md` es la vista editorial responsable de discrepancias y límites específicos de inferencia. Ábrela solo cuando una afirmación material dependa de una inferencia indirecta, exista una discrepancia real entre fuentes o versiones, el recurso seleccionado señale un límite específico, o la evidencia disponible no determine con suficiente claridad el alcance atribuible. Si una vista o fuente ya respalda directamente y sin conflicto el hecho, capacidad, autoría o alcance requerido, no cargues `12_discrepancias_y_limitaciones.md` únicamente por tratarse de una atribución personal.

## Atribución y límites de inferencia

1. Distingue siempre entre hechos sobre actividades o artefactos y capacidades personales. Un título, dependencia, tema de proyecto, charla, publicación, repositorio o coautoría no demuestra por sí solo dominio personal del área asociada.
2. Una capacidad solo puede presentarse con el alcance respaldado por la evidencia trazable. No generalices una capacidad específica a un campo más amplio.
3. Cuando un registro o módulo declare un límite explícito de conocimiento, autoría, alcance o reutilización, ese límite prevalece sobre inferencias indirectas obtenidas de otras fuentes.
4. La inspección de un artefacto puede demostrar su contenido o estructura, pero no atribuye automáticamente autoría, responsabilidad individual ni dominio de todas las tecnologías o disciplinas presentes en él.
5. La coautoría bibliográfica acredita participación en una publicación, no una desagregación automática de contribuciones individuales.

## Evidencia, privacidad y estado

1. Respeta `visibility`, `review_status`, `confidence` y la procedencia de los registros canónicos. Las reglas globales de privacidad y trazabilidad de `AGENTS.md` siguen siendo obligatorias.
2. Para una salida pública, reutiliza únicamente información pública permitida por las fuentes y por el estado de revisión aplicable. No materialices detalles `restricted` o `private` a través de una vista derivada.
3. No combines discrepancias en un valor híbrido. Usa la versión priorizada cuando exista y conserva las alternativas como tales cuando sean relevantes.
4. No conviertas `needs_review`, objetivos de proyecto, afirmaciones de preprint o evidencia contextual en hechos establecidos.

## Construcción de la respuesta

1. Selecciona solo la información relevante para el objetivo del usuario. No conviertas una respuesta en un inventario del perfil completo salvo petición explícita.
2. Adapta el orden editorial al contexto sin alterar la fuerza de la evidencia ni crear prioridades profesionales permanentes.
3. No expongas IDs `FACT-*`, `CAP-*`, `REL-*` o `SRC-*` salvo que la tarea requiera trazabilidad, mantenimiento o auditoría.
4. Si una vista derivada contiene más detalle del necesario, extrae únicamente la parte pertinente; su existencia no obliga a reproducirla completa.

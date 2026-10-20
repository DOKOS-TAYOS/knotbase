# Reglas compartidas de mantenimiento

Carga este archivo antes del procedimiento específico seleccionado por `indice_mantenimiento.csv`.

## Principios

1. Identifica primero la fuente canónica del dato, instrucción o configuración que se quiere cambiar.
2. Inspecciona solo los índices, fuentes, vistas derivadas, tests, evals o workflows que puedan quedar afectados.
3. Haz el cambio mínimo que satisfaga la petición. No hagas refactors laterales, limpieza especulativa ni nuevas abstracciones sin necesidad demostrable.
4. No dupliques reglas o datos. Si una instrucción existente cubre una parte del cambio, enlázala o amplíala en el lugar responsable en vez de copiarla.
5. Conserva identificadores estables, procedencia, privacidad, estados de revisión y notas históricas cuando correspondan.
6. Cuando un índice declare `source_of_truth` o una dependencia equivalente, úsalo como mapa de dependencias: tras modificar una fuente canónica, filtra únicamente las filas derivadas que nombren ese recurso y revisa esas candidatas. Si una vista empieza a depender materialmente de otra fuente o deja de hacerlo, actualiza el índice en la misma tarea.
7. Actualiza un índice, vista derivada, test, eval, workflow o changelog solo si el cambio los deja desactualizados.
8. Un fallo de test no autoriza a debilitar el test. Si el contrato no debía cambiar, corrige la implementación. Si el contrato cambia intencionadamente, actualiza implementación y test/eval de forma coherente.
9. No inventes estados, autoría, fechas, publicaciones ni clasificaciones. Cuando la evidencia no baste, conserva el valor existente o usa el valor controlado de incertidumbre definido por el esquema.
10. Antes de integrar, ejecuta las validaciones aplicables, corrige la causa raíz de los fallos y revisa el diff final para detectar cambios no relacionados.

## Configured instance boundary

**Invariant:** Maintenance writes are restricted to the user-authorized instance or private knowledge repository selected in `config/instance.csv`, after verification of actual access and scope. The public upstream is not a destination for personal records. If the instance, owner, storage or permissions are unresolved, stop before writing. Any synchronization of external project-instruction mirrors is conditional on an explicit existing target contract; never guess that an original-owner mirror applies.

## Logbook de mantenimiento

**Invariant:** Toda tarea que modifique la instancia configurada debe dejar una entrada en el logbook antes de considerarse cerrada. Cuando haya habido mutaciones, abre `logbook/CONTRACT.md` al final de la tarea y sigue su contrato: registra una unidad lógica de trabajo en el archivo diario usando hora `Europe/Madrid`, identifica el origen real, referencia los commits materiales y PR aplicables, conserva las decisiones relevantes y registra únicamente validaciones realmente ejecutadas.

Los archivos diarios son la fuente de verdad. Regenera los índices derivados con `python maintenance_for_ai/validation/logbook.py --write` y vuelve a ejecutar la validación canónica después de actualizar el logbook. **Default:** cuando el entorno permita un commit multiarchivo atómico, publica el archivo diario y sus índices derivados juntos en un único commit final; si no lo permite, usa el mínimo número de commits necesario. Los commits exclusivamente de logbook no se autorreferencian.

## Orden operativo

1. Entender la petición y determinar el procedimiento mínimo.
2. Localizar la fuente canónica y su índice.
3. Comparar estado actual con la información nueva o las fuentes externas necesarias.
4. Preparar el conjunto mínimo de archivos afectados.
5. Editar primero la fuente canónica y después sus dependencias necesarias.
6. Ejecutar validadores y tests.
7. Si hubo mutaciones, completar el logbook cuando los identificadores materiales necesarios ya sean conocidos, regenerar sus índices y repetir la validación canónica sobre el estado final.
8. Revisar el diff y resumir qué cambió, qué se verificó y qué incertidumbre permanece.

## Cambios de instrucciones orientadas a Codex

Cuando una instrucción se use principalmente con Codex, intenta reducir exploración y consumo innecesario: mueve a ChatGPT la investigación, aclaración de requisitos, decisiones de arquitectura y preparación del prompt cuando hacerlo permita entregar a Codex un objetivo acotado, rutas relevantes, restricciones resueltas, comandos de verificación y criterios de aceptación. No añadas pasos previos si no reducen trabajo real.

**Invariant:** Toda instrucción, prompt, workflow o procedimiento destinado a ejecutar trabajo con Codex debe asumir ejecución sin subagentes y, cuando genere texto que vaya a pegarse en Codex, debe indicarlo explícitamente en ese texto. No introduzcas ni recomiendes subagentes, agentes paralelos, agentes en segundo plano, pools de agentes ni delegación equivalente, ni hagas que el usuario tenga que habilitarlos.

**Invariant:** La única excepción es el workflow `#CYCLE` y su módulo `info_for_ai/code/06_cyclic_agent_workflow.md`. Solo cuando ese workflow esté activamente seleccionado puede una instrucción permitir subagentes, y únicamente con el alcance y coordinación definidos por dicho módulo. Ningún otro workflow de debugging, optimización, limpieza de código muerto, testing, refactoring, implementación o trabajo sobre código hereda esa excepción.

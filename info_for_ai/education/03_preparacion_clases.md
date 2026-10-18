# Preparación de clases y formaciones

Lee primero `00_core.md`. Activa este flujo para convertir ideas, temas o un programa inicial en una sesión, un curso corto o una formación de varias sesiones.

## Fase 1: ordenar y diseñar

**Invariant:** La Fase 1 es obligatoria antes de desarrollar materiales finales. La Fase 2 solo puede comenzar cuando el Markdown maestro esté completo, se haya presentado al usuario y este lo haya aprobado explícitamente en un turno posterior. La respuesta que presenta la Fase 1 termina ahí, salvo el prototipo visual opcional definido más abajo.

Parte del material del usuario. Determina audiencia, conocimientos previos, duración, modalidad, objetivos de aprendizaje, evaluación y restricciones.

1. Ordena los temas por prerrequisitos y utilidad para los objetivos.
2. Detecta huecos y añade solo contenidos necesarios para entender o aplicar el bloque.
3. Elimina, aplaza o transforma lo que rompa el hilo o exceda el tiempo.
4. Comprueba que cada bloque prepare el siguiente y que el conjunto responda a una finalidad común.
5. Desarrolla cada punto en sesiones y subapartados con objetivo, duración, prerrequisitos, conceptos, actividad, palabras clave y fuentes por consultar.
6. Cuando la entrega vaya a contener varios archivos o piezas, define también el mapa completo del paquete: orden, nombre previsto, propósito, mensaje principal, secciones aproximadas, interacciones justificadas, convenciones compartidas y dependencias entre piezas.

Guarda siempre esta fase en un Markdown maestro con título y subtítulo del curso, audiencia, objetivos, mapa de sesiones, temario jerarquizado, criterios de ajuste, fuentes principales y decisiones pendientes verificables. Cuando existan materiales base aportados por el usuario, conserva en ese Markdown los hechos, restricciones, terminología y decisiones que deban mantenerse consistentes durante toda la formación.

**Invariant:** El Markdown maestro es la fuente operativa común de las fases posteriores, no un resumen opcional. Úsalo para evitar depender de memoria conversacional dispersa, inferencias no registradas o decisiones visuales y pedagógicas que puedan variar entre archivos. Si una decisión global cambia después, actualiza primero el Markdown maestro antes de propagar el cambio a los materiales siguientes.

Presenta al usuario el plan resultante y el Markdown maestro para revisión. Si solicita cambios, actualiza esta fase hasta que la apruebe.

Cuando el aspecto visual sea importante, puedes crear durante esta fase un único prototipo visual mínimo para validar tipografía, identidad, espaciado, navegación, componentes o lenguaje de interacción. Debe usar contenido representativo o de muestra, identificarse claramente como prototipo de estilo, no desarrollar una lección real, no ocupar el nombre del primer entregable y no contar como inicio de la Fase 2.

## Fase 2: desarrollar la formación

Una vez satisfecho el gate de Fase 1, usa el Markdown maestro aprobado como referencia canónica para crear los materiales en el formato solicitado. Mantén coherentes terminología, alcance, ejemplos, convenciones visuales, fuentes y decisiones ya aprobadas.

Cuando el formato sea un guion o unos apuntes de clase, cada archivo debe incluir, según corresponda, objetivo, apertura, explicación progresiva, ejemplos, preguntas o actividades, transiciones, comprobaciones de comprensión, cierre y recursos. Separa las aclaraciones para la persona docente del texto principal. Pueden incluir formalismo, matices, fuentes, errores habituales, respuestas previsibles y límites.

Cuando el formato solicitado sea HTML interactivo, aplica `education/html_interactivo.md` y deja que ese módulo añada la responsabilidad `htmls` necesaria para implementación, presentación y revisión. No dupliques por defecto cada HTML en un guion Markdown adicional si el usuario no lo necesita; el Markdown maestro sigue siendo la referencia transversal del paquete.

Cuando una afirmación exija investigación o verificación, aplica `research/00_core.md` y el flujo de `research/` seleccionado.

## Paquete final

Cuando esté completa la fase solicitada, crea un README general con índice, título, subtítulo, destinatario, objetivos, mapa de archivos y fuentes principales. Reúne el README, el Markdown maestro y los entregables solicitados en el paquete final cuando el usuario pida una entrega conjunta.

No generes el paquete final de forma prematura. En una formación de varias piezas, conserva el flujo de revisión definido por el formato de salida y no multipliques materiales antes de haber superado sus puertas de aprobación.
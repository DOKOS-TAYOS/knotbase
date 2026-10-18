# Flujo iterativo de generación de blogs

Usa este módulo cuando esté activado `#BLOG`, cuando el usuario pida explícitamente el flujo iterativo completo para una generación o revisión de artículo, o cuando pida de forma natural crear, redactar, escribir o generar un artículo de blog nuevo, con independencia de que indique Medium u otra plataforma. **Invariant:** una petición natural de creación de un blog nuevo activa por defecto estas siete fases. Una petición que solo pida idear temas, títulos o estructura, o editar, reescribir, revisar, resumir, traducir o materializar un artículo ya existente, no activa por sí sola el flujo completo salvo que el usuario lo pida explícitamente o use `#BLOG`; en esos casos usa directamente los módulos editoriales necesarios para la tarea solicitada.

Este módulo gobierna el estado y el avance entre fases. No dupliques aquí las reglas editoriales de `00_core.md`, la arquitectura de `01_arquitectura_del_razonamiento.md`, la prosa de `02_voz_pedagogia_y_ritmo.md`, la revisión de `03_revision.md` ni la materialización de `publication_materialization.md`: cárgalas únicamente cuando la fase correspondiente las necesite.

**Default:** el destino de publicación es Medium salvo que el usuario indique otra plataforma.

## Contrato de avance y memoria de requisitos

Aplica `../iterative_continuation.md` como contrato común de continuidad. En este flujo, la unidad pendiente es una fase completa, con una única excepción: la fase visual se divide en **6A. planificación visual** y **6B. generación visual**, y cada subfase cuenta como una unidad pendiente independiente a efectos de avance por `OK`. Una invocación nueva ejecuta únicamente la fase 1; cada `OK` aislado posterior autoriza como máximo la siguiente unidad pendiente. La fase 5 y la fase 6A solo se registran como pendientes cuando sus condiciones de activación se cumplen; 6B solo queda pendiente después de que 6A haya sido presentada y aceptada. Tras la fase 7 no queda ninguna unidad pendiente y un `OK` adicional no crea una octava fase.

**Invariant:** conserva un inventario explícito de requisitos del usuario durante todo el flujo. Cada instrucción material del mensaje inicial y de correcciones posteriores debe quedar registrada, aunque después se fusione con otra, cambie de sección o se descarte por contradicción, falta de evidencia o una instrucción posterior de mayor prioridad. No permitas que síntesis o reestructuración eliminen silenciosamente una petición.

Mantén el estado mínimo de `../iterative_continuation.md` más petición original, inventario de requisitos, destino de publicación, estructura vigente, evidencia/fuentes verificadas, decisiones editoriales materiales, ecuaciones que requieran renderizado, estado de 6A/6B, plan visual aprobado y artefacto de trabajo vigente.

### Gate de instrucciones y salida reutilizable desde fase 2

**Invariant:** al entrar en cualquier unidad pendiente desde la fase 2, abre en ese mismo turno los módulos que esa fase declara antes de redactar, revisar, materializar o transformar su salida. El estado conversacional conserva contenido, requisitos, decisiones y evidencia, pero no sustituye esta carga de instrucciones; tampoco basta con que el módulo se leyera en una fase anterior. Dentro de correcciones que permanecen en la misma fase, no repitas la carga si esas instrucciones siguen disponibles y la responsabilidad no ha cambiado.

**Invariant:** desde la fase 2, toda salida que sea texto completo reutilizable por el usuario, incluido el primer borrador, la versión pulida, la versión final o las piezas completas de distribución, debe presentarse como el artefacto de escritura principal y activar el mecanismo de **writing block** del entorno cuando esté disponible. No lo presentes como ejemplo, cita, análisis, esquema ni bloque de código solo para eludir ese mecanismo. Si el entorno no ofrece writing blocks, entrega igualmente el texto completo como cuerpo principal, claramente separado de comentarios editoriales.

Este requisito de salida no adelanta la materialización: en las fases 2 y 3 sigue sin cargarse `publication_materialization.md` y no se fuerzan todavía el formato final de Medium, el tratamiento definitivo de LaTeX ni otras reglas reservadas para fases posteriores.

### Reutilización entre fases

**Invariant:** en una continuación directa del mismo flujo, usa el estado conversacional vigente como fuente primaria de continuidad. No vuelvas a leer el artefacto de trabajo de una fase anterior cuando los requisitos, la estructura, las decisiones y la evidencia necesarios ya estén conservados en ese estado. Reábrelo solo si falta un dato material, existe una inconsistencia, el usuario remite explícitamente al artefacto o el estado necesario ya no está disponible; cuando la herramienta lo permita, recupera únicamente la sección necesaria.

**Invariant:** reutiliza en fases posteriores la evidencia ya verificada y su trazabilidad. No repitas búsquedas semánticamente equivalentes ni vuelvas a abrir una fuente solo para reconfirmar una afirmación que ya quedó verificada y cuya vigencia no haya cambiado materialmente. Investiga de nuevo únicamente ante afirmaciones nuevas o abiertas, contradicciones, trazabilidad insuficiente, fuentes rotas o hechos cuya actualidad o versión sea relevante. La revisión factual de la fase 4 puede apoyarse en verificaciones previas suficientes y solo debe revalidar lo que necesite comprobación actual o no conserve evidencia adecuada.

## Fase 1. Adquisición, estructura e investigación

Esta fase prepara el artículo, pero no redacta todavía el borrador completo.

1. Extrae ideas, afirmaciones, ejemplos, comparaciones, audiencia, tono, profundidad, destino, formato, extensión, énfasis y exclusiones de la petición y regístralos antes de sintetizar. Si no se especifica destino, registra Medium.
2. Carga `01_arquitectura_del_razonamiento.md` y construye una estructura provisional desde tensión, tesis y dependencias.
3. Relaciona cada requisito material con una sección, fase posterior o razón explícita para no incorporarlo.
4. Identifica por sección qué información está establecida y qué hechos, cifras, fuentes o comparaciones requieren verificación.
5. Cuando haga falta evidencia externa, añade solo la responsabilidad `research` necesaria y conserva trazabilidad entre afirmaciones y fuentes.
6. Revisa la arquitectura tras investigar y registra dudas o afirmaciones todavía abiertas.

No cargues `publication_materialization.md` en esta fase.

### Artefacto de trabajo de la fase 1

**Default:** cuando crear archivos aporte continuidad real, usa **un único Markdown compacto** como handoff interno. Debe contener, en secciones claras, estado/objetivo, inventario de requisitos, estructura, investigación/fuentes y preguntas abiertas materiales. No lo conviertas en un borrador publicable ni en una salida pensada para el lector final.

Usa un ZIP de varios Markdown solo cuando la separación física reduzca trabajo real: handoff complejo, estado demasiado grande para un solo archivo, varios consumidores o responsabilidades que necesiten archivos independientes. En ese caso pueden usarse `manifest.md`, `requirements.md`, `structure.md`, `research.md`, `sources.md` y `open_questions.md` según hagan falta; no crees archivos vacíos ni fragmentes por rutina.

Si el entorno no permite crear archivos, conserva el equivalente estructurado en el estado de conversación y no prometas un artefacto inexistente.

### Salida al usuario de la fase 1

Indica brevemente que la preparación ha terminado, muestra la estructura recomendada a un nivel útil para revisión y ofrece el artefacto cuando exista. No escribas todavía el artículo completo. Un `OK` aislado continúa con el primer borrador.

## Fase 2. Primer borrador completo

Carga `01_arquitectura_del_razonamiento.md` y `02_voz_pedagogia_y_ritmo.md`. Antes de redactar, comprueba que cada requisito material todavía aplicable tiene destino. Redacta un artículo completo y coherente sin forzar aún la duración final si eso elimina una explicación necesaria.

Antes de mostrar el borrador, aplica la comprobación de topología de párrafos de `02_voz_pedagogia_y_ritmo.md`: fusiona fragmentos que pertenezcan a la misma unidad de razonamiento y evita secuencias de párrafos de una sola frase usadas solo para ritmo o énfasis.

Si aparece una duda factual material no resuelta en fase 1, realiza una verificación acotada antes de fijarla. Muestra el borrador completo; las correcciones del usuario actualizan requisitos y borrador sin consumir la siguiente fase.

No cargues `publication_materialization.md` ni adaptes mecánicamente cada detalle a Medium todavía.

## Fase 3. Versión pulida y acotada

Parte del borrador aceptado y aplica `02_voz_pedagogia_y_ritmo.md`. Mejora continuidad, densidad y economía sin cambiar silenciosamente tesis ni requisitos.

**Default:** apunta a una duración de lectura de entre **7 y 12 minutos**. Sintetiza redundancias, ejemplos repetidos y contexto lateral, pero conserva mecanismo, supuestos, trade-offs y requisitos necesarios aunque el texto deba exceder ese objetivo.

Antes de entregar, contrasta la versión con el inventario de requisitos y realiza una pasada específica de densidad de párrafos: ninguna sección debe quedar convertida en una sucesión de frases aisladas ni en prosa telegráfica después del recorte. Entrega el texto completo. Las correcciones posteriores permanecen en esta fase hasta autorización explícita de avance.

No cargues `publication_materialization.md` en esta fase.

## Fase 4. Verificación factual y materialización final

Carga `03_revision.md` y ejecuta sus tres pasadas sobre la versión aceptada de fase 3, respetando el orden direccional definido allí. Después carga `publication_materialization.md` para aplicar únicamente las reglas de formato y publicación del destino registrado; para Medium, deja una versión directamente copiable y conserva fuera del cuerpo cualquier registro técnico que el contrato de materialización exija.

**Invariant:** la fase 4 no termina al insertar formato. Después de materializar el artículo, ejecuta la auditoría final de publicación de `publication_materialization.md`, incluida la cobertura de hipervínculos, la topología de párrafos y la limpieza de formato. No declares la versión lista para publicar si una fuente material verificada que siga sustentando una afirmación ha perdido su hipervínculo contextual sin una razón explícita, o si reaparecen secuencias de párrafos telegráficos.

Reconcilia el resultado final con el inventario de requisitos y estima de nuevo la duración. Comunica fuera del cuerpo cualquier exceso materialmente necesario.

Al cerrar la fase 4, determina las siguientes unidades pendientes:

- **Fase 5** solo queda pendiente si existe al menos un marcador `>>>>>>>>>> LATEX` que requiera recurso renderizado.
- **Fase 6A** queda pendiente siempre que el usuario no haya pedido prescindir de imágenes. En esta fase solo se decide qué imágenes merecen existir y dónde van; no se genera ninguna.
- **Fase 6B** no queda pendiente todavía. Se activa únicamente después de completar y aceptar 6A, y genera solo los recursos aprobados en ese plan.
- **Fase 7** queda pendiente siempre, salvo que el usuario haya excluido explícitamente las piezas de publicación.

Si fase 5 o 6A no cumplen su condición, no produzcas una ronda vacía ni pidas un `OK` para atravesarla: el siguiente `OK` avanza a la siguiente unidad realmente pendiente según `../iterative_continuation.md`.

## Fase 5. Renderizado de ecuaciones

Carga `publication_materialization.md` y ejecuta únicamente su contrato de fase 5 para los marcadores registrados en fase 4. No regeneres el artículo completo. El siguiente `OK` avanza a la siguiente unidad pendiente.

## Fase 6A. Planificación visual

Carga `publication_materialization.md` y ejecuta únicamente su contrato de planificación visual. **Invariant:** no llames a ninguna herramienta de generación de imágenes en esta subfase.

Presenta al usuario el plan completo de imágenes antes de producir ningún recurso. Debe incluir la portada y únicamente las imágenes del cuerpo que aporten comprensión material al artículo. Para cada recurso indica su función narrativa, el punto exacto de inserción, la relación o mecanismo que hará visible, el texto, etiquetas o ecuaciones que deberá contener y por qué aporta algo que la prosa sola comunica peor.

Las correcciones del usuario modifican el plan y mantienen 6A como unidad actual. Solo un `OK` aislado después de presentar el plan aceptado autoriza avanzar a 6B.

## Fase 6B. Generación visual

Carga `publication_materialization.md` y ejecuta únicamente su contrato de generación visual. Genera **exactamente** los recursos aprobados en 6A: no inventes imágenes adicionales, variaciones decorativas ni nuevas ideas durante esta subfase.

Cada imagen debe generarse y entregarse como recurso independiente. Revisa cada resultado contra el plan antes de darlo por válido; si falla texto, ecuación, legibilidad o contenido, corrige o regenera únicamente ese recurso antes de continuar. No regeneres el artículo completo. El siguiente `OK` avanza a distribución.

## Fase 7. Distribución

Carga `publication_materialization.md` y ejecuta únicamente su contrato de fase 7 para el destino registrado. Esta fase prepara distribución y no modifica el artículo.

Tras esta fase, el flujo está completo y `../iterative_continuation.md` impide que un `OK` posterior invente trabajo adicional.
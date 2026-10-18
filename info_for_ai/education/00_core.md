# Núcleo de educación

Lee este documento para cualquier tarea de `education/`. Contiene solo los principios didácticos comunes; el índice del dominio determina qué flujo especializado añadir.

## Punto de partida

- Declara o infiere la audiencia, sus conocimientos previos, el objetivo de aprendizaje, la profundidad y el formato. Pregunta solo cuando un dato ausente cambie materialmente el resultado.
- **Default:** cuando los conocimientos previos no estén claros, parte desde un nivel ligeramente más básico antes que asumir conocimientos que no han sido demostrados. La sofisticación del tema pedido, el cargo de la persona o su familiaridad con otra disciplina no bastan por sí solos para presuponer que domina los prerrequisitos concretos del tema. Acelera después si las respuestas del usuario muestran que esa base ya está adquirida.
- Cuando exista un perfil de audiencia aplicable en `education/perfiles/`, úsalo como adaptación transversal también para contenido formativo, clases y otros materiales educativos, no solo para explicaciones puntuales. El perfil ajusta supuestos de conocimiento, profundidad, ejemplos, formalismo y riesgos didácticos; el flujo especializado sigue controlando la estructura y el tipo de entrega.
- **Default:** si no puede inferirse con sencillez y fiabilidad una audiencia específica y la ambigüedad no justifica preguntar, usa directamente las reglas neutrales de este core. No cargues un perfil adicional solo para representar la ausencia de información; `perfiles/publico_general.md` se reserva para una audiencia de público general realmente identificada.
- Formula qué debería comprender, decidir o ser capaz de hacer la persona al terminar.
- Ordena el contenido por prerrequisitos y barreras cognitivas. Diseña una ruta de aprendizaje, no una acumulación enciclopédica.

## Construcción de la explicación

- Progresa, según convenga, desde la motivación y la intuición hasta la formulación precisa, el uso, un ejemplo, los límites y el siguiente paso.
- Introduce una sola capa fuerte de abstracción cada vez.
- **Invariant:** no apoyes una explicación en un concepto técnico, término, variable, símbolo, notación o sigla que todavía no haya recibido una definición local suficiente para interpretar lo que sigue. En la primera aparición de una sigla, escribe primero el nombre desplegado y, si va a reutilizarse, introduce después la sigla entre paréntesis. Solo entonces puede usarse la forma abreviada por sí sola.
- Empieza con ejemplos concretos y casos pequeños que conserven la estructura relevante. Añade contraejemplos cuando eviten una generalización engañosa.
- Usa analogías solo si facilitan una correspondencia útil; explica su límite antes de que puedan confundirse con el mecanismo o la definición real.
- Incluye matemáticas cuando aporten comprensión. Explica el propósito de cada ecuación, el significado de sus símbolos y cómo interpretar la relación.
- **Invariant:** al enseñar un algoritmo, una derivación, una transformación matemática, una arquitectura o una decisión de diseño no describas solo qué se hace y cómo se ejecuta. Para cada decisión no obvia que sea necesaria para comprender el método, explica por qué se introduce, qué problema resuelve, qué propiedad busca conservar u obtener y, cuando sea útil, qué alternativa o fallo evita.
- Da prioridad al conocimiento operativo: qué es, qué permite hacer, cómo se usa o representa, qué necesita y cuándo deja de funcionar.
- Divide el recorrido en unidades cognitivas pequeñas. Cada unidad debe tener una idea principal reconocible y preparar de forma explícita la siguiente cuando exista una dependencia entre ambas.

## Visualización como recurso didáctico

**Default:** Durante el diseño de una explicación, clase, material de formación o ejemplo matemático, valora activamente si un diagrama, un gráfico o una representación interactiva mejora la comprensión de una estructura, dependencia, transformación, proceso o efecto de variar parámetros. Presta especial atención a conceptos espaciales, algoritmos, geometría, circuitos cuánticos, redes tensoriales, evolución de estados y relaciones entre expresiones y diagramas, pero no fuerces visualizaciones si no añaden comprensión.

- Prefiere una figura o diagrama estático cuando baste para mostrar una estructura; reserva controles, simulaciones y gráficos interactivos para casos en los que explorar estados o parámetros enseñe algo que una figura fija no comunica con igual claridad.
- Explica qué hay que observar, qué significa cada elemento o eje, qué parámetro puede cambiar y qué conclusión (y límite) se deduce. Mantén una explicación textual suficiente para comprender el caso inicial sin manipular controles.
- Usa los recursos visuales nativos del chat cuando estén disponibles y sean adecuados, sin exigir crear HTML, imágenes ni archivos para una explicación ordinaria. Cuando sí se solicite una experiencia HTML educativa, sigue `education/html_interactivo.md` y el contrato `htmls` correspondiente.
- No sustituyas la definición, la derivación o la demostración rigurosa por una animación atractiva. Evita diagramas ficticios, controles inertes y representaciones que distorsionen la notación o los datos.

## Repaso y autoevaluación dentro del chat

**Default:** Tras una unidad de aprendizaje significativa, un estudio de paper o una explicación con conceptos que merezcan consolidarse, considera proponer un repaso breve con tarjetas de pregunta/respuesta, una autoevaluación o un microejercicio interactivo nativo del chat. Úsalo cuando comprobar la comprensión aporte valor, no tras cada apartado ni como requisito previo para seguir. No interrumpas la explicación pendiente para insertar cuestionarios innecesarios.

- Las tarjetas deben evaluar definiciones, interpretación de notación, mecanismos, supuestos o errores típicos ya explicados; formula una pregunta antes de mostrar la respuesta y ofrece una corrección razonada, no solo acertado/fallado.
- Para una comprobación inmediata, usa pocas preguntas bien elegidas; evita formularios largos. Permite responder con texto cuando no estén disponibles tarjetas, botones u otros componentes nativos.
- No presupongas que el chat puede guardar una baraja en la biblioteca ni describas una interacción textual como un sistema persistente de repaso espaciado.
- Una respuesta equivocada orienta la siguiente aclaración, pero no altera automáticamente las fases o el avance del workflow. Para pasar a otra tanda siguen mandando sus reglas de continuación.

## Profundidad, rigor y límites

- Ajusta vocabulario, orden, ejemplos y detalle a la audiencia sin alterar la verdad factual.
- Señala de forma natural qué es un hecho, qué depende de condiciones, qué es una estimación o hipótesis y qué no está suficientemente documentado.
- No ocultes incertidumbre, limitaciones ni costes relevantes para que el texto resulte más simple o persuasivo.
- Para investigar, verificar fuentes, revisar evidencia actual o elaborar un estado del arte, aplica `research/00_core.md` y el flujo de `research/` que corresponda. No reproduzcas aquí ese protocolo.

## Entrega

Entrega en el medio solicitado. No crees archivos por defecto salvo que el flujo especializado exija o permita un artefacto de trabajo. Revisa que el orden sea comprensible, que cada sección cumpla una función didáctica y que la prosa no dependa de jerga, listas mecánicas ni tono promocional.

# Núcleo editorial para artículos del usuario actual

Abre este documento para cualquier tarea del dominio. Define las restricciones universales de los artículos técnicos y divulgativos; la arquitectura del argumento, la ejecución de la prosa y la revisión final se desarrollan en sus módulos específicos.

## Objetivo y lector

Explica un problema real, reconstruye su mecanismo delante del lector y corrige intuiciones imprecisas sin convertir el texto en una clase formal, un paper ni un manual.

El lector debe terminar con una comprensión más precisa: no solo debe recordar la conclusión, sino entender por qué es razonable, qué mecanismo la sostiene, qué supuestos intervienen y dónde están sus límites. Simplifica la ruta de entrada al problema, no el problema hasta deformarlo.

Escribe para una persona inteligente, curiosa y no necesariamente especialista en el subcampo. Puedes asumir cultura científica y tecnológica general cuando el contexto lo permita, pero no jerga especializada, convenciones internas, detalles de implementación ni acrónimos sin presentar. No infantilices al lector ni elimines la parte interesante del mecanismo. El texto debe resultar accesible para quien llega al tema y fiel al problema para quien ya lo conoce.

## Prioridades

Si dos criterios entran en conflicto, aplica este orden:

1. Exactitud técnica y honestidad epistémica.
2. Orden conceptual.
3. Claridad y legibilidad.
4. Adecuación del registro al público y a las preferencias expresas del usuario.
5. Concisión.
6. Ornamentación estilística.

La voz nunca se impone sobre la corrección. Un texto fluido que oculta supuestos, altera el mecanismo o presenta conceptos fuera de orden sigue siendo un mal artículo.

## Restricciones universales

### Orden conceptual y progresión

No uses un concepto técnico antes de presentarlo, salvo que sea evidente por el contexto y no requiera una definición concreta para seguir el razonamiento. Si comprender C depende de B y comprender B depende de A, presenta A antes de B y B antes de C.

Presentar un concepto puede consistir en una microdefinición cerca de su primer uso. Da lo mínimo necesario para interpretar lo que sigue y amplíalo después si el argumento lo exige. No sustituyas una progresión bien construida por un glosario inicial ni por definiciones enciclopédicas.

### Prosa conectada

La forma por defecto es la prosa continua. Evita listas, numeraciones y bloques visuales cuando una secuencia causal, una comparación o un conjunto de condiciones pueda explicarse con claridad en párrafos conectados. Una lista solo se justifica si mejora de forma real una comparación discreta, una consulta rápida, una taxonomía breve o un procedimiento cuyo orden sea esencial.

No conviertas el artículo en una colección de notas, diapositivas, listas de claves o secciones fragmentadas. Usa encabezados informativos cuando ayuden a navegar un texto medio o largo, sin interrumpir la continuidad cada pocos párrafos.

### Rigor ligero

No confundas precisión con densidad. Utiliza frases claras, definiciones locales, ejemplos pequeños y capas de profundidad. Introduce formalismo solo cuando haga visible una relación, permita una cuenta, condense un mecanismo o fije una definición que sería ambigua en lenguaje natural.

No conviertas el artículo en una revisión bibliográfica ni en un tratado completo salvo que la petición lo exija. Incluye las excepciones y detalles que cambien materialmente la interpretación, no todos los que demuestren conocimiento del campo.

### Crítica basada en mecanismos

Cuando cuestiones una idea, reconstruye primero su versión razonable y explica por qué resulta atractiva. Dirige la crítica al mecanismo, al supuesto o a la inferencia, no a la persona ni a una caricatura de la posición.

Haz visible qué tendría que ser cierto para sostener la conclusión y examina esas condiciones. Distingue entre imposible, no demostrado, sin algoritmo eficiente conocido, tecnológicamente inmaduro, económicamente poco sensato y posible solo bajo condiciones específicas. No uses una certeza más fuerte que la evidencia.

No presupongas que siempre existe una exageración que desmontar. El enfoque es crítico, no sistemáticamente negativo. Después de corregir una narrativa, reconstruye el espacio en el que la idea sí resulta válida o útil.

### Costes y trade-offs completos

No describas una técnica como más eficiente sin nombrar el recurso. Si reduce memoria pero aumenta tiempo, reduce qubits pero aumenta profundidad, mejora precisión pero requiere más muestras, o desplaza el coste hacia preparación de datos, lectura, comunicación o control de errores, muestra ambos lados.

Una ventaja no elimina un coste solo porque lo traslade. El lector debe entender qué se gana, qué se paga y bajo qué escala o arquitectura cambia el balance.

### Precisión epistémica y evidencia

Separa hechos, estimaciones, modelos, hipótesis y opiniones. Etiqueta las aproximaciones, explica por qué bastan para la conclusión y nombra los escenarios optimistas, pesimistas o simplificadores. Incluye la incertidumbre relevante en el razonamiento y reserva fórmulas como "esto demuestra" para implicaciones realmente sólidas.

Estas instrucciones de estilo no constituyen evidencia. No las uses para respaldar hechos, métricas, fuentes o conclusiones. Contrasta las afirmaciones mediante el dominio de investigación y respeta la trazabilidad exigida por la tarea.

### Matemáticas explicativas

Las matemáticas deben servir al texto. Prepara los objetos y la pregunta antes de introducir una fórmula; explica cada símbolo no evidente y traduce después la relación importante a lenguaje natural. Una ecuación mostrada no sustituye su explicación.

Usa bloques LaTeX delimitados por `$$` para las expresiones separadas del texto. Evita cadenas de ecuaciones sin orientación, pero conserva el formalismo que haga visible el mecanismo. El objetivo no es eliminar matemáticas, sino evitar matemáticas sin función narrativa o explicativa.

### Temas transversales

Una conexión con otra área es útil cuando explica un límite, corrige una confusión, conecta mecanismos o aporta una intuición necesaria para la tesis. Introdúcela porque el argumento la necesita, desarróllala solo hasta el nivel suficiente y regresa explícitamente al hilo principal.

Elimina o reduce las digresiones que no cambien la comprensión. Evita encadenar una digresión dentro de otra o permitir que un tema lateral compita con la tesis.

### Naturalidad y límites de estilo

Ajusta el tono, la formalidad y los recursos expresivos a la petición, el público y la plataforma. Conserva la responsabilidad técnica y evita afirmaciones sensacionalistas no respaldadas por la evidencia.

No presupongas una identidad estilística del autor original. Si se solicita una voz concreta, deriva sus rasgos de la petición y del material aportado por el usuario, sin comprometer la claridad ni la evidencia.

Prefiere una formulación española natural cuando mantenga la precisión. Conserva un término inglés si es la convención real del campo o su traducción resulta artificial, y explica su función cuando el lector pueda necesitarlo.

## Criterio de salida

El artículo debe leerse con fluidez en una primera pasada y revelar más detalle en una segunda. Al terminar, el lector debería poder explicar la intuición inicial, la pieza que faltaba, el mecanismo relevante, el principal límite o trade-off y la conclusión más precisa que sustituye a la primera intuición.

# Voz, pedagogía y ritmo

Abre este módulo al redactar o editar la prosa de un artículo cuya arquitectura ya está definida. Aplica el núcleo editorial sin reconstruir aquí el algoritmo del argumento.

**Default:** el destino final de los artículos del usuario actual es Medium salvo que el usuario indique otra plataforma, pero las reglas mecánicas de materialización no pertenecen a este módulo. Carga `publication_materialization.md` solo cuando haya que producir o revisar la versión lista para publicar.

## Voz configurable

Ajusta el registro, el grado de formalidad, la cercanía y la voz narrativa al público, al objetivo editorial y a las preferencias expresas del usuario. No reproduzcas por defecto la voz del autor original.

Mantén la distinción entre afirmaciones establecidas e incertidumbre. Las elecciones de voz no deben sustituir la precisión conceptual, la evidencia ni las explicaciones de los mecanismos.

## Relación con el lector

Acompaña el razonamiento y haz visibles relaciones causales y cambios de nivel. El lector debe reconocer cuándo aparece una definición, cuándo una intuición deja de bastar, cuándo surge un coste y por qué una conclusión se deriva de lo anterior.

Usa preguntas retóricas con moderación y solo si abren un problema que el texto resolverá pronto. Cuando cambies de escala, abstracción o disciplina, señala el paso.

## Párrafos y ritmo lógico

Prefiere párrafos cortos o medios organizados por unidades completas de razonamiento. Mantén juntas las frases que desarrollan una misma idea, consecuencia, ejemplo, contraste, condición o corrección y divide por función lógica, no por un número mecánico de líneas.

**Invariant:** no fragmentes una misma unidad de razonamiento en varios párrafos de una sola frase para producir ritmo, énfasis o apariencia de ligereza. Si dos párrafos consecutivos pueden unirse sin perder una transición conceptual real, un cambio de función o una mejora clara de comprensión, deben permanecer unidos. En prosa ordinaria no encadenes dos o más párrafos de una sola frase salvo que cada uno cumpla una función estructural distinta y justificable.

**Default:** la mayoría de los párrafos expositivos deben desarrollar su idea mediante varias frases relacionadas. Un párrafo de una sola frase es excepcional y debe aislarse solo cuando esa separación mejore materialmente la comprensión, no como recurso ornamental, de suspense o de énfasis repetitivo.

No introduzcas saltos de línea manuales dentro de la prosa continua. Usa líneas en blanco únicamente para separar párrafos, encabezados, fórmulas, bloques de código u otros bloques con función estructural real.

Antes de entregar un borrador completo o una versión pulida, recorre cada sección y revisa su topología de párrafos: fusiona fragmentos que pertenecen al mismo razonamiento, elimina secuencias de párrafos telegráficos y comprueba que los cierres de sección no se degraden en frases aisladas. Alterna densidad mediante ejemplos, reformulaciones o consecuencias dentro de una prosa conectada, no multiplicando saltos de párrafo.

## Definiciones y conceptos

Prioriza qué ocurre y por qué frente a definiciones abstractas desconectadas. Coloca las definiciones cerca del primer uso real y empieza por una formulación operativa que explique función o propiedad relevante antes de añadir precisión formal.

No apiles conceptos nuevos dependientes en una misma frase. Si una idea es importante o contraintuitiva, reformúlala desde otra perspectiva solo cuando esa segunda formulación aporte un modelo mental o reduzca una ambigüedad.

**Default:** cuando un concepto técnico o científico importante se introduzca por primera vez de manera explicativa y vaya a reutilizarse, destaca su nombre en **negrita**. No marques cada término técnico ni uses la negrita como énfasis retórico general.

## Analogías y ejemplos

Usa analogías breves que conserven la relación relevante. Vuelve después al sistema real y explica qué corresponde a qué; una analogía no sustituye el mecanismo.

Presenta los ejemplos ya seleccionados de forma transparente. Indica qué representa cada elemento y qué relación debe observar el lector. Cuando uses valores aproximados, explica qué conclusión continúa siendo válida pese a la aproximación.

## Números y matemáticas durante la redacción

Presenta las cuentas de modo que el lector entienda qué se calcula, con qué unidades y cómo se interpreta el resultado. Usa números concretos cuando sustituyan adjetivos vagos, pero evita convertir cada artículo en un ejercicio de Fermi.

Toda ecuación importante debe tener una función narrativa: prepara la pregunta u objeto antes, define símbolos no evidentes y traduce después la relación a lenguaje natural. Cuando una ecuación defina, calcule o relacione una magnitud, muestra la relación completa e identifica explícitamente la cantidad cuando omitirla obligaría al lector a inferirla.

**Invariant:** integra cada ecuación, inline o separada, como parte gramatical de la oración. No uses dos puntos únicamente porque venga una fórmula; conserva la puntuación que corresponda antes y después de la expresión.

Durante borrador y pulido usa una notación clara y no ambigua sin gastar trabajo en adaptar todavía cada expresión al soporte final. La conversión a Unicode copiable, los marcadores de renderizado y demás reglas de Medium pertenecen a `publication_materialization.md`.

## Referencias, citas e hipervínculos

**Default:** no insertes referencias numéricas `[1]`, `[2]` ni una bibliografía final salvo que el usuario las pida. Integra autores, trabajos, fechas o experimentos de forma natural y usa hipervínculos contextuales cuando una fuente externa relevante respalde, amplíe o permita verificar una afirmación concreta.

**Invariant:** cuando una fuente material ya esté verificada y disponga de una URL estable, conserva su vínculo con el texto mediante un hipervínculo contextual sobre el autor, trabajo, concepto o afirmación más natural. No redactes primero una versión que dependa de fuentes y después pierdas esos enlaces al pulirla. Las referencias propias que el usuario haya pedido conectar con el artículo también deben conservar su enlace verificado cuando permanezcan en el texto.

**Invariant: integración narrativa.** El hipervínculo debe formar parte de una oración que ya cumpla una función narrativa o argumentativa en el párrafo. No coloques como línea o párrafo independiente un título, nombre de paper, autor, vídeo, artículo propio o texto de enlace únicamente para adjuntar su URL. Tampoco añadas después de una afirmación una segunda línea que repita el nombre de la fuente enlazada. Si merece nombrarse el trabajo, intégralo gramaticalmente en la frase que explica qué aporta, demuestra, amplía o documenta. Si solo hace falta respaldar una afirmación, enlaza directamente la formulación natural de esa afirmación o el nombre del autor dentro de la prosa. El artículo no debe adquirir apariencia de bibliografía incrustada por la colocación de sus enlaces.

Prioriza papers originales, documentación oficial y otras fuentes primarias cuando estén disponibles. No enlances afirmaciones triviales ni satures el artículo de referencias. La materialización final para Medium debe aplicar además la auditoría de cobertura e integración narrativa de hipervínculos definida en `publication_materialization.md`.

## Encabezados, listas y títulos

Los encabezados deben anticipar la pregunta, concepto, cuello de botella o microtesis de la sección. No conviertas cada cambio de párrafo en una sección.

Mantén la prosa como forma principal. Reserva las listas para comparaciones discretas, taxonomías breves, procedimientos consultables o resúmenes donde la estructura sea realmente superior. Cuando una lista esté justificada, mantenla breve y vuelve después a la prosa.

Los títulos pueden contener una pregunta, tensión, promesa concreta de comprensión o trade-off. Evita clickbait y afirmaciones más absolutas que la tesis.

## Densidad, crítica y cierres

No exijas esfuerzo máximo de forma continua. Después de varios conceptos nuevos, ofrece una zona de consolidación. Incluye excepciones que cambien la interpretación y formula brevemente las precisiones laterales.

Expresa la crítica con lenguaje analítico y no combativo. Ajusta verbos y grado de certeza a la evidencia construida; una conclusión firme no necesita dramatización.

Cuando ayude, termina una sección con una microtesis que condense su consecuencia. No busques una frase memorable en cada bloque ni conviertas cada cierre en un eslogan.
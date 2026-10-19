# Materialización y postproducción de publicación

Usa este contrato solo cuando un artículo deba convertirse en una versión lista para publicar o cuando el flujo iterativo alcance las fases de postproducción. **Default:** los artículos del usuario actual se preparan para Medium salvo que el usuario indique explícitamente otra plataforma.

No cargues este módulo durante la arquitectura, el primer borrador o el pulido ordinario. En `#BLOG`, cárgalo a partir de la fase 4 y reutilízalo en las fases 5–7. En una petición natural no iterativa, cárgalo únicamente cuando el usuario pida una versión final lista para publicar o cuando la entrega final deba materializarse para Medium.

Si el usuario especifica otra plataforma, conserva las reglas editoriales generales de `00_core.md` y `02_voz_pedagogia_y_ritmo.md`, pero sustituye únicamente las reglas de formato o metadatos propias de Medium por las del destino indicado.

## Versión final para Medium

La versión lista para Medium debe poder copiarse y pegarse con la menor reconstrucción manual posible. No incluyas notas de proceso dentro del cuerpo publicable.

### Números y notación copiable

- Los números ordinarios en prosa se escriben como texto normal: `1948`, `0.1`, `13 pascales` o `100 nanómetros`.
- Para matemáticas inline, prefiere símbolos Unicode y notación directamente copiable cuando sean claros y estables, por ejemplo `π`, `ħ`, `ω`, `a⁴`, `1/a⁴`, `10¹⁰` o `n = 0`.
- **Invariant para exponentes numéricos:** cuando la base o el exponente contengan varios dígitos, conserva cada número como una unidad visual y semántica. Usa una representación Unicode completa y estable cuando exista, por ejemplo `10¹⁰` o `2³²`; si no, usa una forma textual inequívoca como `10^10`. No compongas un exponente mediante formatos parciales que puedan separar o reordenar dígitos.
- **Default para subíndices simples:** usa Unicode cuando exista una representación completa y estable, por ejemplo `D₀`, `E₀` o `xᵢ`. Usa `D_0` o `x_i` como fallback cuando Unicode no sea adecuado para todo el subíndice.
- **Default:** presenta ecuaciones y símbolos matemáticos en cursiva cuando el formato de salida lo permita sin alterar el símbolo, la copia o la legibilidad.

### Ecuaciones que requieren renderizado

**Invariant:** si límites, subíndices, superíndices, fracciones, sumatorios, integrales, casos u otra estructura matemática no pueden representarse limpiamente en texto/Unicode, no presentes una notación degradada como definitiva. Coloca inmediatamente antes de la expresión, en una línea independiente, el marcador exacto:

`>>>>>>>>>> LATEX`

Debajo conserva una versión textual o Unicode suficientemente explícita para identificar sin ambigüedad la ecuación que debe renderizarse. No insertes LaTeX bruto como parte publicable de la versión final para Medium.

Mantén fuera del cuerpo publicable un registro ordenado de cada marcador con su expresión LaTeX canónica y una posición inequívoca. Las reglas generales de significado, símbolos, igualdad completa y puntuación de las ecuaciones siguen perteneciendo a `02_voz_pedagogia_y_ritmo.md`.

### Hipervínculos y URLs

- Usa hipervínculos reales sobre texto de anclaje natural y descriptivo cuando el soporte los conserve al copiar y pegar.
- Si un hipervínculo no puede conservarse de forma fiable, coloca la URL canónica entre paréntesis inmediatamente después del fragmento, nombre o afirmación a la que corresponde.
- No uses marcadores `[LINK n]`, URLs desnudas desplazadas al final del párrafo ni tablas posteriores de correspondencia.
- Enlaza la URL canónica más limpia que conserve el destino y los parámetros funcionalmente necesarios. Elimina `utm_source=chatgpt.com` y otros parámetros de seguimiento prescindibles; no retires parámetros necesarios para navegación, consulta o identificación.

**Invariant: integración narrativa de hipervínculos.** Todo enlace material debe quedar embebido en la oración que ya explica por qué esa fuente, autor, trabajo, vídeo o artículo es relevante. No dejes títulos o nombres enlazados en una línea independiente, no añadas un párrafo formado únicamente por un hipervínculo y no repitas debajo de una afirmación el título enlazado de la fuente como si fuera una referencia bibliográfica. Si el nombre del trabajo aporta contexto, intégralo dentro de la frase; si no lo aporta, enlaza la afirmación, autor o concepto natural que la fuente respalda. La materialización final debe conservar una narrativa continua y no parecer una bibliografía insertada entre párrafos.

**Invariant: cobertura de hipervínculos.** Antes de considerar el artículo listo para publicar, recorre de arriba abajo todas las afirmaciones materiales, autores, trabajos, datos, resultados y referencias propias que dependan de una fuente verificada. Cuando exista una URL estable y el enlace aporte trazabilidad o ampliación útil, debe quedar al menos un hipervínculo contextual sobre el ancla natural correspondiente. No sustituyas esta integración por citas del chat, una lista de fuentes al final, URLs entregadas aparte ni la mera existencia de una fuente en el estado interno.

Si una misma fuente respalda varias frases contiguas, un único enlace bien colocado puede bastar; no enlaces cada repetición. Si decides no insertar un enlace verificado porque sería redundante, trivial o perjudicaría claramente la lectura, conserva la decisión de forma explícita fuera del cuerpo durante la revisión. Una versión de Medium que dependa materialmente de fuentes pero haya perdido sus hipervínculos durante el pulido o la materialización no está terminada.

### Separadores y revisión de copia

**Default para Medium:** antes de cada nueva sección principal del cuerpo, inserta una regla horizontal Markdown `---` en una línea independiente y después el encabezado. No la coloques antes del título ni entre párrafos de una misma sección.

## Auditoría final de publicación

Después de aplicar formato, enlaces y notación, realiza una última auditoría sobre la versión exactamente materializada:

1. **De abajo arriba:** revisa las últimas secciones primero para detectar párrafos de una sola frase, secuencias telegráficas, enlaces perdidos, cierres degradados, separadores mal colocados y restos de formato.
2. **De arriba abajo:** relee el artículo en orden natural para comprobar continuidad, densidad de párrafos, integración narrativa y contexto de los hipervínculos, y experiencia de copia/publicación.
3. Comprueba que no queden LaTeX bruto publicable, marcadores `[LINK n]`, parámetros de tracking prescindibles ni ecuaciones cuya estructura se haya degradado.
4. Comprueba la cobertura de hipervínculos contra el conjunto de fuentes verificadas realmente utilizadas en el artículo y contra las referencias propias solicitadas por el usuario.
5. Comprueba que no exista ningún título, paper, vídeo, autor o artículo enlazado como línea o párrafo huérfano únicamente para adjuntar una URL; integra esos casos en la prosa antes de cerrar.

**Invariant:** no cierres la materialización si reaparecen dos o más párrafos consecutivos de una sola frase en prosa ordinaria sin funciones estructurales distintas, si una fuente material ha perdido su enlace contextual sin justificación, si persisten hipervínculos bibliográficos huérfanos fuera de la narrativa, o si el artículo requiere reconstrucción manual evitable antes de publicarlo.

## Fase 5 de `#BLOG`: renderizado de ecuaciones

Activa esta fase únicamente para los marcadores `>>>>>>>>>> LATEX` registrados al cerrar la fase 4. Si falta una expresión canónica o existe ambigüedad material, mantén la fase bloqueada; no inventes notación.

**Invariant:** genera un archivo independiente por ecuación, no una hoja ni collage. Usa preferentemente un renderizador matemático determinista, fondo blanco puro, ecuación negra, márgenes razonables y nitidez suficiente. Exporta por defecto como PNG con nombres estables como `eq-01.png` y verifica cada render contra su LaTeX canónico.

Entrega los archivos por separado y una correspondencia breve con su posición. Un ZIP adicional puede ser comodidad, nunca sustituto. No regeneres el artículo completo.

## Fase 6A de `#BLOG`: planificación visual

Activa esta subfase siempre que el usuario no haya pedido prescindir de imágenes. Su objetivo es decidir **qué imágenes merecen existir y dónde**, no generarlas.

**Invariant:** durante 6A no llames a ninguna herramienta de generación de imágenes.

### Qué debe planificarse

Para Medium, el plan incluye una **portada** y solo las imágenes del cuerpo que aporten comprensión material. Puede haber 0 imágenes de cuerpo si ninguna mejora realmente el artículo; como referencia normal, usa entre **1 y 3 imágenes del cuerpo** cuando cada una tenga una función distinta.

Una imagen del cuerpo supera el gate únicamente si hace visible al menos una pieza que la prosa comunica peor: un mecanismo, una comparación, una secuencia, una estructura, una escala, un trade-off, una relación matemática, una taxonomía o un criterio de decisión. Descarta cualquier candidato que sea principalmente decorativo, atmosférico, una repetición del título, una colección de iconos o una escena genérica asociada al tema.

Para cada recurso propuesto registra y muestra al usuario:

1. función narrativa y pregunta concreta que resuelve;
2. punto exacto de inserción en el artículo;
3. contenido visual y relación que debe quedar clara;
4. **texto, etiquetas, símbolos o ecuaciones exactos** que deben aparecer;
5. por qué esa imagen aporta comprensión adicional y no solo decoración.

La portada también debe tener una función informativa: identificar con claridad el tema o la distinción central del artículo. Puede contener el título o una formulación breve equivalente y un recurso visual simple; no debe ser una escena bonita sin información.

El plan presentado en 6A es el contrato de generación para 6B. Las correcciones del usuario se incorporan al plan antes de avanzar.

## Fase 6B de `#BLOG`: generación visual

Genera únicamente los recursos aprobados en 6A. No añadas imágenes, variantes ni composiciones nuevas por iniciativa propia.

### Reglas de producción

**Invariant:** todas las imágenes, tanto portada como cuerpo, deben generarse mediante una herramienta de generación de imágenes. No uses Python, matplotlib, SVG, HTML, Canvas, plotting, librerías de diagramación ni composición programática.

**Invariant:** cada imagen se genera y entrega como **archivo independiente**. No agrupes portada e imágenes del cuerpo en una sola lámina, cuadrícula, collage o imagen maestra.

**Default para Medium:** usa formato horizontal o moderadamente apaisado, composición clara y **fondo blanco**. La jerarquía debe leerse bien al ancho habitual de un artículo de Medium, sin depender de detalles diminutos.

Las imágenes del cuerpo deben ser explicativas antes que bonitas. Prioriza esquemas, comparaciones, relaciones y composiciones simples. Se permiten dos columnas, pasos o paneles cuando esa estructura sea precisamente lo que explica la idea, pero cada imagen debe desarrollar **una sola idea principal**.

**Invariant:** las imágenes del cuerpo deben incluir texto explicativo, etiquetas, símbolos o ecuaciones cuando esos elementos sean parte de la comprensión prevista en 6A. No elimines texto útil para conseguir una estética más limpia. El texto debe ser breve, legible y funcional; evita párrafos largos dentro de la imagen.

La portada puede usar menos texto que una imagen de cuerpo, pero debe comunicar de forma inequívoca el tema central. Si el plan aprobado incluye título o subtítulo, consérvalos.

Evita recursos que produzcan apariencia de *AI slop*: fondos oscuros o futuristas, neón, hologramas, partículas, ciencia ficción genérica, criostatos o átomos usados solo como decoración, escritorios de stock, paisajes épicos, interfaces ficticias, exceso de brillo, iconos acumulados o composiciones espectaculares que no enseñan nada.

### Generación y revisión secuencial

**Invariant:** genera un recurso cada vez y revísalo antes de pasar al siguiente. No lances una tanda de imágenes sin inspeccionar los resultados intermedios.

Antes de aceptar cada imagen, comprueba:

1. que responde exactamente a la función narrativa fijada en 6A;
2. que todo texto, símbolo y ecuación visible es correcto y legible, incluidos acentos, `ñ`, signos, números, unidades y notación matemática;
3. que el fondo es blanco y la composición funciona en formato Medium;
4. que no introduce elementos decorativos o relaciones que no estaban en el plan;
5. que puede insertarse en el artículo sin explicación adicional para justificar su presencia.

Si falla cualquiera de estos puntos, corrige o regenera **solo ese recurso**. No continúes con el siguiente hasta que el actual sea válido. Si una imagen aprobada en 6A resulta imposible de representar con suficiente claridad mediante generación generativa, no la sustituyas por una imagen decorativa: informa del problema y conserva la explicación en la prosa.

Entrega la portada como recurso compartido de Medium/LinkedIn y cada visual del cuerpo por separado con su punto de inserción y texto alternativo breve. No rehagas el artículo.

## Fase 7 de `#BLOG`: distribución

Esta fase prepara distribución y no modifica el artículo.

Para Medium por defecto:

1. redacta un resumen orientado a SEO de un máximo de 140 caracteres, centrado en la pregunta, mecanismo o conclusión principal;
2. redacta un post de LinkedIn listo para compartir el artículo, con contexto suficiente y sin convertirlo en un índice comentado;
3. ajusta el tono al público, la plataforma y las preferencias editoriales expresas del usuario; evita afirmaciones no verificadas y elementos de distribución no solicitados;
4. usa una URL solo cuando exista y esté verificada; no inventes marcadores ficticios;
5. **Default:** cuando el post de LinkedIn comparta un artículo, utiliza un cierre coherente con el tono solicitado y la plataforma; no impongas una fórmula de despedida personal del autor original.

Si el usuario ha indicado otra plataforma de publicación, sustituye el resumen específico de Medium por el metadato equivalente que esa plataforma realmente necesite; conserva el texto de LinkedIn salvo que el usuario lo excluya.

Entrega primero el resumen o metadato de publicación y después el texto de LinkedIn, claramente separados y listos para copiar. No repitas el artículo ni regeneres recursos.
# Revisión final de un artículo

Abre este módulo solo al revisar un borrador completo o antes de entregar un artículo. Usa `00_core.md` y los módulos de arquitectura y voz que hayan gobernado el borrador como autoridad; este módulo define el método de revisión y comprueba desviaciones observables sin volver a copiar sus contratos editoriales.

Si la entrega debe quedar lista para publicación, aplica `publication_materialization.md` después de las pasadas editoriales. Medium es el destino predeterminado salvo que el usuario haya indicado otro.

## Orden de revisión

Realiza tres pasadas sobre el artículo completo antes de entregarlo:

1. **Factual y conceptual, de arriba abajo:** comprueba hechos, cifras, enlaces, DOI, relaciones técnicas, mecanismo, supuestos y correspondencia entre afirmaciones y evidencia. Corrige alcance o certeza cuando la evidencia no sostenga la formulación.
2. **Editorial y formal, de abajo arriba:** empieza por la última sección y avanza hasta la introducción; dentro de cada sección revisa primero sus últimos párrafos. Aplica `02_voz_pedagogia_y_ritmo.md` buscando especialmente degradación acumulada, párrafos de una sola frase, secuencias telegráficas, cierres débiles, transiciones huérfanas, repeticiones y enlaces desplazados. Reagrupa localmente lo que pertenezca a una misma unidad de razonamiento.
3. **Coherencia y lectura, de arriba abajo:** relee el texto completo en su orden natural después de las correcciones locales. Comprueba que las fusiones de párrafos, recortes y ajustes anteriores no hayan creado saltos conceptuales, paredes de texto, referencias sin contexto ni cambios bruscos de ritmo. Esta pasada valida la experiencia real de lectura y el cierre del argumento.

**Invariant:** no omitas ninguna de las dos direcciones de revisión editorial. La pasada de abajo arriba evita que la atención se degrade en las últimas secciones; la pasada final de arriba abajo verifica que las correcciones locales sigan formando un artículo coherente como conjunto. Corrige localmente lo necesario y no reescribas por sistema lo que ya funciona.

## Lista de control compacta

- **Argumento y pedagogía:** orden conceptual, continuidad entre secciones, densidad razonable, definiciones antes de uso, mecanismo visible, supuestos/trade-offs relevantes y cierre que responda a la pregunta inicial.
- **Evidencia:** toda afirmación material debe conservar el alcance y grado de certeza que permiten sus fuentes. Verifica datos concretos y enlaces usados; no conviertas una estimación o modelo en hecho.
- **Matemáticas:** cada fórmula debe corresponder exactamente a la afirmación, conservar miembros y magnitudes, definir símbolos necesarios e integrarse gramaticalmente en la oración según `02_voz_pedagogia_y_ritmo.md`. No hagas aquí una segunda conversión al formato de plataforma.
- **Publicación:** cuando la salida deba quedar lista para publicar, delega en `publication_materialization.md` la notación copiable, los marcadores `>>>>>>>>>> LATEX`, hipervínculos, URLs, separadores y comprobaciones específicas del destino. No dupliques esas reglas en esta checklist.
- **Naturalidad:** revisa de forma ligera calcos del inglés y morfología técnica poco natural en español de España sin castellanizar términos cuya forma inglesa sea la convención real del campo.
- **Ritmo y topología de párrafos:** no aceptes secuencias de dos o más párrafos de una sola frase en prosa ordinaria salvo que cada bloque tenga una función estructural distinta y justificable. Fusiona frases aisladas con el párrafo que desarrolla su misma idea y comprueba también los dos últimos párrafos de cada sección, donde es más frecuente que aparezca fragmentación residual.

## Diagnóstico

Aligera cuando haya demasiadas dependencias, digresiones, formalismo sin función o contexto lateral; profundiza cuando aparezcan conclusiones sin mecanismo, escalas sustituidas por adjetivos, términos sin función explicada o analogías que reemplazan la explicación real. Ninguna de las dos operaciones justifica eliminar rigor ni añadir jerga por sí misma.

Antes de entregar, comprueba que el lector pueda reconstruir la intuición inicial, el mecanismo, el principal límite o trade-off y la conclusión corregida sin tener que recomponer el artículo mediante varias relecturas.
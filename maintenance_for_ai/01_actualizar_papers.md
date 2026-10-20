# Actualizar papers

Usa este procedimiento para mantener `info_for_ai/info_user/papers.csv`.

**Invariant:** Before any discovery or write, verify the configured user identity, writable private knowledge destination and the user's authorization. Never infer the publication author from the public upstream or an empty catalog. If any prerequisite is missing, stop and request the missing information.

## Objetivo

Añadir trabajos que falten y actualizar únicamente metadatos que hayan cambiado de forma material, especialmente título vigente, fecha de versión/publicación, DOI, venue y estado de publicación.

## Alcance

**Default:** Conserva el alcance explícito de la petición. Si el usuario identifica uno o varios trabajos concretos, inspecciona únicamente esos trabajos, sus identificadores y las fuentes necesarias para verificarlos. Haz descubrimiento global del perfil bibliográfico solo cuando se solicite una sincronización general o cuando sea imprescindible para resolver identidad, duplicados o pertenencia a una misma familia bibliográfica.

## Semántica cronológica y orden del catálogo

**Invariant:** `año` representa el año de la última versión o publicación documentada del trabajo. Cuando `fecha_ultima_version_o_publicacion` esté informada, `año` debe coincidir con el año de esa fecha.

**Invariant:** `año_primera_version_o_publicacion` conserva el primer año documentado de la familia bibliográfica. Usa la primera versión arXiv o la primera publicación verificable, según exista; si no hay evidencia para distinguir un año inicial anterior, usa el mismo valor que `año` y no lo infieras.

**Invariant:** `tipo_publicacion` usa únicamente `revista`, `conferencia` o `preprint`. Un trabajo que tenga además versión arXiv se clasifica por su publicación formal cuando exista: revista antes que conferencia, y solo como preprint cuando no haya publicación formal documentada.

**Invariant:** Mantén las filas ordenadas por estas claves, en este orden:
1. `año`, descendente;
2. `tipo_publicacion`, con prioridad `revista` > `conferencia` > `preprint`;
3. `fecha_ultima_version_o_publicacion`, descendente dentro del mismo tipo.

Cuando falte la fecha exacta, conserva el año documentado y coloca esa fila después de las filas con fecha exacta dentro del mismo año y tipo. Si dos filas comparten todas esas claves, su orden relativo no es significativo.

## Identificación y fuentes

No relaciones trabajos solo por similitud de título. Prioriza identificadores estables como arXiv ID y DOI, y usa combinación de autores/título/año solo como apoyo cuando falten identificadores.

Orden de uso de fuentes:

1. Google Scholar para descubrir trabajos o detectar diferencias generales en el perfil de autor.
2. arXiv para título vigente de la versión arXiv, autores, identificador, DOI de arXiv y fecha de versión.
3. DOI, editorial, revista o actas oficiales para título definitivo publicado, venue, DOI y estado de publicación.
4. ResearchGate como fuente secundaria de descubrimiento o contraste, nunca por encima de arXiv o la publicación oficial para los campos que estas controlan.

## Procedimiento

1. Lee el CSV actual y construye claves por arXiv ID o DOI suficientes para el alcance seleccionado.
2. En una sincronización general, busca nuevos trabajos asociados al autor y contrástalos con el catálogo. En una actualización focalizada, limita la búsqueda a los trabajos indicados y a las comprobaciones necesarias para identificarlos correctamente.
3. Para registros existentes, revisa solo señales de cambio: nueva versión de arXiv, título modificado, aparición de DOI/venue o paso de preprint a publicación.
4. Añade solo trabajos ausentes. No dupliques una versión publicada y su preprint si representan la misma familia; conserva ambos identificadores en la misma fila cuando proceda.
5. Si cambia el título, usa el vigente en `titulo_actual` y conserva el anterior en `notas` si ayuda a reconocer referencias antiguas.
6. No reescribas autores, notas o URLs que sigan siendo correctos solo para homogeneizar estilo.
7. Después de cualquier alta o cambio de versión/publicación, actualiza `año`, `año_primera_version_o_publicacion` y `tipo_publicacion` cuando corresponda, y vuelve a aplicar el orden cronológico definido arriba.
8. Si el cambio altera vistas editoriales o hechos trazables sobre publicaciones, actualízalos solo cuando esos documentos hayan quedado realmente desfasados.
9. Ejecuta las validaciones del repositorio y revisa el diff del CSV para confirmar que solo aparecen filas nuevas, reordenaciones exigidas por el contrato o campos justificadamente modificados.

Si una fuente discrepa con otra, conserva la fuente primaria que controla ese metadato y documenta la discrepancia cuando sea relevante.

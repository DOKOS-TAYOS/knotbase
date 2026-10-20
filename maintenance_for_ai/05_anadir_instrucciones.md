# Añadir nuevas instrucciones

Usa este procedimiento cuando el usuario proporcione una o varias instrucciones nuevas, aunque vengan en una lista enumerada con subapartados.

`00_core.md` gobierna fuente canónica, cambio mínimo, reutilización, propagación, Codex, tests, validación, diff y logbook. Aquí se define únicamente cómo incorporar responsabilidades nuevas con estructura mínima y recuperable.

## Procedimiento

1. Trata la lista del usuario como requisitos, no como una obligación de crear un archivo por punto.
2. Busca primero un dominio, core o módulo que ya tenga la responsabilidad y agrupa requisitos relacionados en el menor número coherente de owners.
3. Crea un módulo nuevo solo si la responsabilidad es suficientemente distinta para justificar una ruta propia; crea un dominio nuevo únicamente si no encaja razonablemente en ninguno existente.
4. Mantén cada módulo enfocado en qué comportamiento controla y cuándo se selecciona. La descripción del índice debe ser recuperable por intención, no solo por el nombre interno del archivo.
5. **Default:** Reserva `00_core.md` para el núcleo compartido. Usa prefijos numéricos en la colección principal cuando ayuden a lectura estable; para auxiliares o transversales prefiere nombres semánticos sin numeración. Crea subdirectorios solo cuando agrupen varias responsabilidades reales y no renumeres una serie estable solo para insertar una instrucción.
6. Actualiza router, índices o responsabilidades solo cuando la estructura nueva lo requiera. Antes de cerrar, comprueba si la misma capacidad podía expresarse con menos archivos o reglas sin perder localización ni claridad.

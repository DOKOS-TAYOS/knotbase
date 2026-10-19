# Renderizado y entrega de CV estándar sin plantilla obligatoria

## Activación

Carga este contrato únicamente cuando comience la fase 2 de un CV estándar o cuando un reajuste local ya autorizado requiera generar, maquetar o verificar un CV estándar. No lo cargues durante la fase 1 estratégica.

La estrategia, evidencia, privacidad, publicaciones y prioridades editoriales pertenecen a `00_core.md`; la creación o reajuste concreto pertenece a `01_crear_cv.md` o `02_reajustar_cv.md`. Este archivo controla materialización, assets, composición, formatos y verificación del CV estándar.

## Formato de salida

**Default:** Si el usuario no especifica formato, entrega PDF generado directamente desde el HTML semántico preparado para el CV. Si pide HTML, entrega ese HTML final. Si pide DOCX, materializa una versión editable con el mismo contenido, orden, enlaces y estructura aprobados, mediante conversión desde HTML u otro método fiable que no exija plantilla. No generes DOCX por defecto ni lo uses como paso intermedio obligatorio para producir PDF.

**Invariant:** Diseña el HTML de cada candidatura a partir de la estrategia y de evidencia verificable. No existe una plantilla HTML, DOCX, paleta, icono, logo ni catálogo de assets obligatorio. No cargues los recursos privados de DIK ni presupongas una base personal instalada en Knotbase.

**Invariant:** Genera PDF directamente a partir del HTML terminado cuando el entorno disponga de una herramienta compatible. Inspecciona el PDF final renderizado y corrige desplazamientos, líneas rotas, recortes, solapamientos o cualquier fallo visible antes de entregar. Si no puede generarse o inspeccionarse, indica con precisión qué verificación queda pendiente.

**Invariant:** Cuando se solicite DOCX, genera un archivo editable desde el mismo contenido y orden de lectura; conserva hipervínculos, títulos, jerarquía y estructura, e inspecciona su render final. Los ajustes específicos de Word no deben alterar la estrategia de evidencia aprobada.

## HTML autosuficiente y recursos opcionales

**Invariant:** Construye un HTML semántico autónomo y accesible para la candidatura, sin depender de un HTML canónico preexistente. Organiza la información en `main`, `header`, `section`, encabezados jerárquicos, entradas con organizaciones y fechas próximas, y enlaces reales. Utiliza estilos locales y reglas de impresión A4 sin imponer un diseño personal heredado.

**Invariant:** La fuente factual es el material que el usuario haya aportado o autorizado, no un documento de ejemplo. No incorpores nombres, contactos, experiencia, perfiles ni resultados predeterminados, y elimina todos los placeholders antes de exportar.

**Invariant:** Si se generan varios formatos, mantén la selección de evidencia, estructura editorial, enlaces y semántica de contacto de la estrategia aprobada. El HTML es la referencia de estructura para el PDF; el DOCX puede generarse mediante un método editable equivalente cuando una conversión directa no sea fiable.

**Default:** No son obligatorios iconos, logos, fotografías, fuentes especiales, colores prefijados ni archivos del índice de assets. Cuando el usuario solicite un recurso visual, usa solo un archivo disponible y autorizado cuya procedencia y derechos puedan comprobarse; la falta de ese recurso no debe bloquear un CV legible sin él.

## Arquitectura visual

Principios de composición de un CV estándar accesible:

- nombre dominante y posicionamiento profesional breve;
- enlaces a perfiles públicos verificados solo cuando sean pertinentes y autorizados;
- jerarquía clara entre cargo, organización, fechas y descripción;
- secciones escaneables con jerarquía visual coherente, sin iconografía obligatoria;
- arquitectura robusta y fácil de extraer;
- densidad suficiente sin convertir la página en un muro de texto;
- bloques finales diferenciados para investigación/publicaciones, software, formación, comunicación/docencia, reconocimientos e idiomas cuando mejore la lectura.

### Contacto y perfiles opcionales

**Invariant:** Incluye solo ubicación y medios de contacto confirmados y autorizados por el usuario para esa candidatura. No presupongas correo, teléfono, nacionalidad, nombre de empleador, ni presencia de perfiles específicos. Un dato ausente se omite en lugar de rellenarse con un ejemplo.

Cuando haya correo y teléfono autorizados, usa enlaces `mailto:` y `tel:` válidos, con texto seleccionable. Mantén cada dato y su identificador juntos para facilitar lectura y extracción de texto.

Los perfiles externos son opcionales y se enlazan solo cuando hayan sido verificados y aporten valor. Si se incluyen logos o iconos, deben tener procedencia legítima, no alterar identidades de marca y no reemplazar información imprescindible en texto.

### Iconografía y consistencia

**Default:** Usa una tipografía legible, jerarquía consistente, separaciones y reglas visuales que permitan explorar el CV con facilidad. Los encabezados no deben quedar huérfanos al final de página; no dependen de una familia de iconos predeterminada.

Aplica la misma gramática a entradas del mismo tipo: jerarquía, alineación, sangría, separación, viñetas, puntuación y fechas.

### Pie, densidad y paginación

**Invariant:** El pie muestra únicamente el número de página. No incluyas nombre, puesto, empresa, vacante, metadatos ni fecha de generación.

**Default:** No comprimas evidencia prioritaria mientras queden grandes huecos ni fuerces saltos que dejen media página vacía.

Si queda un hueco inferior materialmente grande, corrígelo en este orden: (1) elimina saltos o espaciados accidentales; (2) amplía con evidencia sustantiva un pilar aprobado que haya quedado demasiado comprimido; (3) incorpora la siguiente evidencia ya aprobada que aporte valor real; (4) acepta el espacio si llenarlo empeoraría relevancia, legibilidad o jerarquía. Nunca rellenes con contenido irrelevante ni infles tipografía, márgenes o espaciado para disimularlo.

Las competencias deben ser compactas y selectivas. No repitas exhaustivamente tecnologías ya demostradas en experiencia, investigación o software.

## Hipervínculos, fotografía y ATS

Usa hipervínculos limpios para papers, repositorios, software, demos, charlas, premios y otras evidencias públicas cuando aporten valor. Para certificaciones o badges verificables enlaza al menos los más relevantes. No inventes enlaces.

**Invariant:** Si se generan varios formatos, los elementos enlazables conservan el mismo destino y papel visual siempre que el formato lo permita.

La fotografía es opcional. Úsala solo cuando la persona usuaria la aporte o autorice expresamente y exista una procedencia adecuada; no presupongas una biblioteca de retratos ni un índice de assets.

Mantén la información esencial como texto real y un orden de lectura claro. Evita estructuras frágiles, texto invisible o información profesional esencial solo en imágenes.

**Invariant:** Cuando la entrega incluya PDF, ejecuta un preflight ATS mediante extracción de texto nativa, no OCR. Confirma que nombre, contacto, secciones, cargos o titulaciones, organizaciones, fechas y descripciones aparecen en secuencia lógica y suficientemente próximos para que un parser pueda asociarlos correctamente.

**Invariant:** No dependas de columnas, grids o posicionamiento visual para relacionar campos que un ATS deba leer juntos. Si la extracción intercala columnas, separa fechas de sus entradas o agrupa primero todos los títulos y después todas las organizaciones, corrige la estructura fuente y regenera el PDF.

**Invariant:** Cuando la entrega incluya DOCX, renderiza e inspecciona visualmente el DOCX final derivado; no des por válida la conversión por el mero hecho de que el archivo abra. Corrige clipping, saltos, iconos, enlaces, jerarquía o paginación degradados por la conversión sin cambiar materialmente la estrategia aprobada.

No fuerces una longitud fija. Dos páginas son adecuadas cuando bastan; tres son válidas para perfiles científicos o senior si la tercera aporta evidencia sustantiva.

## Verificación final

Antes de entregar:

- verifica hechos, fechas, cargos, enlaces y privacidad contra `00_core.md` y la estrategia aprobada;
- confirma que los pilares tienen suficiente desarrollo y que internships o experiencias tempranas solo permanecen cuando aportan evidencia única;
- confirma que competencias e investigación no duplican sustancialmente los mismos métodos o problemas;
- confirma que divulgación/docencia priorizadas tienen desarrollo sustantivo;
- elimina primera persona explícita, repeticiones, lenguaje artificial y metatítulos editoriales;
- verifica en publicaciones título enlazado, año, autores compactos, venue real cuando exista y ausencia de `arXiv` como venue visible;
- confirma que el HTML generado no depende de una plantilla privada, que no contiene placeholders ni datos ajenos y que los recursos visuales opcionales tienen procedencia legítima;
- inspecciona visualmente contacto, enlaces, encabezados, pie, densidad, desbordamientos y todas las páginas del formato final;
- si hay varios formatos, comprueba consistencia editorial, orden de lectura e hipervínculos contra el mismo contenido aprobado;
- si hay PDF, comprueba además extracción ATS y el PDF final ya convertido;
- si hay DOCX, comprueba además el render final del DOCX derivado.

No prometas entrevistas, preselección ni contratación.

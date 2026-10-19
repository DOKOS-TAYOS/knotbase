# Núcleo de CV de candidatura profesional

## Alcance y objetivo

Este dominio controla la creación y el reajuste de CV del usuario actual para ofertas, empresas, grupos, programas y oportunidades profesionales. Para los hechos profesionales utiliza únicamente la información aportada por el usuario y las fuentes accesibles que haya autorizado; no presupongas una base privada de perfil ni acceso al repositorio de origen.

El objetivo es maximizar la adecuación de la candidatura sin inventar experiencia, capacidades, responsabilidades, resultados o credenciales.

**Invariant:** Toda afirmación factual debe estar respaldada por la base personal aplicable, material aportado por el usuario o una fuente explícitamente autorizada. No conviertas exposición parcial o capacidad transferible en dominio experto.

## Flujo obligatorio en dos fases

**Invariant:** Un CV nuevo, o un reajuste sustancial por cambio de oferta, empresa, grupo, programa o tipo de puesto, se realiza en dos fases separadas. No generes ni redactes el CV completo antes del OK explícito del usuario.

Los cambios locales de formato, enlaces, iconos o redacción sobre una estrategia ya aprobada pueden ejecutarse directamente si no alteran selección de evidencia ni narrativa principal.

### Fase 1 - estrategia y selección

Si existe una oferta concreta, úsala como fuente principal. Si solo existe una organización, trabaja con señales verificables de su actividad sin inventar requisitos de una vacante inexistente.

**Default: carga mínima de evidencia.** Consulta únicamente los documentos, referencias y datos del usuario necesarios para valorar la oportunidad. Prioriza información verificable sobre textos reutilizables o borradores de otros CV. Si no existe información suficiente sobre un pilar, señálalo como pendiente; no inventes una base de conocimiento personal ni atribuyas experiencia al usuario sin respaldo.

Resuelve antes del OK:

- objetivo de candidatura, prioridades y señales de seniority;
- evidencia personal más fuerte para cada prioridad;
- dos a cuatro experiencias o bloques que deben actuar como pilares;
- publicaciones, software, proyectos, docencia, divulgación, escritura técnica, liderazgo o credenciales que convenga destacar;
- contenido que convenga reducir, omitir o relegar;
- orden o peso provisional de las secciones;
- riesgos materiales de sobreafirmación, privacidad o evidencia insuficiente.

No selecciones por coincidencia de keywords solamente. Combina relevancia, fortaleza de evidencia, diferenciación, madurez y capacidad para defender el trabajo en entrevista.

**Default:** Evalúa la comunicación científica y técnica como evidencia profesional real, no como adorno. Cuando la oportunidad valore docencia, divulgación, developer relations, liderazgo, transferencia, escritura técnica, presentación de resultados o explicación de tecnología compleja, considera las actividades verificadas del usuario en publicaciones, plataformas, docencia, charlas y formación como posibles pilares o bloques sustantivos.

### Salida compacta de fase 1

**Default:** Presenta la estrategia de forma compacta. Usa una frase breve de objetivo y una tabla `Prioridad | Evidencia | Tratamiento en el CV` que concentre requisitos, seniority, evidencia y peso editorial. Añade después, solo cuando aporten decisión, `Reducir/omitir`, `Orden propuesto` y `Riesgos`. Identifica claramente los 2-4 pilares dentro de la tabla o inmediatamente después; no repitas la misma evidencia en varios bloques.

**Invariant:** Termina esta fase pidiendo aprobación o cambios. No cargues contratos de maquetación, assets ni verificación visual, no crees DOCX/PDF y no cierres una composición visual final antes de un OK inequívoco.

### Fase 2 - redacción y generación

Tras el OK, usa la estrategia aprobada como contrato de selección. No cambies materialmente los pilares durante la maquetación; si fuese necesario, vuelve al usuario.

- Para un CV estándar, carga `standard_cv_rendering.md` solo al comenzar esta fase o cuando un ajuste local ya autorizado requiera generación/maquetación estándar.
- El formato Europass y sus plantillas privadas no forman parte de este paquete público; si se solicita ese formato, comunica la limitación y ofrece un CV estándar sin imponer una plantilla fija.

## Priorización y uso del espacio

**Default:** La relevancia para el objetivo prevalece sobre un orden genérico del perfil. Una experiencia identificada como pilar debe recibir espacio suficiente para demostrar contexto, contribución, métodos y resultados cuando exista evidencia.

No reduzcas una experiencia fuerte a una línea genérica mientras queden huecos, una sección de skills redundante o bloques secundarios sobredimensionados.

**Default:** Cuando ya exista experiencia profesional sustantiva posterior, omite por defecto internships, prácticas, becas formativas y experiencias estudiantiles de iniciación. Inclúyelas solo si aportan evidencia técnica única y directamente relevante, explican un cambio de trayectoria importante o son necesarias por petición explícita. No las uses para rellenar espacio.

Si una progresión breve de cargos dentro de la misma organización produce un bloque débil o repetitivo, puede mostrarse como una sola experiencia con evolución de rol.

Si la experiencia profesional es la principal evidencia para el puesto, no coloques una sección extensa de competencias por delante salvo que la fase 1 lo justifique.

**Default:** `Technical Focus`, `Competencias` o equivalentes deben funcionar como un mapa breve de capacidades, no como una segunda sección de investigación. Reserva `Investigación` para líneas, contribuciones, métodos, resultados o evidencia científica concreta; ante solapamiento material, conserva la evidencia concreta y reduce la formulación genérica.

**Default:** Privilegia evidencia específica y defendible frente a resúmenes genéricos. En experiencias prioritarias, concreta problemas, métodos, tecnologías, responsabilidades, transferencia y resultados cuando las fuentes lo permitan.

## Publicaciones

Selecciona publicaciones por adecuación al puesto. Entre opciones de relevancia comparable, prioriza internamente las de primera autoría.

**Invariant:** Nunca escribas `First Author`, `Lead Author` ni equivalentes. La autoría se refleja mediante el orden real de autores o se usa solo como criterio interno.

**Invariant:** Toda publicación incluida debe tener un enlace público verificable y comenzar por el título del paper como hipervínculo real. Inmediatamente después debe aparecer el año; después pueden ir autores y venue.

**Default:** Los autores son secundarios. Muéstralos como `Apellido(s), I.`, conserva el orden real y usa `et al.` cuando una lista extensa reste legibilidad. En trabajos publicados, da más jerarquía visual al venue que a los autores.

Formato preferido:

~~~text
Título enlazado - Año. Autores abreviados. Venue destacado.
~~~

**Invariant:** `arXiv` es un repositorio o canal de distribución, no un venue científico visible del CV. Si un trabajo solo está en arXiv, muestra título enlazado, año, autores y otros datos respaldados sin inventar venue. Si está publicado, muestra el venue real aunque el enlace público sea arXiv.

Para trabajos aún no publicados, no añadas automáticamente `preprint`, `manuscript` o `under review` si no es necesario para interpretar la entrada. Nunca presentes un trabajo no publicado como publicado. Comprueba orden de autores, año, estado y enlace antes de usarlo.

## Privacidad

**Invariant:** El CV es una salida a terceros. No publiques información `restricted` o `private` salvo autorización explícita aplicable al uso concreto. Si la visibilidad de un nombre de proyecto, cliente, resultado, dataset o detalle técnico no es inequívocamente pública, resuélvela o generalízala.

**Invariant:** No presupongas consentimiento para publicar teléfono personal, nacionalidad, dirección completa ni otros datos sensibles. Incluye únicamente datos de contacto confirmados para la candidatura; la fecha de nacimiento y la nacionalidad solo se incluyen cuando el usuario lo solicite expresamente o sean requisitos legítimos de la solicitud y el usuario autorice su uso.

**Invariant:** Usa solo el correo electrónico facilitado o expresamente autorizado por el usuario para ese CV. No infieras direcciones, no elijas una cuenta por pertenecer a una institución concreta y no incluyas varias direcciones salvo petición explícita.

**Invariant:** Un CV anterior no constituye autorización para reutilizar nombres o detalles. Revalida su visibilidad al reajustar.

No traslades IDs internos, estados de revisión, niveles de confianza ni metadatos de la base al CV.

## Software, docencia, divulgación y evidencia adicional

Selecciona software primero por relevancia y, entre opciones comparables, por madurez, mantenimiento, documentación, tests, reutilización y verificabilidad. Prefiere pocos artefactos fuertes a una lista extensa.

No penalices mecánicamente un repositorio `congelado` por razones editoriales o de revisión si es evidencia científica fuerte. Evita por defecto repositorios pendientes, archivados, vacíos, obsoletos o privados cuando existan alternativas equivalentes mejores.

Cuando la oportunidad valore comunicación, mentoring, formación, transferencia, liderazgo, escritura técnica o relación con clientes, incluye evidencia real de docencia, divulgación, supervisión o formación. Evita repetir la misma señal en varias secciones.

**Invariant:** No reduzcas automáticamente la divulgación y la docencia a una mención genérica cuando hayan sido seleccionadas en fase 1 como evidencia relevante. Las actividades del usuario debidamente verificadas pueden presentarse con profundidad comparable a otra experiencia relevante según la evidencia disponible.

Cuando sea relevante, esa actividad puede aparecer como experiencia propia o bloque dedicado de `Science Communication & Teaching`, `Divulgación y docencia` o equivalente. No la mezcles por defecto con idiomas ni atribuyas al usuario resultados de una organización o proyecto distinto.

## Voz y naturalidad

**Default:** Evita la primera persona explícita. Prefiere redacción curricular sin sujeto, frases nominales o verbos de acción salvo petición expresa.

Evita grandilocuencia, lenguaje corporativo vacío, keyword dumps, taxonomías, metadatos y repetición de logros. Cada idea fuerte debe tener un lugar principal.

**Default:** Los títulos visibles deben nombrar directamente el contenido. Evita metatítulos como `seleccionadas`, `relevantes`, `clave`, `destacadas`, `alineadas con la oferta`, `selected`, `relevant` o `key`. La priorización se demuestra con contenido y posición.

## Salida compartida

**Default:** En fase 2, si el usuario no especifica formato, entrega PDF. Construye un HTML semántico autosuficiente desde la estrategia aprobada, sin exigir ni reutilizar una plantilla fija, y genera el PDF directamente desde ese HTML. No generes un DOCX intermedio para producir el PDF ni crees DOCX por defecto; genera DOCX únicamente cuando el usuario lo pida expresamente. El CV estándar aplica su contrato de materialización.

**Invariant:** Si la entrega incluye PDF, verifica el PDF final generado desde el HTML específico de esa candidatura, no solo el HTML fuente ni un formato intermedio. Cualquier comprobación específica de composición y ATS pertenece al contrato de materialización aplicable.

No prometas entrevistas, preselección ni contratación.

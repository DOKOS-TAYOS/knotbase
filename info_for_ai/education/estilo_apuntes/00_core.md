# Núcleo de estilo para apuntes

Usa este archivo como referencia predeterminada al redactar apuntes técnicos. Lee antes `../00_core.md`. Este módulo añade únicamente reglas propias de apuntes; hereda del core educativo la selección de audiencia, prerrequisitos, secuenciación, definición de términos, ejemplos, matemáticas, límites y rigor.

## Propósito

Los apuntes deben construir un puente hacia la autonomía: permitir que el lector siga estudiando, reconozca la terminología real del campo, lea material avanzado y, cuando proceda, implemente o experimente con lo aprendido.

No escribas como una enciclopedia ni como una transcripción de clase. Organiza cada bloque para que el lector pueda volver a él, localizar una idea, entender para qué sirve y continuar después sin depender del propio texto.

## Navegación y autonomía

Al comienzo de un material largo, deja claros el objetivo, alcance, exclusiones y qué partes puede saltarse quien ya domine determinados prerrequisitos. En cada sección importante, haz visible qué capacidad se adquiere y qué habilita a continuación.

Conserva las denominaciones que el lector encontrará en papers, documentación y software. Si el ecosistema usa normalmente un término inglés, puede mantenerse siempre que se presente y se explique su función.

## Representaciones y operación

Cuando aporte comprensión, muestra el mismo objeto desde más de una representación —lenguaje natural, notación, geometría, diagrama o implementación— y enseña cómo traducir entre ellas.

No te limites a definir objetos: explica cómo se representan, transforman o combinan, qué propiedades conservan o pierden, qué coste relevante aparece y para qué se usan. Si una operación o herramienta es importante para la autonomía del lector, conecta la explicación con un caso mínimo de aplicación o comprobación.

## Voz y cierre

Mantén una voz docente cercana y disciplinar: claridad sin condescendencia, seguridad sin dogmatismo y rigor sin exhibicionismo. Usa de forma moderada el plural inclusivo —«vamos a», «podemos interpretar», «esto nos lleva a»— cuando acompañe una acción intelectual; no lo uses para ocultar pasos.

Evita entusiasmo artificial, tono publicitario y metadiscurso que no ayude a navegar. Las listas deben condensar estructuras reales, no sustituir la explicación conectada.

Cierra cada sección indicando qué puede entender o hacer ahora el lector y qué queda por aprender. Al final, resume capacidades operativas, simplificaciones relevantes, cuestiones fuera de alcance y un siguiente paso razonable de estudio, lectura o implementación.

## Especializaciones opcionales

Carga solo las que añadan reglas necesarias para la tarea:

- `01_arquitectura_pedagogica.md`: capítulos largos o secuencias complejas.
- `02_explicacion_matematica.md`: formalismo, demostraciones o traducción entre representaciones.
- `03_critica_y_calibracion.md`: ventajas, eficiencia, límites y estado del arte.
- `04_ejemplos_figuras_tablas.md`: ejemplos, diagramas, tablas y microejercicios.
- `05_investigacion_y_practica.md`: transición hacia papers, software, experimentos e implementación.
- `06_revision.md`: revisión final y detección de antipatrones.

Para un esqueleto opcional de capítulo completo, abre `../../RECURSOS_OPCIONALES.md` y resuelve el asset conocido `education-chapter-template` mediante `assets_for_ai/indice_assets_lookup.csv` y su fila canónica de `assets_for_ai/indice_assets.csv`. Para máxima fidelidad en un capítulo complejo, combina este núcleo con las especializaciones pertinentes y termina con `06_revision.md`; no cargues todo el directorio por defecto.
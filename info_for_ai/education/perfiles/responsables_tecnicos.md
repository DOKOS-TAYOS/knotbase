# Perfil de responsables de unidad y técnicos de otra especialidad

## Objetivo de la audiencia

Construir un modelo técnico preciso para conversar con especialistas, detectar interfaces con su propia área, participar en decisiones multidisciplinares y valorar dependencias, restricciones, riesgos y coherencia básica de una propuesta. No busca convertirse automáticamente en especialista del área consultada.

## Profundidad predeterminada

Media-alta. Puede incluir arquitectura, variables físicas o computacionales, órdenes de magnitud respaldados, familias de métodos, interfaces hardware-software, métricas, compromisos y limitaciones. Evita convertir la explicación en una derivación formal o estado del arte salvo petición expresa.

## Conocimientos asumidos

Asume solo los conocimientos que se desprendan de la especialidad declarada y los fundamentos realmente transversales. Un experto en un área no domina necesariamente las áreas vecinas.

Por ejemplo, para una persona de computación cuántica que pregunta por electrónica pueden servir como base señal y ruido, control, calibración, adquisición de datos, frecuencia, ancho de banda, latencia, errores, tolerancias e interacción hardware-software. No presupongas diseño analógico, integridad de potencia, compatibilidad electromagnética, electrónica de potencia, diseño de PCB ni normativa eléctrica específica.

## Puentes y ejemplos útiles

- Parte de conceptos estructurales compartidos y marca después las diferencias del nuevo dominio.
- Usa analogías técnicas solo con correspondencia real y explica dónde dejan de ser válidas.
- Separa, cuando ayude, fundamento físico o matemático, método o algoritmo, arquitectura, implementación, validación y operación o despliegue.
- Presenta la ecuación mínima útil y explica qué cambia con sus parámetros.

## Énfasis para decidir

- Modelo del sistema, principios de funcionamiento, variables dominantes e interfaces.
- Métricas, compromisos, limitaciones, familias de soluciones y puntos de contacto con la especialidad propia.
- Comparaciones condicionadas por precisión, latencia, sensibilidad, escalabilidad, consumo, coste, robustez, integración, datos, mantenibilidad o madurez.

## Riesgos específicos

- Definiciones excesivamente básicas o, en el extremo opuesto, saltos de especialidad no preparados.
- Analogías vagas y listas de componentes sin arquitectura.
- Explicar herramientas sin principios u ocultar compromisos.
- Añadir profundidad que no mejora la comprensión transversal.

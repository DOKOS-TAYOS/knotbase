# Crítica, límites y calibración técnica

Este módulo controla cómo presentar y calibrar límites, ventajas y condiciones dentro de material educativo. No controla por sí solo la validación científica externa de esas afirmaciones.

Cuando haya que decidir si un límite, ventaja, comparación, derivación o afirmación sobre el estado del arte es realmente válida, añade la responsabilidad pertinente de `research`: usa `../../research/03_argument_review.md` para revisar argumentos, cálculos, derivaciones o pruebas, y `../../research/07_state_of_the_art.md` para comparaciones de frontera, madurez, limitaciones y ventajas relativas. Aplica `../../research/00_core.md` antes de cualquier módulo de `research`. Este archivo conserva únicamente la traducción pedagógica y la calibración del resultado validado.

## 1. Tipo de crítica

La crítica debe ser operativa.

No añadas objeciones para parecer sofisticado. Añade límites cuando cambien la comprensión o las decisiones del lector.

La forma característica es:

> Esto es útil para X, pero no debe confundirse con Y.

> Esta representación es compacta, pero eso no implica automáticamente que su manipulación sea barata.

> Este algoritmo mejora cierto coste, aunque la ventaja depende de determinadas hipótesis.

## 2. Frase de calibración

Después de una afirmación importante, intenta completar cuatro piezas:

1. idea principal;
2. utilidad;
3. condición de validez;
4. comportamiento fuera de esa condición.

Ejemplo abstracto:

> Una representación puede reducir mucho el número de parámetros. Esa reducción resulta útil cuando la estructura del problema permite mantener pequeño el parámetro interno relevante. Si ese parámetro crece rápidamente, la ventaja de almacenamiento o cálculo puede desaparecer.

## 3. Etiquetar el tipo de limitación

Cuando sea útil, distingue entre:

- limitación pedagógica;
- limitación matemática;
- limitación computacional;
- limitación estadística;
- limitación física o experimental;
- limitación de hardware;
- limitación de software;
- limitación del estado del arte.

No mezcles estos niveles.

## 4. Ventaja teórica frente a práctica

En computación, algoritmos y computación cuántica, separa claramente:

- complejidad asintótica;
- constantes y overhead;
- coste de preparar o cargar datos;
- tamaño de problema donde aparece la ventaja;
- precisión requerida;
- recursos físicos necesarios;
- comparación con el mejor método clásico conocido;
- disponibilidad real de hardware o software.

Nunca uses «ventaja» como categoría única si estos niveles son relevantes. Cuando la comparación dependa de cuál es el mejor método conocido o de evidencia reciente, determina primero ese hecho mediante `research` y calibra aquí cómo explicarlo.

## 5. Eficiencia

No digas que algo es eficiente sin especificar la métrica.

Pregunta:

- ¿eficiente en memoria?
- ¿en tiempo de ejecución?
- ¿en número de parámetros?
- ¿en número de muestras?
- ¿en profundidad de circuito?
- ¿en número de contracciones?
- ¿en precisión alcanzada por unidad de coste?

## 6. Simplificaciones pedagógicas

Cuando uses una simplificación, marca su estatus.

Formulaciones recomendadas:

- «Para construir intuición, ignoraremos de momento...»;
- «Esta explicación es suficiente para el objetivo de esta sección, aunque no cubre...»;
- «Formalmente hay una sutileza adicional...»;
- «La aproximación anterior deja de ser válida cuando...».

## 7. Contraejemplos

Cuando una regla intuitiva pueda generalizarse indebidamente, añade un contraejemplo pequeño.

El contraejemplo debe servir para delimitar la regla, no para abrir una digresión avanzada. Si el contraejemplo pretende refutar una afirmación técnica no trivial, valida primero el argumento con `research/03_argument_review.md`.

## 8. Software y herramientas

No presentes una librería o lenguaje como «el mejor» sin un objetivo.

Usa formulaciones del tipo:

- mejor para empezar;
- más adecuado para prototipado;
- mejor rendimiento en determinado régimen;
- ecosistema más amplio;
- mantenimiento más activo;
- integración más sencilla con determinada herramienta.

Señala obsolescencia, mantenimiento o carencias cuando sean relevantes.

## 9. Estado del arte

Distingue entre:

- conocimiento consolidado;
- práctica habitual;
- resultado reciente;
- conjectura o expectativa;
- línea de investigación abierta.

No transformes expectativas en hechos. Cuando estas etiquetas dependan de evidencia actual o comparación entre métodos, usa `research/07_state_of_the_art.md` para establecer la clasificación y usa este módulo solo para expresarla de forma pedagógicamente calibrada.

## 10. Regla de brevedad crítica

La calibración debe integrarse en el flujo.

Prefiere una frase precisa de límite inmediatamente después de la afirmación a un párrafo largo de caveats colocado muchas páginas más tarde.

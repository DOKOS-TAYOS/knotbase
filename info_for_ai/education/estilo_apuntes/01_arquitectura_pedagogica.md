# Arquitectura pedagógica de los apuntes

Este archivo define cómo organizar el contenido antes de redactarlo.

Para secuenciación conceptual compartida, carga `../../conceptual_sequencing.md`. Ese contrato gobierna únicamente el mapa mínimo de dependencias, la construcción por capas, la profundidad progresiva, los ejemplos mínimos, la corrección explícita de intuiciones y la conexión entre unidades. Este módulo conserva como propias las barreras cognitivas, la arquitectura de capítulos y secciones, la apertura de conceptos, la navegación didáctica y la poda pedagógica.

## 1. Diseñar desde la barrera cognitiva

La unidad principal de diseño no debe ser «el concepto que toca según el índice», sino la barrera que impide al lector comprender lo siguiente.

Antes de cada sección, determina:

- qué sabe ya el lector;
- qué no puede todavía interpretar;
- qué nuevo concepto elimina esa limitación;
- qué cantidad mínima de formalismo es necesaria ahora.

Cada sección debe justificar su posición dentro de la secuencia.

## 2. Construcción acumulativa

Aplica el mapa mínimo de dependencias y la construcción por capas definidos en `../../conceptual_sequencing.md`.

Dentro de apuntes, una progresión pedagógica frecuente es:

1. objeto familiar;
2. notación para describirlo;
3. operación sobre ese objeto;
4. generalización;
5. interpretación disciplinar;
6. uso en un problema real.

No uses una herramienta matemática antes de haber dado al lector una forma de entenderla.

## 3. Apertura de capítulo

Un capítulo debería comenzar respondiendo a cinco preguntas:

1. ¿Por qué aparece este tema?
2. ¿Qué problema intenta resolver?
3. ¿Qué aprenderá el lector?
4. ¿Qué conocimientos previos se presuponen?
5. ¿Qué queda explícitamente fuera del alcance?

Si hay lectores con niveles distintos, explica cómo navegar el capítulo.

## 4. Apertura de concepto

Para un concepto nuevo, sigue preferentemente esta secuencia:

### A. Necesidad

Describe el problema que hace necesario el concepto.

### B. Intuición mínima

Da una frase, imagen o ejemplo que permita construir una primera representación mental.

### C. Corrección de la intuición

Aplica la corrección explícita de intuición definida en `../../conceptual_sequencing.md` e indica qué parte de la intuición era simplificada.

### D. Definición

Introduce la formulación precisa.

### E. Representación

Muestra la notación, diagrama, tabla o representación geométrica adecuada.

### F. Operación

Explica qué se hace con el objeto.

### G. Ejemplo mínimo

Aplica el contrato de ejemplo mínimo de `../../conceptual_sequencing.md` y usa el caso más pequeño que muestre la estructura.

### H. Límite

Explica una condición de validez, excepción o coste.

### I. Conexión

Aplica la conexión entre unidades de `../../conceptual_sequencing.md` y muestra por qué ahora se puede introducir el siguiente concepto.

## 5. Control de profundidad

Aplica la profundidad progresiva definida en `../../conceptual_sequencing.md`. Este módulo decide además cómo adaptar esa profundidad a la autonomía y al objetivo de aprendizaje del lector.

## 6. Preguntas como transiciones

Cuando sea natural, transforma la transición entre conceptos en una pregunta necesaria.

Ejemplos de estructura:

- Ya sabemos representar X. ¿Cómo representamos ahora una transformación sobre X?
- Ya podemos calcular Y. ¿Qué ocurre cuando el tamaño del sistema crece?
- Esta representación es compacta. ¿Significa eso que también es barata de manipular?

La pregunta debe surgir de una limitación del concepto anterior.

## 7. Cierre de sección

Una sección no debería terminar simplemente porque se ha terminado la definición.

Debe cerrar con una frase que establezca:

- qué sabemos ahora;
- qué podemos hacer ahora;
- qué sigue faltando.

## 8. Cierre de capítulo

Incluye, cuando sea útil:

- mapa de conceptos adquiridos;
- simplificaciones utilizadas;
- errores o confusiones que el lector ya debería evitar;
- problemas sencillos para comprobar comprensión;
- conexión con el siguiente capítulo;
- recursos o temas que ya está preparado para abordar.

## 9. Regla de poda

Si un apartado no cumple al menos una de estas funciones, considera eliminarlo o moverlo:

- elimina una barrera;
- prepara una definición posterior;
- corrige una intuición incompleta;
- enseña una operación necesaria;
- delimita un caso de validez;
- conecta con práctica o investigación.

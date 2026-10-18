# Instrucciones para explicar matemáticas y formalismo

## 1. El formalismo debe tener motivo

No empieces una sección con símbolos si el lector todavía no sabe qué pregunta van a resolver.

Antes de una ecuación importante, explica qué representa y por qué necesitamos escribirla.

Después de la ecuación, explica cómo leerla.

## 2. Tres capas de explicación

Cuando sea posible, presenta cada objeto matemático en tres capas.

### Capa 1. Intuición

Una descripción sencilla que capture la función principal.

### Capa 2. Estructura matemática

Definición, espacios, índices, dimensiones, dominio/codominio o propiedades necesarias.

### Capa 3. Uso disciplinar

Qué representa en el contexto físico, computacional o algorítmico.

Estas capas pueden aparecer próximas, pero no deben confundirse.

## 3. Notación

Cada símbolo nuevo debe definirse la primera vez que aparece.

Si una ecuación usa mucha notación, introduce primero sus componentes.

No ocultes un paso no trivial mediante una formulación que lo presente como evidente para el lector objetivo.

Cuando escribas una ecuación en bloque, usa:

```markdown
$$
A = U\Sigma V^{\dagger}
$$
```

No uses una fórmula como sustituto de una explicación.

## 4. Definiciones

Una definición importante debería estar rodeada de contexto.

Patrón recomendado:

> Como primera intuición, X puede verse como...
>
> Esta descripción es útil, aunque todavía omite...
>
> Formalmente, definimos X como...

Después, explica al menos una consecuencia inmediata de la definición.

## 5. De caso pequeño a caso general

Empieza por la dimensionalidad o ejemplo más pequeño que conserve la estructura relevante.

Por ejemplo:

- vector de dimensión 2 antes de dimensión general;
- matriz 2x2 antes de operador arbitrario;
- dos tensores antes de una red extensa;
- dos qubits antes de un registro de n qubits.

Generaliza solo después de que el patrón sea visible.

## 6. Operaciones

Para cada operación importante, explica:

1. qué entra;
2. qué sale;
3. qué dimensiones cambian;
4. qué significado tiene la operación;
5. qué coste puede tener, si es relevante.

En temas tensoriales, distingue especialmente entre:

- coste de almacenamiento;
- coste de contracción;
- coste de aproximación;
- precisión de la aproximación.

No digas que una representación es «eficiente» sin aclarar en qué sentido.

## 7. Demostraciones

Las demostraciones deben utilizarse cuando mejoran comprensión, no como ritual formal.

Antes de una demostración, indica qué vamos a probar y por qué importa.

Durante la demostración:

- no ocultes pasos críticos;
- verbaliza las transformaciones no triviales;
- identifica qué propiedad se usa;
- justifica cualquier salto que no sea inmediato para el lector objetivo.

Al final, interpreta el resultado.

## 8. Traducción entre representaciones

Siempre que el tema lo permita, enseña a traducir en ambas direcciones:

- ecuación ↔ diagrama;
- vector ↔ geometría;
- estado ↔ amplitudes;
- operador ↔ transformación;
- índice compartido ↔ contracción;
- estructura algebraica ↔ implementación.

La traducción bidireccional es más valiosa que mostrar dos representaciones de forma independiente.

## 9. Jerarquía de precisión

Distingue explícitamente entre:

- analogía;
- intuición;
- definición operativa;
- definición formal;
- teorema;
- aproximación;
- heurística.

No presentes categorías epistemológicas distintas con el mismo tono de certeza.

## 10. Regla de lectura

Después de cualquier bloque matemático denso, el lector debería poder responder:

- ¿qué significa este objeto?
- ¿por qué apareció aquí?
- ¿qué puedo hacer ahora con él?

Si no puede, añade interpretación antes de avanzar.

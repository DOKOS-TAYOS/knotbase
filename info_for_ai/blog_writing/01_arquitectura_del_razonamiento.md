# Arquitectura del razonamiento

Abre este módulo antes de diseñar un artículo. Construye aquí el argumento; no conviertas sus pasos en una plantilla visible ni repitas las decisiones de voz y ritmo de `02_voz_pedagogia_y_ritmo.md`.

Para la secuenciación conceptual compartida, carga `../conceptual_sequencing.md`. Ese contrato gobierna únicamente el mapa mínimo de dependencias, la construcción por capas, la profundidad progresiva, los ejemplos mínimos, la corrección explícita de intuiciones y la conexión entre unidades. Este módulo conserva como propias la tensión central, la tesis, el punto de entrada editorial, los cuellos de botella, la crítica, las conexiones laterales y el cierre del artículo.

**Invariant:** abre `04_flujo_iterativo_de_generacion.md` cuando esté activado `#BLOG`, el usuario pida explícitamente ese flujo iterativo completo o solicite de forma natural crear, redactar, escribir o generar un artículo de blog nuevo. Una petición que solo pida idear temas, títulos o estructura, o editar, reescribir, revisar, resumir, traducir o materializar un artículo ya existente no activa por sí sola las siete fases salvo petición explícita del flujo o uso de `#BLOG`: usa directamente los módulos editoriales necesarios para la tarea solicitada. Cuando el flujo iterativo esté activo, `04_flujo_iterativo_de_generacion.md` gobierna qué fase puede ejecutarse en el turno actual.

## 1. Encontrar la tensión central

No partas solo de un tema. Busca la pregunta concreta que hace que merezca un artículo. "Corrección de errores cuánticos" es un área; "por qué un millón de qubits físicos puede seguir siendo insuficiente para ejecutar un algoritmo útil" contiene una tensión. "RAG" es una técnica; "por qué dar más documentos a un LLM no equivale a darle más conocimiento utilizable" plantea un problema.

La tensión puede ser una contradicción aparente, una intuición incompleta, una diferencia entre teoría e implementación, un trade-off o una confusión entre capas del sistema. Elige una tensión principal. Las preguntas secundarias deben contribuir a la misma trayectoria.

## 2. Formular la tesis provisional

Resume en una o dos frases qué debería comprender el lector al final. La tesis debe ser más precisa que un titular provocador: si el título afirma que algo "no funciona", concreta en qué sentido, a qué escala, bajo qué arquitectura y con qué supuestos.

Usa la tesis para separar la información necesaria del contenido interesante pero lateral. No retrases de forma artificial la respuesta; la curiosidad puede mantenerse sin ocultar de qué trata el artículo.

## 3. Construir el mapa de dependencias

Aplica el mapa mínimo de dependencias de `../conceptual_sequencing.md` a la tesis del artículo. Conserva solo las dependencias que condicionan la comprensión de esa tesis, no todas las conexiones académicamente posibles.

## 4. Elegir el punto de entrada

Comienza desde algo que el lector pueda manejar: una pregunta, una intuición popular, un resultado reciente, una consecuencia tecnológica, un ejemplo sencillo o una paradoja aparente. Evita abrir con una definición fría salvo que el concepto sea la propia pregunta.

El orden en que una persona investigadora descubrió el problema no tiene por qué ser el mejor orden pedagógico. La introducción debe establecer pronto qué se va a resolver, por qué la intuición inicial parece razonable y qué pieza merece una mirada más cuidadosa.

## 5. Construir por capas

Aplica la construcción por capas y la profundidad progresiva definidas en `../conceptual_sequencing.md`. En un artículo, cada capa debe servir además a la trayectoria de la tesis y mantener sensación de avance, sin convertir el mecanismo en una plantilla visible.

Una progresión frecuente es:

Intuición inicial → definición operativa → mecanismo → ejemplo pequeño → escala realista → límite o trade-off → interpretación correcta.

La secuencia puede cambiar. Cuando incorpores una sección técnica, su función en el argumento ya debe estar clara.

## 6. Seleccionar ejemplos, números y formalismo

Aplica el contrato de ejemplo mínimo de `../conceptual_sequencing.md` y elige ejemplos que aclaren una relación entre recurso, coste, transformación o límite. Si la conclusión depende del escalado, pasa después a una escala realista y muestra qué rompe la intuición inicial.

Cuando resulte útil, examina un escenario favorable u optimista para la posición que estás evaluando. Si la limitación persiste bajo esos supuestos, la conclusión resulta más informativa y robusta.

Cuando la intuición falle por órdenes de magnitud, incluye una cuenta transparente. Si una ecuación hace visible la relación central, resérvale un lugar en el argumento y prepara antes las cantidades que conecta. Resume el desarrollo matemático que no cambie la conclusión y conserva la parte que aporta comprensión.

Cuando una capa posterior corrija una intuición usada como punto de entrada, aplica la corrección explícita de `../conceptual_sequencing.md` en vez de sustituir silenciosamente el modelo inicial.

## 7. Localizar el cuello de botella y los recursos

Pregunta dónde desaparece una ventaja aparente. El límite puede estar en la preparación de datos, la profundidad, la memoria, la comunicación, la medida, el ruido, la precisión, la latencia, el condicionamiento, la disponibilidad de un oráculo, los permisos u otro recurso omitido por la formulación sencilla.

No inventes un cuello de botella si no existe. Cuando una mejora desplaza el coste entre recursos, diseña el argumento para mostrar el intercambio completo y las condiciones bajo las que cambia el balance.

## 8. Diseñar una crítica justa

Si el artículo cuestiona una narrativa, construye primero su mejor versión razonable. Enumera para ti, no necesariamente en el texto final, los supuestos que necesita y examínalos mediante el mecanismo correspondiente.

Prefiere una restricción decisiva y bien explicada a una acumulación de objeciones débiles. Si varias barreras son independientes y afectan de forma material a la conclusión, muéstralas. El cierre crítico debe indicar qué versión de la idea sobrevive al análisis.

## 9. Gestionar conexiones transversales

Incluye una conexión lateral solo si el lector perdería una pieza importante del razonamiento al eliminarla. Define por qué entra, cuánto contexto mínimo necesita y en qué punto regresa a la tesis.

No permitas que una conexión requiera otra digresión o reciba más desarrollo que el tema central, salvo que el foco del artículo haya cambiado deliberadamente. Es preferible una conexión útil y completa que varias menciones superficiales.

En un artículo de longitud media suele bastar con una o dos conexiones transversales relevantes. Un texto largo puede admitir más, pero nunca deben competir con la tesis central.

### Referencias a artículos propios

**Default:** no recorras `info_user/articulos_medium_linkedin_usuario.csv` en cada artículo solo para comprobar si quizá existe una coincidencia. Consúltalo cuando el usuario pida relacionar contenido propio, el contexto ya identifique un artículo potencialmente relevante o exista una razón concreta para buscar una ampliación interna.

Cuando se active esa consulta, usa `temas`, `resumen_para_referencia`, `cuando_referenciarlo` y `relacionados` para localizar candidatos y las columnas de URL para recuperar el enlace publicado disponible.

Una referencia interna debe ahorrar repetición, ofrecer al lector una ampliación útil o conectar explícitamente con un argumento anterior. No introduzcas autocitas solo porque exista una coincidencia de palabras clave y no sustituyas con ellas la evidencia externa que necesite una afirmación factual. Si ninguna pieza previa mejora realmente el artículo actual, no fuerces ninguna referencia.

## 10. Diseñar el cierre desde el principio

Decide qué corrección conceptual debe producir el final. La conclusión debe volver a la pregunta inicial y mostrar qué ha cambiado, no repetir el índice del artículo.

Aplica la conexión entre unidades de `../conceptual_sequencing.md` cuando ayude a que cada sección prepare la siguiente, pero el cierre del artículo debe resolver la tensión editorial: la intuición inicial captaba X, pero ignoraba Y; al incorporar Y, la conclusión precisa pasa a ser Z. Cuando resulte útil, traduce esa conclusión a una decisión práctica para investigadores, profesionales, empresas o lectores técnicos. No fuerces una moraleja ni una predicción futurista.
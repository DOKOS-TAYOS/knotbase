# Creación de contenido formativo escrito

Lee primero `00_core.md`. Activa este flujo para crear apuntes, texto didáctico u otro contenido formativo escrito. Los vídeos y el HTML educativo tienen módulos propios para evitar cargar reglas irrelevantes.

## Preparación

Delimita tema, audiencia, nivel, objetivo de aprendizaje, formato y extensión. Revisa el borrador como una persona inteligente que no domina el subcampo: debe poder explicar qué aprende, por qué aparece cada concepto y qué puede hacer después.

Para investigar o verificar afirmaciones, añade `research/00_core.md` y el flujo de `research/` pertinente únicamente cuando haga falta evidencia externa, actualidad o comprobación detallada.

## Apuntes

Usa `estilo_apuntes/00_core.md` como estilo predeterminado. Añade solo las especializaciones de `estilo_apuntes/` necesarias para la tarea.

Incluye, cuando aporten valor, objetivos, prerrequisitos, notación, ejemplos mínimos, ejercicios o preguntas de comprobación, errores frecuentes, límites, resumen y recursos para continuar. La estructura debe favorecer autonomía y lectura posterior, no reproducir una clase palabra por palabra.

## Texto didáctico y artículos

Para texto didáctico que no sea un artículo de blog, este dominio controla la estructura de aprendizaje, la audiencia, la profundidad y la selección de contenido.

Para un artículo de blog, `education` conserva únicamente esas decisiones didácticas como restricciones de entrada y `blog_writing` controla la forma artículo. **Default:** el destino de publicación es Medium salvo que el usuario indique otra plataforma.

- Si el usuario activa `#BLOG`, pide explícitamente el flujo iterativo completo o solicita de forma natural crear, redactar, escribir o generar un artículo de blog nuevo, añade `blog_writing`, abre su core e índice y selecciona `04_flujo_iterativo_de_generacion.md`. Deja que ese workflow cargue arquitectura, voz, revisión y materialización únicamente cuando alcance la fase correspondiente.
- Si la petición solo pide idear temas, títulos o estructura, o editar, reescribir, revisar, resumir, traducir o materializar un artículo ya existente sin pedir el flujo iterativo completo, añade `blog_writing` y selecciona solo los módulos necesarios para la tarea activa. No fuerces las siete fases para esas tareas parciales.

No mantengas aquí una segunda definición de la arquitectura, la voz, la densidad, las transiciones ni el workflow editorial del blog.

## Otros formatos

Para un vídeo educativo, usa `video_youtube.md`; YouTube es el destino predeterminado salvo instrucción contraria.

Para una experiencia web educativa, usa `html_interactivo.md`; ese módulo decide la función pedagógica y añade la responsabilidad `htmls` solo cuando la implementación lo requiera.
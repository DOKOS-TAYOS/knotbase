# Actualizar o revisar instrucciones existentes

Usa este procedimiento para modificar, eliminar parcialmente o auditar de forma localizada una instrucción o un comportamiento de routing existente. Una revisión de un único subsistema sigue aquí aunque sea profunda; usa `07_revision_integral.md` solo para revisar el repositorio completo o varias familias independientes.

`00_core.md` gobierna fuente canónica, cambio mínimo, no duplicación, propagación selectiva, tests, validación, diff y logbook. Este procedimiento añade solo las decisiones propias de instrucciones.

## Procedimiento

1. Localiza el owner mediante su índice. En `info_for_ai/`, sigue `indice_dominios.csv -> core si existe -> indice_<dominio>.csv -> módulo responsable`. En `maintenance_for_ai/`, conserva el procedimiento seleccionado por `indice_mantenimiento.csv` y abre solo sus dependencias directas.
2. Modifica el owner existente siempre que pueda expresar el cambio con claridad. Toca un `00_core.md` solo para reglas genuinamente compartidas y crea un módulo nuevo solo para una responsabilidad distinta y reutilizable.
3. En revisiones read-only, limita la inspección a la responsabilidad seleccionada y sus dependencias directas; no amplíes el alcance por similitud temática.
4. Si eliminas o renombras una regla, ruta o módulo, corrige únicamente las referencias, índices, tests o evals que queden incorrectos. Mantén las descripciones de índice suficientemente específicas para seleccionar sin cargar módulos irrelevantes.
5. **Default:** Conserva la serie numérica principal cuando ayude a navegación estable. Usa nombres semánticos sin numeración para contratos auxiliares o transversales, crea subdirectorios solo ante una agrupación real y no renumeres una serie estable solo para insertar una responsabilidad.
6. No eleves una preferencia local a regla global. Si la fuerza normativa puede cambiar comportamiento, aplica la jerarquía de `AGENTS.md` sin duplicar sus definiciones.

## Registro de comandos compactos

Si el cambio afecta `info_for_ai/comandos.csv`, `info_for_ai/comandos_lookup.csv` o su mecanismo:

- `comandos.csv` sigue siendo la fuente semántica canónica y `comandos_lookup.csv` una vista derivada de localización. Modifica `AGENTS.md` solo si cambia el mecanismo general, no para repetir semántica de comandos concretos.
- Preserva esquema, modos, argumentos, scope, authorization y precondiciones definidos por `AGENTS.md`.
- Si cambian posiciones o comandos, actualiza el lookup en la misma tarea y verifica cobertura exacta, unicidad case-insensitive y correspondencia comando-fila.
- Conserva categorías contiguas porque `#HELP` depende de lecturas acotadas.
- **Default:** `authorization` contiene solo permisos, límites de mutación y stopping conditions específicos del comando; el procedimiento técnico pertenece a los módulos seleccionados.
- Si cambia el contrato observable del registro, actualiza sus tests sin debilitar las invariantes que continúen vigentes.

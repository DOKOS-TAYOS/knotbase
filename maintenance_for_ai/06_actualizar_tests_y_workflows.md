# Actualizar tests, evals y workflows

Usa este procedimiento cuando una actualización afecte contratos automatizados, comandos de validación o GitHub Actions. `00_core.md` conserva las reglas compartidas de causa raíz, no debilitamiento de tests, cambio mínimo, validación final, diff y logbook.

## Procedimiento

1. Determina si el cambio altera intencionadamente un contrato observable, caso de routing, comando, runtime, dependencia, permiso, trigger o check requerido. Si no debía cambiar, corrige la implementación y conserva la protección; si cambia intencionadamente, actualiza implementación y test/eval de forma coherente.
2. Añade tests solo para invariantes nuevas que merezcan protección; evita checks duplicados y acoplamiento a detalles internos sin valor contractual.
3. Modifica workflows solo cuando cambien comandos, versiones soportadas, dependencias, permisos, triggers o validadores obligatorios. Mantén permisos mínimos y prefiere comprobaciones deterministas locales frente a secretos o servicios externos innecesarios.
4. **Default:** Evita runners, checkouts e historial Git duplicados cuando una misma garantía pueda comprobarse secuencialmente dentro del job de validación. Para freshness de un PR puede usarse una comparación determinista del base ref actual contra el head sin descargar todo el historial, siempre que falle para estados `behind` o `diverged` y acepte únicamente un head basado en el base actual.
5. **Default:** Configura `concurrency` con cancelación de ejecuciones supersedidas cuando varios pushes del mismo PR o ref hagan obsoleto el resultado anterior; no canceles unidades independientes.
6. Conserva la suite completa como gate final salvo decisión explícita y justificada. Los tests focalizados pueden ejecutarse antes, pero no la sustituyen. Si un checkout limpio difiere del entorno local, revisa sus logs y corrige la causa sin reducir cobertura ni volver el fallo no bloqueante.

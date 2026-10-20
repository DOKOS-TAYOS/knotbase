# Actualizar repositorios GitHub

Usa este procedimiento para mantener `info_for_ai/info_user/repositorios_github.csv`.

**Invariant:** Verify `instance_repository`, `github_owner`, the private knowledge destination and actual write permissions before updating inventory. When the owner or full authorized scope is unknown, stop; do not enumerate repositories belonging to the original upstream owner or treat an empty inventory as complete.

## Objetivo

Sincronizar el inventario de repositorios propios con el estado visible en GitHub sin convertir metadatos ambiguos en hechos.

## Alcance

**Default:** Conserva el alcance explícito de la petición. Si el usuario identifica uno o varios repositorios concretos, inspecciona únicamente esos repositorios y las dependencias que queden afectadas. Enumera todos los repositorios propiedad de the verified `github_owner` from `config/instance.csv` solo cuando se solicite una sincronización general o cuando sea imprescindible para resolver una inconsistencia del inventario.

## Procedimiento

1. Determina si la tarea es focalizada o una sincronización general.
2. En una sincronización general, enumera repositorios propiedad de the verified `github_owner` from `config/instance.csv` mediante la conexión autenticada a GitHub cuando esté disponible. En una actualización focalizada, consulta únicamente los repositorios indicados.
3. Compara por nombre y URL las filas dentro del alcance seleccionado. Añade solo repositorios ausentes y actualiza solo metadatos que hayan cambiado.
4. Usa metadatos del repositorio y, cuando haga falta, su README para escribir `descripcion_resumen` y clasificar `tipo`.
5. Valores de `tipo`: `libreria`, `cientifico_paper`, `aplicacion`, `plantilla`, `otros`.
6. Valores de `visibilidad`: `publico`, `privado`.
7. Valores de `estado_desarrollo`: `finalizado`, `pendiente`, `continuo`, `congelado`, `no_determinado`. Usa `congelado` cuando exista evidencia explícita de que el repositorio no tendrá mantenimiento activo pero se conserva accesible o sin archivar por despliegue, demo o servicio, por ejemplo Streamlit. No deduzcas `congelado` solo por ausencia de commits, issues o GitHub Actions, ni `finalizado` porque lleve tiempo sin commits ni `pendiente` porque tenga issues abiertas.
8. `archivado` y `es_fork` usan `si` o `no` y se toman directamente de GitHub. `archivado` es independiente de `estado_desarrollo`: archivar un repositorio no demuestra `finalizado` o `congelado`, y un repositorio `congelado` puede seguir sin archivar.
9. Registra en `ultima_verificacion` la fecha de la inspección efectiva.
10. Si la finalidad o el estado no se pueden justificar con metadata, README o indicación explícita del usuario, usa `otros` o `no_determinado` y explica el límite brevemente en `notas`.
11. Cuando se sincronice `dependabot_dias_versiones`, inspecciona directamente `.github/dependabot.yml` en los repositorios no archivados ni congelados. Registra los días semanales efectivos de las entradas de version updates con los nombres canónicos en inglés (`monday` a `sunday`), deduplicados y separados por `;`. Si `schedule.interval=weekly` omite `day`, registra `monday`, que es el valor predeterminado de GitHub. Usa `none` solo cuando se haya verificado que el repositorio mantenido no tiene configuración de version updates; deja el campo vacío cuando el repositorio esté excluido o el calendario no se haya inspeccionado. Este campo describe version updates y no debe usarse para inferir el calendario de security updates.
12. Si se modifica `repositorios_github.csv`, regenera también `info_for_ai/info_user/repositorios_github_lookup.csv` de forma mecánica. El lookup contiene exactamente `nombre,line`, una fila por repositorio canónico, y `line` debe señalar la fila física actual del repositorio en `repositorios_github.csv`. Conserva unicidad case-insensitive de `nombre`; el lookup es una vista derivada de localización y nunca sustituye al CSV canónico para metadatos o estado.
13. Si se modifica `repositorios_github.csv`, abre `info_for_ai/info_user/indice_info_user.csv` y filtra únicamente las filas `authority=derived` cuyo `source_of_truth` incluya `info_user/repositorios_github.csv`. Revisa solo esas vistas candidatas y actualiza únicamente las que hayan quedado materialmente desfasadas. No mantengas aquí una lista manual de vistas dependientes.
14. Ejecuta validadores y revisa que el diff no reescriba filas sin cambios salvo las columnas cuya sincronización forme parte explícita de la tarea.

## Orden operativo del CSV

**Invariant:** Mantén las filas en tres bloques contiguos y en este orden:

1. **Activos u operativos:** `archivado=no` y `estado_desarrollo!=congelado`.
2. **Congelados:** `archivado=no` y `estado_desarrollo=congelado`.
3. **Archivados:** `archivado=si`, con independencia de `estado_desarrollo`.

Dentro del bloque activo, ordena por el primer día semanal registrado en `dependabot_dias_versiones`, usando `monday` a `sunday` como orden natural de la semana. Si una fila contiene varios días, usa el más temprano para ordenar. Las filas con `none` o con el campo vacío van después de `sunday`. Desempata alfabéticamente por `nombre`, sin distinguir mayúsculas de minúsculas.

Dentro de los bloques congelado y archivado, ordena alfabéticamente por `nombre`, sin distinguir mayúsculas de minúsculas.

Cuando se añada un repositorio nuevo o cambien `archivado`, `estado_desarrollo`, `dependabot_dias_versiones` o `nombre`, inserta o mueve su fila al bloque y posición que correspondan. No conserves el orden histórico de inserción si contradice este contrato.

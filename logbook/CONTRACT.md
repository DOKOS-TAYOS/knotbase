# Contrato del logbook

El `logbook/` conserva trazabilidad operativa y de decisiones desde su primera operación de mantenimiento. Complementa a `CHANGELOG.md`: el changelog resume evolución relevante; el logbook registra unidades de trabajo, procedencia, decisiones y validación.

## Fuente de verdad

- `logbook/YYYY-MM/YYYY-MM-DD.md` es la fuente canónica diaria.
- `logbook/README.md` y `logbook/YYYY-MM/README.md` son vistas derivadas; no se editan manualmente.
- Regenera los índices con `python maintenance_for_ai/validation/logbook.py --write`.
- La validación canónica comprueba que esos índices estén sincronizados.

## Alcance temporal

- El registro comienza con la primera operación mantenida en esta instancia; no se atribuye historial del autor original.
- Todas las horas usan `Europe/Madrid` con precisión de minutos.

## Archivo diario

Cada día con actividad tiene un único archivo:

```text
logbook/YYYY-MM/YYYY-MM-DD.md
```

Debe comenzar con:

```md
# YYYY-MM-DD

Cambios: <número de bloques>
Resumen: <resumen breve del conjunto del día>
```

`Cambios` coincide con el número real de bloques `##`.

## Bloque de cambio

Cada unidad lógica se registra así:

```md
## HH:MM - <título resumen>

Origen: <ChatGPT|Codex|Mixto|Manual>

Commits:
- `<sha>` - <descripción breve>

PR:
- #<número>

Acciones:
- <qué se hizo>

Motivo:
- <decisiones o razón material>

Validación:
- <qué se comprobó>
```

Reglas:

1. Usa un bloque por unidad lógica, no por commit.
2. `Origen` admite únicamente `ChatGPT`, `Codex`, `Mixto` o `Manual`.
3. `Commits` referencia los commits materiales necesarios para identificar el estado documentado. **Default:** si existe PR, registra el head material validado y, como máximo, los pocos commits adicionales cuyo SHA sea relevante para comprender una decisión; el PR conserva el historial completo y no hace falta duplicar todos los commits intermedios. Si la operación no tiene commit, usa `- N/A`.
4. No incluyas commits cuyo único propósito sea añadir o sincronizar el propio logbook; evita así la autorreferencia imposible del SHA.
5. `PR` enumera los pull requests asociados o `- N/A`.
6. `Acciones` describe hechos y `Motivo` conserva decisiones sin repetir las acciones. **Default:** usa 1–3 bullets concisos por `Acciones`, `Motivo` y `Validación`; amplía solo cuando una decisión futura dependa de ese detalle.
7. `Validación` recoge únicamente comprobaciones realmente ejecutadas.
8. Conserva las decisiones necesarias para comprender el estado futuro, pero no cadenas de razonamiento internas, conversaciones completas ni información sensible innecesaria.
9. Las entradas son append-only por defecto. Corrige una entrada histórica solo para reparar un error factual; una decisión posterior genera un bloque nuevo.

## Índices derivados

El índice global muestra por mes días con cambios, número total de bloques y resumen compacto de los días recientes. Cada índice mensual muestra por día número de bloques y resumen. Los resúmenes se derivan deterministamente de los archivos diarios, sin IA.

## Flujo de mantenimiento

Para una modificación normal:

1. realiza y valida el cambio material;
2. crea el commit o commits materiales;
3. añade el bloque diario usando los SHA materiales ya conocidos;
4. actualiza `Cambios` y `Resumen` del día;
5. ejecuta `python maintenance_for_ai/validation/logbook.py --write`;
6. publica el archivo diario y todos los índices derivados modificados **en un único commit multiarchivo cuando el entorno lo permita**; si no, usa el mínimo número de commits necesario;
7. ejecuta `python maintenance_for_ai/validation/validate.py` sobre el árbol final;
8. integra únicamente ese estado final validado.

`CHANGELOG.md` se actualiza de forma independiente cuando el cambio sea suficientemente relevante para el historial de evolución del proyecto.

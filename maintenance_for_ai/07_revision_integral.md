# Revisión integral del repositorio

Usa este procedimiento cuando el usuario pida revisar que todo el repositorio esté bien y corregir lo necesario. No lo uses solo porque una revisión sea profunda o transversal dentro de un único subsistema; esas auditorías permanecen en el procedimiento propietario de esa responsabilidad.

## Procedimiento

1. Ejecuta primero el validador canónico antes de proponer cambios:
   - `python maintenance_for_ai/validation/validate.py`
   Este entrypoint reúne las validaciones de routing, repositorio, privacidad, corpus de evals y la suite `unittest`; no mantengas aquí una segunda lista de scripts de validación.
   - Si el entorno no dispone de checkout local, acepta como fallback únicamente una ejecución de CI exitosa del validador canónico cuyo contenido pueda demostrarse idéntico al objetivo de la revisión mediante el mismo `tree SHA`. No basta con que coincida la rama, el commit nominal o una ejecución reciente: compara el árbol validado por CI con el árbol exacto que se está revisando.
   - Si no puede demostrarse que CI validó el mismo árbol, considera la validación bloqueada y decláralo como limitación; no sustituyas esa evidencia por una ejecución antigua o aproximada.
2. Investiga la causa raíz de cada fallo antes de editar.
3. Si la suite pasa, revisa incoherencias concretas que los validadores no puedan cubrir completamente: archivos no indexados, índices obsoletos, enlaces rotos, responsabilidades ambiguas, duplicación de instrucciones, deriva entre fuentes trazables y vistas editoriales, evals obsoletos, política LFS y workflows.
4. Corrige solo problemas demostrados. No conviertas una revisión en un refactor general ni en una oportunidad para introducir nuevas abstracciones.
5. Si una posible mejora no es necesaria para corregir un problema actual, sepárala como recomendación en vez de implementarla automáticamente.
6. Repite `python maintenance_for_ai/validation/validate.py` después de las correcciones y revisa el diff final. Si sigues sin checkout local, aplica el mismo fallback de CI sobre el `tree SHA` exacto del estado corregido; si no puede verificarse ese mismo árbol, la validación queda bloqueada.
7. Informa de problemas corregidos, comprobaciones ejecutadas y cualquier incertidumbre que no pueda resolverse con las fuentes disponibles.

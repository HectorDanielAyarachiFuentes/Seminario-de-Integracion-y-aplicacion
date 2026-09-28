# 🕸️ GitNexus Workspace Rule — Inteligencia de Código y Control de Arquitectura

Este archivo define las directivas y pautas operativas obligatorias para el uso de **GitNexus** en este repositorio de **Trabajo Final de Graduación (TFG) / Tesina**.

---

## 📌 1. Misión y Alcance de GitNexus en el Repositorio

GitNexus actúa como el **Cerebro Técnico y Arquitectural** del proyecto, complementando a NotebookLM (Cerebro Académico y Metodológico). Su función principal es:

1. **Gobernar la Arquitectura *Docs-as-Code*:** Indexar y mapear las dependencias entre scripts de automatización (`compilar_todos.py`, `compilar_todos.ps1`), plantillas (`assets/`, `plantillas_pdf/`), filtros y documentos Quarto (`.qmd`) y Typst (`.typ`).
2. **Protección del Pipeline de Compilación:** Salvaguardar la integridad de `compilar_todos.py` (post-procesador de Word/PDF, tablas APA 7, sangría francesa, numeración dinámica y carátulas) ante cualquier refactorización o adición.
3. **Análisis de Impacto Previo (*Blast Radius*):** Garantizar que ninguna modificación técnica rompa entregas previas o flujos de trabajo existentes.

---

## 🛡️ 2. Reglas Operativas Obligatorias (Guardarraíles)

### ✅ Obligatorio (Always Do):
1. **Análisis de Impacto Antes de Editar:**
   - Antes de modificar cualquier función, clase o método en `compilar_todos.py` u otros scripts, ejecutar el análisis de impacto:
     ```powershell
     node .gitnexus/run.cjs impact "<nombreSimbolo>" --direction upstream --repo .
     ```
   - Evaluar los llamadores (*callers*), flujos de ejecución (*processes*) y nivel de riesgo (*risk*).
2. **Detección de Cambios en el Grafo Antes de Confirmar (Commit):**
   - Antes de realizar cualquier commit de código o refactorización:
     ```powershell
     node .gitnexus/run.cjs detect-changes --scope all --repo .
     ```
   - Si se analiza regresión contra la rama principal:
     ```powershell
     node .gitnexus/run.cjs detect-changes --scope compare --base-ref "main" --repo .
     ```
3. **Gestión Rigurosa de Riesgos:**
   - Alertar inmediatamente si el análisis arroja riesgo **HIGH** o **CRITICAL**.
   - Tratar `risk: UNKNOWN` como advertencia no resuelta (requiere verificación manual adicional antes de continuar).
4. **Navegación Asistida por Grafo:**
   - Para explorar conceptos o arquitectura:
     ```powershell
     node .gitnexus/run.cjs query "<concepto>" --repo .
     ```
   - Para inspeccionar un símbolo o función específica:
     ```powershell
     node .gitnexus/run.cjs context "<nombreSimbolo>" --repo .
     ```

### ❌ Prohibido (Never Do):
1. **Nunca editar funciones o clases críticas a ciegas** sin previo análisis de impacto.
2. **Nunca renombrar símbolos mediante búsqueda y reemplazo masivo de texto (*find-and-replace*)** sin verificar el grafo de llamadas.
3. **Nunca confirmar cambios (commit) en scripts del pipeline sin verificar `detect-changes`**.
4. **Nunca ignorar advertencias de riesgo alto** o romper compatibilidad entre los módulos de compilación.

---

## 🔄 3. Mantenimiento y Actualización del Índice

Si se incorporan nuevos módulos, scripts o cambios estructurales mayores:

* **Reindexar de forma rápida (solo índice):**
  ```powershell
  node .gitnexus/run.cjs analyze --index-only
  ```
* **Consultar estado actual del grafo:**
  ```powershell
  node .gitnexus/run.cjs status
  ```

---

## 🛠️ 4. Guía Rápida de Skills y Tareas de GitNexus

| Tarea Requerida | Skill de Referencia | Comando / Flujo |
| :--- | :--- | :--- |
| **Comprender arquitectura / "¿Cómo funciona X?"** | `.agents/skills/gitnexus-exploring/SKILL.md` | `node .gitnexus/run.cjs context "<simbolo>"` |
| **Radio de impacto / "¿Qué se rompe si toco X?"** | `.agents/skills/gitnexus-impact-analysis/SKILL.md` | `node .gitnexus/run.cjs impact "<simbolo>" --direction upstream` |
| **Diagnosticar fallas / "¿Por qué falla la compilación?"** | `.agents/skills/gitnexus-debugging/SKILL.md` | Rastreo de flujo y ejecución de pruebas controladas |
| **Refactorizar / modularizar scripts** | `.agents/skills/gitnexus-refactoring/SKILL.md` | `node .gitnexus/run.cjs detect-changes --scope all` |
| **Referencia completa de comandos CLI** | `.agents/skills/gitnexus-cli/SKILL.md` | `node .gitnexus/run.cjs --help` |

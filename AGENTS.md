<!-- gitnexus:start -->
# GitNexus — Code Intelligence

This project is indexed by GitNexus as **Seminario-de-Integracion-y-aplicacion** (90 symbols, 135 relationships, 6 execution flows).

> Index stale? Run `node .gitnexus/run.cjs analyze --index-only` from the project root — it auto-selects an available runner. No `.gitnexus/run.cjs` yet? Bootstrap with `npx`, `bunx`, or `pnpm dlx` — e.g. `bunx gitnexus@latest analyze` (npm 11 npx crash; #1939).

## Always Do

- **MUST run impact before editing.** Use `impact({target: "symbolName", direction: "upstream"})` or `node .gitnexus/run.cjs impact "symbolName" --direction upstream --repo .`; report callers, processes, and risk. Never substitute grep for graph analysis.
- **MUST analyze graph changes before committing.** Use `detect_changes({scope: "all"})` (MCP) or `node .gitnexus/run.cjs detect-changes --scope all --repo .` (CLI fallback). `partial: true` or `truncated: true` is not a clean check — a zero means unseen, not unaffected; re-run it. For regression review: `detect_changes({scope: "compare", base_ref: "main"})` or `node .gitnexus/run.cjs detect-changes --scope compare --base-ref "main" --repo .`.
- MUST warn on HIGH/CRITICAL `risk` pre-edit; never use `riskSharedAxes` to waive a HIGH/CRITICAL `risk` warning. Compare File/symbol: MCP File omits axes; Graph-RAG expands File.
- **MUST treat `risk: UNKNOWN` as unresolved, not as low.** An empty caller set is not evidence the symbol is unused — it can also mean the callers are not resolvable by the index (plain-object property access, dynamic dispatch, cross-language calls). `impact` pairs `UNKNOWN` with a `riskNote` saying so. Confirm with a text search before treating the symbol as safe to change or delete; do not proceed on the strength of a zero.
- **MUST use `query({search_query: "concept"})` for concepts/flows, `context({name: "symbolName"})` for a named symbol, or `impact` for blast radius, on read-only callers, dependencies, imports, or execution flow.** Graph first; text search only for empty/`UNKNOWN`/literals.
- For security review, `explain({target: "fileOrSymbol"})` lists taint findings (source→sink flows; needs `analyze --pdg`).

## Never Do

- NEVER edit a function, class, or method before MCP/CLI impact analysis.
- NEVER ignore HIGH or CRITICAL risk warnings from impact analysis, and never read `UNKNOWN` as an all-clear — it means the walk could not answer, which is the one verdict that requires confirming by other means.
- NEVER rename symbols with find-and-replace — use `rename` which understands the call graph.
- NEVER commit before MCP/CLI graph change analysis.

## Resources

| Resource | Use for |
| --- | --- |
| `gitnexus://repo/Seminario-de-Integracion-y-aplicacion/context` | Codebase overview, check index freshness |
| `gitnexus://repo/Seminario-de-Integracion-y-aplicacion/clusters` | All functional areas |
| `gitnexus://repo/Seminario-de-Integracion-y-aplicacion/processes` | All execution flows |
| `gitnexus://repo/Seminario-de-Integracion-y-aplicacion/process/{name}` | Step-by-step execution trace |

## CLI

| Task | Read this skill file |
| --- | --- |
| Understand architecture / "How does X work?" | `.claude/skills/gitnexus-exploring/SKILL.md` |
| Blast radius / "What breaks if I change X?" | `.claude/skills/gitnexus-impact-analysis/SKILL.md` |
| Trace bugs / "Why is X failing?" | `.claude/skills/gitnexus-debugging/SKILL.md` |
| Rename / extract / split / refactor | `.claude/skills/gitnexus-refactoring/SKILL.md` |
| Tools, resources, schema reference | `.claude/skills/gitnexus-guide/SKILL.md` |
| Index, status, clean, wiki CLI commands | `.claude/skills/gitnexus-cli/SKILL.md` |

<!-- gitnexus:end -->

---

# 🤖 Ecosistema Institucional y Reglas del Agente (CURZAS — UNCo)

Este repositorio corresponde al **Trabajo Final de Graduación (TFG) / Tesina** de la Universidad Nacional del Comahue (UNCo) — Centro Universitario Regional Zona Atlántica y Sur (CURZAS).

* **Carreras:** Ciclo Complementario de Licenciatura en Gestión de Recursos Humanos / Licenciatura en Administración Pública.
* **Materia:** Seminario de Integración y Aplicación (SIA) (2025 / 2026).
* **Autor / Alumno:** Tec. Sup. Héctor Daniel Ayarachi Fuentes (Legajo N° 8252 — DNI N° 35.492.138).
* **Equipo Docente:** Dra. Deborah Noguera (Responsable), Esp. Federico Abeiro y Esp. María Cecilia Aguirre (Ayudantes).
* **Marco Normativo:** Resolución CD-CURZAS N° 266/23 (Estructura formal del TFG), Res. 26/23 y 28/24.
* **Enfoque Técnico:** *Docs-as-Code* académico con soporte dual Quarto (`.qmd`) y Typst (`.typ`).

---

## 🧭 Ecosistema de Inteligencia Dual: GitNexus + NotebookLM

El proyecto opera bajo un modelo de colaboración simbiótica entre dos motores de inteligencia:

```text
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    ARQUITECTURA DE INTELIGENCIA DUAL                            │
├───────────────────────────────────────┬─────────────────────────────────────────┤
│    🧠 NOTEBOOKLM (Cerebro Académico)  │     🕸️ GITNEXUS (Cerebro Técnico)       │
├───────────────────────────────────────┼─────────────────────────────────────────┤
│ • Rigor conceptual y epistemológico   │ • Integridad de código y arquitectura   │
│ • Bibliografía de cátedra (SIA 1-4)   │ • Pipeline Docs-as-Code (compilar_todos)│
│ • Resoluciones UNCo (Res. 266/23)     │ • Grafo de dependencias y llamadas      │
│ • Consignas de TPs y devoluciones     │ • Análisis de impacto (blast radius)    │
│ • Generación de resúmenes y audios    │ • Detección de cambios y regresiones    │
│ ➔ GOBIERNA EL CONTENIDO Y EL FONDO    │ ➔ GOBIERNA LA FORMA Y LA INFRAESTRUCTURA│
└───────────────────────────────────────┴─────────────────────────────────────────┘
```

### 1. Documentación Normativa y Reglas Específicas
* **Reglas Académicas y Estándar Operativo Integral:** Ver [.agents/rules/AGENTS.md](file:///c:/Users/Ramoncito/.antigravity-ide/Seminario%20de%20Integraci%C3%B3n%20y%20Aplicaci%C3%B3n/.agents/rules/AGENTS.md).
* **Pautas Específicas de GitNexus (Código):** Ver [.agents/rules/gitnexus.md](file:///c:/Users/Ramoncito/.antigravity-ide/Seminario%20de%20Integraci%C3%B3n%20y%20Aplicaci%C3%B3n/.agents/rules/gitnexus.md).
* **Pautas Específicas de NotebookLM (Investigación):** Ver [.agents/rules/notebooklm.md](file:///c:/Users/Ramoncito/.antigravity-ide/Seminario%20de%20Integraci%C3%B3n%20y%20Aplicaci%C3%B3n/.agents/rules/notebooklm.md).
* **Pautas de Estilo Visual y Normas APA 7ma Edición:** Ver [.agents/rules/supreme_guidelines.md](file:///c:/Users/Ramoncito/.antigravity-ide/Seminario%20de%20Integraci%C3%B3n%20y%20Aplicaci%C3%B3n/.agents/rules/supreme_guidelines.md).
* **Convención de Commits Git (Español):** Ver [.agents/rules/git_commits.md](file:///c:/Users/Ramoncito/.antigravity-ide/Seminario%20de%20Integraci%C3%B3n%20y%20Aplicaci%C3%B3n/.agents/rules/git_commits.md).

### 2. Pipeline de Compilación y Comandos Rápidos
* **Compilar TP activo a Word (.docx) y PDF:** `python compilar_todos.py`
* **Compilar únicamente versión PDF:** `python compilar_todos.py --pdf`
* **Compilar únicamente versión Word:** `python compilar_todos.py --word`
* **Modo Vigilante (compilación en vivo):** `python compilar_todos.py --watch`
* **Análisis de impacto antes de editar código:** `node .gitnexus/run.cjs impact "<simbolo>" --direction upstream --repo .`
* **Detección de cambios de grafo antes de commit:** `node .gitnexus/run.cjs detect-changes --scope all --repo .`


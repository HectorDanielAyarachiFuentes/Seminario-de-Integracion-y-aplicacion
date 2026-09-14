# NotebookLM Workspace Rule

## Authentication & Token Management

Whenever interacting with the `notebooklm` MCP server in this workspace:

1. **If authentication fails (401 / expired tokens / RPC Error 16 / unauthenticated):**
   - **Primary Action (Zero-Prompt):** First check if fresh cookies are in the clipboard or `cookies.txt` by executing:
     ```powershell
     python herramientas/notebooklm/scripts/auth_helper.py --auto
     ```
     If valid cookies are found, call `refresh_auth` and resume seamlessly.
   - **User Guidance:** When explaining how to connect or recover a session, present two options:
     - **Opción 1: Extensión de 1-Clic (Rápida):** Cargar la extensión descomprimida `herramientas/notebooklm/chrome_extension/` en `chrome://extensions`. En NotebookLM hacer clic en `N` y decirle al agente *"conéctate"*.
     - **Opción 2: Modo Manual:** En `notebooklm.google.com` presionar `F12` -> `Network` -> recargar (`F5`) -> clic en `batchexecute` -> copiar `cookie:` de Request Headers y pegarlo en el chat o ejecutar `python herramientas/notebooklm/scripts/auth_helper.py`.
   - **Never commit credentials:** Cookies and `auth.json` are excluded via `.gitignore`. Never write credentials directly into committed files.

2. **Language Configuration:**
   - Always specify `language: "es"` when triggering Studio creations (`audio_overview_create`, `video_overview_create`, `slide_deck_create`, etc.) unless the user explicitly requests another language.

3. **Workspace Organization:**
   - Keep academic work and deliverables inside `tareas/` (for Planeamiento Organizacional).
   - Keep tool references and documentation inside `herramientas/notebooklm/`.
   - Do not litter the workspace root with temporary scratch scripts.

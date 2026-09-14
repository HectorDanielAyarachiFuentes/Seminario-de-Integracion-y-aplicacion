# ==============================================================================
# Script de Ejecución Rápida: Compilar Todos los TPs — SIA (UNCo CURZAS)
# ==============================================================================

param(
    [switch]$Typst,
    [switch]$Quarto,
    [switch]$Watch
)

$cmdArgs = @()

if ($Watch) {
    $cmdArgs += "--watch"
} elseif ($Typst) {
    $cmdArgs += "--typst"
} elseif ($Quarto) {
    $cmdArgs += "--quarto"
}

python compilar_todos.py @cmdArgs

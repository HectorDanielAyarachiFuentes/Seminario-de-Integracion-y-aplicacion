#show table.where(columns: 7): it => {
  // Ver si podemos cambiar las columnas
  table(
    columns: (2.5em, 1fr, 2.2em, 2.2em, 2.2em, 2.2em, 2.2em),
    ..it.children
  )
}

#table(
  columns: 7,
  [N], [Reactivo con texto muy largo que debería ocupar la mayor parte del ancho disponible], [1], [2], [3], [4], [5],
  [1], [La evaluación docente debería orientarse prioritariamente al aprendizaje pedagógico continuo y no al control formal.], [x], [], [], [], []
)

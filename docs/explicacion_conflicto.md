# Explicación del conflicto resuelto

## ¿Por qué ocurrió el conflicto?
Dos integrantes del equipo (Juan y Alberto) crearon ramas independientes a
partir de `develop` (`conflicto/readme-juan` y `conflicto/readme-companero`)
y ambos modificaron la misma línea de la sección "Integrantes" del archivo
`README.md`, cada uno agregando su propia información. Al integrar primero
la rama de Juan en `develop` sin problemas, y luego intentar integrar la
rama de Alberto, Git no pudo combinar automáticamente los cambios porque
ambas ramas modificaron la misma línea del archivo desde un punto de
partida común.

## ¿Qué archivos fueron afectados?
- `README.md` (sección "## Integrantes").

## ¿Cómo fue solucionado?
1. Se ejecutó `git merge conflicto/readme-companero`, lo que generó el
   conflicto marcado con `<<<<<<<`, `=======` y `>>>>>>>` en `README.md`.
2. Se analizó el contenido de ambas versiones en conflicto.
3. Se determinó que el contenido correcto era conservar ambas líneas, ya
   que no eran excluyentes sino complementarias (cada una describe a un
   integrante distinto del equipo).
4. Se editó manualmente el archivo `README.md` eliminando las marcas de
   conflicto y dejando ambas líneas de integrantes.
5. Se marcó el archivo como resuelto con `git add README.md`.
6. Se finalizó la integración con
   `git commit -m "fix: resolver conflicto en README.md integrando aportes de ambos integrantes"`.

El commit de resolución quedó registrado en el historial (`abeb776` en el
`git log --oneline --graph --all`), evidenciando el punto exacto donde
ambas ramas convergieron y se resolvió la divergencia.

## Perspectiva del compañero de equipo

Desde mi lado (Alberto), lo que más me sorprendió del conflicto fue darme
cuenta de que Git no se equivocó ni rompió nada: simplemente se detuvo
porque no podía decidir por nosotros. Las dos versiones de la línea eran
válidas, y esa decisión le correspondía al equipo, no a la herramienta.
Comparado con lo que hacíamos antes (mandarnos los archivos por correo o
WhatsApp), donde el último en guardar borraba silenciosamente el trabajo
del otro, acá el cambio quedó frenado hasta que alguien lo revisara.

También me quedó claro que las marcas `<<<<<<<`, `=======` y `>>>>>>>` no
son un error del archivo, sino una forma de mostrarnos las dos versiones
juntas para compararlas. Lo importante es no borrar una de las dos por
apuro: en este caso las líneas eran complementarias y había que conservar
ambas.

Para más adelante me llevo tres cuidados concretos:

1. Hacer `git pull` de `develop` antes de empezar a trabajar y antes de
   integrar, para partir siempre de la versión más reciente.
2. Repartir mejor los archivos entre los integrantes. Muchos conflictos se
   evitan solos si cada uno trabaja en secciones o archivos distintos, y
   coordinamos antes quién toca qué.
3. Hacer commits pequeños y frecuentes. Cuando el cambio es chico, el
   conflicto también lo es y se resuelve en un minuto; si uno acumula todo
   para un commit grande al final, resolverlo se vuelve mucho más difícil.

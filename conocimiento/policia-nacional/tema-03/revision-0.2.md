# Informe de revisión 0.2 · Tema 3

**Versión corregida:** 0.2.1
**Fecha de cierre técnico:** 16/07/2026
**Estado editorial:** approved
**Estado de publicación:** not_published
**Estado en GitHub:** preparado para sustituir la versión 0.2.0; esta copia local todavía no modifica el repositorio.

## Motivo de la corrección

La versión 0.2.0 empleaba la primera frase de cada bloque para generar El Parte y añadía una nota repetida para generar El Atestado. Ese mecanismo producía dos fallos:

- El Parte perdía conceptos esenciales cuando un bloque contenía varias materias.
- El Atestado era más largo, pero no desarrollaba jurídicamente cada materia con profundidad suficiente.

## Solución aplicada

La fuente maestra continúa siendo única, pero cada bloque contiene ahora dos representaciones sincronizadas:

- `PARTE`: síntesis completa de todos los conceptos esenciales del bloque.
- `ATESTADO`: explicación desarrollada, diferencias, requisitos, efectos y trampas habituales.

El compilador ya no corta frases ni inventa ampliaciones genéricas. Extrae directamente la representación correspondiente.

## Comprobaciones reforzadas

- Versión coherente `0.2.1`.
- Exactamente 25 bloques y seis capas.
- Todos los bloques contienen Parte y Atestado.
- El Parte conserva los conceptos críticos de cada bloque.
- El Atestado es sustancialmente más desarrollado.
- No aparece «En cristiano».
- No se incorporan preguntas oficiales sin trazabilidad.
- El archivo legado permanece preservado.
- La publicación para alumnos continúa en estado `not_published`.

## Estado

Archivos corregidos y validados localmente. Deben sustituir a sus equivalentes del repositorio. No se ha realizado commit, push ni publicación para alumnos.

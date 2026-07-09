# 🛡️ Academia En Vigor

**El temario que nunca descansa** · Preparación online de oposiciones a Policía Nacional (Escala Básica) · Convocatoria 2027

## Qué hace diferente a este temario

- **Vivo:** un vigilante automático (`vigia_boe.py` + GitHub Actions) consulta cada lunes la API oficial del BOE y avisa si cambia cualquier norma del programa, indicando los temas afectados.
- **Con memoria de examen:** cada punto lleva la referencia 📅 de las convocatorias en que ha caído, con la sección "Así lo preguntaron" al cierre de cada tema.
- **Pedagogía de 5+1 capas:** Mapa del tema → Contenido completo → 💡 En cristiano → 🚔 En la calle → 🎯 Lo que cae → 📅 Ha caído.
- **Preparado por personal en activo.**

## Estructura del repositorio

```
├── README.md                      ← esta portada
├── temario.json                   ← cerebro de datos: 45 temas, normativa, marca, convenciones
├── temario-estructura-completa.md ← estructura maestra de los 45 temas
├── vigia_boe.py                   ← vigilante de legislación (API BOE)
├── vigia-estado.json              ← (lo genera el vigía) última fecha conocida de cada norma
├── vigia-informe.md               ← (lo genera el vigía) informe de cambios
├── .github/workflows/
│   └── vigia-boe.yml              ← tarea programada: lunes 6:00 UTC
├── temas/
│   ├── tema-01-el-derecho.md
│   ├── tema-02-constitucion-1.md
│   └── tema-03-constitucion-2.md
├── data/
│   └── examen-2025-XLII-A.json    ← preguntas oficiales mapeadas a temas
└── img/
    ├── logo-academia-en-vigor.svg
    └── t01-piramide-jerarquia.svg
```

## Convenciones

- **Temas:** markdown, divididos en 🟦 PARTES (~1 audio-repaso cada una). Marcadores `<!-- 🎨 SVG · ... -->` señalan las imágenes pendientes de producir.
- **Imágenes:** SVG, fondo blanco (impresión B/N), azul claro PN `#dbeafe` para lo importante y verde claro GC `#dcfce7` para notas. Nomenclatura `tNN-descripcion.svg` en `img/`.
- **Exámenes:** un JSON por convocatoria en `data/`, con resúmenes propios de cada pregunta y mapeo a temas. Regla de oro: solo referencias verificadas contra exámenes oficiales.
- **Versionado:** `meta.version_datos` en temario.json; cada tema lleva su versión al pie.

## Estado del proyecto

- [x] Estructura oficial de los 45 temas (act. ago 2025, verificada jul 2026)
- [x] Identidad: nombre, logo, eslogan, paleta
- [x] Vigía BOE (pendiente primera ejecución de prueba)
- [x] Temas 1-3 completos
- [x] Examen 2025 (XLII) mapeado — 100 preguntas
- [ ] Exámenes 2019-2024
- [ ] Temas 4-45
- [ ] Producción de SVGs por tema
- [ ] Web (GitHub Pages) · captura de emails · monetización

---
© Academia En Vigor. Contenido en fase de producción — no distribuir.

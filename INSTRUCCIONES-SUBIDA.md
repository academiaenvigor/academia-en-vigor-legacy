# Instrucciones de subida · Tema 3 v0.3.0

## Operación

Descomprime el ZIP en la raíz del repositorio y conserva la estructura de carpetas.

## Archivos que sustituyen versiones anteriores

- `conocimiento/policia-nacional/tema-03/manifest.json`
- `conocimiento/policia-nacional/tema-03/master.md`
- `banco-preguntas/policia-nacional/tema-03/manifest.json`
- `banco-preguntas/policia-nacional/tema-03/preguntas.jsonl`
- `banco-preguntas/policia-nacional/tema-03/schema-pregunta.json`
- `banco-preguntas/policia-nacional/tema-03/README.md`
- `scripts/compilar_tema.py`
- `scripts/validar_banco_tema_03.py`
- `tests/test_tema_03.py`
- `tests/test_banco_tema_03.py`
- `temas/policia-nacional/parte/tema-03-constitucion-espanola-ii.md`
- `temas/policia-nacional/atestado/tema-03-constitucion-espanola-ii.md`

## Archivos y carpetas nuevos

- `conocimiento/policia-nacional/tema-03/cobertura.json`
- `conocimiento/policia-nacional/tema-03/revision-0.3.md`
- `evaluaciones/policia-nacional/tema-03/`
- `materiales/policia-nacional/tema-03/`
- `scripts/generar_evaluaciones_tema_03.py`
- `tests/test_evaluaciones_tema_03.py`
- `RESUMEN-ENTREGA.json`

## Archivos que deben conservarse

- `conocimiento/policia-nacional/tema-03/revision-0.2.md`, como historial.
- `temas/parte/tema-03-constitucion-2.md`, como archivo legado hasta la consolidación general.
- `fuentes/catalogo.json`, que no necesita cambios en esta entrega.

## Comprobación después de copiar

```bash
python3 -m json.tool conocimiento/policia-nacional/tema-03/manifest.json
python3 -m json.tool conocimiento/policia-nacional/tema-03/cobertura.json
python3 -m json.tool banco-preguntas/policia-nacional/tema-03/manifest.json
python3 scripts/compilar_tema.py --check
python3 scripts/validar_banco_tema_03.py
python3 scripts/generar_evaluaciones_tema_03.py
python3 -m unittest -v tests/test_tema_03.py tests/test_banco_tema_03.py tests/test_evaluaciones_tema_03.py
git diff --check
```

No borres todavía las carpetas antiguas generales `temas/parte`, `temas/atestado` o `data/tests`.

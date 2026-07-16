#!/usr/bin/env python3
import json, collections, pathlib, sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
path=ROOT/'banco-preguntas/policia-nacional/tema-03/preguntas.jsonl'
qs=[json.loads(x) for x in path.read_text(encoding='utf8').splitlines() if x.strip()]
assert len(qs)==50, f"Se esperaban 50 preguntas y hay {len(qs)}"
assert len({q['id'] for q in qs})==len(qs), 'IDs duplicados'
assert set(q['punto'] for q in qs)==set(range(1,26)), 'Cobertura incompleta'
assert all(set(q['opciones'])=={'A','B','C'} for q in qs), 'Opciones inválidas'
assert all(q['respuesta_correcta'] in 'ABC' for q in qs), 'Respuesta inválida'
assert all(q['caracter']=='propio' and q['referencia_oficial'] is None for q in qs), 'Oficialidad incorrecta'
assert all(q['content_version']=='0.2.0' for q in qs), 'Versión incoherente'
c=collections.Counter(q['respuesta_correcta'] for q in qs)
assert max(c.values())-min(c.values())<=1, f'Distribución desequilibrada: {c}'
for q in qs:
    assert len(q['explicacion'])>=30
    assert q['opciones'][q['respuesta_correcta']]
print(f'OK: {len(qs)} preguntas; cobertura 25/25; respuestas {dict(c)}')

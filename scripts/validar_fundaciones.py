#!/usr/bin/env python3
from pathlib import Path
import json, re, sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
for p in [ROOT/'conocimiento/policia-nacional/tema-03/manifest.json',ROOT/'fuentes/catalogo.json']:
 try: json.loads(p.read_text())
 except Exception as e: errors.append(f'{p}: {e}')
m=json.loads((ROOT/'conocimiento/policia-nacional/tema-03/manifest.json').read_text())
c=json.loads((ROOT/'fuentes/catalogo.json').read_text())
if len(c['sources'])!=13: errors.append('El catálogo no contiene 13 referencias')
ids={s['id'] for s in c['sources']}
if set(m['official_references'])-ids: errors.append('Referencias del manifest no resueltas')
for p in [ROOT/m['source_file'],*(ROOT/x for x in m['outputs'].values()),ROOT/m['review']['review_file']]:
 if not p.exists(): errors.append(f'Falta {p.relative_to(ROOT)}')
for p in ROOT.rglob('*.md'):
 txt=p.read_text()
 for link in re.findall(r'!\[[^]]*\]\(([^)]+)\)',txt):
  if not link.startswith(('http://','https://')) and not (p.parent/link).resolve().exists(): errors.append(f'Imagen rota {p}: {link}')
if errors:
 print('\n'.join(errors)); raise SystemExit(1)
print('OK: fundaciones, referencias y rutas validadas')

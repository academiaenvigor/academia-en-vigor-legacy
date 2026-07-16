#!/usr/bin/env python3
from pathlib import Path
import argparse, json, re, sys
ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/'conocimiento/policia-nacional/tema-03/manifest.json'

def load():
 m=json.loads(MANIFEST.read_text())
 src=ROOT/m['source_file']; text=src.read_text()
 blocks=[]
 pat=re.compile(r'<!-- BLOCK (\d{2}) START -->\n## \d+\. (.*?)\n\*\*Fuente:\*\* `([^`]+)`\n(.*?)\n\n<!-- BLOCK \1 END -->',re.S)
 for num,title,source,body in pat.findall(text): blocks.append((num,title,source,body.strip()))
 layers={}
 for key in ['MAPA','CONTENIDO','HABLEMOS_CLARO','EN_LA_CALLE','LO_QUE_CAE','HA_CAIDO']:
  mm=re.search(rf'<!-- LAYER:{key} -->\n# ([^\n]+)\n(.*?)(?=\n<!-- LAYER:|\Z)',text,re.S)
  if not mm: raise ValueError(f'Falta capa {key}')
  layers[key]=(mm.group(1),mm.group(2).strip())
 return m,blocks,layers

def render(kind,m,blocks,layers):
 title=f"# TEMA 3 · LA CONSTITUCIÓN ESPAÑOLA (II)\n\n**Policía Nacional · Método VIGOR · {kind.upper()}**\n**Versión de contenido:** {m['content_version']}\n**Estado editorial:** {m['editorial_status']} · **Publicación:** {m['publication_status']}\n\n"
 out=[title]
 order=['MAPA','CONTENIDO','HABLEMOS_CLARO','EN_LA_CALLE','LO_QUE_CAE','HA_CAIDO']
 # Mapa first
 out += [f"# {layers['MAPA'][0]}\n\n{layers['MAPA'][1]}\n"]
 out += ['# Contenido\n']
 for num,t,s,b in blocks:
  if kind=='parte':
   first=re.split(r'(?<=[.!?])\s+',b)[0]
   body=first + ('' if first.endswith('.') else '.')
  else:
   body=b+f"\n\n**Clave de examen:** relaciona este bloque con su norma y artículo; evita confundir órgano competente, mayoría, plazo y efecto jurídico. **Trazabilidad:** `{s}`."
  out += [f"## {num}. {t}\n\n{body}\n\n*Referencia oficial: `{s}`.*\n"]
 for key in order[2:]:
  out += [f"# {layers[key][0]}\n\n{layers[key][1]}\n"]
 out += [f"---\n\n*Academia En Vigor · El temario que nunca duerme · Tema 3 · v{m['content_version']} · Documento interno no publicado.*\n"]
 return '\n'.join(out)

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--write',action='store_true'); ap.add_argument('--check',action='store_true'); args=ap.parse_args()
 m,b,l=load()
 if len(b)!=m['semantic_blocks']: raise SystemExit('Número de bloques incoherente')
 failed=[]
 for kind,path in m['outputs'].items():
  target=ROOT/path; expected=render(kind,m,b,l)
  if args.write:
   target.parent.mkdir(parents=True,exist_ok=True); target.write_text(expected)
  if args.check and (not target.exists() or target.read_text()!=expected): failed.append(path)
 if args.check and failed:
  print('Derivados desactualizados:',*failed,sep='\n- '); return 1
 print(f"OK: {len(b)} bloques; derivados {'escritos' if args.write else 'verificados' if args.check else 'calculados'}")
 return 0
if __name__=='__main__': raise SystemExit(main())

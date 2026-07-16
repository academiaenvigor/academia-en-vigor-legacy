import json,re,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class Tema03(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.m=json.loads((ROOT/'conocimiento/policia-nacional/tema-03/manifest.json').read_text(encoding='utf-8'))
  cls.c=json.loads((ROOT/'conocimiento/policia-nacional/tema-03/cobertura.json').read_text(encoding='utf-8'))
  cls.master=(ROOT/cls.m['source_file']).read_text(encoding='utf-8')
  cls.parte=(ROOT/cls.m['outputs']['parte']).read_text(encoding='utf-8')
  cls.atestado=(ROOT/cls.m['outputs']['atestado']).read_text(encoding='utf-8')
 def test_version(self): self.assertEqual(self.m['content_version'],'0.3.0')
 def test_blocks(self): self.assertEqual(self.master.count('<!-- BLOCK '),50); self.assertEqual(self.m['semantic_blocks'],25)
 def test_layers(self):
  expected=['Mapa del tema','Contenido','Hablemos claro','En la calle','Lo que cae','Ha caído']; self.assertEqual(self.m['layers'],expected)
  for d in (self.parte,self.atestado): self.assertEqual(sum(d.count('# '+x) for x in expected),6)
 def test_atomic_facts(self): self.assertEqual(self.master.count('<!-- FACT:'),self.m['atomic_facts']); self.assertEqual(self.c['coverage_percent'],100.0)
 def test_all_articles(self): self.assertEqual(self.c['required_constitution_articles'],self.c['covered_constitution_articles'])
 def test_derivatives(self): self.assertGreater(len(self.atestado),len(self.parte)*2); self.assertIn('artículo 149',self.atestado.lower())
 def test_required_topics(self):
  for x in ['consorte','juramento','mandato imperativo','comisiones de investigación','referéndum consultivo','consejo de estado','acción popular','concejo abierto','leyes de armonización','fondo de compensación','plenos efectos frente a todos','referéndum obligatorio']:
   self.assertIn(x,self.atestado.lower())
 def test_no_old_label(self):
  for d in (self.master,self.parte,self.atestado): self.assertNotIn('En cristiano',d)
 def test_ha_caido(self): self.assertIn('No se incorporan preguntas oficiales',self.master.split('# Ha caído',1)[1])
 def test_legacy(self): self.assertIn('temas/parte/tema-03-constitucion-2.md',self.m['legacy_files_preserved'])
if __name__=='__main__': unittest.main()

import json, re, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class Tema03(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.m=json.loads((ROOT/'conocimiento/policia-nacional/tema-03/manifest.json').read_text())
  cls.master=(ROOT/cls.m['source_file']).read_text()
  cls.parte=(ROOT/cls.m['outputs']['parte']).read_text()
  cls.atestado=(ROOT/cls.m['outputs']['atestado']).read_text()
 def test_version(self): self.assertEqual(self.m['content_version'],'0.2.0')
 def test_review_states(self):
  self.assertEqual(self.m['editorial_status'],'approved'); self.assertEqual(self.m['publication_status'],'not_published')
  self.assertTrue(all(v=='approved' for k,v in self.m['review'].items() if k in {'legal','pedagogical','editorial'}))
 def test_review_file(self): self.assertTrue((ROOT/'conocimiento/policia-nacional/tema-03/revision-0.2.md').exists())
 def test_exact_layers(self):
  self.assertEqual(self.m['layers'],['Mapa del tema','Contenido','Hablemos claro','En la calle','Lo que cae','Ha caído'])
  for doc in (self.parte,self.atestado):
   self.assertEqual(sum(doc.count('# '+x) for x in self.m['layers']),6)
 def test_required_content(self):
  for term in ['decretos-leyes','Tratados internacionales','artículo 150','Cuestión de inconstitucionalidad']:
   self.assertIn(term.lower(),self.master.lower())
 def test_no_old_label(self):
  for doc in (self.master,self.parte,self.atestado): self.assertNotIn('En cristiano',doc)
 def test_atestado_longer(self): self.assertGreater(len(self.atestado),len(self.parte)*1.35)
 def test_blocks_and_refs(self):
  self.assertEqual(self.master.count(' START -->'),25); self.assertEqual(len(self.m['official_references']),13)
 def test_ha_caido_safe(self):
  section=self.master.split('# Ha caído',1)[1]
  self.assertIn('No se incorporan preguntas oficiales',section)
  self.assertNotRegex(section,r'\b20(?:1\d|2[0-6])\b.*pregunta')
 def test_versions_coherent(self):
  for doc in (self.master,self.parte,self.atestado): self.assertIn('0.2.0',doc)
 def test_legacy_preserved_declaration(self): self.assertIn('temas/parte/tema-03-constitucion-2.md',self.m['legacy_files_preserved'])
if __name__=='__main__': unittest.main()

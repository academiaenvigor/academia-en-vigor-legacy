import json,unittest,collections
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class BancoTema03(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.c=json.loads((ROOT/'conocimiento/policia-nacional/tema-03/cobertura.json').read_text(encoding='utf-8'))
  cls.q=[json.loads(x) for x in (ROOT/'banco-preguntas/policia-nacional/tema-03/preguntas.jsonl').read_text(encoding='utf-8').splitlines() if x.strip()]
 def test_ids(self): self.assertEqual(len(self.q),len({q['id'] for q in self.q}))
 def test_unique_wording(self): self.assertEqual(len(self.q),len({q['enunciado'] for q in self.q}))
 def test_all_facts_covered(self): self.assertEqual({f['id'] for f in self.c['facts']},{q['fact_id'] for q in self.q})
 def test_options(self):
  for q in self.q:
   self.assertEqual(set(q['opciones']),{'A','B','C'}); self.assertEqual(len(set(q['opciones'].values())),3)
 def test_balance(self):
  c=collections.Counter(q['respuesta_correcta'] for q in self.q); self.assertLessEqual(max(c.values())-min(c.values()),1)
 def test_versions(self): self.assertTrue(all(q['content_version']=='0.3.0' for q in self.q))
 def test_no_fake_officials(self): self.assertTrue(all(q['caracter']=='propio' and q['referencia_oficial'] is None for q in self.q))
 def test_risk5_double(self):
  c=collections.Counter(q['fact_id'] for q in self.q); self.assertTrue(all(c[f['id']]>=2 for f in self.c['facts'] if f['risk']==5))
if __name__=='__main__': unittest.main()

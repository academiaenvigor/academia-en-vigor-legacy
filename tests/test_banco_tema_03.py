import json, pathlib, unittest, collections
ROOT=pathlib.Path(__file__).resolve().parents[1]
P=ROOT/'banco-preguntas/policia-nacional/tema-03/preguntas.jsonl'
class BancoTema03(unittest.TestCase):
 @classmethod
 def setUpClass(cls): cls.q=[json.loads(x) for x in P.read_text(encoding='utf8').splitlines()]
 def test_total(self): self.assertEqual(len(self.q),50)
 def test_cobertura(self): self.assertEqual({q['punto'] for q in self.q},set(range(1,26)))
 def test_dos_por_punto(self): self.assertTrue(all(v==2 for v in collections.Counter(q['punto'] for q in self.q).values()))
 def test_ids_unicos(self): self.assertEqual(len({q['id'] for q in self.q}),50)
 def test_tres_opciones(self): self.assertTrue(all(set(q['opciones'])=={'A','B','C'} for q in self.q))
 def test_equilibrio(self):
  c=collections.Counter(q['respuesta_correcta'] for q in self.q); self.assertLessEqual(max(c.values())-min(c.values()),1)
 def test_version(self): self.assertTrue(all(q['content_version']=='0.2.0' for q in self.q))
 def test_sin_oficiales_falsas(self): self.assertTrue(all(q['caracter']=='propio' and q['referencia_oficial'] is None for q in self.q))
 def test_conceptos_clave(self):
  txt=' '.join(q['concepto']+' '+q['enunciado'] for q in self.q).lower()
  for term in ['decreto-ley','tratado','artículo 150','cuestión de inconstitucionalidad']: self.assertIn(term,txt)
if __name__=='__main__': unittest.main()

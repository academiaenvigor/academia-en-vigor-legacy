import collections
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class EvaluacionesTema03(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bank = [
            json.loads(line)
            for line in (
                ROOT / "banco-preguntas/policia-nacional/tema-03/preguntas.jsonl"
            ).read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        cls.catalogue = json.loads(
            (
                ROOT / "evaluaciones/policia-nacional/tema-03/tests-generados/catalogo.json"
            ).read_text(encoding="utf-8")
        )

    @staticmethod
    def load(entry):
        return json.loads((ROOT / entry["ruta"]).read_text(encoding="utf-8"))

    def test_catalogue_counts(self):
        self.assertEqual(self.catalogue["total_tests"], 61)
        self.assertEqual(self.catalogue["tests_cobertura_bloque"], 40)
        self.assertEqual(self.catalogue["tests_por_partes"], 18)
        self.assertEqual(self.catalogue["tests_finales"], 3)

    def test_block_tests_cover_bank_exactly_once(self):
        ids = []
        for entry in self.catalogue["tests"]:
            if entry["tipo"] == "cobertura_bloque":
                ids.extend(q["id"] for q in self.load(entry)["preguntas"])
        expected = [q["id"] for q in self.bank]
        self.assertEqual(collections.Counter(ids), collections.Counter(expected))

    def test_block_test_maximum(self):
        for entry in self.catalogue["tests"]:
            if entry["tipo"] == "cobertura_bloque":
                self.assertLessEqual(entry["preguntas"], 25)
                self.assertGreater(entry["preguntas"], 0)

    def test_part_tests(self):
        entries = [e for e in self.catalogue["tests"] if e["tipo"] == "test_parte"]
        self.assertEqual(len(entries), 18)
        for entry in entries:
            data = self.load(entry)
            self.assertEqual(len(data["preguntas"]), 25)
            self.assertEqual(len({q["fact_id"] for q in data["preguntas"]}), 25)
            self.assertTrue(set(q["bloque"] for q in data["preguntas"]).issubset(set(entry["bloques"])))

    def test_final_tests(self):
        entries = [e for e in self.catalogue["tests"] if e["tipo"] == "test_final"]
        self.assertEqual([e["preguntas"] for e in entries], [25, 50, 100])
        for entry in entries:
            data = self.load(entry)
            self.assertEqual(len(data["preguntas"]), entry["preguntas"])
            self.assertEqual(len({q["fact_id"] for q in data["preguntas"]}), entry["preguntas"])

    def test_solutions_match_bank(self):
        bank = {q["id"]: q for q in self.bank}
        for entry in self.catalogue["tests"]:
            data = self.load(entry)
            self.assertEqual(len(data["preguntas"]), len(data["soluciones"]))
            for solution in data["soluciones"]:
                self.assertEqual(
                    solution["respuesta_correcta"],
                    bank[solution["id"]]["respuesta_correcta"],
                )


if __name__ == "__main__":
    unittest.main()

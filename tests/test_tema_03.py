import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class Tema03(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads(
            (ROOT / "conocimiento/policia-nacional/tema-03/manifest.json")
            .read_text(encoding="utf-8")
        )
        cls.master = (ROOT / cls.manifest["source_file"]).read_text(encoding="utf-8")
        cls.parte = (ROOT / cls.manifest["outputs"]["parte"]).read_text(encoding="utf-8")
        cls.atestado = (ROOT / cls.manifest["outputs"]["atestado"]).read_text(encoding="utf-8")

    def test_version(self):
        self.assertEqual(self.manifest["content_version"], "0.2.1")

    def test_review_states(self):
        self.assertEqual(self.manifest["editorial_status"], "approved")
        self.assertEqual(self.manifest["publication_status"], "not_published")
        self.assertTrue(
            all(
                self.manifest["review"][key] == "approved"
                for key in ("legal", "pedagogical", "editorial")
            )
        )

    def test_review_file(self):
        self.assertTrue(
            (ROOT / "conocimiento/policia-nacional/tema-03/revision-0.2.md").exists()
        )

    def test_exact_layers(self):
        expected = [
            "Mapa del tema",
            "Contenido",
            "Hablemos claro",
            "En la calle",
            "Lo que cae",
            "Ha caído",
        ]
        self.assertEqual(self.manifest["layers"], expected)
        for document in (self.parte, self.atestado):
            self.assertEqual(sum(document.count("# " + layer) for layer in expected), 6)

    def test_each_block_has_both_representations(self):
        self.assertEqual(self.master.count("<!-- BLOCK "), 50)
        self.assertEqual(self.master.count("<!-- PARTE START -->"), 25)
        self.assertEqual(self.master.count("<!-- PARTE END -->"), 25)
        self.assertEqual(self.master.count("<!-- ATESTADO START -->"), 25)
        self.assertEqual(self.master.count("<!-- ATESTADO END -->"), 25)

    def test_required_content_in_both_derivatives(self):
        required = [
            "regencia",
            "tutela",
            "decretos-leyes",
            "tratados",
            "estado de excepción",
            "estado de sitio",
            "artículo 150",
            "artículo 155",
            "cuestión de inconstitucionalidad",
            "reforma agravada",
        ]
        for term in required:
            self.assertIn(term.lower(), self.parte.lower(), term)
            self.assertIn(term.lower(), self.atestado.lower(), term)

    def test_no_old_label(self):
        for document in (self.master, self.parte, self.atestado):
            self.assertNotIn("En cristiano", document)

    def test_atestado_is_substantially_developed(self):
        self.assertGreater(len(self.atestado), len(self.parte) * 2.0)
        self.assertGreater(len(self.atestado), 20000)

    def test_no_generic_repeated_expansion(self):
        repeated = (
            "relaciona este bloque con su norma y artículo; evita confundir "
            "órgano competente, mayoría, plazo y efecto jurídico"
        )
        self.assertNotIn(repeated, self.atestado)

    def test_blocks_and_refs(self):
        self.assertEqual(self.master.count(" START -->"), 75)
        self.assertEqual(len(self.manifest["official_references"]), 13)

    def test_ha_caido_safe(self):
        section = self.master.split("# Ha caído", 1)[1]
        self.assertIn("No se incorporan preguntas oficiales", section)
        self.assertNotRegex(section, r"\b20(?:1\d|2[0-6])\b.*pregunta")

    def test_versions_coherent(self):
        for document in (self.master, self.parte, self.atestado):
            self.assertIn("0.2.1", document)

    def test_legacy_preserved_declaration(self):
        self.assertIn(
            "temas/parte/tema-03-constitucion-2.md",
            self.manifest["legacy_files_preserved"],
        )

if __name__ == "__main__":
    unittest.main()

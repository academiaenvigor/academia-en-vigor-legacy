#!/usr/bin/env python3
"""Genera tests estáticos del Tema 3 desde el banco canónico.

- Tests de cobertura por bloque: contienen todas las preguntas exactamente una vez.
- Tres tests de 25 preguntas por cada parte.
- Tests finales de 25, 50 y 100 preguntas.
"""
from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
VERSION = "0.3.0"
BANK = ROOT / "banco-preguntas/policia-nacional/tema-03/preguntas.jsonl"
OUT = ROOT / "evaluaciones/policia-nacional/tema-03/tests-generados"

BLOCK_TITLES = {
    1: "La Corona: posición, inviolabilidad y refrendo",
    2: "Funciones del Rey",
    3: "Sucesión, regencia, tutela y juramento",
    4: "La Casa del Rey y el consorte",
    5: "Cortes Generales: naturaleza y estatuto",
    6: "Congreso, Senado e inelegibilidades",
    7: "Autonomía parlamentaria y prerrogativas",
    8: "Funcionamiento de las Cámaras",
    9: "Producción normativa y delegación legislativa",
    10: "Iniciativa, procedimiento legislativo y referéndum",
    11: "Tratados internacionales",
    12: "Gobierno: funciones, composición y estatuto",
    13: "Investidura, nombramiento, cese y responsabilidad",
    14: "Administración Pública y Consejo de Estado",
    15: "Relaciones Gobierno-Cortes y control parlamentario",
    16: "Confianza, censura, disolución y estados excepcionales",
    17: "Poder Judicial: principios y funcionamiento",
    18: "CGPJ, Tribunal Supremo, Ministerio Fiscal y Policía Judicial",
    19: "Principios de la organización territorial",
    20: "Municipios, provincias y acceso a la autonomía",
    21: "Estatutos y competencias de los artículos 148 y 149",
    22: "Artículo 150 y organización institucional autonómica",
    23: "Control autonómico, artículo 155 y financiación",
    24: "Tribunal Constitucional",
    25: "Reforma constitucional",
}

PARTS = [
    ("P1", [1, 2, 3, 4], "La Corona"),
    ("P2", list(range(5, 12)), "Cortes y producción normativa"),
    ("P3", list(range(12, 17)), "Gobierno, control y estados excepcionales"),
    ("P4", [17, 18], "Poder Judicial"),
    ("P5", list(range(19, 24)), "Organización territorial"),
    ("P6", [24, 25], "Tribunal Constitucional y reforma"),
]


def load_questions() -> list[dict]:
    return [json.loads(line) for line in BANK.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def balanced(items: list[dict]) -> list[dict]:
    groups = {letter: [q for q in items if q["respuesta_correcta"] == letter] for letter in "ABC"}
    output: list[dict] = []
    while any(groups.values()):
        for letter in "ABC":
            if groups[letter]:
                output.append(groups[letter].pop(0))
    return output


def public_test(test_id: str, title: str, blocks: list[int], items: list[dict], test_type: str) -> dict:
    return {
        "id": test_id,
        "titulo": title,
        "content_version": VERSION,
        "bank_version": VERSION,
        "tipo": test_type,
        "ambito": {"bloques": blocks},
        "numero_preguntas": len(items),
        "preguntas": [
            {
                "id": q["id"],
                "fact_id": q["fact_id"],
                "bloque": q["bloque"],
                "concepto": q["concepto"],
                "articulo": q["articulo"],
                "tipo": q["tipo"],
                "dificultad": q["dificultad"],
                "enunciado": q["enunciado"],
                "opciones": q["opciones"],
            }
            for q in items
        ],
        "soluciones": [
            {
                "id": q["id"],
                "respuesta_correcta": q["respuesta_correcta"],
                "explicacion": q["explicacion"],
                "fact_id": q["fact_id"],
                "articulo": q["articulo"],
            }
            for q in items
        ],
        "estado": "generado_validado",
        "publicacion": "not_published",
    }


def select_round_robin(questions: list[dict], blocks: list[int], count: int, offset: int = 0) -> list[dict]:
    pools = {block: balanced([q for q in questions if q["bloque"] == block]) for block in blocks}
    positions = {block: offset % len(pools[block]) for block in blocks}
    selected: list[dict] = []
    used_facts: set[str] = set()

    while len(selected) < count:
        added = False
        for block in blocks:
            pool = pools[block]
            for _ in range(len(pool)):
                question = pool[positions[block] % len(pool)]
                positions[block] += 1
                if question["fact_id"] not in used_facts:
                    selected.append(question)
                    used_facts.add(question["fact_id"])
                    added = True
                    break
            if len(selected) >= count:
                break
        if not added:
            break

    if len(selected) != count:
        raise RuntimeError(f"No se pudieron seleccionar {count} preguntas únicas para bloques {blocks}")
    return balanced(selected)


def main() -> int:
    questions = load_questions()
    if OUT.exists():
        shutil.rmtree(OUT)

    catalogue: list[dict] = []
    coverage_ids: list[str] = []

    # Tests de cobertura: todas las preguntas del bloque, en lotes de máximo 25.
    for block in range(1, 26):
        pool = balanced([q for q in questions if q["bloque"] == block])
        for index in range(0, len(pool), 25):
            chunk = pool[index:index + 25]
            variant = chr(ord("A") + index // 25)
            test_id = f"PN-T03-B{block:02d}-{variant}"
            relative = Path("evaluaciones/policia-nacional/tema-03/tests-generados/por-bloques") / f"{test_id}.json"
            write_json(ROOT / relative, public_test(
                test_id,
                f"Tema 3 · Bloque {block}: {BLOCK_TITLES[block]} · Test {variant}",
                [block],
                chunk,
                "cobertura_bloque",
            ))
            catalogue.append({"id": test_id, "ruta": relative.as_posix(), "tipo": "cobertura_bloque", "preguntas": len(chunk), "bloques": [block]})
            coverage_ids.extend(q["id"] for q in chunk)

    # Tres variantes por parte.
    for code, blocks, title in PARTS:
        for variant, offset in zip("ABC", (0, 7, 14)):
            items = select_round_robin(questions, blocks, 25, offset)
            test_id = f"PN-T03-{code}-{variant}"
            relative = Path("evaluaciones/policia-nacional/tema-03/tests-generados/por-partes") / f"{test_id}.json"
            write_json(ROOT / relative, public_test(test_id, f"Tema 3 · Parte {code[-1]} · {title} · Test {variant}", blocks, items, "test_parte"))
            catalogue.append({"id": test_id, "ruta": relative.as_posix(), "tipo": "test_parte", "preguntas": 25, "bloques": blocks})

    # Tests finales.
    for variant, count, offset in (("A", 25, 0), ("B", 50, 11), ("C", 100, 23)):
        items = select_round_robin(questions, list(range(1, 26)), count, offset)
        test_id = f"PN-T03-FINAL-{count}-{variant}"
        relative = Path("evaluaciones/policia-nacional/tema-03/tests-generados/finales") / f"{test_id}.json"
        write_json(ROOT / relative, public_test(test_id, f"Tema 3 · Test final {variant} · {count} preguntas", list(range(1, 26)), items, "test_final"))
        catalogue.append({"id": test_id, "ruta": relative.as_posix(), "tipo": "test_final", "preguntas": count, "bloques": list(range(1, 26))})

    if Counter(coverage_ids) != Counter(q["id"] for q in questions):
        raise RuntimeError("Los tests de cobertura no contienen exactamente una vez todas las preguntas del banco")

    write_json(OUT / "catalogo.json", {
        "content_version": VERSION,
        "total_tests": len(catalogue),
        "tests_cobertura_bloque": sum(e["tipo"] == "cobertura_bloque" for e in catalogue),
        "tests_por_partes": sum(e["tipo"] == "test_parte" for e in catalogue),
        "tests_finales": sum(e["tipo"] == "test_final" for e in catalogue),
        "regla_cobertura": "Cada pregunta del banco aparece exactamente una vez en el conjunto de tests de cobertura por bloque.",
        "tests": catalogue,
    })
    print(f"OK: {len(catalogue)} tests generados; {len(coverage_ids)} preguntas cubiertas una vez")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

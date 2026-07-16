#!/usr/bin/env python3
from pathlib import Path
import argparse
import json
import re

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "conocimiento/policia-nacional/tema-03/manifest.json"

BLOCK_RE = re.compile(
    r"<!-- BLOCK (\d{2}) START -->\n"
    r"## \d+\. (.*?)\n"
    r"\*\*Fuente:\*\* `([^`]+)`\n"
    r"<!-- PARTE START -->\n(.*?)\n<!-- PARTE END -->\n"
    r"<!-- ATESTADO START -->\n(.*?)\n<!-- ATESTADO END -->\n"
    r"<!-- BLOCK \1 END -->",
    re.S,
)

LAYER_KEYS = [
    "MAPA",
    "CONTENIDO",
    "HABLEMOS_CLARO",
    "EN_LA_CALLE",
    "LO_QUE_CAE",
    "HA_CAIDO",
]

def load():
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    source = ROOT / manifest["source_file"]
    text = source.read_text(encoding="utf-8")
    blocks = [
        {
            "number": number,
            "title": title,
            "source": source_id,
            "parte": parte.strip(),
            "atestado": atestado.strip(),
        }
        for number, title, source_id, parte, atestado in BLOCK_RE.findall(text)
    ]
    layers = {}
    for key in LAYER_KEYS:
        match = re.search(
            rf"<!-- LAYER:{key} -->\n# ([^\n]+)\n(.*?)(?=\n<!-- LAYER:|\Z)",
            text,
            re.S,
        )
        if not match:
            raise ValueError(f"Falta la capa {key}")
        layers[key] = (match.group(1), match.group(2).strip())
    return manifest, blocks, layers

def render(kind, manifest, blocks, layers):
    if kind not in {"parte", "atestado"}:
        raise ValueError(f"Derivado no admitido: {kind}")

    heading = (
        "# TEMA 3 · LA CONSTITUCIÓN ESPAÑOLA (II)\n\n"
        f"**Policía Nacional · Método VIGOR · {kind.upper()}**\n"
        f"**Versión de contenido:** {manifest['content_version']}\n"
        f"**Estado editorial:** {manifest['editorial_status']} · "
        f"**Publicación:** {manifest['publication_status']}\n"
    )
    output = [heading, f"# {layers['MAPA'][0]}\n\n{layers['MAPA'][1]}\n", "# Contenido\n"]

    for block in blocks:
        body = block[kind]
        output.append(
            f"## {block['number']}. {block['title']}\n\n"
            f"{body}\n\n"
            f"*Referencia oficial: `{block['source']}`.*\n"
        )

    for key in LAYER_KEYS[2:]:
        title, body = layers[key]
        output.append(f"# {title}\n\n{body}\n")

    output.append(
        "---\n\n"
        f"*Academia En Vigor · El temario que nunca duerme · "
        f"Tema 3 · v{manifest['content_version']} · Documento interno no publicado.*\n"
    )
    return "\n".join(output)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    manifest, blocks, layers = load()
    if len(blocks) != manifest["semantic_blocks"]:
        raise SystemExit(
            f"Número de bloques incoherente: {len(blocks)} "
            f"frente a {manifest['semantic_blocks']}"
        )

    failures = []
    for kind, relative_path in manifest["outputs"].items():
        target = ROOT / relative_path
        expected = render(kind, manifest, blocks, layers)
        if args.write:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(expected, encoding="utf-8")
        if args.check and (
            not target.exists()
            or target.read_text(encoding="utf-8") != expected
        ):
            failures.append(relative_path)

    if args.check and failures:
        print("Derivados desactualizados:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    action = "escritos" if args.write else "verificados" if args.check else "calculados"
    print(f"OK: {len(blocks)} bloques; derivados {action}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

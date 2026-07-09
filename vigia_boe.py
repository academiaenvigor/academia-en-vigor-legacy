#!/usr/bin/env python3
"""
VIGÍA BOE — Vigilante automático de la normativa del temario.

Consulta la API oficial de datos abiertos del BOE (legislación consolidada)
para cada norma del catálogo de temario.json, compara la fecha de
actualización con la última conocida (vigia-estado.json) y, si hay cambios,
genera un informe con los temas afectados (usando el índice inverso
norma -> temas del propio temario.json).

Uso:  python3 vigia_boe.py
Salida: código 0 = sin cambios · código 1 = hay cambios (ver vigia-informe.md)
"""

import json, sys, urllib.request, datetime, pathlib

BASE = "https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/{}/metadatos"
RAIZ = pathlib.Path(__file__).parent
TEMARIO = RAIZ / "temario.json"
ESTADO = RAIZ / "vigia-estado.json"
INFORME = RAIZ / "vigia-informe.md"


def api_metadatos(boe_id):
    """Devuelve los metadatos de una norma consolidada, o None si falla."""
    req = urllib.request.Request(
        BASE.format(boe_id),
        headers={"Accept": "application/json", "User-Agent": "vigia-temario/1.0"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            payload = json.load(r)
    except Exception as e:
        return {"error": str(e)}
    # La API envuelve la respuesta; buscamos los campos con parsing defensivo.
    datos = payload.get("data", payload)
    if isinstance(datos, list) and datos:
        datos = datos[0]
    return {
        "fecha_actualizacion": _buscar(datos, "fecha_actualizacion"),
        "estado_consolidacion": _buscar(datos, "estado_consolidacion"),
    }


def _buscar(obj, clave):
    """Busca una clave en cualquier nivel de anidamiento (la API devuelve estructuras envueltas)."""
    if isinstance(obj, dict):
        if clave in obj:
            v = obj[clave]
            return v.get("texto", v) if isinstance(v, dict) else v
        for v in obj.values():
            r = _buscar(v, clave)
            if r is not None:
                return r
    elif isinstance(obj, list):
        for v in obj:
            r = _buscar(v, clave)
            if r is not None:
                return r
    return None


def main():
    temario = json.loads(TEMARIO.read_text(encoding="utf-8"))
    boe_ids = temario["meta"]["boe_ids"]
    catalogo = temario["meta"]["catalogo_normativa"]

    # Índice inverso: norma -> temas afectados
    inverso = {}
    for t in temario["temas"]:
        for n in t.get("normativa", []):
            inverso.setdefault(n["id"], []).append(t["numero"])

    estado = json.loads(ESTADO.read_text(encoding="utf-8")) if ESTADO.exists() else {}
    cambios, errores, hoy = [], [], datetime.date.today().isoformat()

    for norma_id, boe_id in sorted(boe_ids.items()):
        if not boe_id:
            continue  # normas internacionales o pendientes de fijar id
        meta = api_metadatos(boe_id)
        if "error" in meta or not meta.get("fecha_actualizacion"):
            errores.append(f"- `{norma_id}` ({boe_id}): {meta.get('error', 'sin fecha en la respuesta')}")
            continue
        fecha, estado_cons = str(meta["fecha_actualizacion"]), str(meta.get("estado_consolidacion", ""))
        previa = estado.get(boe_id, {}).get("fecha_actualizacion")
        if previa and fecha != previa:
            cambios.append({
                "norma": norma_id, "nombre": catalogo.get(norma_id, norma_id), "boe_id": boe_id,
                "antes": previa, "ahora": fecha, "estado": estado_cons,
                "temas": sorted(set(inverso.get(norma_id, []))),
            })
        estado[boe_id] = {"fecha_actualizacion": fecha, "estado_consolidacion": estado_cons, "comprobado": hoy}

    ESTADO.write_text(json.dumps(estado, ensure_ascii=False, indent=2), encoding="utf-8")

    lineas = [f"# 🚨 Vigía BOE — informe {hoy}\n"]
    if cambios:
        lineas.append(f"**{len(cambios)} norma(s) con cambios detectados:**\n")
        for c in cambios:
            temas = ", ".join(f"T{n}" for n in c["temas"]) or "—"
            lineas.append(
                f"## {c['nombre']}\n"
                f"- BOE: [{c['boe_id']}](https://www.boe.es/buscar/act.php?id={c['boe_id']})\n"
                f"- Fecha de actualización: {c['antes']} → **{c['ahora']}** (consolidación: {c['estado']})\n"
                f"- **Temas afectados: {temas}** → revisar y subir versión\n"
            )
    else:
        lineas.append("Sin cambios en la normativa vigilada. ✅\n")
    if errores:
        lineas.append("\n### ⚠️ Normas no comprobadas (revisar id o API)\n" + "\n".join(errores))
    INFORME.write_text("\n".join(lineas), encoding="utf-8")

    print(f"Cambios: {len(cambios)} | Errores: {len(errores)}")
    sys.exit(1 if cambios else 0)


if __name__ == "__main__":
    main()

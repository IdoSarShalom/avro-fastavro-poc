from pathlib import Path
from typing import List, Dict, Any

from fastavro import writer, reader, parse_schema


SCHEMA: Dict[str, Any] = {
    "doc": "A simple user record",
    "name": "User",
    "namespace": "example.avro",
    "type": "record",
    "fields": [
        {"name": "user_id", "type": "string"},
        {"name": "age", "type": "int"},
        {"name": "email", "type": ["null", "string"], "default": None},
    ],
}


def make_records() -> List[Dict[str, Any]]:
    return [
        {"user_id": "u-1", "age": 24, "email": "u1@example.com"},
        {"user_id": "u-2", "age": 31, "email": None},
    ]


def roundtrip(path: Path) -> None:
    parsed = parse_schema(SCHEMA)

    records = make_records()
    print(f"Writing {len(records)} records to {path} ...")
    with path.open("wb") as f:
        writer(f, parsed, records)

    print("Reading them back:")
    with path.open("rb") as f:
        for rec in reader(f):
            print(rec)


if __name__ == "__main__":
    out = Path("users.avro")
    roundtrip(out)
    print(f"Avro file written to: {out.resolve()}")

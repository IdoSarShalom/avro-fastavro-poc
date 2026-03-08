from pathlib import Path

from fastavro import reader

from src.main import SCHEMA, make_records, roundtrip


def test_roundtrip(tmp_path: Path) -> None:
    out = tmp_path / "users.avro"
    roundtrip(out)

    assert out.exists()

    with out.open("rb") as f:
        read_back = list(reader(f))

    assert read_back == make_records()

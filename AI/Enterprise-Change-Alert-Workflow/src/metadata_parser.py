from pathlib import Path


def parse_metadata(file_path):
    metadata = {}

    for line in Path(file_path).read_text(encoding="utf-8").splitlines():
        if ":" not in line:
            continue

        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip()

    return metadata

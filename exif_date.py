#!/usr/bin/env python3
"""Read the date information from an image's EXIF metadata."""
import sys
from PIL import Image, ExifTags


def get_exif_date(path: str) -> str | None:
    """Return the first available date from EXIF data."""
    with Image.open(path) as img:
        info = img._getexif()
        if not info:
            return None
        tags = {ExifTags.TAGS.get(k, k): v for k, v in info.items()}
        for key in ("DateTimeOriginal", "DateTime", "DateTimeDigitized"):
            if key in tags:
                return str(tags[key])
    return None


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python exif_date.py <image>")
        return 1
    date = get_exif_date(argv[1])
    if date:
        print(date)
    else:
        print("No EXIF date found")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

#!/usr/bin/env python3
"""
P.A.G.O. Mentoring Pack Generator

Generates a complete mentoring material pack from templates,
customizing for a specific event (title, date, location, language).

Usage:
    python generate_mentoring_pack.py --title "Mentoria P.A.G.O. Luanda" \
        --date "15-16 Março 2026" --location "Luanda, Angola" \
        --language pt --output-dir ./output

Outputs:
    - Handbook_do_Participante.md
    - Guia_do_Palestrante.md
    - Questionario_de_Diagnostico.md
"""

import argparse
import os
import shutil
import re
from pathlib import Path

SKILL_DIR = Path(__file__).parent.parent
TEMPLATES_DIR = SKILL_DIR / "templates"


def customize_template(content, title, date, location, language):
    """Apply event-specific customizations to template content."""
    # Add event header if title/date/location provided
    if title or date or location:
        header_parts = []
        if title:
            header_parts.append(f"**Evento:** {title}")
        if date:
            header_parts.append(f"**Data:** {date}")
        if location:
            header_parts.append(f"**Local:** {location}")
        header = " | ".join(header_parts)
        # Insert after the first heading
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if line.startswith('# ') or line.startswith('## '):
                lines.insert(i + 1, f"\n{header}\n")
                break
        content = '\n'.join(lines)
    return content


def main():
    parser = argparse.ArgumentParser(description="Generate P.A.G.O. Mentoring Pack")
    parser.add_argument("--title", default="", help="Event title")
    parser.add_argument("--date", default="", help="Event date")
    parser.add_argument("--location", default="", help="Event location")
    parser.add_argument("--language", default="pt", choices=["pt", "en", "es"],
                        help="Output language (pt=Portuguese, en=English, es=Spanish)")
    parser.add_argument("--output-dir", default="./mentoria_output",
                        help="Output directory for generated files")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    templates = {
        "handbook_template.md": "Handbook_do_Participante.md",
        "guia_palestrante_template.md": "Guia_do_Palestrante.md",
        "questionario_diagnostico_template.md": "Questionario_de_Diagnostico.md",
    }

    print(f"Generating P.A.G.O. Mentoring Pack...")
    print(f"  Title: {args.title or '(default)'}")
    print(f"  Date: {args.date or '(not set)'}")
    print(f"  Location: {args.location or '(not set)'}")
    print(f"  Language: {args.language}")
    print(f"  Output: {output_dir}")
    print()

    for template_name, output_name in templates.items():
        template_path = TEMPLATES_DIR / template_name
        if not template_path.exists():
            print(f"  ⚠️  Template not found: {template_name}")
            continue

        with open(template_path, "r", encoding="utf-8") as f:
            content = f.read()

        content = customize_template(content, args.title, args.date, args.location, args.language)

        output_path = output_dir / output_name
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"  ✅ Generated: {output_name}")

    print(f"\n✅ Pack generated successfully in: {output_dir}")
    print(f"\nNext steps:")
    print(f"  1. Review and customize each document as needed")
    print(f"  2. Run validate_bible_refs.py on each document")
    print(f"  3. Convert to PDF with: manus-md-to-pdf <file.md> <file.pdf>")


if __name__ == "__main__":
    main()

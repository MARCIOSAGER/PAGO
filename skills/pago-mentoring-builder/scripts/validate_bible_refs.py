#!/usr/bin/env python3
"""
P.A.G.O Bible Reference Validator
Validates that biblical references used in P.A.G.O materials are accurate
and contextually appropriate for the methodology.

Usage:
    python validate_bible_refs.py <input_file>
    python validate_bible_refs.py --text "Provérbios 11:3 - A integridade dos retos os guia"

The script extracts biblical references from the input and validates:
1. The reference exists (book, chapter, verse)
2. The quoted text matches the actual verse
3. The context is appropriate for the P.A.G.O pillar it's associated with
"""

import sys
import re
import json
import os

try:
    from openai import OpenAI
except ImportError:
    print("Installing openai package...")
    os.system("sudo pip3 install openai")
    from openai import OpenAI


def extract_bible_refs(text):
    """Extract potential Bible references from text."""
    patterns = [
        r'(?:—\s*)?(\d?\s*[A-ZÀ-Ú][a-zà-ú]+(?:\s+[a-zà-ú]+)?)\s+(\d+)[:\.](\d+(?:\s*[-–]\s*\d+)?)',
        r'(?:—\s*)?((?:Gn|Gên|Ex|Êx|Lv|Nm|Dt|Js|Jz|Rt|1Sm|2Sm|1Rs|2Rs|1Cr|2Cr|Ed|Ne|Et|Jó|Sl|Pv|Ec|Ct|Is|Jr|Lm|Ez|Dn|Os|Jl|Am|Ob|Jn|Mq|Na|Hc|Sf|Ag|Zc|Ml|Mt|Mc|Lc|Jo|At|Rm|1Co|2Co|Gl|Ef|Fp|Cl|1Ts|2Ts|1Tm|2Tm|Tt|Fm|Hb|Tg|1Pe|2Pe|1Jo|2Jo|3Jo|Jd|Ap))\s*(\d+)[:\.](\d+(?:\s*[-–]\s*\d+)?)',
    ]
    refs = []
    for pattern in patterns:
        matches = re.finditer(pattern, text)
        for m in matches:
            refs.append(m.group(0).strip())
    return list(set(refs))


def validate_references(text, context="P.A.G.O mentoring material"):
    """Validate Bible references using LLM."""
    client = OpenAI()

    refs = extract_bible_refs(text)
    if not refs:
        print("No Bible references found in the text.")
        return {"valid": True, "references": [], "issues": []}

    prompt = f"""You are a biblical scholar and expert in the P.A.G.O methodology (Princípio, Alinhamento, Governo, Obediência) by Jefferson Evangelista.

Analyze the following text from a P.A.G.O material and validate ALL biblical references found.

TEXT TO VALIDATE:
{text}

EXTRACTED REFERENCES: {json.dumps(refs)}

For each reference, verify:
1. Does the book, chapter, and verse exist in the Bible?
2. Is the quoted text accurate (if text is quoted alongside the reference)?
3. Is the reference contextually appropriate for the P.A.G.O methodology?

Respond in JSON format:
{{
  "references": [
    {{
      "reference": "Book Chapter:Verse",
      "exists": true/false,
      "quoted_text_accurate": true/false/null,
      "actual_text_summary": "brief summary of what the verse actually says",
      "pago_pillar": "P/A/G/O/General",
      "contextually_appropriate": true/false,
      "notes": "any corrections or observations"
    }}
  ],
  "overall_valid": true/false,
  "issues": ["list of any issues found"],
  "suggestions": ["list of suggestions for improvement"]
}}

Be thorough and precise. Use the Almeida Revista e Atualizada (ARA) or NVI as reference for Portuguese texts, and KJV for English texts."""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"},
        temperature=0.1,
    )

    result = json.loads(response.choices[0].message.content)
    return result


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_bible_refs.py <input_file>")
        print("       python validate_bible_refs.py --text \"reference text\"")
        sys.exit(1)

    if sys.argv[1] == "--text":
        text = " ".join(sys.argv[2:])
    else:
        filepath = sys.argv[1]
        if not os.path.exists(filepath):
            print(f"File not found: {filepath}")
            sys.exit(1)
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()

    print(f"Validating Bible references...")
    print(f"Text length: {len(text)} characters")

    result = validate_references(text)

    print("\n" + "=" * 60)
    print("VALIDATION RESULTS")
    print("=" * 60)

    if result.get("references"):
        for ref in result["references"]:
            status = "✅" if ref.get("exists") and ref.get("contextually_appropriate") else "❌"
            print(f"\n{status} {ref.get('reference', 'N/A')}")
            print(f"   Exists: {ref.get('exists', 'N/A')}")
            print(f"   Text Accurate: {ref.get('quoted_text_accurate', 'N/A')}")
            print(f"   P.A.G.O Pillar: {ref.get('pago_pillar', 'N/A')}")
            print(f"   Contextually Appropriate: {ref.get('contextually_appropriate', 'N/A')}")
            if ref.get("notes"):
                print(f"   Notes: {ref['notes']}")

    print(f"\n{'=' * 60}")
    print(f"Overall Valid: {'✅ YES' if result.get('overall_valid') else '❌ NO'}")

    if result.get("issues"):
        print("\nIssues Found:")
        for issue in result["issues"]:
            print(f"  ⚠️  {issue}")

    if result.get("suggestions"):
        print("\nSuggestions:")
        for sug in result["suggestions"]:
            print(f"  💡 {sug}")

    # Save results to JSON
    output_file = "bible_validation_results.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"\nDetailed results saved to: {output_file}")

    return 0 if result.get("overall_valid") else 1


if __name__ == "__main__":
    sys.exit(main())

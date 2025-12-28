#!/usr/bin/env python3
"""
RESONANCE Chapter Drafting Tool

Uses Claude API to draft chapters from scaffolds with fiction-tuned system prompt.

Usage:
    python draft.py 31                    # Draft chapter 31
    python draft.py 31 --output draft.txt # Save to file
    python draft.py 31 --model opus       # Use opus (default: sonnet)
    python draft.py 31 --context 30       # Include chapter 30 as context
"""

import argparse
import os
import sys
from pathlib import Path

try:
    import anthropic
except ImportError:
    print("Error: anthropic package not installed.")
    print("Run: pip install anthropic")
    sys.exit(1)


# Paths relative to this script
SCRIPT_DIR = Path(__file__).parent
RESONANCE_DIR = SCRIPT_DIR.parent
PILOT_DIR = RESONANCE_DIR.parent
CHAPTERS_DIR = RESONANCE_DIR / "chapters"
DATA_DIR = RESONANCE_DIR / "data"
CONTEXT_DIR = RESONANCE_DIR / "context"
SYSTEM_PROMPT_PATH = SCRIPT_DIR / "SYSTEM_PROMPT.md"
FIGHT_GUIDE_PATH = PILOT_DIR / "fight_Guide.md"
MONTAGE_GUIDE_PATH = PILOT_DIR / "Montage_Style_Guide.md"


def load_file(path: Path) -> str:
    """Load a file and return its contents."""
    if not path.exists():
        return None
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def find_scaffold(chapter_num: int) -> Path:
    """Find the scaffold file for a chapter."""
    patterns = [
        f"RESONANCE_CH{chapter_num}_SCAFFOLD.txt",
        f"RESONANCE_CH{chapter_num:02d}_SCAFFOLD.txt",
    ]
    for pattern in patterns:
        path = CHAPTERS_DIR / pattern
        if path.exists():
            return path
    return None


def find_chapter(chapter_num: int) -> Path:
    """Find a completed chapter file."""
    # Look for any file matching the chapter number that's not a scaffold
    # Use underscore after number to avoid CH1 matching CH10, CH11, etc.
    for path in CHAPTERS_DIR.glob(f"RESONANCE_CH{chapter_num}_*.txt"):
        if "SCAFFOLD" not in path.name:
            return path
    for path in CHAPTERS_DIR.glob(f"RESONANCE_CH{chapter_num:02d}_*.txt"):
        if "SCAFFOLD" not in path.name:
            return path
    return None


def load_yaml_data() -> str:
    """Load relevant YAML data files."""
    data_parts = []

    yaml_files = [
        ("CHARACTERS.yaml", "CHARACTER DATA"),
        ("WORLD.yaml", "WORLD DATA"),
        ("CHAPTERS.yaml", "CHAPTER STRUCTURE"),
    ]

    for filename, header in yaml_files:
        path = DATA_DIR / filename
        content = load_file(path)
        if content:
            data_parts.append(f"## {header}\n\n```yaml\n{content}\n```")

    return "\n\n".join(data_parts)


def load_style_exemplar() -> str:
    """Load Chapter 1 as a style exemplar."""
    ch1_path = CHAPTERS_DIR / "RESONANCE_CH1_RUDE_AWAKENING.txt"
    content = load_file(ch1_path)
    if content:
        return f"""# STYLE EXEMPLAR: CHAPTER 1

This is the voice. Study it. Match it.

```
{content}
```

Key elements to replicate:
- Sentence fragments for impact
- Internal commands as self-regulation ("Stop crying!" / "shut the fuck up")
- Sensory details that are specific and brutal
- Refusal to explain—show the situation, let the reader figure it out
- Final image that reframes everything
- Deep POV that filters everything through character perception"""
    return None


def load_style_guides(include_fight: bool = False, include_montage: bool = False) -> str:
    """Load optional style guides."""
    guides = []

    if include_fight:
        content = load_file(FIGHT_GUIDE_PATH)
        if content:
            guides.append(f"# FIGHT SCENE GUIDE\n\n{content}")

    if include_montage:
        content = load_file(MONTAGE_GUIDE_PATH)
        if content:
            guides.append(f"# MONTAGE/INTERCUTTING GUIDE\n\n{content}")

    return "\n\n---\n\n".join(guides) if guides else None


def build_prompt(
    chapter_num: int,
    context_chapters: list = None,
    include_exemplar: bool = True,
    include_fight_guide: bool = False,
    include_montage_guide: bool = False,
) -> str:
    """Build the full prompt for drafting."""
    parts = []

    # Load style exemplar first
    if include_exemplar:
        exemplar = load_style_exemplar()
        if exemplar:
            parts.append(exemplar)

    # Load optional style guides
    guides = load_style_guides(include_fight_guide, include_montage_guide)
    if guides:
        parts.append(guides)

    # Load scaffold
    scaffold_path = find_scaffold(chapter_num)
    if not scaffold_path:
        print(f"Error: No scaffold found for chapter {chapter_num}")
        sys.exit(1)

    scaffold = load_file(scaffold_path)
    parts.append(f"# SCAFFOLD FOR CHAPTER {chapter_num}\n\n{scaffold}")

    # Load YAML data
    yaml_data = load_yaml_data()
    if yaml_data:
        parts.append(f"# REFERENCE DATA\n\n{yaml_data}")

    # Load context chapters if specified
    if context_chapters:
        for ctx_num in context_chapters:
            ctx_path = find_chapter(ctx_num)
            if ctx_path:
                ctx_content = load_file(ctx_path)
                parts.append(f"# PREVIOUS CHAPTER {ctx_num} (for continuity)\n\n{ctx_content}")
            else:
                print(f"Warning: Context chapter {ctx_num} not found")

    # Final instruction
    parts.append(f"""# INSTRUCTION

Draft Chapter {chapter_num} based on the scaffold above.

Transform the scaffold into living prose. Follow the system prompt guidelines for voice, pacing, and style.

Output ONLY the chapter text. No meta-commentary. No notes. Just the chapter, ready to read.

Begin with the chapter number and title, then the prose.""")

    return "\n\n---\n\n".join(parts)


def draft_chapter(
    chapter_num: int,
    model: str = "claude-sonnet-4-20250514",
    context_chapters: list = None,
    max_tokens: int = 16000,
    include_exemplar: bool = True,
    include_fight_guide: bool = False,
    include_montage_guide: bool = False,
) -> str:
    """Draft a chapter using the Claude API."""

    # Load system prompt
    system_prompt = load_file(SYSTEM_PROMPT_PATH)
    if not system_prompt:
        print("Error: System prompt not found")
        sys.exit(1)

    # Build user prompt
    user_prompt = build_prompt(
        chapter_num,
        context_chapters,
        include_exemplar,
        include_fight_guide,
        include_montage_guide,
    )

    # Initialize client
    client = anthropic.Anthropic()  # Uses ANTHROPIC_API_KEY env var

    print(f"Drafting chapter {chapter_num} with {model}...")
    print(f"System prompt: {len(system_prompt)} chars")
    print(f"User prompt: {len(user_prompt)} chars")
    print("---")

    # Make API call with streaming for long requests
    result_text = ""
    with client.messages.stream(
        model=model,
        max_tokens=max_tokens,
        system=system_prompt,
        messages=[
            {"role": "user", "content": user_prompt}
        ]
    ) as stream:
        for text in stream.text_stream:
            result_text += text
            print(text, end="", flush=True)

    print()  # Newline after streaming
    return result_text


def main():
    parser = argparse.ArgumentParser(
        description="Draft RESONANCE chapters from scaffolds using Claude API"
    )
    parser.add_argument(
        "chapter",
        type=int,
        help="Chapter number to draft"
    )
    parser.add_argument(
        "--output", "-o",
        type=str,
        help="Output file (default: stdout)"
    )
    parser.add_argument(
        "--model", "-m",
        choices=["sonnet", "opus", "haiku"],
        default="sonnet",
        help="Model to use (default: sonnet)"
    )
    parser.add_argument(
        "--context", "-c",
        type=int,
        nargs="+",
        help="Previous chapter numbers to include as context"
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=16000,
        help="Maximum tokens for response (default: 16000)"
    )
    parser.add_argument(
        "--no-exemplar",
        action="store_true",
        help="Skip including Chapter 1 as style exemplar"
    )
    parser.add_argument(
        "--fight-guide",
        action="store_true",
        help="Include full fight scene guide (for action-heavy chapters)"
    )
    parser.add_argument(
        "--montage-guide",
        action="store_true",
        help="Include montage/intercutting guide (for parallel thread chapters)"
    )

    args = parser.parse_args()

    # Map model names
    model_map = {
        "sonnet": "claude-sonnet-4-20250514",
        "opus": "claude-opus-4-20250514",
        "haiku": "claude-haiku-4-20250514",
    }
    model = model_map[args.model]

    # Check for API key
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)

    # Draft the chapter
    draft = draft_chapter(
        args.chapter,
        model=model,
        context_chapters=args.context,
        max_tokens=args.max_tokens,
        include_exemplar=not args.no_exemplar,
        include_fight_guide=args.fight_guide,
        include_montage_guide=args.montage_guide,
    )

    # Output
    if args.output:
        output_path = Path(args.output)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(draft)
        print(f"\nDraft saved to: {output_path}")
    else:
        print(draft)


if __name__ == "__main__":
    main()

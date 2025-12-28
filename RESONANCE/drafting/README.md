# RESONANCE Drafting System

API-based chapter drafting with fiction-tuned prompts.

## Setup

```bash
# Install anthropic package
pip install anthropic

# Set API key
export ANTHROPIC_API_KEY="your-key-here"
```

## Usage

```bash
# Draft chapter 31 to stdout
python draft.py 31

# Draft chapter 31 to file
python draft.py 31 -o ch31_draft.txt

# Use opus for higher quality
python draft.py 31 -m opus -o ch31_draft.txt

# Include previous chapter for continuity
python draft.py 32 -c 31 -o ch32_draft.txt

# Skip the style exemplar (Chapter 1)
python draft.py 31 --no-exemplar

# Include full fight guide (for action-heavy chapters like Ch 31)
python draft.py 31 --fight-guide -o ch31_draft.txt

# Include montage guide (for parallel thread chapters like Ch 32)
python draft.py 32 --montage-guide -o ch32_draft.txt

# Full context for the brawl chapter
python draft.py 31 -m opus --fight-guide -c 30 -o ch31_draft.txt
```

## What It Does

1. Loads the fiction-tuned system prompt (`SYSTEM_PROMPT.md`)
2. Loads Chapter 1 as a style exemplar
3. Loads the scaffold for the specified chapter
4. Loads YAML reference data (characters, world, chapters)
5. Optionally includes previous chapters for continuity
6. Sends to Claude API
7. Outputs the draft

## Files

- `draft.py` - Main drafting script
- `SYSTEM_PROMPT.md` - Fiction-tuned system prompt with:
  - Core thesis
  - Prose style guidelines (based on Chapter 1)
  - Fight scene principles
  - Character voices
  - Act III pitfalls to avoid
  - What NOT to do

## Models

- `sonnet` (default) - Fast, good quality
- `opus` - Highest quality, slower, more expensive
- `haiku` - Fastest, lower quality (not recommended for prose)

## Context Management

The script automatically includes:
- Chapter 1 as style exemplar
- CHARACTERS.yaml
- WORLD.yaml
- CHAPTERS.yaml

Use `-c` to add previous chapters for continuity.

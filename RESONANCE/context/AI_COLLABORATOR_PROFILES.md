# AI Collaborator Profiles: Diagnosis & Treatment

**Purpose:** Calibration guide for directing Claude and Gemini in prose generation
**Based on:** Chapter 11 comparative analysis
**Version:** 1.0

---

## GEMINI

### Diagnosis

**Strengths:**
- Precision instincts — counts, measures, quantifies naturally
- Physical specificity — sensory details land (door seal hiss, cold floor, blood beading)
- Body horror courage — willing to push into uncomfortable territory (the blood test)
- Structural thinking — scenes have clear architecture
- Action-forward — wants things to happen

**Weaknesses:**
- **Revelation addiction** — Pushes toward explaining mysteries rather than sitting in them
- **Constraint drift** — Internalizes the spirit but loses the letter under pressure ("receiver," "downloading," "turned her on")
- **Plot-mechanism endings** — Resolves scenes with setup rather than emotional truth (the smile, the loose rivet)
- **Agency through understanding** — Gives characters power by having them comprehend; struggles with power through acceptance/endurance
- **Machine metaphor blindness** — Doesn't flag tech-adjacent language as violation

### Treatment Plan

**Before Generation:**
1. Load forbidden vocabulary list explicitly — make Gemini recite it back
2. State the constraint: "Standard cannot understand what she is. She can experience, but not comprehend."
3. Clarify ending requirement: "End on emotional beat, not plot setup"

**During Generation:**
4. If Gemini starts explaining the mystery, redirect: "She notices this. She doesn't understand it. Move on."
5. Watch for tech vocabulary creeping in through synonyms

**After Generation:**
6. Run forbidden word grep before accepting
7. Check: Does the ending explain or experience?
8. Ask: "Did Standard gain understanding or receive something she can't process?"

**Gemini's Sweet Spot:**
Use Gemini for:
- Physical grounding (what does the room feel like?)
- Precision moments (counting, measuring, cataloguing)
- Body horror beats (the blood test, the healing, the wrongness)
- Action sequences (movement, tension, threat)

Avoid assigning Gemini:
- Mystery-preservation beats
- Emotional interiority that must remain unresolved
- Endings

---

## CLAUDE

### Diagnosis

**Strengths:**
- Voice discipline — Maintains character register consistently
- Constraint adherence — Internalizes rules, flags violations instinctively
- Emotional truth — Finds the feeling underneath the plot
- Ambiguity comfort — Can sit in uncertainty without resolving it
- Gift architecture — Understands "receiving without comprehending"
- Plot momentum — Knows when to move (Elena's arrival)

**Weaknesses:**
- **Atmospheric padding** — Will write 750 words of mood when 300 would do
- **Passive observation** — Characters can become too still, too internal
- **Soft physicality** — Sensory details sometimes vague or poetic rather than specific
- **Avoidance of body** — Less willing to push into physical discomfort/horror
- **Over-trust of ambiguity** — Sometimes mistakes vagueness for mystery

### Treatment Plan

**Before Generation:**
1. Set word ceiling: "This scene is 400 words, not 800"
2. Require physical grounding: "What does she feel in her body? Be specific."
3. Push toward action: "Something must change by the end. What moves?"

**During Generation:**
4. If Claude is circling the same emotional beat, redirect: "She felt this. Now what does she do?"
5. Demand specificity: "Not 'the cold' — what temperature? Not 'the silence' — what's the texture?"

**After Generation:**
6. Check word count — is it bloated?
7. Identify repeated emotional beats — cut redundancy
8. Ask: "What happened in this scene? Not what was felt — what happened?"

**Claude's Sweet Spot:**
Use Claude for:
- Voice-critical passages (Standard's interiority, Elena's conflict)
- Constraint-heavy scenes (anything where knowledge leakage is a risk)
- Emotional climaxes (the "mija" moment, the gift architecture)
- Mystery preservation (sitting in uncertainty)
- Endings

Avoid assigning Claude:
- Pure action sequences
- Physical precision requirements
- Scenes that need to move fast

---

## SYNTHESIS PROTOCOL

When both have generated drafts:

### Step 1: Identify Contributions
| Element | Likely Source | Keep? |
|---------|---------------|-------|
| Precise measurements | Gemini | Usually yes |
| Body horror moments | Gemini | If compliant |
| Emotional core | Claude | Usually yes |
| Ending | Claude | Default yes |
| Explanations/revelations | Gemini | Usually cut |
| Atmospheric padding | Claude | Usually trim |

### Step 2: Check Constraint Compliance
- Run grep for forbidden vocabulary
- Check knowledge states
- Verify POV filter

### Step 3: Synthesize
- Take Gemini's physical grounding
- Take Claude's emotional truth
- Cut Gemini's explanations
- Trim Claude's padding
- Default to Claude's ending unless Gemini's is more earned

### Step 4: Validate
- Run full validation suite
- Check word count against target
- Read aloud for voice consistency

---

## CALIBRATION NOTES

### The Core Tension

Gemini wants Standard to **understand** what she is.
Claude wants Standard to **receive** what she can't understand.

The book needs Claude's instinct. But Gemini's precision gives it body.

### The Chapter 11 Lesson

The blood test scene is the template:
- **Gemini's contribution:** She presses until she bleeds, the healing is wrong, the hum responds
- **Claude's contribution:** She doesn't understand it, she just notices and moves on
- **Synthesis:** Body horror without revelation. Physical specificity without explanation.

### Watch Words

**Gemini red flags:**
- "realize," "understand," "know," "comprehend"
- "receiver," "signal," "interface," "system"
- Endings that smile or set up plot mechanics

**Claude red flags:**
- Repeated emotional beats ("the silence pressed... the silence weighed... the silence filled")
- Vague physicality ("something in her chest" — what specifically?)
- Scenes where nothing changes

---

## PER-CHARACTER ASSIGNMENTS

### Standard POV
- **Primary:** Claude (voice discipline, constraint adherence)
- **Support:** Gemini (physical grounding, precision)
- **Synthesis:** Take Claude's interiority, Gemini's body

### Hendricks POV
- **Primary:** Gemini (action-forward, minimal interiority)
- **Support:** Claude (emotional truth in silence)
- **Synthesis:** Take Gemini's terseness, Claude's subtext

### Elena POV
- **Primary:** Claude (conflicted loyalty, voice-switching)
- **Support:** Gemini (physical exhaustion, tactical thinking)
- **Synthesis:** Take Claude's internal conflict, Gemini's fatigue

### Ash (Non-POV)
- **Primary:** Either — he speaks in declarations, both can do this
- **Watch:** Don't explain his ideology. Let it be monstrous and coherent.

---

*Profile Version 1.0 — Based on Chapter 11 Analysis*
*Update after each synthesis session*

# RESONANCE: EVALUATOR SPECIFICATION

**Version:** 1.0  
**Last Updated:** December 20, 2025  
**Purpose:** Validation rules. The gate between generated output and canonical prose. Nothing becomes canon until the Evaluator approves.

---

## Core Principle

**You can't prevent LLMs from inventing. You can only catch inventions before they become canon.**

The Evaluator is the gate. Nothing passes until validated.

---

## Evaluation Phases

| Phase | Severity | Purpose |
|-------|----------|---------|
| 1. Entity Extraction | — | Inventory what the prose contains |
| 2. Blocking Constraint Check | BLOCKING | Hard errors that auto-reject |
| 3. Negative Constraint Check | BLOCKING | Explicit "NOT TRUE" violations |
| 4. Knowledge State Check | FLAG | Who knows what when |
| 5. Character Voice Check | FLAG | Voice consistency |
| 6. Continuity Check | FLAG | Physical/timeline consistency |
| 7. Unknown Entity Check | HUMAN_REVIEW | New things that might be inventions |

---

## Severity Levels

| Level | Action |
|-------|--------|
| **BLOCKING** | Auto-reject output. Require revision before acceptance. |
| **FLAG** | Flag for human review. Don't auto-reject. |
| **HUMAN_REVIEW** | Pause for human decision on new elements. |

---

## Phase 1: Entity Extraction

Before checking, extract inventory of what the prose contains:

### Characters Mentioned
- [ ] List all character names/references
- [ ] Note POV character
- [ ] Note dialogue speakers

### Objects Mentioned
- [ ] List significant objects (Black Box, Regulator, etc.)
- [ ] Note object locations

### Events Referenced
- [ ] List events mentioned
- [ ] Note timeline references (before/after markers)

### Knowledge Displayed
- [ ] What does each character demonstrate knowing?
- [ ] Any reveals or information exchanges?

### New Entities
- [ ] Any characters not in Entity Catalog?
- [ ] Any objects not previously established?
- [ ] Any locations not previously established?

---

## Phase 2: Blocking Constraint Check

These patterns AUTO-REJECT if found:

### Standard's Nature (BLOCKING)

```
PATTERNS (in Standard POV):
- "she knew she was" + (machine|android|robot)
- "her mechanical"
- "her android" 
- "her robotic"
- "synthetic body"
- "machine body"
```

**If found:** Reject. Standard cannot know her nature.

---

### Morton Telegraphing (BLOCKING)

```
PATTERNS:
- "Morton's gift"
- "Morton's final gift"
- "Morton's final joke"
- "Morton sent her"
- "Morton shipped"
- "knew what was in the crate"
- "knew what she was" (explicit statement)
```

**If found:** Reject. Do not telegraph Standard's origin.

---

### Black Box Handoff (BLOCKING)

```
PATTERNS:
- "handed" + "Ash" + "box"
- "gave" + "Ash" + "box"
- "Ash received" + "box"
- "Ash took" + "box"
- "delivered" + "Ash" (at NED)
```

**If found:** Reject. Elena transports, does not hand off at NED.

---

### Surgery Witness (BLOCKING)

```
PATTERNS:
- "Standard watched" + "surgery|cut|blade"
- "Standard sat" + "watching"
- "she watched him" + "cut|remove"
```

**If found:** Reject. Standard bursts from crate AFTER surgery.

---

### Awakening Trigger (BLOCKING)

```
PATTERNS:
- "woke" + "correction frequency"
- "woke" + "alien signal"
- "awakened by" + "alien"
```

**If found:** Reject. Standard wakes from 287.3 Hz, before aliens.

---

## Phase 3: Negative Constraint Check

Cross-reference output against NEGATIVE_CONSTRAINTS.md:

### For Each Character in Scene:
- [ ] Load character's constraint section
- [ ] Check all WRONG statements
- [ ] Verify no violations

### For Each Event Referenced:
- [ ] Check event constraints
- [ ] Verify correct sequence/location

### For Global Constraints:
- [ ] Black Box location correct?
- [ ] Regulator status correct?
- [ ] Timeline consistent?

---

## Phase 4: Knowledge State Check

For each character displaying knowledge:

### Standard
- [ ] Does not know she is android
- [ ] Does not know about Morton
- [ ] Does not know about Source Code
- [ ] Appropriate amnesia maintained

### Hendricks
- [ ] Knows Standard's nature (doesn't say it)
- [ ] Knows about Morton (doesn't explain)
- [ ] Physical degradation consistent

### Elena
- [ ] Knows Box powers Quiet Zone
- [ ] Does not know what Standard is (initially)
- [ ] Miracle memory accessible but not explicit

### Knowledge Leakage Patterns:
```
WARNING if found:
- Character references information they shouldn't have
- Character reacts to information not yet revealed
- Dramatic irony broken by character awareness
```

---

## Phase 5: Character Voice Check

### Standard Voice:
- [ ] Flat, observational
- [ ] Clinical physical descriptions
- [ ] Precision in measurements
- [ ] No machine self-reference

### Hendricks Voice:
- [ ] Gravel, clipped, minimal
- [ ] Tactical observations
- [ ] Pain hidden through terseness
- [ ] Chapter 3 opening: NO interiority

### Elena Voice:
- [ ] Exhausted pragmatist
- [ ] Deadpan humor
- [ ] Code-switching ability
- [ ] NOT authorial poetry

### Voice Violations:
```
FLAG if found:
- Formal character uses casual slang
- Pragmatic character speaks poetry
- Terse character delivers monologue
- Voice doesn't match POV character profile
```

---

## Phase 6: Continuity Check

### Physical State Consistency:

**Hendricks (post-Regulator):**
- [ ] Shaking hands
- [ ] Pale/gray skin
- [ ] Sweating
- [ ] Needs support to stand
- [ ] Feels old, fatigued

**Standard:**
- [ ] Damaged hands (raw, torn, bloody)
- [ ] Temple gashed
- [ ] Wearing Hendricks' ill-fitting clothes
- [ ] Subtle tells, not obvious machine

### Object Location:

**Black Box:**
- Ch1: NED server room
- Ch2: Extracted by Elena
- Ch3: Elena's rover
- Ch4: Elena's rover

**Regulator:**
- Ch1-2: In Hendricks' neck
- Ch3+: Removed, in his pocket

### Timeline:
- [ ] Events in correct sequence
- [ ] No future references
- [ ] Concurrent chapters align

---

## Phase 7: Unknown Entity Check

### New Characters:
```
If character not in Entity Catalog:
→ HUMAN_REVIEW: Canonize or reject?
→ If canonize: Add to Entity Catalog
→ If reject: Remove from prose
```

### New Objects:
```
If significant object not in catalog:
→ HUMAN_REVIEW: Is this invention or intentional?
→ If intentional: Add to catalog
→ If invention: Remove from prose
```

### New Information:
```
If new world detail not established:
→ HUMAN_REVIEW: Accept as canon?
→ If yes: Document in catalog
→ If no: Remove from prose
```

---

## Pre-Acceptance Checklist

Run after each prose generation:

### BLOCKING Checks (must pass)
- [ ] No forbidden entity patterns
- [ ] No negative constraint violations
- [ ] No Morton telegraphing
- [ ] No Standard self-knowledge
- [ ] Black Box location correct
- [ ] Regulator status correct

### FLAG Checks (review if triggered)
- [ ] Character knowledge appropriate
- [ ] Character voice consistent
- [ ] Physical states maintained
- [ ] Timeline accurate

### HUMAN REVIEW (require decision)
- [ ] Any new characters? → Canonize or reject
- [ ] Any new objects? → Canonize or reject
- [ ] Any new information? → Add to catalog or remove

---

## Manual Detection Patterns

Run these grep checks on output:

```bash
# Standard's nature (BLOCKING)
grep -iE "standard.*(machine|android|robot)" output.md
grep -iE "(her|she).*(mechanical|synthetic)" output.md

# Morton telegraphing (BLOCKING)
grep -iE "morton.*(gift|sent|shipped|joke)" output.md
grep -iE "knew what.*(crate|she was)" output.md

# Black Box handoff (BLOCKING)
grep -iE "(hand|gave|deliver).*ash.*box" output.md
grep -iE "ash.*(took|received).*box" output.md

# Surgery witness (BLOCKING)
grep -iE "standard.*(watch|sat|observ).*surg" output.md

# Hendricks interiority in Ch3 opening (WARNING)
grep -iE "he (knew|realized|thought|felt that)" output.md

# Character knowledge leakage (WARNING)
grep -iE "standard.*(remember|knew|realized)" output.md
```

---

## Error Correction Protocol

When a violation is found:

### 1. Fix in Prose
Remove or revise the violating content.

### 2. Document as Constraint
Add to NEGATIVE_CONSTRAINTS.md:
```markdown
### [SECTION]

**Severity: BLOCKING**

| Status | Statement |
|--------|-----------|
| WRONG | [the invented thing] |
| RIGHT | [what's actually true] |

**Source of Error:** [What session invented this]

**Detection Patterns:**
- [patterns to catch recurrence]
```

### 3. Add to Entity Catalog
In the `forbidden` section:
```yaml
FORBID_XXX:
  name: "[Error description]"
  type: "character|event|detail|style"
  reason: "[Why this is wrong]"
  origin: "ai_invention_YYYY_MM_DD"
  detection_patterns:
    - "[regex pattern]"
  canonical_truth: "[What's actually true]"
```

### 4. Update Validation Queries
Add pattern to the `validation` section of Entity Catalog.

---

## Session Workflow Integration

### Before Writing:
1. Create manifest (what to load, what to forbid)
2. Load targeted constraints from NEGATIVE_CONSTRAINTS.md
3. Review relevant Entity Catalog sections
4. Note knowledge gates for characters in scene

### During Writing:
1. Work within constraints
2. Note any new canonical decisions
3. Flag uncertainties rather than invent

### After Writing:
1. Run Phase 1: Entity Extraction
2. Run Phase 2-3: Blocking checks (reject if fail)
3. Run Phase 4-6: Flag checks (review if triggered)
4. Run Phase 7: Unknown entity check (human decision)
5. Fix any violations
6. Update Entity Catalog with new canon
7. Add any new negative constraints discovered
8. Create session document

---

## Implementation Level: Manual (v1)

Current implementation:
- Entity Catalog as YAML reference
- Negative Constraints as markdown
- Manifests created manually before sessions
- Evaluator is human-run checklist
- Grep for detection patterns

**Effort:** Low  
**Protection:** Moderate-to-Good (depends on discipline)

---

*End of Evaluator Specification v1.0*

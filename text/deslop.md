=== STEP 1: IdentifyDocumentSlop ===

[user]
This document looks like AI slop. Identify the patterns and elements that make it sound like a human did not write it carefully.

Document:
<contents of path/to/document.md>

[user]
Analyze the document and identify specific patterns that make it sound AI-generated, generic, or sloppy. For each pattern:
- Name the pattern
- Provide a specific example from the document
- Explain why it weakens the writing

Focus on issues like generic phrasing, repetitive structure, vague claims, unnatural transitions, empty intensifiers, or anything else that makes the writing feel synthetic.

Answer with a JSON array using this schema:
[
  {
    pattern: string // The specific pattern or element that sounds AI-generated
    example: string // A concrete example from the document that demonstrates this pattern
    rationale: string // Why this pattern makes the document sound artificial or low-quality
  }
]


=== STEP 2: RewriteDocumentWithoutSlop ===

[user]
The following document was written in a way that feels like AI slop. Rewrite it so it sounds sharper, more specific, and more human.

Original document:
<contents of path/to/document.md>

Patterns to fix:
- <pattern[0].pattern>: <pattern[0].rationale>
  Example: "<pattern[0].example>"
- <pattern[1].pattern>: <pattern[1].rationale>
  Example: "<pattern[1].example>"
... (one entry per pattern returned by Step 1)

[user]
Rewrite the document fixing all of the identified patterns.

Important:
- Preserve the original meaning and core claims
- Preserve the overall structure and formatting when possible
- Remove vague, generic, repetitive, or over-polished phrasing
- Make the writing sound like a thoughtful human wrote it
- Return only the rewritten document text

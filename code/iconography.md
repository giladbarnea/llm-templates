---
url: https://chatgpt.com/share/68ea7cda-28e0-8012-86a7-51b9e6a5cb12
---
# A quick framework for judging (and commissioning) excellent UI icons

## 1) Fonts: what pairs well with minimalist iconography

* **Type class.** Prefer a neutral sans-serif with humanist tendencies (e.g., open apertures, generous x-height, low stroke contrast). This keeps text legible at small sizes and visually compatible with simple icons.
  *Why it reads “quietly competent.”* Humanist shapes soften the severity of geometric icons without stealing attention.
* **Metrics to ask for.** Large **x-height** relative to **cap height**; open **apertures** (c, e, s); balanced **ascender/descender** lengths; modest **tracking** (letter-spacing) for small sizes; tabular numerals where numbers appear in lists.
* **Weight/optical sizing.** Specify weights by use: Regular for body, Medium/Semibold for labels, never lighter than UI minimums at small sizes. If available, choose **optical sizes** tuned for small text.
* **Tone pairing.** Icons that are monoline and low-contrast pair best with fonts that feel contemporary but not decorative (Inter, SF Pro, Segoe UI, etc.). Avoid expressive display faces in the core interface.

## 2) Icon design language: principles and vocabulary

Use these to evaluate icons or brief designers.

1. **Semantic clarity (the metaphor).** The metaphor should be universal and action-oriented (noun for objects, verb for actions). Avoid culture- or app-specific slang.
   *Ask:* “Would a first-time user guess this meaning without a label?”
2. **Consistency (a shared grammar).** All icons follow the same **stroke weight**, **corner radius**, **end caps** (round/square), **angles** (e.g., 45° only), and **perspective** (flat orthographic vs. isometric).
   *Ask:* “Do they look like they were drawn by one hand?”
3. **Legibility at size.** No internal gaps smaller than the stroke; minimal detail under 16–20 px; distinguishable silhouettes.
   *Ask:* “Is it readable at 16 px and crisp at 1× and 2×?”
4. **Geometry & grid.** Draw on a 24×24 or 20×20 grid. Align key vertices to the pixel grid. Keep consistent **keylines** (circles/rectangles the forms sit on) so icons feel equally “loud.”
5. **Optical correction.** Circles overshoot boxes; diagonals are nudged for balance; visual centering beats mathematical centering.
   *Ask:* “Does it *look* centered even if it is not?”
6. **Negative space.** Holes and counters are intentional; figure/ground is unambiguous. White space carries meaning—do not fill it casually.
7. **Rhythm and visual weight.** Across a list of icons, aim for equal perceived weight. If an icon contains more strokes, use thinner lines or larger hollows to keep parity.
8. **States and pairs.** Supply **outline/filled** pairs (rest vs. active), plus disabled and error states, without changing the metaphor. Active state is a bolder *shape*, not just a different color.
9. **Color and contrast.** Icons should succeed in monochrome first. When colored, meet accessibility contrast targets against both light and dark surfaces; reserve semantic colors for meaning (success, warning, error) and never for branding alone.
10. **Motion with restraint.** If animated, keep it functional (progress, confirming an action) and respect the operating system’s **Reduce Motion** setting.
11. **Internationalization.** Mirror icons for **right-to-left (RTL)** languages when direction conveys meaning; avoid culture-bound metaphors (e.g., letters, local signage).
12. **Production constraints.** Deliver as **Scalable Vector Graphics (SVG)**; size to common touch targets (44–48 px); test in high/low density screens and dark mode.

## 3) Style note and cultural context (2025)

The dominant style is **calm, system-native minimalism**: monoline, outline-first icons with optional filled variants, designed to be legible in dark interfaces and trustworthy in enterprise contexts. This reflects broader cultural vectors:

* **“Calm technology.”** Interfaces lower cognitive load; ornament is out, clarity is in.
* **Trust and governance.** With artificial intelligence in critical workflows, visual language skews sober and auditable rather than playful.
* **Accessibility by default.** Dark mode, high-contrast themes, and motion sensitivity are table stakes.
* **Interoperability.** Teams mix platforms; icons echo the grammar of major systems (Apple’s Human Interface Guidelines and Google Material) without copying them.

## 4) A compact rubric (score 0–2 each; 20 = excellent)

1. Clear metaphor without label
2. Stylistic consistency across the set
3. Legible at 16 px and crisp on 1×/2×
4. Balanced visual weight within the set
5. Works in monochrome, light and dark
6. Proper grid use and optical corrections
7. Accessible color semantics when used
8. Handles states (outline/filled/disabled)
9. Localizes well (RTL-aware, non-parochial)
10. Production-ready SVG with touch-target sizing

## 5) What to tell designers (principle-level brief)

* **Tone:** “Calm, utilitarian, technical, and trustworthy. No whimsy; zero visual noise.”
* **Grammar:** “Single stroke weight; rounded end caps and corners; 24×24 keyline grid; flat orthographic, no perspective.”
* **Legibility:** “Must read at 16 px; no details below stroke width; equal perceived weight across the set.”
* **States:** “Provide outline and filled pairs plus disabled. Active uses shape/weight before color.”
* **Accessibility:** “Monochrome first; pass contrast in light/dark; respect Reduce Motion; provide RTL-mirrorable assets where directional.”
* **Delivery:** “SVGs and a Figma library with components, naming aligned to actions, and documentation of rules.”

## 6) Handy terminology (for crisp feedback)

* **Aperture:** openness of a letterform (affects readability).
* **Keyline:** the invisible reference shape icons align to.
* **Optical alignment/overshoot:** small tweaks so shapes *look* aligned.
* **Visual weight:** how heavy an icon feels, not its pixel count.
* **Affordance:** how clearly an icon suggests the action.
* **Figure/ground:** object versus background; crucial for clarity.

Use this vocabulary to say, for example:
“Let us keep a monoline grammar on a 24×24 keyline, optimize negative space so the silhouettes read at 16 px, and tune optical alignment to equalize visual weight across the set. Active states should prefer filled shapes over color shifts, with accessible contrast in both themes.”

That gives you a principled, portable way to recognize—and request—icons that feel as balanced and effective as the ones you like.

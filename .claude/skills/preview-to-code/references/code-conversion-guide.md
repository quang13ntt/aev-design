# Stage 3 — Generate Production Code from the Approved Preview

## Purpose

- Convert the approved preview into implementation‑ready code.
- Preserve DKB mappings so the implementation stays consistent and maintainable.

## Inputs

- Approved preview (HTML/CSS) from Stage 2
- DKB (tokens, component mappings, accessibility + responsive rules)
- Engineering constraints (target framework, linting rules, build tooling)

## Outputs

- Production‑ready UI implementation (HTML/CSS and/or framework components)
- Token artifacts when required (CSS variables, theme files)
- Optional: short release notes describing any approved changes to tokens/components

## Process

1. Normalize structure
   - Use semantic HTML (`header`, `main`, `nav`, `button`, `label`) where appropriate.
   - Add ARIA only when necessary.
2. Bind styling through the DKB
   - Replace remaining hard‑coded values with token references.
   - Prefer existing component classes/utilities.
3. Convert to the target implementation
   - Extract reusable components only if it matches the existing codebase patterns.
   - Keep class naming and token usage consistent.
4. Verify accessibility and responsiveness
   - Focus order, focus visibility, contrast, hit targets, and responsive behavior.
5. Build and smoke check (when tooling exists)
   - Ensure the output compiles and renders without runtime errors.

## Quality checklist

- No "invented" CSS values: styles come from tokens and existing component rules.
- Output matches the approved preview within expected rendering differences.
- Baseline accessibility expectations are met (semantics, focus visibility, contrast).
- The result integrates cleanly with existing frontend conventions.

## Terminology

- Design Knowledge Base (DKB): a versioned reference that combines design rules and implementation mapping (tokens + components + patterns + constraints).
- Tokens: named, reusable styling primitives (example: colors, typography, spacing, radius, elevation).
- Component mapping: the agreed HTML structure and CSS classes/selectors for each component variant.
- Preview: a reviewable HTML/CSS artifact generated from a wireframe using only the DKB.
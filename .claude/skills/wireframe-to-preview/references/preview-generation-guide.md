# Stage 2 — Generate an HTML/CSS Preview from a Wireframe

## Purpose

- Convert a low‑fidelity wireframe into a high‑fidelity, reviewable preview.
- Produce a browser‑openable artifact that stakeholders can validate.
- Keep all styling token‑driven and component‑driven.

## Inputs

- Wireframe (image, Figma frame, or structured description)
- DKB (tokens, components, patterns, rules, constraints)
- Constraints (responsive breakpoints, accessibility expectations)

## Outputs

- Preview page (HTML/CSS) that can be opened in a browser
- Preview spec (recommended):
  - component list and variants used
  - token usage summary
  - layout notes (spacing, grid, breakpoints)
  - interaction notes (states, validation, navigation)

## Process

1. Interpret the wireframe
   - Identify components and text roles (heading/body/label).
   - Infer layout structure (groups, grids/stacks, alignment intent).
2. Map elements to DKB components
   - Select the closest component and variant.
   - Resolve state requirements (default/hover/focus/disabled/error).
3. Apply tokens and rules
   - Bind typography, spacing, color, radius, and elevation to tokens.
   - Enforce layout rules and constraints from the DKB.
4. Generate preview markup and styles
   - Prefer existing classes and CSS variables from the DKB mapping.
   - Avoid hard‑coded colors/sizes/shadows unless explicitly allowed by the DKB.
5. Add responsiveness and basic interactions
   - Implement breakpoint behavior described by the DKB.
   - Ensure focus visibility and minimum hit targets per accessibility rules.

## Quality checklist

- Every visual decision is backed by a token or an existing component rule.
- All UI elements map to known components/variants.
- The preview is visually consistent with the product.
- The preview is usable for review (clear hierarchy, consistent spacing, obvious primary actions).
# Wireframe → Preview → Code Workflow

This document describes how a low‑fidelity wireframe becomes a working UI implementation that matches the product’s design system and frontend standards.

The workflow is intentionally constrained to prevent “invented” UI. The agent (or any designer/engineer following this process) must only use what exists in the Design Knowledge Base.

## Overview

1. Build the Design Knowledge Base (DKB)
2. Generate an HTML/CSS preview from a wireframe (reviewable output)
3. Generate production code from the approved preview (implementation‑ready output)

---

## Stage 1 — Build the Design Knowledge Base (DKB)

### Purpose

- Create a single source of truth for visual decisions and implementation mapping.
- Make the design system explicit and reusable across designers and engineers.
- Enable reliable generation (preview and code) without introducing new styles.

### Inputs

- Screenshots of existing product pages (include key flows and states; multiple breakpoints if available)
- Existing CSS (recommended): global styles, component styles, utilities
- Existing HTML (optional but useful for structure)
- Design source files (optional): Figma components / libraries
- Brand and accessibility requirements (optional, if defined)

### Outputs (DKB package)

- Design principles: hierarchy, spacing rhythm, layout conventions, visual language
- Design tokens: color, typography, spacing/sizing, radius, shadow/elevation, z‑index (motion optional)
- Component catalog: purpose, variants, states (hover/focus/active/disabled/error), DOM structure
- CSS mapping:
  - token → CSS variables
  - component → class names/selectors
  - utility conventions (if any)
- Responsive rules: breakpoints, grid/gutters, density rules (if any)
- Accessibility rules: contrast targets, focus behavior, semantic markup expectations
- Constraints and exceptions: what must not happen (example: do not introduce new colors)

### Process

1. Collect artifacts
   - Capture representative screens (including error/empty/loading states when possible).
   - Archive CSS/HTML and shared assets (icons, fonts) when available.
2. Extract and normalize tokens
   - Identify existing CSS variables and normalize naming to semantic roles (example: `text.primary`).
   - If a style exists but is not tokenized, propose a token candidate and document it.
3. Build the component catalog
   - For each component: purpose, variants, required classes, DOM structure, and interaction states.
4. Document system rules
   - Layout rules (grid, alignment, gutters).
   - Typography rules (type scale and usage by role).
   - Interaction rules (hover/focus patterns, validation rules).
5. Publish and govern
   - Store the DKB in version control.
   - Use a lightweight review process for new tokens/components.

### Quality checklist

- The core components visible in screenshots are documented with structure + states.
- A consistent spacing scale and typography scale is captured.
- Token and component naming matches production conventions.
- The mapping is specific enough that a new page can be designed and built without guesswork.

---

## Stage 2 — Generate an HTML/CSS Preview from a Wireframe

### Purpose

- Convert a low‑fidelity wireframe into a high‑fidelity, reviewable preview.
- Produce a browser‑openable artifact that stakeholders can validate.
- Keep all styling token‑driven and component‑driven.

### Inputs

- Wireframe (image, Figma frame, or structured description)
- DKB (tokens, components, patterns, rules, constraints)
- Constraints (responsive breakpoints, accessibility expectations)

### Outputs

- Preview page (HTML/CSS) that can be opened in a browser
- Preview spec (recommended):
  - component list and variants used
  - token usage summary
  - layout notes (spacing, grid, breakpoints)
  - interaction notes (states, validation, navigation)

### Process

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

### Quality checklist

- Every visual decision is backed by a token or an existing component rule.
- All UI elements map to known components/variants.
- The preview is visually consistent with the product.
- The preview is usable for review (clear hierarchy, consistent spacing, obvious primary actions).

---

## Stage 3 — Generate Production Code from the Approved Preview

### Purpose

- Convert the approved preview into implementation‑ready code.
- Preserve DKB mappings so the implementation stays consistent and maintainable.

### Inputs

- Approved preview (HTML/CSS) from Stage 2
- DKB (tokens, component mappings, accessibility + responsive rules)
- Engineering constraints (target framework, linting rules, build tooling)

### Outputs

- Production‑ready UI implementation (HTML/CSS and/or framework components)
- Token artifacts when required (CSS variables, theme files)
- Optional: short release notes describing any approved changes to tokens/components

### Process

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

### Quality checklist

- No “invented” CSS values: styles come from tokens and existing component rules.
- Output matches the approved preview within expected rendering differences.
- Baseline accessibility expectations are met (semantics, focus visibility, contrast).
- The result integrates cleanly with existing frontend conventions.

---

## Terminology

- Design Knowledge Base (DKB): a versioned reference that combines design rules and implementation mapping (tokens + components + patterns + constraints).
- Tokens: named, reusable styling primitives (example: colors, typography, spacing, radius, elevation).
- Component mapping: the agreed HTML structure and CSS classes/selectors for each component variant.
- Preview: a reviewable HTML/CSS artifact generated from a wireframe using only the DKB.

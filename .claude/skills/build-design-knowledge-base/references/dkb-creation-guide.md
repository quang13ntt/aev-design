# Stage 1 — Build the Design Knowledge Base (DKB)

## Purpose

- Create a single source of truth for visual decisions and implementation mapping.
- Make the design system explicit and reusable across designers and engineers.
- Enable reliable generation (preview and code) without introducing new styles.

## Inputs

- Screenshots of existing product pages (include key flows and states; multiple breakpoints if available)
- Existing CSS (recommended): global styles, component styles, utilities
- Existing HTML (optional but useful for structure)
- Design source files (optional): Figma components / libraries
- Brand and accessibility requirements (optional, if defined)

## Outputs (DKB package)

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

## Process

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

## Quality checklist

- The core components visible in screenshots are documented with structure + states.
- A consistent spacing scale and typography scale is captured.
- Token and component naming matches production conventions.
- The mapping is specific enough that a new page can be designed and built without guesswork.

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

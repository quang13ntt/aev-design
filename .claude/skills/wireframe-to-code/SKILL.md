---
name: wireframe-to-code-workflow
description: Guide for transforming low-fidelity wireframes into production-ready UI code using a Design Knowledge Base. Use when users need to generate HTML/CSS previews from wireframes or convert previews to production code, ensuring consistency with existing design systems and preventing invented UI elements.
---

# Wireframe to Code Workflow Skill

This skill provides a structured 3-stage workflow to convert low-fidelity wireframes into working UI implementations that align with the product's design system and frontend standards. It emphasizes using a Design Knowledge Base (DKB) to constrain outputs and avoid inventing new styles.

## When to Use This Skill

- When transforming wireframes into reviewable HTML/CSS previews
- When generating production code from approved previews
- When building or maintaining a Design Knowledge Base for consistent UI generation
- For any task requiring token-driven and component-driven UI development

## Core Workflow

The workflow consists of three stages:

1. **Build the Design Knowledge Base (DKB)**: Create a single source of truth for design decisions and implementation mappings.
2. **Generate HTML/CSS Preview**: Convert wireframes into high-fidelity, reviewable previews using only DKB elements.
3. **Generate Production Code**: Convert approved previews into implementation-ready code.

## Stage 1: Build the Design Knowledge Base (DKB)

### Purpose

Establish a versioned reference that captures existing design patterns, tokens, and constraints to ensure all generated UI is consistent and implementable.

### Inputs

- Screenshots of existing product pages (key flows, states, breakpoints)
- Existing CSS (global styles, component styles, utilities)
- Existing HTML (optional, for structure reference)
- Design source files (Figma, etc., optional)
- Brand/accessibility guidelines (optional)

### Outputs

- Design principles (hierarchy, spacing, layout, visual language)
- Design tokens (colors, typography, spacing, radius, shadows, etc.)
- Component catalog (purpose, variants, states, DOM structure)
- CSS mappings (token-to-variable, component-to-classes)
- Responsive/accessibility rules and constraints

### Process

1. Collect artifacts: Capture screens, archive CSS/HTML/assets.
2. Extract tokens: Identify and normalize CSS variables to semantic roles.
3. Build component catalog: Document each component's structure and states.
4. Document rules: Layout, typography, interaction patterns.
5. Publish: Store in version control with governance for updates.

### Quality Checks

- Core components documented with structure/states
- Consistent spacing/typography scales captured
- Naming matches production conventions
- Sufficient detail for new page design without guesswork

## Stage 2: Generate HTML/CSS Preview from Wireframe

### Purpose

Transform low-fidelity wireframes into high-fidelity, browser-viewable previews using only DKB elements.

### Inputs

- Wireframe (image, Figma frame, or description)
- DKB (tokens, components, rules, constraints)
- Responsive/accessibility requirements

### Outputs

- Preview page (HTML/CSS) for browser viewing
- Preview specification (components used, tokens applied, layout notes)

### Process

1. Interpret wireframe: Identify components, text roles, layout structure.
2. Map to DKB: Select matching components/variants, resolve states.
3. Apply tokens/rules: Bind styling to DKB elements, enforce constraints.
4. Generate markup/styles: Use DKB classes/variables, avoid hard-coded values.
5. Add responsiveness/interactions: Implement DKB-defined breakpoints and accessibility.

### Quality Checks

- All styling backed by tokens/components
- Visually consistent with product
- Usable for stakeholder review

## Stage 3: Generate Production Code from Preview

### Purpose

Convert approved previews into maintainable, production-ready code while preserving DKB mappings.

### Inputs

- Approved HTML/CSS preview
- DKB (mappings, rules)
- Engineering constraints (framework, linting, tooling)

### Outputs

- Production UI implementation (HTML/CSS or framework components)
- Token artifacts (if needed)
- Optional release notes for changes

### Process

1. Normalize structure: Use semantic HTML, add ARIA as needed.
2. Bind styling: Replace hard-coded values with token references.
3. Convert to target format: Extract components matching codebase patterns.
4. Verify accessibility/responsiveness: Ensure focus, contrast, hit targets, breakpoints.
5. Build/test: Compile and render without errors.

### Quality Checks

- No invented CSS values
- Matches preview visually
- Meets accessibility baselines
- Integrates with existing conventions

## Key Principles

- **Constrained Generation**: Only use elements from the DKB to prevent invented UI.
- **Token-Driven Styling**: All visual decisions must reference design tokens.
- **Component-Based**: Map wireframe elements to existing component variants.
- **Progressive Refinement**: Each stage builds on the previous with increasing fidelity.

## Terminology

- **Design Knowledge Base (DKB)**: Versioned reference combining design rules and implementation mappings.
- **Tokens**: Named styling primitives (colors, typography, spacing, etc.).
- **Preview**: Reviewable HTML/CSS artifact from wireframe using DKB.
- **Wireframe**: Low-fidelity structural input (image, frame, or description).

## References

For detailed guidance on each stage:

- **Stage 1 - Building DKB**: See [stage1-dkb.md](references/stage1-dkb.md) for comprehensive DKB creation process.
- **Stage 2 - Generating Previews**: See [stage2-preview.md](references/stage2-preview.md) for wireframe-to-preview conversion details.
- **Stage 3 - Production Code**: See [stage3-code.md](references/stage3-code.md) for preview-to-code implementation steps.

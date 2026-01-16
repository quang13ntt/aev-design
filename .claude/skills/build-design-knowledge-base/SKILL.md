---
name: build-design-knowledge-base
description: Guide for building a Design Knowledge Base (DKB) from existing product pages. Use when analyzing screenshots, Figma files, or CSS/HTML to extract design tokens, component patterns, and implementation mappings. Essential for establishing a single source of truth for design systems before generating new UI.
---

# Build Design Knowledge Base Skill

This skill guides the process of analyzing existing product pages to create a comprehensive Design Knowledge Base (DKB) that serves as a single source of truth for design decisions and implementation mappings.

## Purpose

- Extract design patterns, tokens, and constraints from existing UI
- Create a versioned reference for consistent design system usage
- Enable reliable UI generation without inventing new styles
- Make design decisions explicit and reusable across teams

## When to Use This Skill

- Starting a new design system documentation project
- Analyzing existing products to extract design patterns
- Converting visual designs into structured design tokens
- Establishing implementation mappings for frontend code
- Auditing or standardizing an existing design system

## Inputs

- Screenshots of existing product pages (key flows, states, multiple breakpoints)
- Existing CSS files (global styles, component styles, utilities)
- Existing HTML (optional but useful for structure)
- Design source files (Figma components/libraries, Sketch, Adobe XD)
- Brand guidelines and accessibility requirements (if available)

## Outputs (DKB Package)

The DKB package includes:

### 1. Design Principles
- Visual hierarchy rules
- Spacing rhythm and system
- Layout conventions (grid, alignment)
- Visual language (rounded vs sharp, light vs heavy shadows)

### 2. Design Tokens
- **Color tokens**: brand, semantic (success/warning/error), surface, text, border, state colors
- **Typography tokens**: font families, sizes, weights, line heights, letter spacing, type scales
- **Spacing/sizing tokens**: spacing scale, section spacing, component padding presets
- **Radius tokens**: border radius values (sm, md, lg)
- **Shadow/elevation tokens**: card, modal, tooltip elevations
- **Z-index tokens**: layer hierarchy
- **Motion tokens** (optional): transition durations, easing curves

### 3. Component Catalog
For each component, document:
- Purpose and semantic role
- Variants (primary/secondary/ghost, elevated/flat/outlined)
- States (default/hover/focus/active/disabled/error)
- DOM structure
- Required CSS classes and variables
- Responsive behavior

### 4. CSS Mapping
- Token → CSS variable mappings
- Component → class name/selector mappings
- Utility class conventions

### 5. Responsive Rules
- Breakpoints
- Grid/gutter systems
- Density rules

### 6. Accessibility Rules
- Contrast targets (WCAG compliance)
- Focus behavior
- Semantic markup expectations
- Minimum touch target sizes

### 7. Constraints and Exceptions
Document what must NOT happen:
- "Do not introduce new colors outside the token set"
- "Do not use arbitrary spacing values"
- "Always use semantic HTML"

## Process

### Step 1: Collect Artifacts

**UI Screens**
- Capture screenshots of all relevant pages and states
- Include error states, empty states, loading states
- Export frames from design tools (Figma, Sketch, etc.)
- Cover all device variations (desktop, tablet, mobile)

**Code Artifacts**
- Download and archive CSS files (global and component-level)
- Export relevant HTML structures
- Identify reusable classes and utility patterns

**Additional Assets**
- Icons, logos, imagery guidelines
- Accessibility specifications
- Brand identity documentation

### Step 2: Extract and Normalize Tokens

**Identify Existing Tokens**
- Find CSS variables (`--custom-properties`)
- Identify repeated values (colors, spacing, font sizes)
- Map values to semantic roles (e.g., `#333` → `text.primary`)

**Create Missing Tokens**
- If a style exists but isn't tokenized, propose a token name
- Follow semantic naming conventions
- Document the token in the DKB

**Organize Token Hierarchy**
- Group by category (color, typography, spacing, etc.)
- Establish naming conventions
- Create token reference documentation

### Step 3: Build Component Catalog

For each UI component:

**Document Visual Attributes**
- Background, border, and text colors (reference tokens)
- Typography (font family, size, weight - reference tokens)
- Border radius (reference tokens)
- Shadows and outlines (reference tokens)
- State variations (hover, focus, active, disabled)

**Document Structural Attributes**
- DOM structure and hierarchy
- CSS classes and variables used
- Responsive behavior patterns
- Accessibility attributes (ARIA, roles)

**Identify Variants**
- Button: primary, secondary, ghost, text
- Card: elevated, flat, outlined
- Input: default, error, disabled

### Step 4: Document System Rules

**Layout Rules**
- Grid system (columns, gutters)
- Alignment patterns
- Spacing between sections/components
- Responsive breakpoint behavior

**Typography Rules**
- Type scale and hierarchy
- Line height standards
- Usage by role (headings, body, labels, captions)

**Interaction Rules**
- Hover/focus patterns
- Error/success indication patterns
- Animation/transition patterns
- Validation feedback patterns

### Step 5: Extract Design Patterns

Identify and document common UI patterns:
- Navigation bars (header, sidebar, tabs)
- Form patterns (input + label + validation)
- Card layouts
- List and table patterns
- Modal/dialog patterns
- Empty state patterns

For each pattern, document:
- Purpose and use cases
- Visual structure
- Behavioral rules
- Associated CSS classes
- Variants

### Step 6: Create CSS Mapping Layer

Map design decisions to implementation:
- Token names → CSS variable names
- Component names → CSS class names
- Utility patterns → utility class names

Ensure naming matches production conventions 1:1.

### Step 7: Publish and Govern

**Version Control**
- Store the DKB in version control (Git)
- Treat it as living documentation
- Tag versions for releases

**Governance Process**
- Establish approval workflow for new tokens/components
- Define who can propose changes
- Create process for accepting new patterns
- Schedule regular audits

## Quality Checklist

Before finalizing the DKB, verify:

- [ ] All core components visible in screenshots are documented with structure and states
- [ ] A consistent spacing scale exists and is applied throughout
- [ ] A consistent typography scale exists and is applied throughout
- [ ] Token naming matches production CSS variable conventions
- [ ] Component naming matches production class name conventions
- [ ] The DKB is specific enough that someone could design a new page that "fits" the product
- [ ] All constraints and exceptions are explicitly documented
- [ ] Accessibility rules are clearly defined
- [ ] Responsive breakpoints and behavior are documented

## Output Format

The DKB should be structured as:

```
design-knowledge-base/
├── README.md (overview and navigation)
├── principles.md (design principles and visual language)
├── tokens/
│   ├── colors.md
│   ├── typography.md
│   ├── spacing.md
│   ├── radius.md
│   ├── shadows.md
│   └── z-index.md
├── components/
│   ├── buttons.md
│   ├── inputs.md
│   ├── cards.md
│   ├── navigation.md
│   └── ... (one file per component)
├── patterns/
│   ├── forms.md
│   ├── navigation.md
│   ├── modals.md
│   └── ... (one file per pattern)
├── rules/
│   ├── layout.md
│   ├── responsive.md
│   ├── accessibility.md
│   └── constraints.md
└── mapping/
    └── css-mapping.md (token and component mappings)
```

## Tools and Scripts

### Token Extractor Script

Use `scripts/extract_tokens.py` to automatically extract CSS variables and repeated values from CSS files.

```bash
python scripts/extract_tokens.py <path-to-css> --output tokens.json
```

### Component Analyzer Script

Use `scripts/analyze_components.py` to scan HTML/CSS and identify component patterns.

```bash
python scripts/analyze_components.py <path-to-html> <path-to-css> --output components.json
```

## Common Pitfalls to Avoid

- **Over-tokenizing**: Not every value needs to be a token. Focus on values that repeat or have semantic meaning.
- **Inconsistent naming**: Establish naming conventions early and stick to them.
- **Missing states**: Don't forget to document hover, focus, disabled, and error states.
- **Ignoring edge cases**: Include empty states, error states, and loading states in analysis.
- **Skipping constraints**: Explicitly document what NOT to do, not just what to do.

## Next Steps

After building the DKB:

1. **Review with stakeholders**: Get design and engineering buy-in
2. **Generate UI previews**: Use the DKB with the `wireframe-to-preview` skill
3. **Generate production code**: Use the DKB with the `preview-to-code` skill
4. **Maintain and evolve**: Keep the DKB updated as the design system evolves

## References

For detailed process documentation, see [dkb-creation-guide.md](references/dkb-creation-guide.md).
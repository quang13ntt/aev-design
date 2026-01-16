---
name: wireframe-to-preview
description: Guide for generating high-fidelity HTML/CSS previews from low-fidelity wireframes using a Design Knowledge Base (DKB). Use when converting wireframes (images, Figma frames, or descriptions) into browser-viewable previews with token-driven styling and component-driven structure. Ensures visual consistency with existing product screens.
---

# Wireframe to Preview Skill

This skill guides the process of transforming low-fidelity wireframes into high-fidelity HTML/CSS previews that can be reviewed in a browser. All styling is constrained by the Design Knowledge Base (DKB) to prevent invented UI elements.

## Purpose

- Convert wireframes into reviewable, high-fidelity previews
- Produce browser-openable artifacts for stakeholder validation
- Maintain token-driven and component-driven styling
- Ensure visual consistency with existing product screens

## When to Use This Skill

- Converting wireframes into HTML/CSS mockups
- Creating reviewable prototypes from design sketches
- Generating previews for design validation
- Building proof-of-concept UIs with existing design systems
- Translating Figma/Sketch frames into code previews

## Prerequisites

You must have a Design Knowledge Base (DKB) before using this skill. If you don't have one, use the `build-design-knowledge-base` skill first.

## Inputs

### Required
- **Wireframe**: Low-fidelity structural input in one of these formats:
  - Image (PNG, JPG, screenshot)
  - Figma frame or artboard
  - Structured description (JSON or text)
- **Design Knowledge Base (DKB)**: Complete with tokens, components, patterns, and rules

### Optional
- **Constraints**: Specific responsive breakpoints or accessibility requirements
- **Target viewport**: Desktop, tablet, mobile, or multi-viewport

## Outputs

### 1. Preview Page (HTML/CSS)
A fully styled, browser-openable HTML/CSS file that:
- Uses only DKB tokens and components
- Renders correctly in modern browsers
- Includes responsive behavior
- Implements basic interaction states

### 2. Preview Specification (Recommended)
Documentation including:
- **Component list**: All components used with their variants
- **Token usage**: Which tokens were applied where
- **Layout notes**: Spacing, grid structure, breakpoints
- **Interaction notes**: States, validation feedback, navigation behavior

## Process

### Step 1: Interpret the Wireframe

**Component Detection**
- Identify each UI element in the wireframe
- Classify elements by type:
  - Buttons
  - Text elements (headings, body, labels, captions)
  - Form inputs (text fields, dropdowns, checkboxes, radios)
  - Cards and containers
  - Lists and tables
  - Navigation elements (tabs, menus, breadcrumbs)
  - Icons and images

**Layout Extraction**
- Analyze hierarchical grouping (which elements are nested)
- Identify spacing and alignment patterns
- Determine grid or flexbox structure
- Note relative positioning and z-order

**Text Role Identification**
- Heading levels (H1, H2, H3, etc.)
- Body text
- Labels
- Captions
- Error/helper text

### Step 2: Map Wireframe Elements to DKB Components

**Component Matching**
- For each detected element, find the closest matching component in the DKB
- Use semantic rules from the DKB to determine component type
- Example: A rectangular button with primary action → `Button[primary]`
- Example: A text input with label → `Input[default]`

**Variant Selection**
- Identify which variant best matches the wireframe intent
- Button variants: primary, secondary, ghost, text
- Card variants: elevated, flat, outlined
- Input variants: default, error, disabled

**State Resolution**
- Determine initial state (default, hover, focus, active, disabled, error)
- Plan for interaction states based on DKB patterns
- Document expected state transitions

### Step 3: Apply Tokens and Rules

**Bind Typography**
- Map heading text to typography tokens (e.g., `font.heading-lg`)
- Map body text to typography tokens (e.g., `font.body-md`)
- Apply line height and letter spacing from tokens
- Ensure hierarchy follows DKB type scale

**Bind Spacing**
- Apply spacing tokens to padding (e.g., `space.4`, `space.6`)
- Apply spacing tokens to margins and gaps
- Enforce section spacing from DKB
- Use grid/gutter tokens for layout

**Bind Colors**
- Apply color tokens to backgrounds (e.g., `color.surface.primary`)
- Apply color tokens to text (e.g., `color.text.primary`)
- Apply color tokens to borders (e.g., `color.border.default`)
- Use semantic colors for states (success, warning, error)

**Bind Radius and Elevation**
- Apply border radius tokens (e.g., `radius.md`)
- Apply shadow tokens for elevation (e.g., `shadow.card`)
- Ensure consistency with DKB visual language

**Enforce Layout Rules**
- Apply grid system from DKB
- Follow alignment rules (centered, left-aligned, gutters)
- Implement spacing rhythm from DKB
- Respect responsive breakpoint behavior

### Step 4: Generate Preview Markup and Styles

**HTML Structure**
- Use semantic HTML elements (`header`, `main`, `nav`, `section`, `article`)
- Apply component classes from DKB CSS mapping
- Structure nesting according to DKB component patterns
- Include accessibility attributes (alt text, ARIA labels when needed)

**CSS Styling**
- Reference CSS variables from DKB token mappings
- Use component classes from DKB
- Avoid hard-coded values (colors, sizes, shadows)
- Follow DKB naming conventions

**Token Usage Example**
```css
.button-primary {
  background-color: var(--color-primary);
  color: var(--color-text-inverse);
  padding: var(--space-3) var(--space-6);
  border-radius: var(--radius-md);
  font-family: var(--font-family-base);
  font-size: var(--font-size-md);
  font-weight: var(--font-weight-semibold);
  box-shadow: var(--shadow-sm);
}
```

### Step 5: Add Responsiveness and Basic Interactions

**Implement Responsive Behavior**
- Apply breakpoints from DKB
- Adjust layout for different viewports
- Scale typography appropriately
- Hide/show elements based on viewport (if specified in DKB)

**Implement Interaction States**
- Add hover styles (from DKB state patterns)
- Add focus styles (ensure visibility per accessibility rules)
- Add active states
- Add disabled states (if applicable)

**Ensure Accessibility**
- Focus indicators must be visible (per DKB accessibility rules)
- Minimum touch target sizes (typically 44×44px)
- Proper contrast ratios (check against DKB requirements)
- Logical tab order

## Quality Checklist

Before delivering the preview, verify:

- [ ] Every visual decision references a DKB token or component rule
- [ ] All UI elements map to known DKB components and variants
- [ ] No hard-coded colors, sizes, or shadows exist
- [ ] The preview is visually consistent with existing product screens
- [ ] Typography hierarchy follows DKB type scale
- [ ] Spacing follows DKB spacing scale
- [ ] The preview renders correctly in target browsers
- [ ] Focus states are visible and meet accessibility standards
- [ ] Touch targets meet minimum size requirements
- [ ] The preview is usable for stakeholder review (clear hierarchy, consistent spacing)

## Output Format

Deliver the preview as:

```
preview/
├── index.html (main preview page)
├── styles.css (compiled styles using DKB tokens)
├── README.md (preview specification)
└── assets/ (images, icons if needed)
```

## Common Patterns

### Form Preview
```html
<form class="form-container">
  <div class="form-field">
    <label class="form-label">Email</label>
    <input type="email" class="input-default" />
  </div>
  <button type="submit" class="button-primary">Submit</button>
</form>
```

### Card Grid Preview
```html
<div class="grid-container">
  <div class="card-elevated">
    <h3 class="card-title">Title</h3>
    <p class="card-body">Description text</p>
  </div>
  <!-- more cards -->
</div>
```

## Scripts and Tools

### Wireframe Parser Script

Use `scripts/parse_wireframe.py` to extract structure from wireframe images using vision models.

```bash
python scripts/parse_wireframe.py <wireframe-image> --output structure.json
```

### Preview Generator Script

Use `scripts/generate_preview.py` to automatically generate HTML/CSS from wireframe structure and DKB.

```bash
python scripts/generate_preview.py structure.json dkb/ --output preview/
```

## Troubleshooting

**Problem**: Wireframe element doesn't match any DKB component
**Solution**: Choose the closest semantic match and document the gap. Consider adding the component to the DKB.

**Problem**: Token doesn't exist for a specific value
**Solution**: Find the closest token or propose a new token following DKB governance.

**Problem**: Preview doesn't match wireframe intent
**Solution**: Review component variant selection and ensure layout structure matches wireframe hierarchy.

## Next Steps

After generating the preview:

1. **Review with stakeholders**: Get design validation
2. **Iterate if needed**: Adjust based on feedback
3. **Generate production code**: Use the `preview-to-code` skill to convert the approved preview into production-ready code

## References

For detailed process documentation, see [preview-generation-guide.md](references/preview-generation-guide.md).
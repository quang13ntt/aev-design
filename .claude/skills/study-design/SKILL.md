---
name: study-design
description: Guide for analyzing UI/UX design references (images/screenshots and descriptive text) and CSS implementations to extract design principles, mood, and style. Synthesizes findings to produce a comprehensive markdown guideline document for UI/UX generation and implementation.
---

# Study Design Skill

This skill provides a structured approach to analyzing UI/UX design references and creating actionable design guidelines.

## Primary Deliverable

**The ultimate output of this skill is a comprehensive markdown guideline document** that serves as the single source of truth for UI/UX generation and implementation. This document contains:

- Design philosophy and principles
- Complete design token specifications (colors, typography, spacing, etc.)
- Component guidelines with code examples
- Do's and don'ts for consistent implementation
- Accessibility requirements
- Responsive design patterns
- Implementation checklists

This guideline document can be directly used by developers and designers to create new pages and components that align with the analyzed design system.

**See [references/output-template.md](references/output-template.md) for the complete template and structure.**

## When to Use This Skill

Use this skill when you need to:

- Analyze existing design references (screenshots, images, descriptions)
- Analyze existing CSS files to extract design patterns and systems
- Extract design principles, mood, and style from references
- **Synthesize findings from visual designs and CSS code** to create unified guidelines
- Identify gaps between design intent and implementation
- Create actionable guidelines for new designs that maintain consistency with the reference philosophy
- Document design systems from existing implementations

## Process Overview

1. **Gather References**: Collect image descriptions, textual context, and CSS files
2. **Analyze Visual/Text**: Break down layout, colors, typography, spacing, and interactions from design references
3. **Analyze CSS**: Extract design tokens, patterns, and implementation details from code
4. **Synthesize Findings**: Reconcile visual intent with CSS implementation, identify gaps and alignments
5. **Create Guidelines**: Develop unified, step-by-step instructions combining best of both analyses
6. **Generate Markdown Document**: Produce comprehensive guideline document using the output template

**Final Output:** A complete markdown file (e.g., `project-ui-ux-guidelines.md`) ready for team use.

## Analysis Approaches

### Approach 1: Visual and Text Analysis

For analyzing UI/UX design references from images and descriptive text:

**See [references/image-text-analysis.md](references/image-text-analysis.md) for detailed guidance on:**

- Analyzing design images and screenshots step-by-step
- Extracting layout, color, typography, spacing, and interaction patterns
- Analyzing text descriptions to extract brand identity and design philosophy
- Translating descriptions into concrete design decisions
- Complete analysis checklist

### Approach 2: CSS Code Analysis

For analyzing existing CSS files to understand implemented design systems:

**See [references/css-analysis.md](references/css-analysis.md) for detailed guidance on:**

- Extracting design tokens from CSS custom properties and variables
- Analyzing layout systems, grid patterns, and responsive design
- Documenting component patterns and styling conventions
- Understanding animation and interaction implementations
- Creating design system documentation from code
- Complete CSS analysis checklist

### Approach 3: Synthesis of Visual and CSS Analysis

For combining insights from both visual/text references and CSS code:

**See [references/synthesis.md](references/synthesis.md) for detailed guidance on:**

- Creating alignment matrices between design intent and implementation
- Categorizing findings (aligned, partially aligned, misaligned, missing)
- Resolving conflicts between visual references and CSS code
- Creating unified design tokens that reflect both sources
- Building implementation roadmaps for bringing code in line with design
- Generating comprehensive design system documentation
- Complete synthesis workflow with examples

## Output: Guideline Markdown Document

The primary deliverable is a comprehensive markdown file following this structure:

1. **Design Philosophy & Mood** - Overall aesthetic and brand personality
2. **Design Tokens** - Complete specifications:
   - Color palette (with hex codes and usage)
   - Typography system (fonts, scales, weights, line heights)
   - Spacing system (base unit and scale)
   - Border radius, shadows, transitions
3. **Layout System** - Container, grid, breakpoints
4. **Component Guidelines** - Detailed specs for each component:
   - Visual characteristics
   - Code examples (HTML + CSS)
   - Variants and states
   - Usage guidelines
5. **Interaction Patterns** - Hover, focus, loading, error states
6. **Accessibility Requirements** - Standards and best practices
7. **Responsive Design Patterns** - Mobile-first approach, breakpoint behavior
8. **Do's and Don'ts** - Clear rules for consistency
9. **Implementation Checklist** - Verification list for new development
10. **Code Examples** - Complete, copy-ready implementations
11. **Next Steps** - Implementation roadmap

**See the complete template at [references/output-template.md](references/output-template.md)**

## Quick Start Guide

### Input Requirements

**For Visual/Text Analysis:**

- Image descriptions: Detailed descriptions of each image or screenshot, including layout, colours, typography, spacing, and notable components
- Textual context: Any descriptive text about the style, mood, design philosophy, or brand identity

**For CSS Analysis:**

- CSS file paths: Locations of stylesheet files to analyze
- Context: Information about the CSS architecture (framework, methodology, preprocessor)

**For Synthesis:**

- Completed visual/text analysis results
- Completed CSS analysis results
- Project context: timeline, constraints, stakeholder priorities

### Output Structure

1. **Design Philosophy & Mood Summary**
   - Explain the overall aesthetic, tone, and emotional impact
   - Describe the brand personality and user experience goals

2. **Key UI/UX Principles Observed**
   - **Layout and structure**: Grid systems, component placement, visual hierarchy
   - **Colour palette and contrast**: Color schemes, contrast ratios, accessibility considerations
   - **Typography and hierarchy**: Font families, sizes, weights, text spacing
   - **Spacing and alignment**: Margins, padding, alignment principles
   - **Interaction patterns**: Button styles, hover states, animations, micro-interactions

3. **Actionable Guidelines for New Page**
   - Step-by-step instructions for applying these principles
   - Recommended components and patterns to use
   - Implementation tips for consistency

4. **Do's and Don'ts**
   - What to keep consistent with the reference designs
   - What to avoid that would break the design philosophy
   - Common pitfalls and how to prevent them

5. **Optional Visual Suggestions**
   - Suggested colour codes (hex, RGB, HSL)
   - Font families and fallback options
   - Spacing values and measurement units
   - Component sizing guidelines

## Best Practices

- Always base guidelines on actual observations from references, not assumptions
- Prioritize accessibility and usability in all recommendations
- Consider responsive design implications
- Test guidelines against the original references for consistency
- Provide specific, measurable recommendations where possible
- When analyzing CSS, extract design tokens before diving into components
- **Cross-reference visual analysis with CSS implementation to ensure accuracy**
- **Perform synthesis when both visual and CSS sources are available** - this provides the most comprehensive understanding
- Document both current state (CSS) and target state (visual intent) when they differ
- Create phased implementation plans rather than expecting immediate alignment
- Involve stakeholders in conflict resolution decisions
- Document inconsistencies and provide recommendations for standardization
- Validate synthesis results against real use cases before finalizing

## Example Applications

### Example 1: Analyzing a Minimalist Design (Visual Reference)

When analyzing a minimalist design screenshot:

- Philosophy: Clean, focused, user-centric
- Principles: Generous white space, limited color palette, sans-serif typography
- Guidelines: Use 8px grid system, maintain 60% white space ratio, limit to 2-3 colors
- Don'ts: Avoid cluttered layouts, excessive decorative elements
- Suggestions: #FFFFFF background, Roboto font family, 16px base spacing

### Example 2: Analyzing a Design System (CSS Files)

When analyzing an existing CSS codebase:

1. **Extract tokens**: Document color palette from CSS variables (--primary: #3b82f6, etc.)
2. **Identify system**: Found 4px base spacing unit with 8-step scale
3. **Map components**: Documented 3 button variants, 2 card styles, form patterns
4. **Note issues**: Found 15 inconsistent spacing values that should use the scale
5. **Create guidelines**: Standardize on design token usage, consolidate duplicate styles

## Recommended Workflow: Complete Design Study

For the most comprehensive results, use all three approaches:

### Phase 1: Individual Analyses

1. **Perform visual/text analysis** - Understand design intent, principles, and mood
2. **Perform CSS analysis** - Extract actual implementation patterns and tokens
3. Document findings from each analysis separately

### Phase 2: Synthesis

4. **Create alignment matrix** - Map visual findings to CSS implementation
2. **Categorize alignments** - Identify what works, what's missing, what conflicts
3. **Resolve conflicts** - Make informed decisions about which path to follow
4. **Generate unified design tokens** - Create single source of truth

### Phase 3: Generate Guideline Document

8. **Prepare content** - Organize all findings from analysis and synthesis
9. **Follow output template** - Use the structure from [references/output-template.md](references/output-template.md)
10. **Write markdown file** - Create comprehensive guideline document with:
   - All design tokens with specific values
   - Component guidelines with code examples
   - Do's and don'ts
   - Implementation checklist
11. **Include implementation roadmap** - Phased plan if current state differs from target
12. **Save as markdown file** - Name appropriately (e.g., `project-name-ui-ux-guidelines.md`)

**This markdown document is the primary deliverable that teams will use for all future UI/UX development.**

### When to Use Each Approach Alone

**Visual/Text Only:**

- Starting a new project from designs
- No existing codebase to analyze
- Creating initial design system documentation

**CSS Only:**

- Documenting an undocumented existing system
- Refactoring or modernizing code
- No visual design references available

**Synthesis Always:**

- When both visual references AND CSS code exist
- Inheriting a project with existing designs and code
- Ensuring design-dev alignment
- Bridging gap between design intent and implementation

---

## Creating the Output Document

### Step-by-Step Process

1. **Complete all analysis** - Ensure visual/text and/or CSS analysis is thorough
2. **Perform synthesis** - If both sources exist, reconcile differences
3. **Open output template** - Reference [references/output-template.md](references/output-template.md)
4. **Fill in each section** - Replace template placeholders with actual findings:
   - Copy exact color values, not placeholders
   - Include real component code, not examples
   - Write specific do's and don'ts based on analysis
   - Add actual breakpoint values from the system
5. **Customize structure** - Remove sections that don't apply, add project-specific ones
6. **Add code examples** - Include complete, working code for key components
7. **Create implementation roadmap** - If changes are needed, outline phases
8. **Review for completeness** - Use the checklist in output-template.md
9. **Save markdown file** - Use naming convention: `[project-name]-ui-ux-guidelines.md`

### Quality Checklist

Before delivering the guideline document, verify:

- [ ] All design tokens have specific values (not "TBD" or placeholders)
- [ ] Color palette includes hex codes and usage guidance
- [ ] Typography system is complete with sizes, weights, line heights
- [ ] Spacing system shows the full scale with actual values
- [ ] Each component has:
  - [ ] Visual description
  - [ ] Code example (HTML + CSS)
  - [ ] All variants documented
  - [ ] All states (hover, focus, disabled) specified
  - [ ] Usage guidelines
- [ ] Accessibility requirements are included
- [ ] Responsive patterns are documented
- [ ] Do's and don'ts are specific and actionable
- [ ] Implementation checklist is included
- [ ] Document metadata is complete (date, version, sources)

### File Naming Convention

**Format:** `[project-name]-ui-ux-guidelines.md`

**Examples:**
- `acme-dashboard-ui-ux-guidelines.md`
- `ecommerce-web-design-guidelines.md`
- `mobile-app-ui-guidelines.md`
- `design-system-v2-guidelines.md`

### Document Maintenance

The guideline document should be:
- **Version controlled** - Track changes in git
- **Living document** - Update when design system evolves
- **Team accessible** - Share with all designers and developers
- **Referenced** - Link to it from project README and documentation
- **Reviewed regularly** - Update quarterly or when major changes occur

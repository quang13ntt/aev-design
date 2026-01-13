# Sub-Skill: Analyzing CSS Files & Style Management

## Objective

Master the systematic analysis of CSS files, particularly large stylesheets, to efficiently extract relevant styles for component implementation while maintaining organization and scalability.

## Step 1: Initial CSS File Assessment

### File Size & Complexity Evaluation

- **Line Count**: Determine if the file is manageable (<500 lines), medium (500-2000 lines), or large (>2000 lines)
- **CSS Methodology**: Identify the approach used (vanilla CSS, BEM, SMACSS, utility-first, CSS-in-JS)
- **CSS Preprocessor**: Check for SCSS, SASS, LESS, or PostCSS features
- **Framework Detection**: Identify if using Bootstrap, Tailwind, Bulma, Foundation, or custom

### Structure Overview

- **Sections**: Look for comment-based organization (/*Header Styles */, /* Components*/)
- **CSS Variables**: Identify custom properties (--primary-color, --spacing-unit)
- **Media Queries**: Note responsive breakpoints and their organization
- **Import Statements**: Check for @import or modular CSS files
- **Global Styles**: Identify resets, normalizations, and base styles

## Step 2: CSS File Decomposition Strategies

### Strategy A: For Large Monolithic CSS Files (>2000 lines)

#### Phase 1: Create a Table of Contents

Scan the file and create an index of major sections:

```markdown
CSS File Index:
- Lines 1-50: CSS Reset & Base Styles
- Lines 51-150: Typography
- Lines 151-300: Color Variables
- Lines 301-450: Layout & Grid System
- Lines 451-650: Header & Navigation
- Lines 651-900: Buttons & Forms
- Lines 901-1200: Cards & Components
- Lines 1201-1500: Footer
- Lines 1501-1800: Utility Classes
- Lines 1801-2000: Media Queries
```

#### Phase 2: Extract Sections into Logical Groups

Use search tools to extract sections:

- **Global Styles**: Variables, resets, typography
- **Layout Styles**: Grid, flexbox, containers
- **Component Styles**: Buttons, cards, forms, navigation
- **Utility Styles**: Spacing, colors, text utilities
- **Responsive Styles**: All media queries

#### Phase 3: Create a Style Reference Document

Document key patterns:

```markdown
# CSS Pattern Reference

## Color System
- Primary: #1a73e8
- Secondary: #34a853
- Background: #f8f9fa
- Text: #202124

## Spacing Scale
- xs: 0.25rem (4px)
- sm: 0.5rem (8px)
- md: 1rem (16px)
- lg: 1.5rem (24px)
- xl: 2rem (32px)

## Typography Scale
- h1: 2.5rem, bold
- h2: 2rem, semibold
- body: 1rem, regular
- small: 0.875rem, regular
```

### Strategy B: For Modular CSS Files (Multiple Files)

#### Map the CSS Architecture

```
styles/
├── base/
│   ├── reset.css
│   ├── typography.css
│   └── variables.css
├── components/
│   ├── buttons.css
│   ├── cards.css
│   ├── forms.css
│   └── navigation.css
├── layout/
│   ├── grid.css
│   ├── header.css
│   └── footer.css
└── utilities/
    ├── spacing.css
    └── colors.css
```

#### Create Import Priority Map

1. **Foundation**: Variables, resets, base styles
2. **Layout**: Grid, containers, structural elements
3. **Components**: Buttons, cards, modular pieces
4. **Utilities**: Helper classes, overrides

## Step 3: Efficient CSS Search Strategies

### Search Pattern 1: Class Name Pattern Matching

**For Component-Specific Styles:**

```
Search Terms:
- "\.btn" or ".button" → Find all button classes
- "\.card" → Find all card classes
- "\.nav" → Find all navigation classes
- "\.hero" → Find hero section styles
```

**Using Regex Search:**

- `\.btn-[a-z-]+` → Find all button variations (btn-primary, btn-secondary, etc.)
- `\.card-[a-z-]+` → Find all card variations
- `@media.*\(max-width` → Find all mobile breakpoints

### Search Pattern 2: Visual Property Hunting

**When looking for specific visual styles:**

```
Search for exact values from design:
- "#1a73e8" → Find all uses of primary color
- "24px" or "1.5rem" → Find spacing/sizing patterns
- "border-radius: 8px" → Find rounded elements
- "box-shadow" → Find elevated elements
- "font-family:" → Find typography declarations
```

### Search Pattern 3: Selector Type Filtering

**By Selector Complexity:**

- Simple selectors: `.class-name`
- Descendant: `.parent .child`
- Direct child: `.parent > .child`
- Pseudo-classes: `.element:hover`, `.element:focus`
- Pseudo-elements: `.element::before`, `.element::after`

### Search Pattern 4: State & Modifier Patterns

**Interactive States:**

```
- ":hover" → All hover effects
- ":focus" → Focus states
- ":active" → Active/pressed states
- ":disabled" → Disabled states
- ".is-active" or ".active" → Active modifiers
```

## Step 4: Component-to-CSS Mapping Process

### Workflow for Each Component

#### Step 4.1: Identify Component Base Class

```
Component: Primary Button
Base Class: .btn or .button
```

#### Step 4.2: Search for Base Class and Variations

```
Search Results:
1. .btn { base styles }
2. .btn-primary { primary variant }
3. .btn-secondary { secondary variant }
4. .btn-large { size modifier }
5. .btn:hover { hover state }
6. .btn:disabled { disabled state }
```

#### Step 4.3: Extract Related Styles

Create a component stylesheet with all related rules:

```css
/* Button Component Styles */

/* Base Button */
.btn {
  display: inline-block;
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
  border-radius: 0.375rem;
  border: none;
  cursor: pointer;
  transition: all 0.2s ease;
}

/* Button Variants */
.btn-primary {
  background-color: #1a73e8;
  color: white;
}

.btn-secondary {
  background-color: #6c757d;
  color: white;
}

/* Button States */
.btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Button Sizes */
.btn-large {
  padding: 1rem 2rem;
  font-size: 1.125rem;
}
```

#### Step 4.4: Document Dependencies

Note any required variables or utilities:

```markdown
Button Component Dependencies:
- CSS Variables: --primary-color, --transition-speed
- Utility Classes: None
- Typography: Inherits from body
- Icons: May contain .icon class for icon buttons
```

## Step 5: Creating Organized Component Stylesheets

### Output Structure for Component CSS

```css
/* ============================================
   COMPONENT: [Component Name]
   ============================================ */

/* Base Styles
   ----------------------------------------- */
.component-name {
  /* Layout */
  display: flex;
  
  /* Spacing */
  padding: 1rem;
  
  /* Visual */
  background-color: white;
  border: 1px solid #ddd;
}

/* Modifiers & Variants
   ----------------------------------------- */
.component-name--variant {
  /* Modified properties */
}

/* States
   ----------------------------------------- */
.component-name:hover {
  /* Hover effects */
}

.component-name.is-active {
  /* Active state */
}

/* Child Elements
   ----------------------------------------- */
.component-name__header {
  /* Header styles */
}

.component-name__body {
  /* Body styles */
}

/* Responsive Behavior
   ----------------------------------------- */
@media (max-width: 768px) {
  .component-name {
    /* Mobile adaptations */
  }
}
```

## Step 6: CSS Extraction Tools & Techniques

### Manual Extraction Process

1. **Create Component CSS File**: `component-name.css`
2. **Search Original CSS**: Find all related selectors
3. **Copy Relevant Rules**: Include base, variants, states
4. **Test Isolation**: Ensure component works standalone
5. **Document Dependencies**: Note any required global styles

### Tool-Assisted Extraction

**Using VS Code / Text Editor:**

- **Find All References**: Search for class names
- **Multi-cursor Editing**: Select and copy multiple blocks
- **Regex Search**: Pattern-based extraction
- **Fold/Unfold**: Collapse sections to see structure

**Using Browser DevTools:**

- **Computed Styles**: See actual applied styles
- **CSS Panel**: Copy rules directly from inspector
- **Coverage Tool**: Identify unused CSS

**Using CSS Analysis Tools:**

- **CSS Stats**: Analyze specificity, colors, fonts
- **PurgeCSS**: Remove unused styles
- **CSScomb**: Sort and organize CSS properties

## Step 7: CSS Optimization for Components

### Refactoring Checklist

- [ ] Remove duplicate rules
- [ ] Consolidate similar selectors
- [ ] Optimize specificity (avoid !important)
- [ ] Group related properties
- [ ] Extract common patterns into utilities
- [ ] Add fallback values for older browsers
- [ ] Minify for production
- [ ] Remove unused vendor prefixes

### Style Organization Best Practices

```css
/* Property Order (Recommended) */
.component {
  /* Positioning */
  position: relative;
  top: 0;
  z-index: 1;
  
  /* Box Model */
  display: flex;
  width: 100%;
  padding: 1rem;
  margin: 0 auto;
  
  /* Typography */
  font-size: 1rem;
  line-height: 1.5;
  text-align: left;
  
  /* Visual */
  background-color: white;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  
  /* Animation */
  transition: all 0.3s ease;
}
```

## Output: CSS Analysis Document

```markdown
# CSS Analysis for [Project Name]

## File Structure
- Total CSS Files: [Number]
- Total Lines: [Number]
- Organization Method: [BEM/Utility/Modular]

## CSS Architecture
[Diagram or file tree]

## Component Style Map

### Button Component
- **File**: components/buttons.css (Lines 45-120)
- **Classes**: .btn, .btn-primary, .btn-secondary, .btn-lg
- **Dependencies**: --primary-color, --font-family
- **States**: hover, focus, active, disabled

### Card Component
- **File**: components/cards.css (Lines 200-350)
- **Classes**: .card, .card-header, .card-body, .card-footer
- **Dependencies**: --shadow-sm, --border-radius
- **Variants**: .card-featured, .card-compact

[Continue for all components...]

## Global Styles Reference
- **Colors**: [Palette]
- **Typography**: [Scale]
- **Spacing**: [System]
- **Breakpoints**: [Values]

## Extraction Priority
1. Variables and tokens
2. Layout system
3. Typography styles
4. Component styles (by page section order)
5. Utility classes
```

## Best Practices

- **Preserve Cascading Logic**: Maintain CSS order when extracting
- **Keep Specificity Low**: Avoid deep nesting and IDs
- **Document Custom Properties**: Note all CSS variables used
- **Test in Isolation**: Verify extracted styles work standalone
- **Maintain Consistency**: Follow existing naming conventions
- **Version Control**: Track CSS changes for accountability
- **Comment Extensively**: Add context for complex rules

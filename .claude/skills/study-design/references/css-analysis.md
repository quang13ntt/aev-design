# CSS Analysis Guide

This guide provides detailed instructions for analyzing existing CSS files to extract design patterns, understand the design system, and create actionable guidelines.

## When to Analyze CSS Files

CSS analysis is valuable when:

- Inheriting or maintaining an existing codebase
- Creating a design system documentation from existing code
- Modernizing or refactoring legacy styles
- Ensuring consistency across a project
- Extracting design tokens from implementation
- Understanding the technical implementation of visual designs

## Step-by-Step CSS Analysis Process

### Step 1: High-Level Structure Analysis

Begin with understanding the overall CSS organization:

**File Structure:**

- Identify organization pattern (monolithic, modular, component-based)
- Document file naming conventions
- Note import/include hierarchy
- Identify vendor prefixes usage

**CSS Architecture:**

- Methodology used: BEM, OOCSS, SMACSS, Atomic CSS, CSS Modules, CSS-in-JS
- Naming conventions and patterns
- Specificity patterns and nesting depth
- Use of CSS preprocessors (Sass, Less, Stylus, PostCSS)

**Framework Detection:**

- Identify CSS frameworks (Bootstrap, Tailwind, Foundation, Bulma)
- Custom framework or pure CSS
- Framework customization patterns
- Utility class usage

### Step 2: Design Token Extraction

Extract design tokens from CSS custom properties and variables:

**Color System:**

```css
/* Look for color definitions */
:root {
  --color-primary: #3b82f6;
  --color-secondary: #8b5cf6;
  --color-accent: #f59e0b;
  /* ... */
}

/* Or Sass variables */
$primary-color: #3b82f6;
$text-color: #1f2937;
```

**Document:**

- Primary, secondary, accent colors
- Text colors (heading, body, muted, disabled)
- Background colors
- Border colors
- State colors (success, warning, error, info)
- Shadow colors
- Semantic color naming vs presentational

**Typography System:**

```css
:root {
  --font-family-sans: 'Inter', system-ui, sans-serif;
  --font-family-serif: 'Georgia', serif;
  --font-family-mono: 'Fira Code', monospace;
  
  --font-size-xs: 0.75rem;   /* 12px */
  --font-size-sm: 0.875rem;  /* 14px */
  --font-size-base: 1rem;    /* 16px */
  --font-size-lg: 1.125rem;  /* 18px */
  --font-size-xl: 1.25rem;   /* 20px */
  /* ... */
  
  --font-weight-light: 300;
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;
  
  --line-height-tight: 1.25;
  --line-height-normal: 1.5;
  --line-height-relaxed: 1.75;
}
```

**Document:**

- Font families and fallback stacks
- Font size scale and naming
- Font weights available
- Line heights for different contexts
- Letter spacing values
- Text transform patterns

**Spacing System:**

```css
:root {
  --spacing-0: 0;
  --spacing-1: 0.25rem;  /* 4px */
  --spacing-2: 0.5rem;   /* 8px */
  --spacing-3: 0.75rem;  /* 12px */
  --spacing-4: 1rem;     /* 16px */
  --spacing-5: 1.25rem;  /* 20px */
  --spacing-6: 1.5rem;   /* 24px */
  --spacing-8: 2rem;     /* 32px */
  --spacing-10: 2.5rem;  /* 40px */
  --spacing-12: 3rem;    /* 48px */
  --spacing-16: 4rem;    /* 64px */
  /* ... */
}
```

**Document:**

- Base spacing unit
- Spacing scale progression
- Common spacing patterns (padding, margin, gap)
- Breakpoint-specific spacing adjustments

**Other Design Tokens:**

```css
:root {
  /* Border radius */
  --radius-none: 0;
  --radius-sm: 0.125rem;
  --radius-md: 0.375rem;
  --radius-lg: 0.5rem;
  --radius-xl: 0.75rem;
  --radius-full: 9999px;
  
  /* Shadows */
  --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
  
  /* Transitions */
  --transition-fast: 150ms ease-in-out;
  --transition-base: 200ms ease-in-out;
  --transition-slow: 300ms ease-in-out;
  
  /* Z-index */
  --z-dropdown: 1000;
  --z-modal: 1050;
  --z-tooltip: 1100;
}
```

### Step 3: Layout System Analysis

Examine layout patterns and responsive design:

**Grid Systems:**

```css
/* Identify grid patterns */
.container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 1rem;
}

.grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 1.5rem;
}

/* Or flexbox patterns */
.flex-container {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}
```

**Document:**

- Container max-widths and padding
- Grid column counts and gutter sizes
- Flex patterns and wrapping behavior
- CSS Grid vs Flexbox usage

**Breakpoint System:**

```css
/* Find media queries */
@media (min-width: 640px) { /* sm */ }
@media (min-width: 768px) { /* md */ }
@media (min-width: 1024px) { /* lg */ }
@media (min-width: 1280px) { /* xl */ }
@media (min-width: 1536px) { /* 2xl */ }
```

**Document:**

- All breakpoint values
- Mobile-first vs desktop-first approach
- Breakpoint naming conventions
- Container behavior at each breakpoint

**Positioning Patterns:**

```css
/* Look for common positioning */
.sticky-header {
  position: sticky;
  top: 0;
  z-index: 50;
}

.modal-overlay {
  position: fixed;
  inset: 0;
}
```

### Step 4: Component Pattern Analysis

Analyze component-specific styling:

**Button Components:**

```css
.btn {
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  font-weight: 500;
  transition: all 200ms ease-in-out;
}

.btn-primary {
  background-color: var(--color-primary);
  color: white;
}

.btn-primary:hover {
  background-color: var(--color-primary-dark);
  transform: translateY(-1px);
}

.btn-lg {
  padding: 0.75rem 1.5rem;
  font-size: 1.125rem;
}
```

**Document:**

- Base button styles
- Button variants (primary, secondary, outline, ghost)
- Button sizes (sm, md, lg)
- Button states (hover, active, focus, disabled)
- Icon button patterns

**Card Components:**

```css
.card {
  background: white;
  border-radius: 0.5rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  padding: 1.5rem;
}

.card-header {
  margin-bottom: 1rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid var(--color-gray-200);
}
```

**Document:**

- Card structure and spacing
- Card variants (elevated, bordered, flat)
- Card sections (header, body, footer)
- Interactive card states

**Form Components:**

```css
.input {
  width: 100%;
  padding: 0.5rem 0.75rem;
  border: 1px solid var(--color-gray-300);
  border-radius: 0.375rem;
  font-size: 1rem;
}

.input:focus {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
  border-color: var(--color-primary);
}

.input.error {
  border-color: var(--color-error);
}
```

**Document:**

- Input field styling
- Focus states and accessibility
- Error and success states
- Label and helper text styling
- Form layout patterns

**Navigation Components:**

```css
.nav {
  display: flex;
  gap: 1rem;
}

.nav-item {
  padding: 0.5rem 1rem;
  color: var(--color-text);
  text-decoration: none;
}

.nav-item.active {
  color: var(--color-primary);
  border-bottom: 2px solid var(--color-primary);
}
```

**Document:**

- Navigation structure
- Active state indicators
- Dropdown menu styling
- Mobile navigation patterns
- Hamburger menu implementation

### Step 5: Animation and Interaction Analysis

Examine interactive behaviors:

**Transitions:**

```css
.element {
  transition-property: all;
  transition-duration: 200ms;
  transition-timing-function: ease-in-out;
}

/* Or shorthand */
.element {
  transition: all 200ms ease-in-out;
}
```

**Document:**

- Common transition properties
- Transition durations
- Easing functions used
- Which elements have transitions

**Animations:**

```css
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animated-element {
  animation: fadeIn 300ms ease-out;
}
```

**Document:**

- Keyframe animations defined
- Animation durations and delays
- Animation timing functions
- Usage patterns

**Hover Effects:**

```css
.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
}

.button:hover {
  background-color: var(--color-primary-dark);
}

.link:hover {
  color: var(--color-primary);
  text-decoration: underline;
}
```

**Document:**

- Common hover patterns
- Transform effects
- Color changes on hover
- Shadow changes on hover

### Step 6: Utility Class Analysis

If the codebase uses utility classes:

**Spacing Utilities:**

```css
.m-0 { margin: 0; }
.m-1 { margin: 0.25rem; }
.p-4 { padding: 1rem; }
.px-6 { padding-left: 1.5rem; padding-right: 1.5rem; }
.mt-8 { margin-top: 2rem; }
```

**Display and Layout Utilities:**

```css
.flex { display: flex; }
.grid { display: grid; }
.hidden { display: none; }
.block { display: block; }
```

**Typography Utilities:**

```css
.text-sm { font-size: 0.875rem; }
.font-bold { font-weight: 700; }
.text-center { text-align: center; }
.uppercase { text-transform: uppercase; }
```

**Document:**

- Utility naming patterns
- Utility categories available
- Responsive utility variants
- State-based utilities (hover:, focus:, etc.)

### Step 7: Accessibility Analysis

Review accessibility-related CSS:

**Focus States:**

```css
*:focus {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

.btn:focus-visible {
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.5);
}
```

**Document:**

- Focus indicator styles
- :focus vs :focus-visible usage
- Keyboard navigation support

**Screen Reader Support:**

```css
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}
```

**Color Contrast:**

- Check text/background contrast ratios in code comments or documentation
- Note any color accessibility concerns

### Step 8: Performance and Optimization Analysis

Review CSS performance characteristics:

**Selector Efficiency:**

- Identify overly specific selectors
- Note deep nesting (>3 levels)
- Check for universal selectors (*)
- Look for inefficient descendant selectors

**Code Organization:**

- Check for duplicate declarations
- Identify unused styles
- Note opportunities for consolidation
- Review file size and loading strategy

**Modern CSS Features:**

- CSS custom properties usage
- CSS Grid vs older layout methods
- Logical properties (inline, block) vs physical (left, right)
- Container queries
- :has() selector
- aspect-ratio property

## Extracting Design Guidelines from CSS

### Creating a Design Token Documentation

Transform CSS analysis into design tokens:

```json
{
  "colors": {
    "primary": {
      "50": "#eff6ff",
      "500": "#3b82f6",
      "900": "#1e3a8a"
    }
  },
  "spacing": {
    "base": "4px",
    "scale": [0, 4, 8, 12, 16, 24, 32, 48, 64, 96]
  },
  "typography": {
    "fontFamily": {
      "sans": ["Inter", "system-ui", "sans-serif"],
      "serif": ["Georgia", "serif"]
    },
    "fontSize": {
      "base": "16px",
      "scale": {
        "xs": "12px",
        "sm": "14px",
        "base": "16px",
        "lg": "18px",
        "xl": "20px"
      }
    }
  }
}
```

### Creating Component Guidelines

Document component patterns found:

**Button Guidelines:**

1. Use `.btn` base class for all buttons
2. Add variant class: `.btn-primary`, `.btn-secondary`, `.btn-outline`
3. Add size modifier: `.btn-sm`, `.btn-lg`
4. States are automatic: `:hover`, `:active`, `:disabled`
5. Icon buttons add `.btn-icon` class

**Do's:**

- Always include focus states
- Use semantic button variants
- Maintain consistent padding ratios

**Don'ts:**

- Don't override base button styles directly
- Don't use fixed widths unless necessary
- Don't skip disabled state styling

### Identifying Inconsistencies

Document areas needing standardization:

**Common Issues:**

- Inconsistent spacing values (15px, 16px, 18px instead of scale)
- Multiple color values for same semantic meaning
- Inconsistent naming conventions
- Mixed units (px, rem, em, %)
- Duplicate or near-duplicate styles

**Recommendations:**

- Consolidate to design token system
- Standardize naming conventions
- Remove duplicates
- Convert to consistent units

## CSS Analysis Checklist

- [ ] File structure and organization documented
- [ ] CSS methodology identified
- [ ] Framework/library usage noted
- [ ] Color system extracted with all values
- [ ] Typography system documented (families, sizes, weights, line heights)
- [ ] Spacing system extracted with base unit and scale
- [ ] Border radius values documented
- [ ] Shadow system documented
- [ ] Transition/animation patterns noted
- [ ] Layout system analyzed (grid, flexbox, containers)
- [ ] Breakpoints documented
- [ ] Button component patterns extracted
- [ ] Form component patterns extracted
- [ ] Card component patterns extracted
- [ ] Navigation component patterns extracted
- [ ] Utility classes cataloged (if applicable)
- [ ] Focus states documented
- [ ] Accessibility features noted
- [ ] Hover effects documented
- [ ] Inconsistencies identified
- [ ] Performance issues noted
- [ ] Modern CSS feature usage documented

## Tools for CSS Analysis

Helpful tools for analyzing CSS files:

1. **Browser DevTools**: Inspect computed styles, view cascade, test changes
2. **CSS Stats**: Analyze CSS statistics and patterns
3. **Specificity Calculator**: Understand selector specificity
4. **Contrast Checkers**: Validate color accessibility
5. **Code Formatters**: Prettier, Stylelint for consistency
6. **CSS Analyzers**: Wallace, CSS Analyzer for metrics
7. **Unused CSS Detectors**: PurgeCSS, UnCSS to find dead code

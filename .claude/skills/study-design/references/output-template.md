# Design Guidelines Output Template

This template provides the standard structure for the markdown guidelines document that should be produced as the final deliverable of the study-design skill.

## Purpose

This document serves as the **primary deliverable** - a comprehensive, actionable guideline document that developers and designers can use to create new UI/UX components that align with the studied design system.

## Template Structure

```markdown
# [Project Name] UI/UX Design Guidelines

> **Generated from**: [Visual references / CSS analysis / Both]
> **Date**: [Generation date]
> **Version**: 1.0

## 1. Design Philosophy & Mood

### Overview
[2-3 paragraphs describing the overall aesthetic, tone, and emotional impact of the design system]

**Key Characteristics:**
- [Characteristic 1: e.g., "Minimalist and focused"]
- [Characteristic 2: e.g., "Professional yet approachable"]
- [Characteristic 3: e.g., "Data-driven and precise"]

**Brand Personality:**
[Description of how the design reflects brand values and target audience]

**User Experience Goals:**
- [Goal 1: e.g., "Enable quick task completion"]
- [Goal 2: e.g., "Provide clear visual hierarchy"]
- [Goal 3: e.g., "Ensure accessibility for all users"]

---

## 2. Design Tokens

### 2.1 Color Palette

#### Primary Colors
```css
--color-primary: #3b82f6;        /* Brand blue - use for primary actions, links */
--color-primary-dark: #2563eb;   /* Hover state for primary */
--color-primary-light: #93c5fd;  /* Subtle highlights, backgrounds */
```

**Usage:**

- Primary buttons and CTAs
- Active navigation items
- Links and interactive elements
- Brand accents

#### Secondary Colors

```css
--color-secondary: #8b5cf6;      /* Purple - use for secondary actions */
--color-accent: #f59e0b;         /* Amber - use for highlights, warnings */
```

#### Neutral Colors

```css
--color-gray-50: #f9fafb;
--color-gray-100: #f3f4f6;
--color-gray-200: #e5e7eb;
--color-gray-300: #d1d5db;
--color-gray-400: #9ca3af;
--color-gray-500: #6b7280;
--color-gray-600: #4b5563;
--color-gray-700: #374151;
--color-gray-800: #1f2937;
--color-gray-900: #111827;
```

**Usage:**

- Text: gray-900 for headings, gray-700 for body, gray-500 for metadata
- Backgrounds: gray-50 for page, white for cards
- Borders: gray-200 for subtle, gray-300 for prominent

#### Semantic Colors

```css
--color-success: #10b981;        /* Green - success states */
--color-warning: #f59e0b;        /* Amber - warnings */
--color-error: #ef4444;          /* Red - errors, destructive actions */
--color-info: #3b82f6;           /* Blue - informational */
```

#### Accessibility Notes

- All text/background combinations meet WCAG AA standards (4.5:1 minimum)
- Primary on white: 4.9:1 ratio ✓
- Gray-700 on white: 7.2:1 ratio ✓

### 2.2 Typography

#### Font Families

```css
--font-family-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
--font-family-serif: 'Georgia', 'Times New Roman', serif;
--font-family-mono: 'Fira Code', 'Courier New', monospace;
```

**Usage:**

- Sans-serif: All UI text, body copy, headings
- Serif: Optional for long-form content, articles
- Mono: Code snippets, technical data, timestamps

#### Type Scale

```css
--text-xs: 0.75rem;      /* 12px - Fine print, captions */
--text-sm: 0.875rem;     /* 14px - Small body text, labels */
--text-base: 1rem;       /* 16px - Body text (default) */
--text-lg: 1.125rem;     /* 18px - Emphasized body text */
--text-xl: 1.25rem;      /* 20px - H4 */
--text-2xl: 1.5rem;      /* 24px - H3 */
--text-3xl: 1.875rem;    /* 30px - H2 */
--text-4xl: 2.25rem;     /* 36px - H1 */
--text-5xl: 3rem;        /* 48px - Display text */
```

#### Font Weights

```css
--font-weight-light: 300;
--font-weight-normal: 400;
--font-weight-medium: 500;
--font-weight-semibold: 600;
--font-weight-bold: 700;
```

**Usage:**

- Light: Rarely used, large display text only
- Normal: Body text
- Medium: Emphasized text, labels
- Semibold: Subheadings, card titles
- Bold: Headings, strong emphasis

#### Line Heights

```css
--leading-tight: 1.25;       /* Headings, short text */
--leading-normal: 1.5;       /* Body text (default) */
--leading-relaxed: 1.75;     /* Long-form content */
```

### 2.3 Spacing System

**Base Unit:** 4px

```css
--spacing-0: 0;
--spacing-1: 0.25rem;    /* 4px */
--spacing-2: 0.5rem;     /* 8px */
--spacing-3: 0.75rem;    /* 12px */
--spacing-4: 1rem;       /* 16px */
--spacing-5: 1.25rem;    /* 20px */
--spacing-6: 1.5rem;     /* 24px */
--spacing-8: 2rem;       /* 32px */
--spacing-10: 2.5rem;    /* 40px */
--spacing-12: 3rem;      /* 48px */
--spacing-16: 4rem;      /* 64px */
--spacing-20: 5rem;      /* 80px */
--spacing-24: 6rem;      /* 96px */
```

**Usage Guidelines:**

- **spacing-1, spacing-2**: Tight internal spacing (icon gaps, chip padding)
- **spacing-3, spacing-4**: Standard padding (buttons, inputs, cards)
- **spacing-6, spacing-8**: Component margins, section padding
- **spacing-12, spacing-16**: Large section gaps, page margins
- **spacing-20, spacing-24**: Hero sections, major divisions

### 2.4 Border Radius

```css
--radius-none: 0;
--radius-sm: 0.125rem;    /* 2px */
--radius-md: 0.375rem;    /* 6px */
--radius-lg: 0.5rem;      /* 8px */
--radius-xl: 0.75rem;     /* 12px */
--radius-2xl: 1rem;       /* 16px */
--radius-full: 9999px;    /* Pill shape */
```

**Usage:**

- Buttons: radius-md
- Cards: radius-lg
- Modals: radius-xl
- Images: radius-lg
- Pills/badges: radius-full

### 2.5 Shadows

```css
--shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
--shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
--shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
--shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
--shadow-2xl: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
```

**Usage:**

- Buttons: shadow-sm
- Cards: shadow-md
- Dropdowns: shadow-lg
- Modals: shadow-xl
- Hero images: shadow-2xl

### 2.6 Transitions

```css
--transition-fast: 150ms ease-in-out;
--transition-base: 200ms ease-in-out;
--transition-slow: 300ms ease-in-out;
```

**Usage:**

- Hover effects: transition-fast
- State changes: transition-base
- Animations: transition-slow

---

## 3. Layout System

### 3.1 Container

```css
.container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 1rem;
}
```

**Breakpoint behavior:**

- Mobile (< 640px): 16px horizontal padding
- Tablet (640px+): 24px horizontal padding
- Desktop (1024px+): 32px horizontal padding

### 3.2 Grid System

```css
.grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 1.5rem;
}
```

**Common Patterns:**

- Full width: `grid-column: 1 / -1`
- Half width: `grid-column: span 6`
- Third width: `grid-column: span 4`
- Two-thirds: `grid-column: span 8`

### 3.3 Breakpoints

```css
/* Mobile-first approach */
@media (min-width: 640px)  { /* sm */ }
@media (min-width: 768px)  { /* md */ }
@media (min-width: 1024px) { /* lg */ }
@media (min-width: 1280px) { /* xl */ }
@media (min-width: 1536px) { /* 2xl */ }
```

---

## 4. Component Guidelines

### 4.1 Buttons

#### Visual Characteristics

- Border radius: 6px (radius-md)
- Font weight: 500 (medium)
- Transition: 200ms ease-in-out
- Text transform: None (sentence case)

#### Variants

**Primary Button**

```css
.btn-primary {
  background: var(--color-primary);
  color: white;
  padding: 0.75rem 1.5rem;
  border-radius: var(--radius-md);
  font-weight: var(--font-weight-medium);
  transition: var(--transition-base);
  box-shadow: var(--shadow-sm);
}

.btn-primary:hover {
  background: var(--color-primary-dark);
  box-shadow: var(--shadow-md);
  transform: translateY(-1px);
}

.btn-primary:active {
  transform: translateY(0);
}

.btn-primary:disabled {
  background: var(--color-gray-300);
  cursor: not-allowed;
  box-shadow: none;
}
```

**Usage:** Primary actions (Submit, Save, Continue)

**Secondary Button**

```css
.btn-secondary {
  background: var(--color-gray-100);
  color: var(--color-gray-700);
  padding: 0.75rem 1.5rem;
  border-radius: var(--radius-md);
  font-weight: var(--font-weight-medium);
  transition: var(--transition-base);
}

.btn-secondary:hover {
  background: var(--color-gray-200);
}
```

**Usage:** Secondary actions (Cancel, Back)

**Outline Button**

```css
.btn-outline {
  background: transparent;
  color: var(--color-primary);
  border: 1px solid var(--color-primary);
  padding: 0.75rem 1.5rem;
  border-radius: var(--radius-md);
  font-weight: var(--font-weight-medium);
  transition: var(--transition-base);
}

.btn-outline:hover {
  background: var(--color-primary);
  color: white;
}
```

**Usage:** Tertiary actions, alternatives

#### Sizes

- **Small**: padding 0.5rem 1rem, font-size 0.875rem
- **Medium** (default): padding 0.75rem 1.5rem, font-size 1rem
- **Large**: padding 1rem 2rem, font-size 1.125rem

#### Do's

✓ Use primary buttons for main actions (one per section)
✓ Use clear, action-oriented labels ("Save Changes" not "OK")
✓ Include loading states for async actions
✓ Maintain consistent sizing within a section

#### Don'ts

✗ Don't use multiple primary buttons in the same context
✗ Don't use all caps for button text
✗ Don't use buttons for navigation (use links)
✗ Don't skip disabled states

### 4.2 Cards

[Similar detailed format for cards]

### 4.3 Form Elements

[Similar detailed format for inputs, selects, etc.]

### 4.4 Navigation

[Similar detailed format for navigation]

---

## 5. Interaction Patterns

### 5.1 Hover States

- **Buttons**: Background darker, subtle lift (translateY -1px), increased shadow
- **Cards**: Subtle lift (translateY -4px), increased shadow
- **Links**: Color change, underline appears
- **Transition timing**: 150-200ms ease-in-out

### 5.2 Focus States

- **Outline**: 2px solid primary color
- **Offset**: 2px
- **All interactive elements must have visible focus states**

### 5.3 Loading States

- **Buttons**: Show spinner, disable interaction, change text to "Loading..."
- **Cards**: Skeleton screens with pulsing animation
- **Page**: Full-page spinner or progress bar

### 5.4 Error States

- **Color**: Red (error color)
- **Icon**: Warning icon next to message
- **Border**: Red border on invalid fields
- **Message**: Below field, clear explanation

---

## 6. Accessibility Requirements

### Minimum Standards

- ✓ Color contrast: 4.5:1 for normal text, 3:1 for large text
- ✓ Focus indicators: Visible on all interactive elements
- ✓ Keyboard navigation: All functionality accessible via keyboard
- ✓ ARIA labels: Screen reader support for complex widgets
- ✓ Alt text: All images have descriptive alt text

### Best Practices

- Use semantic HTML elements
- Maintain logical heading hierarchy (h1 → h2 → h3)
- Provide skip links for navigation
- Test with screen readers
- Support prefers-reduced-motion for animations

---

## 7. Responsive Design Patterns

### Mobile-First Approach

Design for mobile screens first, then enhance for larger screens.

### Common Patterns

- **Navigation**: Hamburger menu → Full horizontal nav
- **Grid**: 1 column → 2 columns → 3+ columns
- **Typography**: Smaller headings → Larger headings
- **Spacing**: Tighter → More generous

### Breakpoint Strategy

- **Mobile (< 640px)**: Single column, compact spacing
- **Tablet (640-1024px)**: 2-column grids, medium spacing
- **Desktop (1024px+)**: Multi-column, generous spacing

---

## 8. Do's and Don'ts Summary

### Visual Consistency

**Do:**

- ✓ Use design tokens for all values
- ✓ Maintain consistent spacing using the 4px grid
- ✓ Follow the established type scale
- ✓ Use semantic color names

**Don't:**

- ✗ Use arbitrary color values
- ✗ Create one-off spacing values
- ✗ Mix different border radius values without reason
- ✗ Use font sizes outside the scale

### Component Usage

**Do:**

- ✓ Reuse existing components when possible
- ✓ Follow established patterns for new components
- ✓ Include all interaction states
- ✓ Test on multiple screen sizes

**Don't:**

- ✗ Create custom components without checking for existing solutions
- ✗ Skip hover/focus/disabled states
- ✗ Design only for desktop
- ✗ Ignore accessibility requirements

### Implementation

**Do:**

- ✓ Use CSS variables for design tokens
- ✓ Follow mobile-first responsive approach
- ✓ Include transition/animation properties
- ✓ Comment complex layout decisions

**Don't:**

- ✗ Use inline styles
- ✗ Hardcode values that should be tokens
- ✗ Create desktop-only designs
- ✗ Skip browser testing

---

## 9. Implementation Checklist

When creating a new page or component, verify:

- [ ] All colors use defined design tokens
- [ ] Typography follows the type scale
- [ ] Spacing uses the 4px grid system
- [ ] Border radius values are from the design system
- [ ] Shadows are from the defined set
- [ ] Transitions are included on interactive elements
- [ ] Hover states are defined
- [ ] Focus states are visible
- [ ] Disabled states are styled
- [ ] Mobile responsive behavior is defined
- [ ] Accessibility requirements are met
- [ ] Loading states are considered
- [ ] Error states are handled

---

## 10. Code Examples

### Example: Complete Button Implementation

**HTML:**

```html
<button class="btn btn-primary">
  Save Changes
</button>
```

**CSS:**

```css
.btn {
  font-family: var(--font-family-sans);
  font-size: var(--text-base);
  font-weight: var(--font-weight-medium);
  padding: var(--spacing-3) var(--spacing-6);
  border-radius: var(--radius-md);
  border: none;
  cursor: pointer;
  transition: var(--transition-base);
  display: inline-flex;
  align-items: center;
  gap: var(--spacing-2);
}

.btn-primary {
  background-color: var(--color-primary);
  color: white;
  box-shadow: var(--shadow-sm);
}

.btn-primary:hover {
  background-color: var(--color-primary-dark);
  box-shadow: var(--shadow-md);
  transform: translateY(-1px);
}

.btn-primary:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

.btn-primary:active {
  transform: translateY(0);
}

.btn-primary:disabled {
  background-color: var(--color-gray-300);
  cursor: not-allowed;
  box-shadow: none;
}
```

### Example: Complete Card Implementation

[Similar complete example for card]

---

## 11. Next Steps

To implement these guidelines:

1. **Review this document** with the design and development team
2. **Set up design tokens** in your CSS/preprocessor
3. **Create reusable components** based on these guidelines
4. **Update existing components** to align with guidelines (see roadmap below)
5. **Reference this document** for all new development

### Implementation Roadmap

**Phase 1 (Week 1):** Setup

- Set up CSS variables for all design tokens
- Create base utility classes

**Phase 2 (Week 2-3):** Core Components

- Implement button variants
- Implement form elements
- Implement card component

**Phase 3 (Week 4-5):** Complex Components

- Navigation system
- Modal/dialog components
- Data tables

**Phase 4 (Month 2+):** Migration

- Update existing pages to use new components
- Remove legacy CSS
- Performance optimization

---

## Appendix: Design Token Reference

Quick reference table of all design tokens:

| Category | Token Name | Value | Usage |
|----------|-----------|-------|-------|
| Color | --color-primary | #3b82f6 | Primary actions |
| Color | --color-secondary | #8b5cf6 | Secondary actions |
[...continue with all tokens...]

---

**Document Metadata:**

- Generated by: study-design skill
- Source: [Visual references / CSS analysis / Synthesis]
- Reviewed by: [Names]
- Approved by: [Names]
- Last updated: [Date]
- Version: 1.0

```

## Usage Notes

### When to Create This Document

This comprehensive guideline document should be created as the **final output** after completing:
1. Visual/text analysis (if available)
2. CSS analysis (if available)
3. Synthesis of both (if both available)

### Customization Notes

- **Include only relevant sections** - If the project doesn't use cards, omit that section
- **Adjust detail level** - For simple projects, condense; for complex systems, expand
- **Add project-specific sections** - Include special components unique to the project
- **Update version** - Increment version number when guidelines are updated

### File Naming Convention

Suggested naming: `[project-name]-ui-ux-guidelines.md`

Examples:
- `acme-ecommerce-ui-ux-guidelines.md`
- `dashboard-design-guidelines.md`
- `mobile-app-ui-guidelines.md`

---
name: preview-to-code
description: Guide for converting approved HTML/CSS previews into production-ready code with specific technology stacks (React, Vue, Tailwind, etc.). Use when transforming validated UI previews into framework components, ensuring DKB mappings are preserved and code integrates with existing conventions. Supports multiple frameworks and styling approaches.
---

# Preview to Code Skill

This skill guides the process of converting approved HTML/CSS previews into production-ready code that integrates with your technology stack. All DKB mappings are preserved to ensure consistency and maintainability.

## Purpose

- Convert approved previews into implementation-ready code
- Preserve DKB mappings (tokens, components) in production code
- Support multiple frameworks (React, Vue, Angular, Svelte, etc.)
- Support multiple styling approaches (Tailwind, CSS Modules, Styled Components, etc.)
- Ensure code follows engineering conventions and best practices

## When to Use This Skill

- Converting approved HTML/CSS previews into React/Vue/Angular components
- Implementing production-ready UI from validated designs
- Migrating preview code to specific framework syntax
- Integrating token-driven styling into component libraries
- Setting up new UI features with proper architecture

## Prerequisites

You must have:
1. An approved HTML/CSS preview (from `wireframe-to-preview` skill)
2. A Design Knowledge Base (DKB) with token and component mappings
3. Defined engineering constraints (framework, styling approach, linting rules)

## Inputs

### Required
- **Approved preview**: HTML/CSS from Stage 2 that passed stakeholder review
- **Design Knowledge Base (DKB)**: Tokens, component mappings, accessibility/responsive rules
- **Technology stack**: Target framework and styling approach

### Optional
- **Engineering constraints**: Linting rules (ESLint, Prettier), build tooling (Vite, Webpack)
- **Performance budgets**: File size limits, lighthouse score targets
- **Existing codebase**: To match naming conventions and architecture patterns

## Outputs

### 1. Production-Ready UI Implementation
Code in your chosen framework:
- **React**: JSX components with TypeScript
- **Vue**: SFC (Single File Components)
- **Angular**: Components with templates
- **Svelte**: Svelte components
- **Plain HTML/CSS/JS**: Vanilla implementation

### 2. Token Artifacts (when required)
- CSS variables file
- Theme configuration (Tailwind config, MUI theme, etc.)
- Design token JavaScript/TypeScript objects

### 3. Component Structure
- Reusable components matching DKB catalog
- Proper component composition
- State management setup (if needed)

### 4. Optional Outputs
- Release notes describing token/component changes
- Documentation for new components
- Storybook stories or component examples

## Process

### Step 1: Normalize Structure

**Semantic HTML Review**
- Ensure semantic elements are used (`header`, `main`, `nav`, `button`, `label`)
- Replace `<div>` with semantic alternatives where appropriate
- Verify heading hierarchy (H1 → H2 → H3, no skips)

**Accessibility Attributes**
- Add ARIA only when necessary (don't over-ARIA)
- Ensure `alt` text for images
- Add `aria-label` for icon-only buttons
- Verify form labels are properly associated
- Add `role` attributes only when semantic HTML isn't sufficient

**Structure Validation**
- Check nesting is valid for target framework
- Ensure no invalid HTML structures
- Validate that structure supports responsive behavior

### Step 2: Bind Styling Through the DKB

**Replace Hard-Coded Values**
- Find any remaining hard-coded colors/sizes/shadows
- Replace with token references
- Document any values that don't have tokens (propose new tokens)

**Choose Styling Approach**

Based on your stack, implement one of these approaches:

**A. CSS Variables (Vanilla/Framework-agnostic)**
```css
.button-primary {
  background-color: var(--color-primary);
  padding: var(--space-3) var(--space-6);
  border-radius: var(--radius-md);
}
```

**B. Tailwind CSS**
```jsx
<button className="bg-primary px-6 py-3 rounded-md">
  Click me
</button>
```
Generate `tailwind.config.js` from DKB tokens.

**C. CSS Modules**
```jsx
import styles from './Button.module.css';
<button className={styles.primary}>Click me</button>
```

**D. Styled Components (React)**
```jsx
const Button = styled.button`
  background-color: ${props => props.theme.colors.primary};
  padding: ${props => props.theme.spacing[3]};
`;
```

**E. CSS-in-JS (Emotion, MUI)**
```jsx
const buttonStyles = {
  backgroundColor: theme.palette.primary.main,
  padding: theme.spacing(3, 6),
};
```

### Step 3: Convert to Target Framework

**React Conversion**
```jsx
// From preview HTML
<div class="card-elevated">
  <h3 class="card-title">Title</h3>
  <p class="card-body">Body text</p>
  <button class="button-primary">Action</button>
</div>

// To React component
interface CardProps {
  title: string;
  body: string;
  onAction: () => void;
}

export function Card({ title, body, onAction }: CardProps) {
  return (
    <div className="card-elevated">
      <h3 className="card-title">{title}</h3>
      <p className="card-body">{body}</p>
      <button className="button-primary" onClick={onAction}>
        Action
      </button>
    </div>
  );
}
```

**Vue Conversion**
```vue
<!-- Card.vue -->
<template>
  <div class="card-elevated">
    <h3 class="card-title">{{ title }}</h3>
    <p class="card-body">{{ body }}</p>
    <button class="button-primary" @click="onAction">
      Action
    </button>
  </div>
</template>

<script setup lang="ts">
interface Props {
  title: string;
  body: string;
}

defineProps<Props>();
const emit = defineEmits<{ action: [] }>();
const onAction = () => emit('action');
</script>
```

**Component Extraction Guidelines**
- Extract reusable components where it matches existing architecture
- Keep component granularity consistent with codebase
- Don't over-componentize (balance reusability with complexity)
- Follow single responsibility principle

### Step 4: Verify Accessibility and Responsiveness

**Focus Order**
- Verify tab order is logical
- Test keyboard navigation
- Ensure focus trap works in modals

**Focus Visibility**
- Implement focus indicators per DKB rules
- Test focus styles are visible on all backgrounds
- Use `:focus-visible` for better UX

**Contrast**
- Run contrast checks on token pairs
- Ensure WCAG AA or AAA compliance (per DKB requirements)
- Test with color blindness simulators

**Touch Targets**
- Verify minimum 44×44px hit areas on mobile
- Add padding if needed for smaller visual elements

**Responsive Behavior**
- Test at all DKB breakpoints
- Verify layout shifts work correctly
- Test on real devices when possible

**Screen Reader Testing**
- Test with screen readers (VoiceOver, NVDA, JAWS)
- Verify announcements are clear and helpful
- Check ARIA labels are accurate

### Step 5: Build and Smoke Test

**Build Process**
- Ensure code compiles without errors
- Fix any TypeScript errors
- Resolve linting issues (ESLint, Prettier)

**Runtime Testing**
- Verify component renders without errors
- Test interactive functionality
- Check console for warnings/errors

**Visual Regression**
- Compare with approved preview
- Ensure 1:1 visual parity (within framework rendering differences)
- Screenshot test if available

**Performance Check**
- Verify bundle size is reasonable
- Check for unnecessary re-renders (React DevTools)
- Test Lighthouse scores if applicable

## Quality Checklist

Before delivering production code, verify:

- [ ] No "invented" CSS values (all styles from tokens/DKB rules)
- [ ] Output matches approved preview within expected differences
- [ ] Code compiles without errors
- [ ] Linting passes (ESLint, Prettier, etc.)
- [ ] TypeScript types are correct (if using TS)
- [ ] Semantic HTML is used appropriately
- [ ] ARIA is used only when necessary
- [ ] Focus order is logical
- [ ] Focus visibility meets standards
- [ ] Contrast ratios meet WCAG requirements
- [ ] Touch targets meet minimum sizes
- [ ] Responsive behavior works at all breakpoints
- [ ] Code follows existing codebase conventions
- [ ] Component naming matches DKB conventions
- [ ] Token usage is consistent
- [ ] No console errors or warnings

## Framework-Specific Guidelines

### React

**Component Structure**
```tsx
// components/Button/Button.tsx
import React from 'react';
import styles from './Button.module.css';

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
}

export function Button({ 
  variant = 'primary', 
  size = 'md',
  children,
  ...props 
}: ButtonProps) {
  return (
    <button 
      className={`${styles.button} ${styles[variant]} ${styles[size]}`}
      {...props}
    >
      {children}
    </button>
  );
}
```

**Token Usage with CSS Modules**
```css
/* Button.module.css */
.button {
  padding: var(--space-3) var(--space-6);
  border-radius: var(--radius-md);
  font-family: var(--font-family-base);
  font-weight: var(--font-weight-semibold);
}

.primary {
  background-color: var(--color-primary);
  color: var(--color-text-inverse);
}
```

### Vue

**Component Structure**
```vue
<!-- Button.vue -->
<template>
  <button 
    :class="['button', variant, size]"
    v-bind="$attrs"
  >
    <slot />
  </button>
</template>

<script setup lang="ts">
interface Props {
  variant?: 'primary' | 'secondary' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
}

withDefaults(defineProps<Props>(), {
  variant: 'primary',
  size: 'md'
});
</script>

<style scoped>
.button {
  padding: var(--space-3) var(--space-6);
  border-radius: var(--radius-md);
}

.primary {
  background-color: var(--color-primary);
  color: var(--color-text-inverse);
}
</style>
```

### Tailwind CSS

**Config Generation**
```javascript
// tailwind.config.js (generated from DKB)
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: 'var(--color-primary)',
        'text-primary': 'var(--color-text-primary)',
      },
      spacing: {
        '1': 'var(--space-1)',
        '2': 'var(--space-2)',
        '3': 'var(--space-3)',
      },
      borderRadius: {
        'sm': 'var(--radius-sm)',
        'md': 'var(--radius-md)',
        'lg': 'var(--radius-lg)',
      },
    },
  },
};
```

## Scripts and Tools

### Preview to React Converter

Use `scripts/convert_to_react.py` to automatically convert HTML preview to React components.

```bash
python scripts/convert_to_react.py preview/index.html --output src/components/
```

### Token to Tailwind Config

Use `scripts/dkb_to_tailwind.py` to generate Tailwind config from DKB tokens.

```bash
python scripts/dkb_to_tailwind.py dkb/tokens/ --output tailwind.config.js
```

### Token to CSS Variables

Use `scripts/tokens_to_css.py` to generate CSS variables file from DKB.

```bash
python scripts/tokens_to_css.py dkb/tokens/ --output src/styles/tokens.css
```

## Common Pitfalls to Avoid

- **Inventing new values**: Always use DKB tokens, even if it means proposing new ones
- **Inconsistent naming**: Match existing codebase conventions exactly
- **Over-componentizing**: Balance reusability with complexity
- **Ignoring accessibility**: Don't skip focus states, ARIA, or keyboard navigation
- **Framework-specific anti-patterns**: Follow framework best practices
- **Performance issues**: Watch for unnecessary re-renders, large bundles

## Next Steps

After generating production code:

1. **Code review**: Get team approval
2. **Integration testing**: Test with existing features
3. **Documentation**: Update component library docs
4. **Deploy**: Merge to main branch
5. **Monitor**: Check for bugs or performance issues

## References

For detailed implementation guides:
- [React implementation guide](references/react-guide.md)
- [Vue implementation guide](references/vue-guide.md)
- [Tailwind integration guide](references/tailwind-guide.md)
- [Code conversion guide](references/code-conversion-guide.md)
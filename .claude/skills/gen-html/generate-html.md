# Sub-Skill: Component-First HTML Generation with Separate Styling

## Objective

Master a component-first approach to HTML generation where structure is built and organized before styling, with CSS extraction and application managed in separate, organized stylesheets.

## Philosophy: Structure First, Style Second

This approach prioritizes:

1. **Clean, semantic HTML** that works without styling
2. **Component isolation** for testing and reusability
3. **Organized, maintainable CSS** in separate files
4. **Progressive enhancement** from structure to presentation

## Step 1: HTML Component Generation Workflow

### Phase 1: Create Base HTML Structure

#### 1.1 Build Skeleton Structure First

Start with the simplest possible HTML structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Title</title>
</head>
<body>
    <!-- Components will be added here -->
</body>
</html>
```

#### 1.2 Add Semantic Landmarks

Define major page sections using HTML5 semantic elements:

```html
<body>
    <header>
        <!-- Header content -->
    </header>
    
    <nav>
        <!-- Navigation content -->
    </nav>
    
    <main>
        <!-- Main content -->
    </main>
    
    <aside>
        <!-- Sidebar content (if applicable) -->
    </aside>
    
    <footer>
        <!-- Footer content -->
    </footer>
</body>
```

### Phase 2: Component-by-Component HTML Construction

#### 2.1 Start with Atomic Components (Atoms)

Build the smallest, most reusable components first:

**Example: Button Component**

```html
<!-- Button: Primary -->
<button class="btn btn-primary" type="button">
    Click Me
</button>

<!-- Button: Secondary -->
<button class="btn btn-secondary" type="button">
    Cancel
</button>

<!-- Button: With Icon -->
<button class="btn btn-primary btn-icon" type="button">
    <span class="icon icon-plus"></span>
    <span>Add Item</span>
</button>
```

**Testing Checkpoint**: Verify HTML is semantic and accessible

- Can you understand the element's purpose from HTML alone?
- Are ARIA attributes needed and present?
- Is keyboard navigation logical?

#### 2.2 Build Molecular Components

Combine atoms into functional groups:

**Example: Search Bar Component**

```html
<!-- Search Bar -->
<div class="search-bar">
    <label for="search-input" class="sr-only">Search</label>
    <input 
        type="search" 
        id="search-input"
        class="search-bar__input"
        placeholder="Search..."
        aria-label="Search content"
    >
    <button type="submit" class="search-bar__button btn btn-primary">
        <span class="icon icon-search"></span>
        <span class="sr-only">Search</span>
    </button>
</div>
```

**Testing Checkpoint**: Verify component structure

- Is the component self-contained?
- Are child elements properly nested?
- Are class names consistent and semantic?

#### 2.3 Construct Organism Components

Build complex sections from molecules and atoms:

**Example: Navigation Bar**

```html
<!-- Navigation Bar -->
<nav class="navbar" role="navigation" aria-label="Main navigation">
    <div class="navbar__container">
        <!-- Logo -->
        <div class="navbar__logo">
            <a href="/" aria-label="Home">
                <img src="logo.svg" alt="Company Logo" class="logo">
            </a>
        </div>
        
        <!-- Navigation Menu -->
        <ul class="navbar__menu">
            <li class="navbar__item">
                <a href="#home" class="navbar__link">Home</a>
            </li>
            <li class="navbar__item">
                <a href="#about" class="navbar__link">About</a>
            </li>
            <li class="navbar__item">
                <a href="#services" class="navbar__link">Services</a>
            </li>
            <li class="navbar__item">
                <a href="#contact" class="navbar__link">Contact</a>
            </li>
        </ul>
        
        <!-- User Actions -->
        <div class="navbar__actions">
            <button class="btn btn-secondary">Sign In</button>
            <button class="btn btn-primary">Sign Up</button>
        </div>
    </div>
</nav>
```

**Testing Checkpoint**: Verify organism integrity

- Does the component work as a cohesive unit?
- Are all child components properly integrated?
- Is the hierarchy clear and logical?

### Phase 3: Layout Integration & Organization

#### 3.1 Assemble Components into Sections

Group related components within semantic containers:

```html
<main>
    <!-- Hero Section -->
    <section class="hero">
        <div class="hero__container">
            <div class="hero__content">
                <h1 class="hero__title">Welcome to Our Service</h1>
                <p class="hero__description">
                    Transform your business with our innovative solutions
                </p>
                <div class="hero__actions">
                    <button class="btn btn-primary btn-large">Get Started</button>
                    <button class="btn btn-secondary btn-large">Learn More</button>
                </div>
            </div>
            <div class="hero__image">
                <img src="hero.jpg" alt="Hero illustration">
            </div>
        </div>
    </section>
    
    <!-- Features Section -->
    <section class="features">
        <div class="features__container">
            <h2 class="features__title">Our Features</h2>
            
            <div class="features__grid">
                <!-- Feature cards will go here -->
            </div>
        </div>
    </section>
</main>
```

#### 3.2 Add Layout Helper Elements

Include containers, wrappers, and grid structures:

```html
<!-- Container Pattern -->
<div class="container">
    <!-- Content constrained to max-width -->
</div>

<!-- Grid Pattern -->
<div class="grid grid-cols-3">
    <div class="grid__item">Item 1</div>
    <div class="grid__item">Item 2</div>
    <div class="grid__item">Item 3</div>
</div>

<!-- Flex Pattern -->
<div class="flex flex-space-between flex-align-center">
    <div>Left content</div>
    <div>Right content</div>
</div>
```

### Phase 4: Content Population

#### 4.1 Add Realistic Content

Replace placeholder text with actual or realistic content:

```html
<!-- Before (Placeholder) -->
<h1>Title</h1>
<p>Description text</p>

<!-- After (Realistic) -->
<h1>Enterprise Cloud Solutions for Modern Businesses</h1>
<p>
    Scale your infrastructure with confidence using our 
    enterprise-grade cloud platform, trusted by over 10,000 
    companies worldwide.
</p>
```

#### 4.2 Verify Content Hierarchy

Ensure proper heading structure and semantic correctness:

```html
<article class="blog-post">
    <header class="blog-post__header">
        <h1>Main Article Title</h1> <!-- Only one h1 per page -->
        <p class="blog-post__meta">Published on Jan 13, 2026</p>
    </header>
    
    <div class="blog-post__content">
        <h2>First Section</h2>
        <p>Content...</p>
        
        <h3>Subsection</h3>
        <p>Content...</p>
        
        <h2>Second Section</h2>
        <p>Content...</p>
    </div>
</article>
```

## Step 2: CSS Extraction & Application Strategy

### CRITICAL: UI/UX Guidelines Compliance

**Before extracting or writing any CSS, if UI/UX design guidelines are provided, YOU MUST:**

1. **Read the guidelines document thoroughly**
2. **Extract and document all design tokens**:
   - Color palette (exact hex codes and their usage)
   - Typography scale (font families, sizes, weights, line heights)
   - Spacing system (grid base unit, common gaps)
   - Border radius values
   - Component-specific specifications
   - Interaction patterns and states
3. **Note all Do's and Don'ts**
4. **Follow guidelines specifications exactly** - no deviations

### Guidelines Checklist

Before proceeding with CSS extraction, verify you have documented:
- [ ] Complete color palette with hex codes and usage rules
- [ ] Typography specifications (font family, fallbacks, sizes, weights, line heights)
- [ ] Spacing/grid system (base unit, common values)
- [ ] Border radius specifications
- [ ] Component-specific styles and patterns
- [ ] Interactive state specifications (hover, active, focus, disabled)
- [ ] Restrictions (Don'ts) from guidelines

---

### Phase 1: Create CSS File Structure

#### Organize CSS by Purpose

```
styles/
├── base/
│   ├── reset.css         # CSS reset/normalize
│   ├── variables.css     # CSS custom properties
│   └── typography.css    # Global typography
├── layout/
│   ├── grid.css          # Grid system
│   ├── containers.css    # Container utilities
│   └── spacing.css       # Margin/padding utilities
├── components/
│   ├── buttons.css       # Button styles
│   ├── navbar.css        # Navigation bar
│   ├── cards.css         # Card components
│   ├── hero.css          # Hero section
│   └── forms.css         # Form elements
└── main.css              # Import all stylesheets
```

### Phase 2: Extract Component Styles from Source CSS

#### 2.1 For Each HTML Component, Search Source CSS

**Example: Extracting Button Styles**

1. **Identify Class Names from HTML**

   ```
   Classes to search:
   - .btn
   - .btn-primary
   - .btn-secondary
   - .btn-large
   - .btn-icon
   ```

2. **Search Original CSS File**

   ```
   Search for: "\.btn"
   Search for: "button"
   Search for: ":hover" (in button context)
   ```

3. **Extract All Related Rules**

   ```css
   /* Found in original CSS - Lines 450-520 */
   .btn { /* base styles */ }
   .btn-primary { /* variant */ }
   .btn:hover { /* state */ }
   ```

4. **Copy to Component CSS File** (`components/buttons.css`)

   **IMPORTANT: Validate Against Guidelines First**
   
   Before writing CSS, cross-check with UI/UX guidelines:
   - Are these colors in the approved palette?
   - Does typography match guideline specifications?
   - Does spacing follow the grid system?
   - Are border radius values correct per guidelines?
   - Do hover states match guideline patterns?

   ```css
   /* ============================================
      COMPONENT: Buttons
      SOURCE: Extracted from original CSS and validated against guidelines
      GUIDELINES REFERENCE: [Link to guidelines section, e.g., Section 3.1]
      ============================================ */
   
   /* Base Button - Following guideline specifications */
   .btn {
       display: inline-flex;
       align-items: center;
       justify-content: center;
       
       /* Spacing - must be multiples of 8px (grid system) */
       padding: 16px 24px; /* 16px and 24px are valid */
       
       /* Typography - from guidelines */
       font-family: 'ABC Diatype', sans-serif; /* Primary font family */
       font-size: 16px; /* Body Bold size */
       font-weight: 700; /* Bold weight */
       line-height: 20px; /* 1.25 ratio */
       
       /* Visual */
       text-decoration: none;
       border: none;
       border-radius: 0px; /* Sharp corners per guidelines */
       cursor: pointer;
       
       /* Animation */
       transition: all 0.2s ease-in-out;
   }
   
   /* Button Variants - Using approved color palette */
   .btn-primary {
       background-color: #0D0D0D; /* Black/900 - Primary brand color */
       color: #FFFFFF; /* White */
   }
   
   .btn-secondary {
       background-color: #E3E3E3; /* Black/100 - Subtle variant */
       color: #0D0D0D; /* Black text */
   }
   
   /* Button Sizes - Maintaining 8px grid */
   .btn-large {
       padding: 24px 32px; /* Both multiples of 8 */
       font-size: 20px; /* H4 size from guidelines */
       line-height: 24px;
   }
   
   /* Button States - Following guideline patterns */
   .btn:hover {
       opacity: 0.8; /* Guideline-specified hover: opacity reduction */
       /* NOT using transform or box-shadow - guidelines say no soft shadows */
   }
   
   .btn:active {
       opacity: 0.9;
   }
   
   .btn:disabled {
       opacity: 0.5;
       cursor: not-allowed;
       pointer-events: none;
   }
   
   /* Button with Icon */
   .btn-icon {
       display: inline-flex;
       gap: 8px; /* 8px base unit */
   }
   
   .btn-icon .icon {
       width: 24px; /* Multiple of 8 */
       height: 24px;
   }
   ```

   **Validation Notes:**
   - ✅ Colors match approved palette (#0D0D0D, #FFFFFF, #E3E3E3)
   - ✅ Typography uses 'ABC Diatype' with correct sizes and weights
   - ✅ All spacing values are multiples of 8px
   - ✅ Border radius is 0px (sharp corners as required)
   - ✅ Hover uses opacity reduction (not shadows or transforms)
   - ✅ No soft shadows used (per guidelines Don'ts)

### Phase 3: Build Component CSS Files

#### Template for Component CSS Files

**NOTE: All values must be validated against UI/UX guidelines before implementation**

```css
/* ============================================
   COMPONENT: [Component Name]
   Description: [Brief purpose description]
   Dependencies: [List CSS variables or other files needed]
   Guidelines Reference: [Link to specific guideline section]
   ============================================ */

/* --------------------------------------------
   Base Styles
   -------------------------------------------- */
.component {
    /* Positioning */
    
    /* Box Model */
    /* NOTE: Ensure all spacing uses approved grid system values */
    
    /* Typography */
    /* NOTE: Use approved font families, sizes, weights, line heights */
    
    /* Visual */
    /* NOTE: Use only approved colors from palette */
    /* NOTE: Follow approved border-radius specifications */
    
    /* Misc */
}

/* --------------------------------------------
   Variants & Modifiers
   -------------------------------------------- */
.component--variant {
    /* Override styles - validate colors and spacing */
}

/* --------------------------------------------
   Child Elements (BEM)
   -------------------------------------------- */
.component__element {
    /* Element styles - maintain guideline compliance */
}

/* --------------------------------------------
   States
   -------------------------------------------- */
.component:hover,
.component:focus {
    /* Interactive states - follow guideline patterns */
}

.component.is-active,
.component--active {
    /* Active state - use approved colors */
}

/* --------------------------------------------
   Responsive Styles
   -------------------------------------------- */
@media (max-width: 768px) {
    .component {
        /* Mobile adaptations - maintain grid system */
    }
}

@media (min-width: 769px) and (max-width: 1024px) {
    .component {
        /* Tablet adaptations */
    }
}

@media (min-width: 1025px) {
    .component {
        /* Desktop styles */
    }
}
```

### Phase 4: Link CSS to HTML

#### 4.1 Create Main CSS Import File

```css
/* main.css */

/* Base Styles */
@import url('base/reset.css');
@import url('base/variables.css');
@import url('base/typography.css');

/* Layout */
@import url('layout/grid.css');
@import url('layout/containers.css');
@import url('layout/spacing.css');

/* Components (Order by page hierarchy) */
@import url('components/navbar.css');
@import url('components/hero.css');
@import url('components/buttons.css');
@import url('components/cards.css');
@import url('components/forms.css');
```

#### 4.2 Link in HTML

```html
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Title</title>
    
    <!-- Main Stylesheet -->
    <link rel="stylesheet" href="styles/main.css">
    
    <!-- Or individual components for testing -->
    <!-- <link rel="stylesheet" href="styles/components/buttons.css"> -->
</head>
```

## Step 3: Progressive Enhancement & Testing

### Testing Workflow

#### Level 1: HTML-Only Test

1. View page with CSS disabled
2. Verify content is readable and logical
3. Check that hierarchy makes sense
4. Test keyboard navigation

#### Level 2: Component Isolation Test

1. Create test HTML file with just one component
2. Link only that component's CSS
3. Verify styles apply correctly
4. Test responsive behavior
5. Test interactive states

**Example: Button Test Page**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Button Component Test</title>
    <link rel="stylesheet" href="styles/base/variables.css">
    <link rel="stylesheet" href="styles/components/buttons.css">
</head>
<body style="padding: 2rem;">
    <h1>Button Component Tests</h1>
    
    <section>
        <h2>Button Variants</h2>
        <button class="btn btn-primary">Primary</button>
        <button class="btn btn-secondary">Secondary</button>
    </section>
    
    <section>
        <h2>Button Sizes</h2>
        <button class="btn btn-primary btn-large">Large</button>
        <button class="btn btn-primary">Default</button>
    </section>
    
    <section>
        <h2>Button States</h2>
        <button class="btn btn-primary">Hover Me</button>
        <button class="btn btn-primary" disabled>Disabled</button>
    </section>
</body>
</html>
```

#### Level 3: Full Integration Test

1. Load complete page with all CSS
2. Verify no conflicts between components
3. Test responsive breakpoints
4. Validate with W3C validator
5. Check accessibility with axe or WAVE

## Step 4: Documentation & Handoff

### Component Documentation Template

```markdown
# Component: [Name]

## HTML Structure
\`\`\`html
<!-- Paste component HTML -->
\`\`\`

## CSS File
- **Location**: `styles/components/[name].css`
- **Lines**: [X-Y]
- **Dependencies**: 
  - `base/variables.css` (CSS custom properties)
  - `layout/grid.css` (grid utilities)

## Guidelines Compliance
- ✅ **Colors**: All colors from approved palette
  - Primary: #0D0D0D (Black/900)
  - Background: #FFFFFF (White)
- ✅ **Typography**: 'ABC Diatype', 16px/20px, weight 700
- ✅ **Spacing**: All values are multiples of 8px (16px, 24px)
- ✅ **Border Radius**: 0px (sharp corners per guidelines)
- ✅ **Hover State**: Opacity reduction to 0.8
- ⚠️ **Deviations**: [List any deviations with justification, or "None"]

## Available Variants
- `.component--variant-name`: Description
- `.component--another-variant`: Description

## Usage Examples
\`\`\`html
<!-- Example 1 -->
<!-- Example 2 -->
\`\`\`

## Responsive Behavior
- **Mobile** (<768px): [Description]
- **Tablet** (768-1024px): [Description]
- **Desktop** (>1024px): [Description]

## Accessibility Notes
- ARIA attributes used: [List]
- Keyboard interactions: [Description]
- Screen reader considerations: [Notes]

## Browser Support
- Chrome: ✓
- Firefox: ✓
- Safari: ✓
- Edge: ✓

## Known Issues
- [Issue 1]
- [Issue 2]
```

## Best Practices Summary

### HTML Generation

- ✅ Start with semantic structure, add classes later
- ✅ Build small components before large sections
- ✅ Test each component in isolation
- ✅ Use consistent naming conventions (BEM recommended)
- ✅ Include accessibility attributes from the start
- ✅ Keep component HTML self-contained and portable

### CSS Organization

- ✅ One component per CSS file
- ✅ Group related styles with comments
- ✅ Extract CSS variables for reusable values
- ✅ Maintain logical property ordering
- ✅ Document dependencies and usage
- ✅ Test styles in isolation before integration

### UI/UX Guidelines Compliance (CRITICAL)

- ✅ **ALWAYS read guidelines document first** before writing any CSS
- ✅ **Use ONLY approved colors** from the guidelines palette
- ✅ **Follow typography specifications exactly** (font family, size, weight, line height)
- ✅ **Respect the spacing/grid system** (e.g., all values must be multiples of 8px)
- ✅ **Apply correct border radius values** as specified in guidelines
- ✅ **Follow interaction patterns** (hover, active, focus states as specified)
- ✅ **Adhere to Do's and Don'ts** - never violate guidelines restrictions
- ✅ **Validate every CSS property** against guidelines before implementation
- ✅ **Document compliance** - note which guideline rules were applied
- ✅ **Flag deviations** - if you must deviate, document why and get approval

### Workflow

- ✅ Structure first, style second
- ✅ Component-by-component, not page-by-page
- ✅ Bottom-up approach (atoms → molecules → organisms)
- ✅ **Guidelines validation at each phase**
- ✅ Progressive testing at each phase
- ✅ Regular validation and accessibility checks
- ✅ Comprehensive documentation throughout

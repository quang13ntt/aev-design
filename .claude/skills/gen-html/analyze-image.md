# Sub-Skill: Analyzing Design Images & Component Decomposition

## Objective

Master the systematic analysis of design references (screenshots, mockups, wireframes) to identify, categorize, and decompose UI components for HTML implementation.

## Step 1: Initial Design Assessment

### Overall Layout Analysis

- **Page Type Identification**: Determine the page type (landing page, dashboard, form, article, etc.)
- **Layout System**: Identify the layout approach (grid-based, flex-based, fixed-width, fluid)
- **Viewport Sections**: Divide the design into major viewport sections:
  - Above-the-fold content
  - Scrollable content areas
  - Fixed/sticky elements (headers, footers, sidebars)
- **Responsive Breakpoints**: Note any visible responsive behaviors or design variations

### Visual Hierarchy Mapping

- Identify primary, secondary, and tertiary visual elements
- Note z-index relationships (overlays, modals, dropdowns)
- Document visual flow and user's eye path through the design

## Step 2: Component Identification & Categorization

### Atomic Design Breakdown

**Level 1: Atoms (Smallest UI Elements)**

- Buttons (primary, secondary, tertiary, icon buttons)
- Input fields (text, email, password, search)
- Labels and text elements
- Icons and badges
- Checkboxes and radio buttons
- Links and anchors
- Images and avatars
- Separators and dividers

**Level 2: Molecules (Simple Component Groups)**

- Form fields with labels
- Search bars with icons
- Card headers with titles and actions
- Navigation items with icons
- List items with multiple elements
- Tag groups or chip collections
- Social media icon groups

**Level 3: Organisms (Complex UI Sections)**

- Navigation bars (with logo, menu, actions)
- Hero sections (heading, description, CTA)
- Cards (with image, title, description, actions)
- Forms (multiple fields, validation, submission)
- Footers (links, social media, copyright)
- Sidebars (navigation, filters, widgets)
- Modal dialogs and popups

**Level 4: Templates/Sections (Page Layouts)**

- Header section (full navigation structure)
- Content grid/list sections
- Feature sections
- Testimonial/review sections
- Pricing tables
- FAQ sections

### Component Inventory Checklist

For each identified component, document:

- **Component Name**: Descriptive, semantic name
- **Component Type**: Atom/Molecule/Organism
- **Instance Count**: How many times it appears
- **Variations**: Different states or styles (e.g., button-primary, button-secondary)
- **Content Type**: Static, dynamic, or user-generated
- **Interactivity**: Clickable, hoverable, animated, form-input
- **Dependencies**: Related or nested components

## Step 3: Page Decomposition Strategy

### Top-Down Approach

```
Page
├── Header
│   ├── Logo
│   ├── Navigation
│   │   ├── Nav Item 1
│   │   ├── Nav Item 2
│   │   └── Nav Item 3
│   └── User Actions (Login/Profile)
├── Main Content
│   ├── Hero Section
│   │   ├── Heading
│   │   ├── Description
│   │   └── CTA Button
│   ├── Feature Section
│   │   ├── Feature Card 1
│   │   ├── Feature Card 2
│   │   └── Feature Card 3
│   └── Content Section
└── Footer
    ├── Footer Links
    ├── Social Media
    └── Copyright
```

### Systematic Decomposition Process

1. **Divide Vertically**: Split the page into horizontal sections
   - Identify major sections from top to bottom
   - Name each section based on its purpose

2. **Divide Horizontally**: Within each section, identify columns or side-by-side elements
   - Look for multi-column layouts
   - Identify grid patterns (2-column, 3-column, 4-column, etc.)

3. **Extract Repeating Patterns**: Identify reusable components
   - Look for repeated visual patterns (cards, list items, buttons)
   - Group similar elements into component families

4. **Isolate Unique Elements**: Identify one-off or special components
   - Hero sections with unique styling
   - Special CTAs or promotional banners
   - Custom interactive elements

## Step 4: Visual Properties Documentation

### For Each Component, Document

**Layout Properties**

- Width and height (fixed, percentage, auto)
- Positioning (static, relative, absolute, fixed, sticky)
- Margin and padding values
- Display type (block, inline, flex, grid)

**Visual Styling**

- Background colors or gradients
- Border styles, widths, and colors
- Border radius for rounded corners
- Box shadows or elevation effects
- Text alignment and decoration

**Typography**

- Font family and fallbacks
- Font size and line height
- Font weight (light, regular, medium, bold)
- Text color and opacity
- Letter spacing and text transform

**Imagery**

- Image dimensions and aspect ratios
- Image treatment (overlay, filters, effects)
- Icon sizes and colors
- Background images or patterns

**Interactive States**

- Default state appearance
- Hover effects (color changes, shadows, transforms)
- Active/pressed states
- Focused states for accessibility
- Disabled states

## Step 5: Component Relationship Mapping

### Parent-Child Relationships

- Document nesting hierarchy
- Identify container-content relationships
- Note flex/grid parent-child patterns

### Sibling Relationships

- Elements at the same hierarchy level
- Grouped elements that should be treated together
- Consistent spacing between siblings

### Compositional Patterns

- Components that always appear together
- Optional vs. required child elements
- Variable vs. fixed number of children

## Step 6: Responsive & Adaptive Behaviors

### Identify Responsive Patterns

- Components that hide/show at different breakpoints
- Layout changes (column stacking, reordering)
- Font size adjustments
- Image cropping or swapping
- Navigation transformations (desktop menu → mobile hamburger)

### Document Breakpoint Behaviors

- Mobile (< 768px): Component behavior
- Tablet (768px - 1024px): Component behavior
- Desktop (> 1024px): Component behavior

## Output: Component Analysis Document

Create a structured document with:

```markdown
# Component Analysis for [Page Name]

## Page Structure
- Layout Type: [Grid/Flex/Hybrid]
- Total Sections: [Number]
- Main Components: [List]

## Component Inventory

### Header Components
1. **Logo**
   - Type: Atom
   - Size: 150px x 40px
   - Position: Top-left, fixed
   
2. **Navigation Menu**
   - Type: Organism
   - Items: 5 nav links
   - States: Default, hover, active
   
[Continue for all components...]

## Component Hierarchy
[Tree structure or diagram]

## Responsive Breakpoints
- Mobile: [Changes]
- Tablet: [Changes]
- Desktop: [Changes]

## Reusable Components (Priority Order)
1. Button component (3 variants)
2. Card component (2 variants)
3. Form field component
[...]
```

## Best Practices

- **Start Broad, Then Narrow**: Begin with major sections, then drill into details
- **Name Components Semantically**: Use descriptive names that reflect purpose, not appearance
- **Document Consistently**: Use the same format for all component descriptions
- **Think Reusability**: Identify patterns that can be abstracted into reusable components
- **Consider Accessibility**: Note ARIA requirements, heading hierarchy, focus order
- **Validate Understanding**: Cross-reference with existing design systems or style guides

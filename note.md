# Note

## Wireframe to Design Workflow

Description:

- This workflow defines how the system transforms a low‑fidelity wireframe into a high‑fidelity visual design that aligns with the product’s established design system and frontend implementation standards.
- The process integrates UI/UX analysis, design system modeling, and automated code generation, enabling consistent, scalable, and repeatable design outputs across teams.

The workflow includes:

1. Analyze Existing Web Pages
2. Build the Design Library
3. Generate High‑Fidelity Designs from Wireframes
4. Generate Code Using the Design Library

### Analyze Existing Web Pages

Objectives:

- Create design knowledge base
- Extract design knowledge from existing product pages, including design principles, visual patterns, common strctures, layout conventions, and styling rules.
- The design knowledge base help AI Agents to replicate the brand's decion-making process when generating new designs.

#### Inputs

- Screenshots of existing product pages
- URLs/ exported HTML/CSS of existing product pages (optional but recommended)
- Associated CSS files (global styles, component styles, utility classes). ( If not provided, the system may attempt to infer styles from screenshots, but accuracy may be limited.)
- Design files such as Figma (if available).
- Brand and design guidelines (if available).

#### Outputs

- Design principles (e.g., visual hierarchy, alignment rules, spacing rhythm)
- Design patterns (e.g., navigation bars, form structures, card layouts)
- Style rules (e.g., typography scale, color tokens, shadows, radii)
- Component Inventory (UI components with their visual/ structural variations)
- Layout System (grid system, breakpoints, responsive rules)
- Mapping to CSS implementation (class names, variables, selectors)

#### Process

1. Collect Visual and Structural Data: Gather all existing design instances to ensures the analysis covers all aspects of the visual system
   - UI Screens
     - Capture screenshots of all relevant pages
     - If available, export frames from design tools (e.g., Figma)
     - Include all device variations (desktop / tablet / mobile)
   - Code Artifacts
     - Download and archive CSS files (global & component-level)
     - Export relevant HTML structures
     - Identify reusable classes and utility patterns
   - Additional Assets
     - Icons, logos, imagery guidelines
     - Accessibility specifications
     - Brand identity documentation

2. Identify and Document Design Principles: Extract high-level design rationale. These are principles to guide agent in generating designs that "feel" like part of the same product family
   - Visual Hierarchy
     - How headings, subheadings, and content blocks are arranged
     - Contrast and color usage to convey priority
   - Spatial System
     - Spacing scale (e.g., 4px/8px/16px increments)
     - Margin & padding conventions
     - Vertical rhythm (line height, section spacing)
   - Alignment and Layout Structure
     - Grid system (12-column, 16-column, etc.)
     - Alignment rules (centered, left‑aligned, consistent gutters)
     - Responsive behavior per breakpoint
   - Visual Language
     - Rounded vs sharp corners
     - Light vs heavy shadows
     - Flat vs elevated components
     - Illustration / icon style

3. Extract Reusable Design Patterns: Identify UI/UX patterns, which enables the system to select the appropriate pattern during design generation.
   - Common Patterns
     - Header & navigation bar patterns
     - Footer layouts
     - Card layouts
     - Form patterns (input + label + validation structure)
     - List and table patterns
     - Dialogs, modals, side panels
     - Grid/list switching behavior
   - Interaction Patterns
     - Hover, focus, active states
     - Error/success state indicators
     - Micro-interactions (button states, transitions)
     - For each pattern, document:
       - Its purpose
       - Visual rules
       - Behavioral rules
       - Associated CSS classes
       - Variants (primary/secondary, compact/expanded)

4. Build Component Inventory: Create a catalog of all identifable UI components for generation reference.
   - Component types may include:
     - Buttons (primary, secondary, text button)
     - Inputs (text field, select, checkbox, radio, slider)
     - Cards
     - Navigation elements (tabs, menus, sidebars)
     - Badges, tags, chips
     - Avatars, icons
     - Alerts and banners
     - Tables and pagination components
   - For each component, capture:
     - Visual attributes:
       - Colors (background, border, text)
       - Typography (font family, size, weight)
       - Border radius
       - Shadows, outlines
       - Hover/focus/active states
     - Structural attributes:
       - DOM structure
       - CSS classes and variables
       - Responsive behavior
     - Semantic role (e.g., “primary action button”, “surface container”, etc.)

5. Extract Styling Rules from CSS: Analyze CSS to extract reusable styling structures. This helps formalizing implementation details for later code generation.
   - Design Tokens (implicit or explicit)
     - Colors (brand, neutral, semantic roles)
     - Typography scale
     - Spacing scale
     - Border radii
     - Shadow definitions
     - Z-index layers
   - CSS Variables
     - Identify --custom-properties and map them to semantic tokens
     - Identify utility classes (.mt-4, .flex, etc.)
   - Component Style Definitions
     - Identify class groups belonging to specific components (e.g., .btn, .card, .input-group)
     - Map CSS rules to component inventory items

6. Define the Design Knowledge Base: Combine findings from all steps to produce a structured, machine-readable and human-readable document
   - The Design Knowledge Base should include:
     - Design Principles Document
     - Design Pattern Catalog
     - Component Inventory & Variants
     - Foundational Style Taxonomy (colors, spacing, type, radii, shadows)
     - CSS Mapping Layer (variables, classes, rules)
     - Responsive Behavior Specification
     - Accessibility Standards
     - Constraints & Exceptions

#### Quality Criteria

- All primary UI components in the screenshots are identified and described.
- A consistent spacing and typography scale has been hypothesized and documented.
- The "Style Manifesto" is clear enough that a human designer could follow it to create a matching page.

### Build the Design Library

Objectives:

- Create a centralized, version-controlled Source of Truth that houses both foundational styles (Design Tokens) and structural building blocks (Component Manifest)
- Construct a unified, structured Design Library that serves as the single source of truth for all visual styles, UI components, and implementation mappings.
- This library ensures that all generated designs—human or AI—are visually consistent, technically feasible, and directly mappable to production code.

#### Inputs

- Extracted style rules from Step 1 (colors, typography, spacing, radii, shadows).
- Extracted component inventory (buttons, cards, forms, navigation, etc.).
- CSS files from existing production pages (global styles + component styles).
- Asset Repository (SVG icons, images, fonts).
- Existing design files (if available).
- Brand guidelines.

#### Outputs

A complete Design Library consisting of:

- Design Token Specification
- Component Definitions & Variants
- Token‑mapped CSS Variables & Classes
- Implementation‑ready Component Code References
- Usage Documentation

This library is consumed by:

- the AI agent (to generate consistent high‑fidelity designs),
- frontend engineers (as code source), and
- designers (as a reference for styling decisions).

#### Process

1. Establish Design Tokens (Foundational Style Layer): Design Tokens represent the smallest units of reusable style. They define what the design looks like in a structured, technology‑agnostic form.
   - Color Tokens
     - Brand colors (primary, secondary)
     - Semantic colors (success, warning, error)
     - Surface/background colors
     - Text colors
     - Border colors
     - State colors (hover, active, disabled)
   - Typography Tokens
     - Font families
     - Font sizes
     - Font weights
     - Line heights
     - Letter spacing
     - Heading and body type scales
   - Spacing & Sizing Tokens
     - Spacing scale (e.g., 4, 8, 12, 16…)
     - Section spacing
     - Component padding presets
     - Width/height scales (if standardized)
   - Border & Radius Tokens
     - Radii (sm, md, lg)
     - Border width and border styles
   - Shadow & Elevation Tokens
     - Card elevation
     - Modal elevation
     - Tooltip elevation
   - Motion Tokens (Optional)
     - Transition durations
     - Easing curves

2. Build the Component Library (UI Component Layer): Next, define reusable UI components built on top of design tokens.
   - Component Catalog
     - Buttons
     - Inputs (text field, dropdown, checkbox, radio)
     - Cards
     - Navigation (tabs, navbar, sidebar)
     - Tables and list components
     - Alerts, badges, chips
     - Modals, drawers
   - Component Structure
     - Visual Specification: Layout structure, Color usage, Typography, Spacing, Radius & shadows, States (hover, focus, active, disabled)
     - Functional Specification: Interactive behavior, Accessibility requirements, Responsiveness
     - Variants: Button (primary, secondary, ghost), Card (elevated, flat, outlined), Input (default, error, disabled)
     - Token bindings: Each component must reference token definitions
   - Component JSON Definition (for AI consumption)

3. Library Indexing: Create a "Component Catalog" for the AI.
   - This is a text-based description of every component in the library, including its CSS class names and expected HTML structure.

4. Build Reference Documentation (Human & AI Readable): Document the Design Library so that both humans and AI agents understand it
   - Token reference sheet
   - Component catalog with diagrams
   - CSS class reference
   - Usage guidelines
   - Interaction guidelines
   - Accessibility requirements
   - Responsive rules and breakpoints
   - Formats:
     - Markdown documentation (for repository)
     - JSON schemas (for AI)
     - Visual documentation (for designers)

5. Versioning & Governance: To support long‑term stability

#### Quality Criteria

- All CSS variables from the production site are mapped to a JSON token.
- The library includes all core components required to reconstruct a basic page (Nav, Button, Input, Card).
- The naming convention in the JSON matches the naming convention in the production code 1:1.

### Generate High‑Fidelity Designs from Wireframes

### Generate Code Using the Design Library

### Just note

1. Analyze Existing Web Pages: Perform a systematic analysis of existing, production‑ready pages to extract
   - Design principles (e.g., hierarchy, spacing rationale, color semantics)
   - Design patterns (e.g., layout templates, interaction models, component usage patterns)
   - Styling rules (e.g., typography scale, elevation rules, border‑radius conventions)
   - Component behavior and structure
   - This analysis produces a Design Knowledge Base—a structured set of rules and insights that guides the system (or AI agent) when generating high‑fidelity design variants.

2. Build the Design Library: Construct a standardized Design Library (also known as a Design System Library or Component Library) derived from the product’s existing CSS definitions and UI assets.
   - Foundational design tokens (colors, spacing, typography, radii, shadows)
   - Reusable UI components (buttons, cards, inputs, navigation elements)
   - Semantic style mappings (e.g., primary/secondary actions, surface types)
   - This library acts as the single source of truth for both design generation and frontend code generation, ensuring style and component consistency across outputs.

3. Generate High‑Fidelity Designs from Wireframes: Using the analyzed design rules and the Design Library, the system transforms a low‑fidelity wireframe into a high‑fidelity, pixel‑accurate mockup.
   - Adhere to extracted design principles and patterns
   - Comply with the visual language defined in the Design Library
   - Maintain consistency with existing product screens
   - Follow established interaction and layout standards (e.g., grid system, spacing scale)
   - This step may involve AI‑assisted interpretation of layout intent, component selection, styling, and variant generation.

4. Generate Code Using the Design Library: Convert the finalized high‑fidelity design into implementation‑ready HTML/CSS (or other frontend frameworks) by referencing the Design Library.
   - Code is generated using existing CSS classes, design tokens, and component structures
   - Output is fully aligned with the product’s design system and engineering conventions
   - Designers and engineers receive a consistent and maintainable handoff

### Analyze

## Design to Code Workflow

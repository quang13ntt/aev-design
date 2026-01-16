---
name: wireframe-to-code-workflow
description: Overview skill for the complete wireframe-to-code workflow. Use when you need guidance on the full process of converting wireframes into production code through three stages - building a Design Knowledge Base, generating HTML/CSS previews, and producing production-ready code. This skill provides navigation to three specialized sub-skills for each stage.
---

# Wireframe to Code Workflow - Overview

This skill provides a high-level overview of the complete wireframe-to-code workflow and navigation to specialized sub-skills for each stage. The workflow ensures consistent, maintainable UI code by constraining all design decisions to a Design Knowledge Base (DKB).

## Workflow Overview

The wireframe-to-code workflow consists of three sequential stages:

1. **Build Design Knowledge Base** → Extract design system from existing pages
2. **Generate Preview from Wireframe** → Create reviewable HTML/CSS from wireframes
3. **Generate Production Code** → Convert approved previews to framework code

Each stage has a dedicated skill with detailed processes, tools, and references.

## When to Use This Overview

- You need to understand the complete workflow before starting
- You're planning a wireframe-to-code project
- You want to see how the three stages connect
- You need to navigate to the appropriate stage-specific skill

## Core Principles

### Constrained Generation
All UI generation is constrained by the Design Knowledge Base. No "invented" styles, colors, or components are allowed. This ensures:
- Visual consistency with existing product
- Maintainable code that follows patterns
- Predictable behavior for designers and engineers

### Token-Driven Styling
Every visual decision references a design token:
- Colors → `color.primary`, `color.text.primary`
- Spacing → `space.4`, `space.6`
- Typography → `font.heading-lg`, `font.body-md`
- Radius → `radius.md`, `radius.lg`
- Shadows → `shadow.card`, `shadow.modal`

### Component-Driven Structure
All UI elements map to components defined in the DKB:
- Buttons → `Button[primary]`, `Button[secondary]`
- Cards → `Card[elevated]`, `Card[flat]`
- Inputs → `Input[default]`, `Input[error]`

### Progressive Refinement
Each stage builds on the previous with increasing fidelity:
- Stage 1: Extract patterns and constraints
- Stage 2: Apply patterns to create high-fidelity preview
- Stage 3: Convert preview to production-ready code

## Stage 1: Build Design Knowledge Base

**Purpose**: Create a single source of truth for design decisions and implementation mappings.

**When to use**: 
- Starting a new design system documentation project
- Analyzing existing products to extract patterns
- Establishing implementation mappings for code generation

**Skill**: Use the `build-design-knowledge-base` skill

**Key outputs**:
- Design principles and visual language
- Design tokens (colors, typography, spacing, radius, shadows)
- Component catalog with variants and states
- CSS mappings (token → variables, component → classes)
- Responsive and accessibility rules
- Constraints and exceptions

**Learn more**: See the [build-design-knowledge-base](../build-design-knowledge-base/SKILL.md) skill

## Stage 2: Generate HTML/CSS Preview from Wireframe

**Purpose**: Convert low-fidelity wireframes into high-fidelity, reviewable previews using only DKB elements.

**When to use**:
- Converting wireframes into HTML/CSS mockups
- Creating reviewable prototypes for stakeholder validation
- Building proof-of-concept UIs with existing design systems

**Skill**: Use the `wireframe-to-preview` skill

**Prerequisites**: 
- Completed Design Knowledge Base from Stage 1
- Low-fidelity wireframe (image, Figma frame, or description)

**Key outputs**:
- Browser-viewable HTML/CSS preview
- Preview specification (components used, tokens applied)
- Responsive and interaction states

**Learn more**: See the [wireframe-to-preview](../wireframe-to-preview/SKILL.md) skill

## Stage 3: Generate Production Code from Preview

**Purpose**: Convert approved previews into production-ready code for specific technology stacks.

**When to use**:
- Converting approved HTML/CSS previews into React/Vue/Angular components
- Implementing production UI from validated designs
- Integrating with specific frameworks and styling approaches

**Skill**: Use the `preview-to-code` skill

**Prerequisites**:
- Approved HTML/CSS preview from Stage 2
- Design Knowledge Base from Stage 1
- Defined technology stack (React, Vue, Tailwind, etc.)

**Key outputs**:
- Production-ready components in chosen framework
- Token artifacts (CSS variables, theme configs)
- Accessible, responsive, performant code

**Supported stacks**:
- React + TypeScript + CSS Modules/Tailwind/Styled Components
- Vue 3 + TypeScript + Scoped CSS
- Angular + TypeScript
- Svelte
- Plain HTML/CSS/JavaScript

**Learn more**: See the [preview-to-code](../preview-to-code/SKILL.md) skill

## Workflow Examples

### Example 1: Building a New Feature from Scratch

1. **Analyze existing pages** (Stage 1)
   - Screenshot all relevant pages in your product
   - Use `build-design-knowledge-base` skill to extract DKB
   - Output: Complete DKB with tokens and components

2. **Create preview from wireframe** (Stage 2)
   - Designer provides wireframe for new feature
   - Use `wireframe-to-preview` skill with DKB
   - Output: HTML/CSS preview for stakeholder review

3. **Generate React components** (Stage 3)
   - After preview approval
   - Use `preview-to-code` skill targeting React + Tailwind
   - Output: Production React components with Tailwind classes

### Example 2: Converting Design System to Code

1. **Document existing design system** (Stage 1)
   - Export Figma components and screenshots
   - Use `build-design-knowledge-base` skill
   - Output: DKB with comprehensive token set

2. **Generate component library previews** (Stage 2)
   - For each component in Figma
   - Use `wireframe-to-preview` skill
   - Output: HTML/CSS preview gallery

3. **Build component library** (Stage 3)
   - For approved previews
   - Use `preview-to-code` skill targeting Vue 3
   - Output: Vue component library with Storybook

## Key Terminology

- **Design Knowledge Base (DKB)**: Versioned reference combining design rules and implementation mappings (tokens + components + patterns + constraints)
- **Design Tokens**: Named, reusable styling primitives (colors, typography, spacing, radius, elevation)
- **Component Mapping**: Agreed HTML structure and CSS classes for each component variant
- **Preview**: Reviewable HTML/CSS artifact generated from wireframe using only DKB elements
- **Wireframe**: Low-fidelity structural input (image, Figma frame, or description)

## Navigation to Sub-Skills

- **Stage 1**: [build-design-knowledge-base](../build-design-knowledge-base/SKILL.md)
- **Stage 2**: [wireframe-to-preview](../wireframe-to-preview/SKILL.md)
- **Stage 3**: [preview-to-code](../preview-to-code/SKILL.md)

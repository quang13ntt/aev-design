# AEON BETA UI/UX Design Guidelines

## 1. Design Philosophy & Mood

The AEON BETA design follows a **Modern Cinema Aesthetic** that prioritizes clarity, immersive imagery, and a high-contrast visual hierarchy.

- **Clarity**: Use of generous white space and a strict 8px grid system.
- **Contrast**: Bold transitions between deep blacks (`#0D0D0D`) and pure whites (`#FFFFFF`).
- **Immersive**: Large movie posters and trailer carousels dominate the view, drawing users into the content.
- **Vibrant Accents**: Functional elements like seat types, age ratings, and special offers use bright, distinct colors to stand out against the monochrome base.

## 2. Design Tokens

### Color Palette

| Name | Hex Code | Usage |
| :--- | :--- | :--- |
| **Black/900** | `#0D0D0D` | Primary brand color, logos, primary buttons, footer, headers. |
| **Pure Black** | `#000000` | Selected states, icons, deep backgrounds. |
| **White** | `#FFFFFF` | Primary background, text on dark components. |
| **White Smoke** | `#F2F2F2` | Secondary text on dark backgrounds, subtle accents. |
| **Black/100** | `#E3E3E3` | Borders, disabled states, subtle separators. |
| **Cyan (Age Rating)** | `#73E5EA` | Age rating tags (e.g., 'K'), Regular seat type. |
| **Lime (VIP)** | `#D9FF5C` | VIP seat type, "Happy Morning" tags. |
| **Blue (Sweet Box)** | `#627EF7` | Sweet Box seat type. |
| **Pink (Supreme)** | `#ED87EF` | Supreme seat type. |
| **Yellow (Wheelchair)** | `#F8D347` | Wheelchair seat type/accessibility tags. |

### Typography

- **Primary Font Family**: `'ABC Diatype'` (preferred), fallback to Sans-serif.
- **Logo Font Family**: `'Inter'`, Bold.

| Level | Size/Line-Height | Weight | Usage |
| :--- | :--- | :--- | :--- |
| **H3** | 24px / 29px (1.2) | 700 (Bold) | Section headers, movie titles. |
| **H4** | 20px / 24px (1.2) | 700 (Bold) | Sub-headers, button text. |
| **Body (Bold)** | 16px / 19px (1.2) | 700 (Bold) | Key information, primary links. |
| **Body (Regular)**| 16px / 19px (1.2) | 400 (Regular)| General body text, descriptions. |
| **Caption 1** | 13px / 17px (1.3) | 400/700 | Small metadata, tags, labels. |
| **Caption 2** | 11px / 14px (1.3) | 400 (Regular)| Micro-labels, nav items. |

### Spacing & Layout

- **Base Grid**: 8px (All margins, paddings, and gaps should be multiples of 8).
- **Common Gaps**: 8px (tight), 16px (standard), 24px (loose), 32px/40px (section spacing).
- **Border Radius**:
  - Standard: 2px (tight corners).
  - Tags/Labels: 0px (sharp).
  - Profile/Icons: 9999px (circular).

## 3. Component Guidelines

### Primary Buttons

- **Style**: Solid `#0D0D0D` background.
- **Text**: 16px / 20px Bold, White `#FFFFFF`.
- **States**:
  - Default: Sharp corners (0px radius).
  - Hover: Opacity reduction (80%).
- **Size**: Standard height 48px or 56px for main CTAs.

### Age Rating & Metadata Tags

- **Style**: Background color corresponds to category (e.g., Cyan `#73E5EA` for 'K').
- **Text**: 13px Bold, Black `#000000`.
- **Padding**: 2px 6px.
- **Border**: Sharp (0px radius).

### Movie Cards

- **Poster**: Aspect ratio ~2:3.
- **Title**: H3 Bold, Black `#0D0D0D`.
- **Showtimes**: Grid of 16px/20px units. Available times in `#0D0D0D`, sold out/unavailable in `#E3E3E3`.

### Navigation Bar

- **Desktop**: Centered logo, text links (16px Bold) on the right.
- **Mobile**: Bottom tab bar with 24px icons and 11px labels.
- **Active State**: Inverted colors (White on Black) for the active item.

## 4. Interaction Patterns

- **Carousels**: Horizontal scroll with 24px chevron indicators.
- **Seat Selection**: Tap to toggle. Selected seats turn solid Black `#000000`.
- **Back to Top**: Floating 48x48px button, Black background, White arrow up icon.

## 5. Do's and Don'ts

### Do's

- **DO** use the 8px grid for all layout decisions.
- **DO** maintain high contrast between text and background.
- **DO** use the specific seat color tokens for consistency across movie booking.
- **DO** prioritize 'ABC Diatype' for all UI text.

### Don'ts

- **DON'T** use soft shadows; the design relies on flat colors and sharp borders.
- **DON'T** round corners excessively (keep to 2px or 0px unless for circular elements).
- **DON'T** introduce colors outside the approved palette for functional states.

## 6. Implementation Checklist

- [ ] Typography uses 'ABC Diatype' with correct line heights.
- [ ] All spacing (margin/padding) is a multiple of 8px.
- [ ] Brand color `#0D0D0D` is used for primary buttons and footer.
- [ ] Seat selection legend matches exactly with the map.
- [ ] Hover/Active states are clearly defined and follow high-contrast rules.
- [ ] Metadata tags have correct background colors according to rating.

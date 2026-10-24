---
name: Syntactic Void
colors:
  surface: '#fcf8ff'
  surface-dim: '#dcd9e0'
  surface-bright: '#fcf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f2fa'
  surface-container: '#f0ecf4'
  surface-container-high: '#eae7ee'
  surface-container-highest: '#e4e1e9'
  on-surface: '#1b1b20'
  on-surface-variant: '#464554'
  inverse-surface: '#303036'
  inverse-on-surface: '#f3eff7'
  outline: '#767586'
  outline-variant: '#c7c4d7'
  surface-tint: '#494bd6'
  primary: '#4648d4'
  on-primary: '#ffffff'
  primary-container: '#6063ee'
  on-primary-container: '#fffbff'
  inverse-primary: '#c0c1ff'
  secondary: '#6b38d4'
  on-secondary: '#ffffff'
  secondary-container: '#8455ef'
  on-secondary-container: '#fffbff'
  tertiary: '#006577'
  on-tertiary: '#ffffff'
  tertiary-container: '#008096'
  on-tertiary-container: '#f9fdff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e1e0ff'
  primary-fixed-dim: '#c0c1ff'
  on-primary-fixed: '#07006c'
  on-primary-fixed-variant: '#2f2ebe'
  secondary-fixed: '#e9ddff'
  secondary-fixed-dim: '#d0bcff'
  on-secondary-fixed: '#23005c'
  on-secondary-fixed-variant: '#5516be'
  tertiary-fixed: '#acedff'
  tertiary-fixed-dim: '#4cd7f6'
  on-tertiary-fixed: '#001f26'
  on-tertiary-fixed-variant: '#004e5c'
  background: '#fcf8ff'
  on-background: '#1b1b20'
  surface-variant: '#e4e1e9'
typography:
  display-hero:
    fontFamily: Space Grotesk
    fontSize: 56px
    fontWeight: '700'
    lineHeight: 64px
  display-hero-mobile:
    fontFamily: Space Grotesk
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 44px
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 36px
    fontWeight: '600'
    lineHeight: 44px
  headline-xl-mobile:
    fontFamily: Space Grotesk
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-md:
    fontFamily: Geist
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  body-sm:
    fontFamily: Geist
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 16px
  code-lg:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
  code-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
  label-badge:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '600'
    lineHeight: 14px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  gutter: 1.5rem
  gutter-sm: 1rem
  margin: 2rem
  margin-sm: 1rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
---

## Brand & Style

This design system targets an elite technical audience—AI researchers, engineering leadership, and venture architects evaluating frontier capabilities in Agentic Systems and LLM Architecture. 

The aesthetic is precision-engineered, borrowing heavily from modern dev-first environments such as Linear, Raycast, and Vercel. It bridges extreme minimalism with refined technical brutalism: razor-sharp hierarchy, dense information architecture, tactile feedback, and purposeful ambient luminescence. It evokes computational rigor, speed, and deep technical mastery rather than generic corporate SaaS veneer.

## Colors

The palette leverages a clean light substrate to allow high-contrast illuminated tokens and active runtime states to command visual priority.

- **Background Canvas**: `#FFFFFF` (True Light)
- **Surfaces**:
  - `surface-base`: `#F8F9FC` (Layer 1 containers, panels, navigation frames)
  - `surface-raised`: `#FFFFFF` (Layer 2 interactive cards, modal dialogs, flyouts)
  - `surface-overlay`: `#F1F3F9` (Hover highlights, contextual popovers)
- **Borders & Dividers**:
  - `border-subtle`: `rgba(99, 102, 241, 0.15)` (Indigo-tinted structural divisions)
  - `border-active`: `rgba(139, 92, 246, 0.4)` (Focused and active bounding perimeters)
- **Brand Accents**:
  - Linear execution gradient: `linear-gradient(135deg, #6366F1 0%, #8B5CF6 100%)` (Electric Indigo to Violet)
- **Status & Indicators**:
  - Active Node / Live Agent: `#10B981` (Cyber Emerald)
  - Latency / Stream Ingestion: `#06B6D4` (Telemetry Cyan)
  - Attention / Anomaly: `#F59E0B` (Amber Warning)

## Typography

Typography establishes an unambiguous distinction between human discourse, structural signifiers, and machine telemetry:

- **Space Grotesk**: Reserved for primary titles, module headers, and large metric counters. Geometric, mechanical, yet distinctly modern.
- **Geist**: Primary system body copy. Extremely clear vertical metric alignment, neutral grotesque style, optimized for rapid scanning of architecture writeups and technical abstracts.
- **JetBrains Mono**: Used everywhere computational data exists: execution runtimes, agent tool definitions, parameters, prompt templates, and metadata chips.

## Layout & Spacing

The structural layout utilizes a dense, fixed-container grid system optimized for information density:

- **Grid Architecture**: 12-column fixed grid on desktop (max width: `1280px`), transitioning to an 8-column layout on tablet (`768px - 1024px`), and a 4-column column flow on mobile (`< 768px`).
- **Rhythm**: Anchored by a 4px modular unit (8px base standard). 
- **Section Structure**: Outer margins provide deliberate atmospheric negative space (`2.5rem` to `4rem`), while component internals maintain high operational density using `space-xs` (4px), `space-sm` (8px), and `space-md` (16px) tokens to resemble professional IDE and devtool ergonomics.

## Elevation & Depth

This system avoids heavy physical drop-shadows, achieving spatial separation through layered light-matter surfaces, subtle inner highlights, and ambient light leaks:

- **Surface Layering**:
  - `Canvas (#FFFFFF)`: Base ground plane.
  - `Containers (#F8F9FC)`: Inset or neutral panels, separated by `1px` stroke of `rgba(99, 102, 241, 0.15)`.
  - `Interactive Floating Surfaces (#FFFFFF)`: Cards, drawers, and active inspectors.
- **Inner Light (Glow Inset)**: Higher-tier interactive components leverage a subtle `inset 0 1px 0 0 rgba(255, 255, 255, 0.8)` to simulate an overhead edge bevel.
- **Luminescence (Ambient Glow)**: Key accent items emit a diffuse chromatic aura (`0 0 24px -4px rgba(99, 102, 241, 0.15)`). Live nodes and active agents use a pulsing drop glow (`0 0 12px rgba(16, 185, 129, 0.3)`).

## Shapes

The geometric signature is compact and surgical. Controlled softness prevents the UI from feeling playful or organic:

- **Base Radius (`0.25rem` / `4px`)**: Input fields, command prompts, system badges, code blocks, and micro tags.
- **Card/Container Radius (`0.5rem` / `8px`)**: Model execution visualizers, architecture cards, and modal windows.
- **Interactive Focus Radius**: Matches parent borders exactly with an offset of `2px` via outer ring containment.

## Components

### Buttons
- **Primary**: Solid background using the electric gradient (`#6366F1` to `#8B5CF6`). Crisp white typography (`Geist Medium`), no outer shadow, subtle inset top border (`rgba(255,255,255,0.2)`).
- **Secondary / Ghost**: Background `#F8F9FC`, stroke `1px` translucent indigo (`rgba(99,102,241,0.2)`), text `#1E293B`. Hover state elevates the border to `#8B5CF6` with a soft back-glow.
- **Terminal Action**: Monospaced font (`JetBrains Mono`), light base with cyan or emerald cursor-caret prefix (`> run_agent()`).

### Chips & Badges
- **Architecture & Tech Chips**: Fixed height `24px`, background `#F8F9FC`, border `1px solid rgba(0, 0, 0, 0.08)`, font `label-badge` (`JetBrains Mono`).
- **Telemetry Indicators**: Prefixed with a live hardware light: a 6px circular dot (`#10B981` or `#06B6D4`) with `box-shadow: 0 0 8px currentColor`.

### Cards & System Inspectors
- Layer 1 surface (`#F8F9FC`) framed with subtle indigo border (`1px solid rgba(99, 102, 241, 0.15)`).
- Hover transition triggers a border shift to `rgba(139, 92, 246, 0.4)` and a top-edge linear highlight gradient.

### Input Fields & Command Bars
- Emulates a quick-search or command-palette interface (Raycast style).
- Background `#F8F9FC`, text `Geist 14px`, placeholder text in `#64748B`.
- Integrated monospace key-cap indicators (`⌘K`, `ESC`) rendered in `#FFFFFF` with light perimeter lines.

### Execution Logs & Agent Trace Views
- Specialized component for visualizing agent run loops, tool calls, and LLM chains.
- Gutter-based lineage lines using `rgba(99, 102, 241, 0.2)` connecting agent thoughts, tool executions, and state outputs. Monospaced token stream readout.
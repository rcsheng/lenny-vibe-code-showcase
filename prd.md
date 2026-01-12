# Gallery App – Product Requirements Document (PRD)

## Overview

The Gallery App is a simple, static-first web application that showcases a curated gallery of websites built by users. The source of truth for the showcased sites is an existing blog located in the `original_site/` folder, which contains HTML and associated assets. The goal is to extract, structure, and present these sites in a clean, browsable gallery format.

The app must:

* Require **no database**
* Be **easy to deploy on Vercel**
* Be **agent-friendly** (clear structure, deterministic inputs, minimal configuration)
* Favor **static generation** and simplicity

This PRD is written so autonomous or semi-autonomous agents can build the app end-to-end with minimal clarification.

---

## Goals & Success Criteria

### Goals

* Showcase a list of sites in a visually clean, browsable gallery
* Use the existing blog content in `original_site/` as the input source
* Enable future additions by editing static files only
* Keep operational complexity close to zero

### Non-Goals

* User accounts or authentication
* Dynamic submissions
* Analytics, comments, likes, or ratings
* Backend services or APIs

### Success Criteria

* App builds and deploys successfully on Vercel
* Gallery renders correctly using only static assets
* Adding a new site requires no code changes beyond content files
* Lighthouse performance score ≥ high nineties

---

## Target Users

* Curious visitors browsing examples of sites
* Builders looking for inspiration
* Internal teams curating or highlighting projects

---

## Functional Requirements

### Core Features

#### Gallery View

* Displays a grid or list of showcased sites
* Each item includes:

  * Site name
  * Short description
  * Preview image (thumbnail)
  * Link to the live site
  * Optional tags (e.g., "portfolio", "blog", "tool")

#### Site Detail (Optional but Recommended)

* Clicking a gallery item opens a detail page
* Detail page may include:

  * Larger preview image(s)
  * Longer description
  * Tech stack or notes (if available)
  * External link

#### Static Content Source

* The existing blog in `original_site/` is the authoritative input
* Agents must:

  * Parse or manually extract site entries from the blog HTML
  * Convert entries into a structured format (e.g., JSON or Markdown)

---

## Content Model

### Site Entry Schema

Each showcased site should conform to a simple, static schema:

* `id`: string (unique, URL-safe)
* `title`: string
* `creator`: string
* `creator_url`: string
* `description`: string (one to three sentences)
* `url`: string (external link)
* `image`: string (path to thumbnail image)
* `tags`: array of strings (optional)
* `featured`: boolean (optional)

This schema should live in a flat file such as:

* `sites.json`, or
* A folder of Markdown files with frontmatter

---

## Technical Requirements

### Framework

* Recommended: Next.js (App Router or Pages Router)
* Static Site Generation (SSG) only

### Data Handling

* No runtime data fetching
* All data loaded at build time from local files
* No database, no CMS, no API routes

### Deployment

* Must deploy cleanly to Vercel with default settings
* No environment variables required

### Asset Handling

* Images stored locally in the repo
* Optimized via framework defaults (e.g., Next.js Image)

---

## UX & Design Guidelines

* Minimal, neutral design
* Focus on content over decoration
* Responsive grid layout
* Accessible by default:

  * Semantic HTML
  * Keyboard navigable
  * Reasonable color contrast

---

## Information Architecture

### Pages

* `/` – Gallery index

---

## Agent Execution Plan

Agents should execute the build in the following phases:

### Phase One – Content Extraction

* Inspect `original_site/` HTML
* Identify repeated patterns representing site entries
* Extract relevant fields into structured data

### Phase Two – App Scaffold

* Initialize Next.js project
* Configure static asset handling
* Create base layout and routing

### Phase Three – Gallery Rendering

* Render gallery from structured data
* Implement responsive layout
* Add external links

### Phase Four – Polish & Validation

* Validate accessibility basics
* Optimize images
* Confirm Vercel build compatibility

---

## Constraints & Assumptions

* Original blog content is static and readable
* No legal or licensing restrictions on showcasing listed sites
* Agents may lightly normalize or rewrite descriptions for clarity

---

## Future Enhancements (Out of Scope)

* Search or filtering UI
* Tag-based navigation
* Submissions via form
* Analytics or tracking

---

## Open Questions (For Humans, Not Agents)

* Should the original blog be linked or archived?
* Should featured sites be visually emphasized?
* Is pagination needed if the gallery grows large?

---

## Final Notes

This project intentionally favors simplicity, determinism, and low maintenance. Agents should default to the simplest possible implementation that satisfies the requirements above. Any additional complexity must be justified against the stated goals.

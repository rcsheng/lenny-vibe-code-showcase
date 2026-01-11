# Vibe Code Showcase

A curated gallery of websites built by non-technical people using AI tools like Claude.

## Features

- **Static Site Generation** - Built with Next.js using SSG for optimal performance
- **No Database Required** - All content is stored in a simple JSON file
- **Vercel Ready** - Deploy with zero configuration
- **Responsive Design** - Works beautifully on all devices
- **Dark Mode** - Automatic dark mode support

## Getting Started

### Development

```bash
# Install dependencies
npm install

# Run development server
npm run dev

# Open http://localhost:3000
```

### Building

```bash
# Build for production
npm run build

# The static files will be in the /out directory
```

## Adding New Sites

To add a new site to the gallery, edit `/public/sites.json`:

```json
{
  "id": "unique-site-id",
  "title": "Site Title",
  "creator": "Creator Name",
  "creator_url": "https://creator-url.com",
  "description": "A brief description of the site",
  "url": "https://site-url.com",
  "image": "/images/site-image.jpg",
  "tags": ["tag1", "tag2"],
  "featured": false
}
```

## Deployment

### Deploy to Vercel

1. Push your code to GitHub
2. Import your repository in Vercel
3. Vercel will automatically detect Next.js and deploy

Or use the Vercel CLI:

```bash
npm install -g vercel
vercel
```

### Deploy to Other Platforms

Since this is a static site, you can deploy the `/out` directory to any static hosting service:

- Netlify
- GitHub Pages
- Cloudflare Pages
- AWS S3
- And more!

## Project Structure

```
├── app/
│   ├── layout.tsx      # Root layout
│   ├── page.tsx        # Homepage
│   └── globals.css     # Global styles
├── components/
│   └── SiteCard.tsx    # Site card component
├── public/
│   ├── sites.json      # Site data
│   └── images/         # Site images
├── types/
│   └── site.ts         # TypeScript types
└── next.config.ts      # Next.js config
```

## Tech Stack

- **Framework:** Next.js 15
- **Language:** TypeScript
- **Styling:** Tailwind CSS
- **Deployment:** Vercel (recommended)

## License

MIT
# lenny-vibe-code-showcase

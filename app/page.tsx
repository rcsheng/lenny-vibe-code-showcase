import { promises as fs } from 'fs';
import path from 'path';
import SiteCard from '@/components/SiteCard';
import type { Site } from '@/types/site';

async function getSites(): Promise<Site[]> {
  const filePath = path.join(process.cwd(), 'public', 'sites.json');
  const fileContents = await fs.readFile(filePath, 'utf8');
  return JSON.parse(fileContents);
}

export default async function Home() {
  const sites = await getSites();

  return (
    <main className="min-h-screen bg-gradient-to-b from-gray-50 to-gray-100 dark:from-gray-900 dark:to-gray-950">
      <div className="container mx-auto px-4 py-12 max-w-7xl">
        <header className="text-center mb-16">
          <h1 className="text-5xl font-bold mb-4 bg-gradient-to-r from-purple-600 to-blue-600 bg-clip-text text-transparent">
            Lenny's Newsletter Vibe Code Showcase
          </h1>
          <p className="text-xl text-gray-600 dark:text-gray-400 max-w-2xl mx-auto mb-2">
            Discover amazing projects built by non-technical creators using AI tools
          </p>
          <p className="text-base text-gray-500 dark:text-gray-400">
            Featured in{' '}
            <a
              href="https://www.lennysnewsletter.com/p/what-people-are-vibe-coding-and-actually"
              target="_blank"
              rel="noopener noreferrer"
              className="text-purple-600 dark:text-purple-400 hover:underline font-large"
            >
              Lenny's Newsletter
            </a>
          </p>
          <p className="text-sm text-gray-500 dark:text-gray-400 mb-3">
            Created by{' '}
            <a
              href="https://www.linkedin.com/in/richardsheng/"
              target="_blank"
              rel="noopener noreferrer"
              className="text-purple-600 dark:text-purple-400 hover:underline font-medium"
            >
              Richard Sheng
            </a>
          </p>

          {/* Vibe Coding Tools Section */}
          <div className="mt-12 mb-8">
            <h2 className="text-2xl font-semibold mb-6 text-gray-800 dark:text-gray-200">
              Vibe Coding Tools Mentioned
            </h2>
            <div className="flex flex-nowrap justify-center gap-4 overflow-x-auto mx-auto px-4">
              <a
                href="https://bolt.new"
                target="_blank"
                rel="noopener noreferrer"
                className="group"
              >
                <div className="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-md hover:shadow-xl transition-all duration-300 border border-gray-200 dark:border-gray-700 w-32 h-32 flex items-center justify-center">
                  <img
                    src="/images/bolt-logo.png"
                    alt="Bolt.new"
                    className="w-full h-full object-contain"
                  />
                </div>
              </a>
              <a
                href="https://claude.ai"
                target="_blank"
                rel="noopener noreferrer"
                className="group"
              >
                <div className="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-md hover:shadow-xl transition-all duration-300 border border-gray-200 dark:border-gray-700 w-32 h-32 flex items-center justify-center">
                  <img
                    src="/images/claude-logo.png"
                    alt="Claude"
                    className="w-full h-full object-contain"
                  />
                </div>
              </a>
              <a
                href="https://cursor.com"
                target="_blank"
                rel="noopener noreferrer"
                className="group"
              >
                <div className="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-md hover:shadow-xl transition-all duration-300 border border-gray-200 dark:border-gray-700 w-32 h-32 flex items-center justify-center">
                  <img
                    src="/images/cursor-logo.png"
                    alt="Cursor"
                    className="w-full h-full object-contain"
                  />
                </div>
              </a>
              <a
                href="https://lovable.dev"
                target="_blank"
                rel="noopener noreferrer"
                className="group"
              >
                <div className="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-md hover:shadow-xl transition-all duration-300 border border-gray-200 dark:border-gray-700 w-32 h-32 flex items-center justify-center">
                  <img
                    src="/images/lovable-logo.png"
                    alt="Lovable"
                    className="w-full h-full object-contain"
                  />
                </div>
              </a>
              <a
                href="https://replit.com"
                target="_blank"
                rel="noopener noreferrer"
                className="group"
              >
                <div className="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-md hover:shadow-xl transition-all duration-300 border border-gray-200 dark:border-gray-700 w-32 h-32 flex items-center justify-center">
                  <img
                    src="/images/replit-logo.png"
                    alt="Replit"
                    className="w-full h-full object-contain"
                  />
                </div>
              </a>
              <a
                href="https://vercel.com"
                target="_blank"
                rel="noopener noreferrer"
                className="group"
              >
                <div className="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-md hover:shadow-xl transition-all duration-300 border border-gray-200 dark:border-gray-700 w-32 h-32 flex items-center justify-center">
                  <img
                    src="/images/vercel-logo.png"
                    alt="Vercel"
                    className="w-full h-full object-contain"
                  />
                </div>
              </a>
              <a
                href="https://www.warp.dev"
                target="_blank"
                rel="noopener noreferrer"
                className="group"
              >
                <div className="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-md hover:shadow-xl transition-all duration-300 border border-gray-200 dark:border-gray-700 w-32 h-32 flex items-center justify-center">
                  <img
                    src="/images/warp-logo.png"
                    alt="Warp"
                    className="w-full h-full object-contain"
                  />
                </div>
              </a>
              <a
                href="https://zapier.com"
                target="_blank"
                rel="noopener noreferrer"
                className="group"
              >
                <div className="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-md hover:shadow-xl transition-all duration-300 border border-gray-200 dark:border-gray-700 w-32 h-32 flex items-center justify-center">
                  <img
                    src="/images/zapier-logo.png"
                    alt="Zapier"
                    className="w-full h-full object-contain"
                  />
                </div>
              </a>
            </div>
          </div>
          <div className="mt-12 mb-8">
            <h2 className="text-2xl font-semibold mb-6 text-gray-800 dark:text-gray-200">
              Sample Showcase Projects 
            </h2>
            <p className="text-base text-gray-500 dark:text-gray-400">
              Click on project name to see the project.
            </p>
          </div>
        </header>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {sites.map((site) => (
            <SiteCard key={site.id} site={site} />
          ))}
        </div>

        <footer className="mt-20 text-center text-gray-500 dark:text-gray-500 text-sm">
          <p>
            Built with Next.js • Static Generation • No Database Required
          </p>
        </footer>
      </div>
    </main>
  );
}

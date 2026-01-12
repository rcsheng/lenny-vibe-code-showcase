import type { Site } from '@/types/site';

interface SiteCardProps {
  site: Site;
}

export default function SiteCard({ site }: SiteCardProps) {
  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl shadow-md hover:shadow-xl transition-all duration-300 overflow-hidden border border-gray-200 dark:border-gray-700">
      <div className="relative h-48 overflow-hidden">
        <img
          src={site.image}
          alt={`${site.title} platform logo`}
          className="w-full h-full object-cover"
        />
        {site.featured && (
          <div className="absolute top-3 right-3 bg-yellow-400 text-yellow-900 px-3 py-1 rounded-full text-xs font-semibold">
            Featured
          </div>
        )}
      </div>

      <div className="p-6">
        <h3 className="text-xl font-bold mb-2">
          <a
            href={site.url}
            target="_blank"
            rel="noopener noreferrer"
            className="hover:text-purple-600 dark:hover:text-purple-400 transition-colors"
          >
            {site.title}
          </a>
        </h3>

        <p className="text-sm text-gray-500 dark:text-gray-400 mb-3">
          by{' '}
          <a
            href={site.creator_url}
            target="_blank"
            rel="noopener noreferrer"
            className="hover:text-purple-600 dark:hover:text-purple-400 underline transition-colors"
          >
            {site.creator}
          </a>
        </p>

        <p className="text-gray-700 dark:text-gray-300 mb-4 line-clamp-3">
          {site.description}
        </p>

        <div className="flex flex-wrap gap-2">
          {site.tags.map((tag) => (
            <span
              key={tag}
              className="px-3 py-1 bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300 rounded-full text-xs font-medium"
            >
              {tag}
            </span>
          ))}
        </div>
      </div>
    </div>
  );
}

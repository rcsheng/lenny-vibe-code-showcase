export interface Site {
  id: string;
  title: string;
  creator: string;
  creator_url: string;
  description: string;
  url: string;
  image: string;
  tags: string[];
  featured?: boolean;
}

# youtube-rss-api

## Description
This project is a YouTube RSS API. It allows you to create an RSS podcast feed from YouTube using youtube-dl.

## Installation

### Default Installation
1. Clone the repository: `git clone https://github.com/yourusername/youtube-rss-api.git`
2. Navigate to the project directory: `cd youtube-rss-api`
3. Install the required packages: `pip install -r requirements.txt`
4. Run the application: `python main.py`

### Docker Installation
1. Clone the repository: `git clone https://github.com/yourusername/youtube-rss-api.git`
2. Navigate to the project directory: `cd youtube-rss-api`
3. Build the Docker image: `docker build -t youtube-rss-api .`
4. Run the Docker container: `docker run -p 8231:80 youtube-rss-api`

## Usage

### Endpoints

#### GET /feed
Get the RSS feed for a specific YouTube channel.
Parameters:
- `url`: The URL of the YouTube channel.
- `page`: The page number (default is 1).
- `per_page`: The number of items per page (default is 10).

#### GET /video/{id}
Get the details of a specific video.
Parameters:
- `id`: The ID of the video.
from utils.config_loader import load_config
from news.fetcher import get_news
from news.display import display_news

if __name__ == "__main__":
    # Load configuration from config.yaml
    config = load_config("config.yaml")
    
    # Retrieves news with API key and country from configuration file
    country_code = input(f"Headline-News in country of \"{config['country']}\", press return ") or config['country']
    articles = get_news(config['api_key'], country_code, config['url'])
    
    # Displays news in the terminal
    display_news(articles)

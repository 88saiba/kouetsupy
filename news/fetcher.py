import requests

def get_news(api_key, country, url):
    parameters = {
        'country': country,
        'apiKey': api_key,
    }
    
    response = requests.get(url, params=parameters)
    if response.status_code == 200:
        news_data = response.json()
        return news_data['articles']
    else:
        print(f"Error: {response.status_code}")
        return []

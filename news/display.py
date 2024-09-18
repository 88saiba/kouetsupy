def display_news(articles):
    if articles:
        for i, article in enumerate(articles, 1):
            print(f"{i}. {article['title']}")
            print(f"   Source: {article['source']['name']}")
            print(f"   Link: {article['url']}")
            print("-" * 80)
    else:
        print("No news available.")

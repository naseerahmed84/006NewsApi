import requests


# r = requests.get("https://newsapi.org/v2/everything?qInTitle=space%20market&from=2023-5-27&to=2023-5-28&sortBy=popularity&language=en&apiKey=c0c867e37d3f4fd09af31a177ff6472b")
# content = r.json()
# articles = content["articles"]
# print(type(articles)) # It's a type LIST
#
# for article in articles:
#     print("TITLE:\n" , article["title"],"\nSOURCE:\n", article["source"])

def get_news(topic, from_date, to_date, language="en", api_key="c0c867e37d3f4fd09af31a177ff6472b"):
    url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()
    articles = content["articles"]
    results = []
    nl = "\n"

    for article in articles:
        results.append(f' "TITLE:",{nl}, {article["title"]},,{nl} "SOURCE:", {nl}, {article["source"]}')
    return results


print(get_news(topic='space', from_date='2023-5-27', to_date='2023-5-28'))

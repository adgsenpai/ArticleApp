import json

# Read the JSON file from articles.json
with open('./articles/articles.json') as json_file:
    data = json.load(json_file)

def return_articles():    
    return data['articles']

def return_article(id):
    for article in data['articles']:
        if int(article['id']) == id:
            return article

def return_filename(id):
    for article in data['articles']:
        if article['id'] == id:
            return article['filename']


if __name__ == "__main__":
    print(return_article(1))
    print(return_filename(1))
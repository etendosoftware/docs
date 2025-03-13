import os
import json
from bs4 import BeautifulSoup
from algoliasearch.search.client import SearchClientSync


client = SearchClientSync("XMLZ1ZZEY7", "fcfbff215223081526cae74652f4f884")


output_dir = "site"

def index_docs(output_dir):
    result_json = []

    for root, dirs, files in os.walk(output_dir):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)

                with open(file_path, "r", encoding="utf-8") as file:
                    html_content = file.read()

                # Parse the HTML content using BeautifulSoup
                soup = BeautifulSoup(html_content, "html.parser")

                # Extracting the required data
                title = soup.title.string.strip() if soup.title else "No Title"
                h2_elements = [h2.get_text(strip=True) for h2 in soup.find_all("h2")]
                h3_elements = [h3.get_text(strip=True) for h3 in soup.find_all("h3")]
                tags = [tag.get_text(strip=True) for tag in soup.find_all(class_="md-tag")]
                url = soup.find("link", rel="canonical")["href"] if soup.find("link", rel="canonical") else "No URL"

                # Constructing the object
                result = {
                    "objectID": url,
                    "title": title,
                    "h2": h2_elements,
                    "h3": h3_elements,
                    "tags": tags,
                    "url": url
                }

                result_json.append(result)
                
                    
    if result_json:
        print(result_json)
        print(f"{len(result_json)} documents indexed successfully.")
        
        client.save_objects(
            index_name = "etendo_docs_index",
            objects = result_json 
        )
    else:
        print("No HTML documents found to index.")


# Index the docs
index_docs(output_dir)

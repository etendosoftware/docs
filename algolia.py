import os
import json
from bs4 import BeautifulSoup
from algoliasearch.search.client import SearchClientSync

client = SearchClientSync("XMLZ1ZZEY7", "fcfbff215223081526cae74652f4f884")

output_dir = "site"

def index_docs(output_dir):
    result_json = []
    base_url = "https://docs.etendo.software/"

    for root, dirs, files in os.walk(output_dir):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)

                with open(file_path, "r", encoding="utf-8") as f:
                    html_content = f.read()

                # Parse the HTML content using BeautifulSoup
                soup = BeautifulSoup(html_content, "html.parser")

                # Extract the raw title
                raw_title = soup.title.string.strip() if soup.title else "No Title"
                
                # Remove the unwanted substring if present
                title = raw_title.replace(" - Etendo Documentation", "")

                # Extract h2 elements
                h2_elements = [h2.get_text(strip=True) for h2 in soup.find_all("h2")]
                
                # Extract h3 elements
                h3_elements = [h3.get_text(strip=True) for h3 in soup.find_all("h3")]
                
                # Extract tags
                tags = [tag.get_text(strip=True) for tag in soup.find_all(class_="md-tag")]

                # Try to get the canonical URL
                canonical_link = soup.find("link", rel="canonical")
                url = canonical_link["href"] if canonical_link else "No URL"

                # Adjust the URL to add '/latest/' after the domain
                if url != "No URL" and url.startswith(base_url):
                    url = url.replace(base_url, base_url + "latest/")

                # Build the object to be indexed
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
            index_name="etendo_docs_index",
            objects=result_json
        )
    else:
        print("No HTML documents found to index.")


# Index the docs
index_docs(output_dir)

import os
import sys
import json
from bs4 import BeautifulSoup
from algoliasearch.search.client import SearchClientSync

def index_docs(output_dir, ALGOLIA_WRITE_INDEX_KEY):
    # Create the Algolia client using the passed key
    client = SearchClientSync("XMLZ1ZZEY7", ALGOLIA_WRITE_INDEX_KEY)
    
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

                # Extract h2, h3, h4 elements
                h2_elements = [h2.get_text(strip=True) for h2 in soup.find_all("h2")]
                h3_elements = [h3.get_text(strip=True) for h3 in soup.find_all("h3")]
                h4_elements = [h4.get_text(strip=True) for h4 in soup.find_all("h4")]

                # Extract tags
                tags = [tag.get_text(strip=True) for tag in soup.find_all(class_="md-tag")]

                # Try to get the canonical URL
                canonical_link = soup.find("link", rel="canonical")
                url = canonical_link["href"] if canonical_link else "No URL"

        
                # Replace the version in the URL with "latest"
                if url.startswith(base_url):
                    # Find the next slash after the base
                    idx = url.find('/', len(base_url))
                    if idx != -1:
                        # Replace whatever comes after base up to the next slash with "latest"
                        url = base_url + "latest" + url[idx:]
                    else:
                        # If there's no additional segment, just append "latest"
                        url = base_url + "latest"

                # Build the object to be indexed
                result = {
                    "objectID": url,
                    "title": title,
                    "h2": h2_elements,
                    "h3": h3_elements,
                    "h4": h4_elements,
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

def main():
    # Read the key from command line argument (e.g., sys.argv[1])
    if len(sys.argv) < 2:
        print("Usage: python index_docs.py <ALGOLIA_WRITE_INDEX_KEY>")
        sys.exit(1)

    ALGOLIA_WRITE_INDEX_KEY = sys.argv[1]
    output_dir = "site"

    index_docs(output_dir, ALGOLIA_WRITE_INDEX_KEY)

if __name__ == "__main__":
    main()

document.addEventListener("DOMContentLoaded", function () {
    // Algolia configuration
    const algoliaConfig = {
        appId: 'XMLZ1ZZEY7',
        apiKey: 'de992ae25d65509474690fe8761e2a21',
        indexName: 'etendo_docs_index'
    };

    // Select the search container
    const searchContainer = document.querySelector(".md-search");

    // Create or select the results container (80vh box)
    let resultsContainer = document.querySelector(".md-search__output");
    if (!resultsContainer) {
        resultsContainer = document.createElement("div");
        resultsContainer.className = "md-search__output";
        searchContainer.insertAdjacentElement("afterend", resultsContainer);
    }
    resultsContainer.innerHTML = "";
    resultsContainer.style.display = "none";

    const client = algoliasearch(algoliaConfig.appId, algoliaConfig.apiKey);
    const index = client.initIndex(algoliaConfig.indexName);
    const searchInput = document.querySelector("input.md-search__input");

    // Function to escape special characters in a string for regex
    function escapeRegExp(string) {
        return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    }

    // Helper: Convierte un texto en un slug (ej. "Bulk Posting" -> "bulk-posting")
    function slugify(text) {
        return text.toString().toLowerCase().trim()
            .replace(/\s+/g, '-')       // Reemplaza espacios con -
            .replace(/[^\w\-]+/g, '')    // Elimina caracteres no válidos
            .replace(/\-\-+/g, '-');     // Reemplaza múltiples guiones por uno solo
    }

    // Function to update the visibility of results based on the query
    function updateResultsVisibility() {
        const query = searchInput.value.trim();
        if (query === "") {
            resultsContainer.style.display = "none";
            resultsContainer.innerHTML = "";
        } else {
            performSearch(query);
        }
    }

    // Render the list of results and update the status with the number of hits
    function renderResults(hits, query) {
        resultsContainer.innerHTML = "";
        // Create a status element showing the number of matching documents
        const statusDiv = document.createElement("div");
        statusDiv.className = "md-search-status";
        statusDiv.textContent = `${hits.length} matching documents`;
        resultsContainer.appendChild(statusDiv);

        const ul = document.createElement("ul");
        ul.className = "md-search-result__list";

        // Split the query into words for tag matching
        const queryWords = query.toLowerCase().split(/\s+/).filter(Boolean);

        hits.forEach(hit => {
            const li = document.createElement("li");
            li.className = "md-search-result__item";

            const a = document.createElement("a");
            // Dynamic link building
            let finalUrl = hit.url;
            if (finalUrl) {
                const dynamicSuffix = `?h=${encodeURIComponent(query)}#${slugify(hit.title || "")}`;
                finalUrl += dynamicSuffix;
            }
            a.href = finalUrl;
            a.className = "md-search-result__link";
            a.setAttribute("tabindex", "-1");

            const iconDiv = document.createElement("div");
            iconDiv.className = "md-search-result__icon md-icon";

            const article = document.createElement("article");
            article.className = "md-search-result__article md-typeset";
            article.setAttribute("data-md-score", hit.score || "0");

            // --- Title ---
            const h1 = document.createElement("h1");
            if (hit.title) {
                const escapedQuery = escapeRegExp(query);
                // Regular expression to find the word containing the query (case-insensitive)
                const regex = new RegExp(`\\b([^\\s]*${escapedQuery}[^\\s]*)\\b`, 'gi');
                h1.innerHTML = hit.title.replace(regex, function(match, p1, offset) {
                    return offset > 0
                        ? `<span class="custom-highlight" style="margin-left:0.2em">${match}</span>`
                        : `<span class="custom-highlight">${match}</span>`;
                });
            } else {
                h1.textContent = hit.title;
            }
            article.appendChild(h1);

            // --- Combine sections (h2, h3, h4) ---
            let sectionsArray = [];
            if (hit.h2 && Array.isArray(hit.h2)) {
                sectionsArray = sectionsArray.concat(hit.h2);
            }
            if (hit.h3 && Array.isArray(hit.h3)) {
                sectionsArray = sectionsArray.concat(hit.h3);
            }
            if (hit.h4 && Array.isArray(hit.h4)) {
                sectionsArray = sectionsArray.concat(hit.h4);
            }
            if (sectionsArray.length > 0) {
                const sectionsElem = document.createElement("p");
                sectionsElem.className = "md-search-result__sections";
                sectionsElem.textContent = sectionsArray.join(", ");
                article.appendChild(sectionsElem);
            }

            // --- Tags ---
            if (hit.tags && Array.isArray(hit.tags)) {
                const nav = document.createElement("nav");
                nav.className = "md-tags";
                hit.tags.forEach(tag => {
                    const span = document.createElement("span");
                    span.className = "md-tag custom-tag";
                    const match = queryWords.some(word => tag.toLowerCase().includes(word));
                    if (match) {
                        span.innerHTML = `<span class="custom-tag-highlight">${tag}</span>`;
                    } else {
                        span.textContent = tag;
                    }
                    nav.appendChild(span);
                });
                article.appendChild(nav);
            }

            a.appendChild(iconDiv);
            a.appendChild(article);
            li.appendChild(a);
            ul.appendChild(li);
        });

        resultsContainer.appendChild(ul);
        resultsContainer.style.display = "block";
    }

    // Function to perform a search using Algolia and render the results
    function performSearch(query) {
        index.search(query)
            .then(({ hits }) => {
                renderResults(hits, query);
            })
            .catch(err => {
                console.error("Search error:", err);
            });
    }

    // Update results on input and focus events
    searchInput.addEventListener("input", updateResultsVisibility);
    searchInput.addEventListener("focus", updateResultsVisibility);

    // Initial state
    updateResultsVisibility();


    if (searchContainer) {
        const sectionFilter = document.createElement("select");
        sectionFilter.id = "section-filter";
        sectionFilter.innerHTML = `
            <option value="">All Sections</option>
            <option value="user-guide">User Guide</option>
            <option value="developer-guide">Developer Guide</option>
        `;
        searchContainer.insertAdjacentElement("afterend", sectionFilter);
        const resultsContainer = document.querySelector(".md-search__output");

        function applyFilter() {
            const filterValue = sectionFilter.value;
            const results = document.querySelectorAll(".md-search-result__item");

            results.forEach(result => {
                const resultUrl = result.querySelector("a").href;
                if (filterValue === "" || resultUrl.includes(`/${filterValue}/`)) {
                    result.style.display = "block";
                } else {
                    result.style.display = "none";
                }
            });
        }

        const observer = new MutationObserver(() => {
            applyFilter();
        });

        if (resultsContainer) {
            observer.observe(resultsContainer, { childList: true, subtree: true });
        }

        sectionFilter.addEventListener("change", function () {
            applyFilter();
        });
    }
});

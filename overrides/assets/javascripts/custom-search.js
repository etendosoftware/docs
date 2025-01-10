document.addEventListener("DOMContentLoaded", function () {
    const searchContainer = document.querySelector(".md-search");
    if (searchContainer) {
        const sectionFilter = document.createElement("select");
        const searchInput = document.querySelector("input.md-search__input")
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


        if (searchInput) {
            searchInput.addEventListener('input', function() {
                const query = searchInput.value.trim().toLowerCase();
  
                const results = window.search(query).sort((a, b) => {
                    // Priorizar coincidencias exactas
                    const aExactMatch = a.title.toLowerCase() === query || a.text.toLowerCase().includes(query);
                    const bExactMatch = b.title.toLowerCase() === query || b.text.toLowerCase().includes(query);
  
                    if (aExactMatch && !bExactMatch) return -1;
                    if (!aExactMatch && bExactMatch) return 1;
  
                    // Mantener el orden por relevancia
                    return b.rank - a.rank;
                });
  
                // Mostrar resultados ordenados
                displaySearchResults(results);
            });
        }

    }
});

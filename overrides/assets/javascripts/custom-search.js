document.addEventListener("DOMContentLoaded", function () {
    const searchContainer = document.querySelector(".md-search");
    if (searchContainer) {
        const sectionFilter = document.createElement("select");
        sectionFilter.id = "section-filter";
        sectionFilter.innerHTML = `
            <option value="">All Sections</option>
            <option value="user-guide">User Guide</option>
            <option value="developer-guide">Developer Guide</option>
        `;
        searchContainer.insertAdjacentElement("afterend", sectionFilter);

        // Función para aplicar el filtro
        function applyFilter() {
            const filterValue = sectionFilter.value;
            const results = document.querySelectorAll(".md-search-result__item");

            results.forEach(result => {
                const resultUrl = result.querySelector("a").href; // Obtener el href del enlace
                if (filterValue === "" || resultUrl.includes(`/${filterValue}/`)) {
                    result.style.display = "block"; // Mostrar solo los relevantes
                } else {
                    result.style.display = "none"; // Ocultar los demás
                }
            });
        }

        // Evento para actualizar resultados al cambiar el filtro
        sectionFilter.addEventListener("change", function () {
            applyFilter();
        });

        // Evento para filtrar dinámicamente mientras el usuario busca
        const searchInput = document.querySelector("input.md-search__input");
        searchInput.addEventListener("input", function () {
            applyFilter();
        });

        // Aplicar filtro al cargar
        applyFilter();
    }
});

document.addEventListener("DOMContentLoaded", function () {
    const searchClient = algoliasearch('XMLZ1ZZEY7', 'de992ae25d65509474690fe8761e2a21');
    const search = instantsearch({
        indexName: 'etendo_docs_index', 
        searchClient,
    });

    search.addWidgets([
        instantsearch.widgets.searchBox({
            container: '#searchbox',
            placeholder: 'Search',
        }),

        instantsearch.widgets.hits({
            container: '#hits',
            templates: {
                item: `
                    <div>
                        <a href="{{url}}" class="search-hit-title">
                            {{#helpers.highlight}}{ "attribute": "title" }{{/helpers.highlight}}
                        </a>
                        <p class="search-hit-content">
                            {{#helpers.highlight}}{ "attribute": "content" }{{/helpers.highlight}}
                        </p>
                    </div>
                `,
            },
        }),
    ]);

    search.start();
});

document.addEventListener('DOMContentLoaded', function() {
    // Configuración manual de Algolia
    const algoliaConfig = {
      appId: 'XMLZ1ZZEY7',       // Reemplaza con tus valores reales
      apiKey: 'de992ae25d65509474690fe8761e2a21', // Reemplaza con tus valores reales
      indexName: 'etendo_docs_index'           // Reemplaza con tus valores reales
    };
    
    // Inicializar DocSearch de Algolia
    if (typeof docsearch !== 'undefined') {
      docsearch({
        container: '#docsearch-container',
        appId: algoliaConfig.appId,
        apiKey: algoliaConfig.apiKey,
        indexName: algoliaConfig.indexName,
        placeholder: 'Buscar en la documentación',
        // Configura los atributos facetados y otras opciones según necesites
      });
      
      console.log('Algolia DocSearch inicializado');
    } else {
      console.error('DocSearch no está disponible. Verifica que la librería se ha cargado correctamente.');
    }
  });
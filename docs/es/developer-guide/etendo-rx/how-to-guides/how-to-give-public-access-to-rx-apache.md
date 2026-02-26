Esta guía ofrece un enfoque integral para hacer que el Etendo RX Edge Service sea accesible públicamente, garantizando al mismo tiempo una comunicación segura mediante cifrado SSL. El proceso implica el uso de Apache2, un software de servidor web popular, como proxy inverso. Esta configuración no solo facilita el acceso público, sino que también añade una capa adicional de seguridad al cifrar la transferencia de datos entre los clientes y el servidor.

### Requisitos previos

- Lea la [Guía del servidor de configuración](../../../developer-guide/etendo-rx/concepts/config-server.md) y la [Guía de Edge](../../../developer-guide/etendo-rx/concepts/edge-server.md)
- Etendo RX Edge Service configurado y en ejecución.
- Apache2 instalado en el servidor.
- Una configuración SSL válida
- Acceso root o sudo al servidor.

### Descargo de responsabilidad

Esta guía para configurar el acceso público al Etendo RX Edge Service usando Apache2 SSL Proxy abarca temas complejos que pueden ir más allá de su alcance, requiriendo conocimientos o experiencia adicionales:

* Configuración del servidor web Apache2: requiere habilidades básicas de administración de servidores web, incluida la configuración de hosts virtuales y la configuración de SSL.
* Certificados y cifrado SSL: se asume conocimiento sobre cómo obtener, renovar e instalar certificados SSL.
* Seguridad de red y firewalls: implica ajustar la configuración del firewall para el tráfico HTTPS.
* Configuración de proxy inverso: comprensión del funcionamiento y la configuración de los proxies inversos.

### Paso 1: Configurar Apache2 como un proxy inverso

1. **Habilitar módulos de proxy**: habilite los módulos de proxy necesarios en Apache2.

   ```shell
   sudo a2enmod proxy
   sudo a2enmod proxy_http
   ```

2. **Configurar los ajustes del proxy**: añada la siguiente configuración dentro del bloque `<VirtualHost>` en su archivo de host virtual SSL (`etendorx-ssl.conf`):

   ```apache
   <VirtualHost *:443>
       # ... SSL configurations ...

       ProxyPreserveHost On
       ProxyRequests Off
       ProxyPass / http://localhost:8096/
       ProxyPassReverse / http://localhost:8096/
   </VirtualHost>
   ```

   - Esta configuración reenvía todas las solicitudes desde el dominio expuesto públicamente al Etendo RX Edge Service que se está ejecutando en el puerto 8096.

3. **Reiniciar Apache2 de nuevo**:

   ```shell
   sudo systemctl restart apache2
   ```

### Paso 2: Verificar la configuración

1. **Prueba en el navegador**: abra un navegador web y navegue a `https://yourdomain.com`. Debería ver la interfaz de Etendo RX Edge Service, servida de forma segura a través de HTTPS.

2. **Comprobar la configuración SSL**: utilice una herramienta de comprobación SSL en línea para verificar que su certificado SSL está correctamente instalado y es válido.

### Paso 3: Configuración del firewall (opcional)

Si su servidor está protegido por un firewall, asegúrese de que el puerto 443 (HTTPS) esté abierto para las conexiones entrantes.

### Conclusión

Su Etendo RX Edge Service ahora es accesible públicamente con seguridad SSL proporcionada por Apache2. Esta configuración garantiza que el tráfico entre los clientes y su Edge Service esté cifrado y sea seguro. Recuerde mantener sus certificados SSL y Apache2 actualizados para garantizar la seguridad y el rendimiento.

---
Este trabajo está licenciado bajo :material-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-sa: [ CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="_blank"} por [Futit Services S.L](https://etendo.software){target="_blank"}.
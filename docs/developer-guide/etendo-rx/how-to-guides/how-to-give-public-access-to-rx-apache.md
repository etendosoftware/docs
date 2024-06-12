This guide offers a comprehensive approach to making the Etendo RX Edge Service publicly accessible while ensuring secure communication through SSL encryption. The process involves using Apache2, a popular web server software, as a reverse proxy. This setup not only facilitates public access but also adds an extra layer of security by encrypting data transfer between clients and the server.

### Prerequisites

- Read [Config Server Guide](../../../developer-guide/etendo-rx/concepts/config-server.md) and [Edge Guide](../../../developer-guide/etendo-rx/concepts/edge-server.md)
- Etendo RX Edge Service set up and running.
- Apache2 installed on the server.
- A valid SSL configuration
- Root or sudo access to the server.

### Disclaimer

This guide for setting up public access to the Etendo RX Edge Service using Apache2 SSL Proxy covers complex topics that may extend beyond its scope, requiring extra knowledge or expertise:

* Apache2 Web Server Configuration: Requires foundational web server management skills, including setting up virtual hosts and configuring SSL.
* SSL Certificates and Encryption: Assumes knowledge of obtaining, renewing, and installing SSL certificates.
* Network Security and Firewalls: Involves adjusting firewall settings for HTTPS traffic.
* Reverse Proxy Setup: Understanding the functioning and configuration of reverse proxies.

### Step 1: Configure Apache2 as a Reverse Proxy

1. **Enable Proxy Modules**: Enable the necessary proxy modules in Apache2.

   ```shell
   sudo a2enmod proxy
   sudo a2enmod proxy_http
   ```

2. **Configure Proxy Settings**: Add the following configuration inside the `<VirtualHost>` block in your SSL virtual host file (`etendorx-ssl.conf`):

   ```apache
   <VirtualHost *:443>
       # ... SSL configurations ...

       ProxyPreserveHost On
       ProxyRequests Off
       ProxyPass / http://localhost:8096/
       ProxyPassReverse / http://localhost:8096/
   </VirtualHost>
   ```

   - This configuration forwards all requests from the public-facing domain to the Etendo RX Edge Service running on port 8096.

3. **Restart Apache2 Again**:

   ```shell
   sudo systemctl restart apache2
   ```

### Step 2: Verify Configuration

1. **Browser Test**: Open a web browser and navigate to `https://yourdomain.com`. You should see the Etendo RX Edge Service interface, securely served over HTTPS.

2. **Check SSL Configuration**: Use an SSL checker tool online to verify that your SSL certificate is correctly installed and valid.

### Step 3: Firewall Configuration (Optional)

If your server is protected by a firewall, ensure that port 443 (HTTPS) is open for incoming connections.

### Conclusion

Your Etendo RX Edge Service is now accessible publicly with SSL security provided by Apache2. This setup ensures that the traffic between the clients and your Edge Service is encrypted and secure. Remember to keep your SSL certificates and Apache2 up to date for security and performance.
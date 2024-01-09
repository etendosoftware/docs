## Technical Guide for Public Access to Etendo RX Edge Service with Apache2 SSL Proxy

This guide offers a comprehensive approach to making the Etendo RX Edge Service publicly accessible while ensuring secure communication through SSL encryption. The process involves using Apache2, a popular web server software, as a reverse proxy. This setup not only facilitates public access but also adds an extra layer of security by encrypting data transfer between clients and the server.

### Prerequisites

- Read [Config Server Guide](developer-guide/etendo-rx/concepts/config-server/) and [Edge Guide](/developer-guide/etendo-rx/concepts/edge-server/)
- Etendo RX Edge Service set up and running.
- Apache2 installed on the server.
- A valid SSL configuration
- Root or sudo access to the server.

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

### Step 3: Verify Configuration

1. **Browser Test**: Open a web browser and navigate to `https://yourdomain.com`. You should see the Etendo RX Edge Service interface, securely served over HTTPS.

2. **Check SSL Configuration**: Use an SSL checker tool online to verify that your SSL certificate is correctly installed and valid.

### Step 4: Firewall Configuration (Optional)

If your server is protected by a firewall, ensure that port 443 (HTTPS) is open for incoming connections.

### Conclusion

Your Etendo RX Edge Service is now accessible publicly with SSL security provided by Apache2. This setup ensures that the traffic between the clients and your Edge Service is encrypted and secure. Remember to keep your SSL certificates and Apache2 up to date for security and performance.

### Disclaimer

This guide to configuring public access to the Etendo RX Edge Service with Apache2 SSL Proxy involves several advanced concepts and procedures that may require knowledge or skills beyond the scope of this document. The following areas are particularly complex and might necessitate additional research or expertise:

1. **Apache2 Web Server Configuration**: Understanding the intricacies of Apache2, including virtual host setup, module activation, and SSL configuration, requires a foundational knowledge of web server management. Users unfamiliar with Apache2 might need to consult additional resources or seek expert assistance.

2. **SSL Certificates and Encryption**: The guide assumes familiarity with SSL certificates, including acquisition, renewal, and installation processes. Users should have a basic understanding of how SSL/TLS encryption works and its importance in securing web communications.

3. **Network Security and Firewalls**: Adjusting firewall settings to allow HTTPS traffic involves a fundamental understanding of network security. Users should be cautious and aware of the implications of modifying firewall rules, especially in a production environment.

4. **Reverse Proxy Setup**: The concept of a reverse proxy and its role in forwarding requests from a public-facing server to a backend service can be complex. Understanding how a reverse proxy works and its configuration nuances is crucial for successful implementation.

5. **YAML Syntax and Configuration**: The guide touches upon YAML file configuration for the Etendo RX Edge Service. A solid grasp of YAML syntax and its role in configuration management is necessary for modifying service settings.

6. **Server and Domain Management**: The guide assumes that the user has control over a domain and understands the process of pointing a domain to a server, along with managing domain-related settings.

7. **Linux/Unix Command Line Proficiency**: Executing commands in a Linux/Unix environment, as suggested in the guide, requires basic to intermediate command-line skills.

This guide is intended for users with an intermediate level of technical expertise in these areas. Those with limited experience may need to seek additional resources or professional guidance to fully comprehend and safely implement the steps outlined in the guide.
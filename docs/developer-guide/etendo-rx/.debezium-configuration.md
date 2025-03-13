---
title: Debezium configuration
search:
  exclude: true
---
## Debezium configuration

### Postgres configuration

* Execute
```
> psql -h localhost -U postgres
```
* Obtain the config file location: 
```
> show config_file;
```

* Edit the **postgresql.conf** file. (Make sure that is not starting with the '#')
```
listen_addresses = '*'			## what IP address(es) to listen on;
wal_level = logical			   ## minimal, replica, or logical
```

* Obtain the hba file location
```
show hba_file;
```

* Add to the end of the file
```
hostnossl      all		all		all		md5
```

* Run
```
sudo service postgresql restart
```
### Docker compose configuration

* Add the ‘extra_hosts’ to the debezium services in the docker compose file

``` docker
debezium-ui:
  .
  .
  .
  extra_hosts:
    - "host.docker.internal:host-gateway"
```
``` docker
debezium:
  .
  .
  .
  extra_hosts:
    - "host.docker.internal:host-gateway"
```

### Debezium configuration

Follow the guide to [configure debezium](https://en/technical-documentation/etendo-environment/platform/HowToListenNewTablesInEtendoRX)

* Replace the **‘Hostname’** from **postgres** to **host.docker.internal**.

* Replace the **‘Database’** with the name of your local database.

* Edit the **Advanced Properties**

* Set the Replication Plugin to **pgoutput**

* Validate the connection

##### Kafka verification
Go to the kafka drop server http://localhost:9000/ and verify that your topic is created. When you make a change in a selected table (edit the primary key of a register), you should see in the logs of the kafka the commited changes.

* **Troubleshoots**
	* If the topic do not log the changes, and it was already created, try deleting the topic and running again the debezium configuration.
  
  * If the replication slot is already created, run the query `select pg_drop_replication_slot('debezium');`. Then run again the debezium configuration.
  
	

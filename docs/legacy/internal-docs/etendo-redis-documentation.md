---
title: Etendo Redis documentation
---
## Requirements

-   Configure tomcat to connect to Redis in your preferred way. Recommended: `tomcat-cluster-redis-session-manager` or `redisson-tomcat`

> When using Kubernetes and the Etendo Helm app, the configuration is already done. You will need to take note of the Redis host.

## Configuration

### Default configuration

-   Add the Redis URL to the Properties file in `config/Openbravo.properties`

```plaintext

redis.host=redis://localhost:6379
```

### Custom configuration

> This configuration overrides the host URI configuration

1.  Look for the file:

```plaintext

config/redisson-config.yaml
```

2.  If the file does not exist, create it by running:

```plaintext

## Run gradle setup
./gradlew setup
## Or copy the template directly if you already did the setup before
cp config/redisson-config.yaml.template config/redisson-config.yaml
```

3.  Edit the file `config/redisson-config.yaml` according to the [Redisson documentation](https://github.com/redisson/redisson/wiki/2.-Configuration#221-yaml-file-based-configuration).
4.  Add the path to the Redisson YAML configuration file to the Properties file in `config/Openbravo.properties`

```plaintext

redis.yaml=redisson-config.yaml
```

See [Redisson Wiki on YAML based configurations](https://github.com/redisson/redisson/wiki/2.-Configuration#221-yaml-file-based-configuration)

### Usage

Etendo introduces some special classes so you can cache values in your classes transparently. They will use Redis when the environment is configured, and otherwise they will fallback to standard Java classes. This way you don’t have to limit your developments to a Redis enabled environment.

Those classes are CachedSet, CachedConcurrentMap, and CachedList. You can use them as a Set, Map and List respectively which allows to port existing code easily, and all the common APIs you would expect are available.

This way the usage of those types is transparent whether Redis is being used or not.

For example:

```plaintext

private final Map<String, String> cache = new CachedMap<>("redisKey");
// redisKey is the name of the key that this map will create in Redis. 
// Make sure it is unique

/* ... */
cache.put("cachedKey", valueToCache)
/* ... */
String cachedValue = cache.get("cachedKey")
/* ... */
```

If you want to use all the capabilities of Redis, you will need to use the Redisson library directly, through the singleton class `RedisClient`.

From that client you can access the Redisson Client which contains access to all the Redis APIs.

```plaintext

// You should always check if the server is configured to use Redis when using the RedisClient directly
if (RedisClient.getInstance().isAvailable()) {
  RedissonClient client = RedisClient.getInstance().getClient();
  // Get Redis based implementation of java.util.concurrent.ConcurrentMap
  RMap<String, String> map = redisson.getMap("redisKey");
}
```

See [Redisson Java Docs](https://www.javadoc.io/doc/org.redisson/redisson/latest/) and [Redisson Documentation](https://github.com/redisson/redisson/wiki/Table-of-Content)

## JavaDoc

### RedisClient

```plaintext

  com.etendoerp.redis.RedisClient
```

Singleton which holds a RedissonClient instance. Use `isAvailable()` to check if the environment is configured to use redis. If the environment is available, then use `getClient()` to obtain the [RedissonClient](https://www.javadoc.io/doc/org.redisson/redisson/latest/org/redisson/api/RedissonClient.html) instance and operate on it.

```plaintext

  public static RedisClient getInstance()
  
```

**Returns:** this singleton's instance

```plaintext

public RedissonClient getClient()
```

**Returns:** the RedissonClient instance

```plaintext

public boolean isAvailable()
```

**Returns:** True when the the RedissonClient instance was created successfully.

If a server does not have a redis instance configured, this will return false.

```plaintext

protected void initialize()
```

Initialises the RedissonClient instance with some configuration Configuration is obtained from the Openbravo.properties file. The possible configurations are the default which is just the redis host URI, or a path to a custom YAML file

```plaintext

private InputStream getResource(String name)
```

Obtains a resource from the servlet context if available, or from this class context

**Parameters:** name — the name of the resource to find

**Returns:** the InputStream pointing to the requested resource, null if not found.

### CachedConcurrentMap

```plaintext

com.etendoerp.redis.interfaces.CachedConcurrentMap<K, V> implements ConcurrentMap<K, V>
```

A cached ConcurrentMap that uses Redis or in memory cache depending on the server configuration. Uses a org.redisson.api.RLocalCachedMap when a Redis server is configured, and ConcurrentHashMap otherwise.

**Parameters:**

-   `<K>` — the type of keys maintained by this map.
-   `<V>` — the type of mapped values. They must be Serializable to support Redis usage (refer to the Redisson documentation).

```plaintext

  public CachedConcurrentMap(String name)
  
```

Creates a Map using a Redis cache when possible.

**Parameters:**

-   `name` — key to use in Redis. (This is not used when Redis is not configured.)

```plaintext

public CachedConcurrentMap(String name, boolean localCache)
```

Creates a Map using a Redis cache when possible. When localCache is true, uses the default [LocalCachedMapOptions](https://www.javadoc.io/doc/org.redisson/redisson/latest/org/redisson/api/LocalCachedMapOptions.html)

**Parameters:**

-   `name` — key to use in Redis. (This is not used when Redis is not configured).
-   `localCache` — whether to use [org.redisson.api.RLocalCachedMap](https://www.javadoc.io/doc/org.redisson/redisson/latest/org/redisson/api/RLocalCachedMap.html) or a [org.redisson.api.RMap](https://www.javadoc.io/doc/org.redisson/redisson/latest/org/redisson/api/RMap.html)

```plaintext

 public CachedConcurrentMap(String name, boolean localCache, LocalCachedMapOptions<K, V> options)
 
```

Creates a Map using a Redis cache when possible.

-   `name` — key to use in Redis. (This is not used when Redis is not configured).
-   `localCache` — whether to use [org.redisson.api.RLocalCachedMap](https://www.javadoc.io/doc/org.redisson/redisson/latest/org/redisson/api/RLocalCachedMap.html) or a [org.redisson.api.RMap](https://www.javadoc.io/doc/org.redisson/redisson/latest/org/redisson/api/RMap.html)
-   `option` — [LocalCachedMapOptions](https://www.javadoc.io/doc/org.redisson/redisson/latest/org/redisson/api/LocalCachedMapOptions.html) cache options. Only used when localCache is true.

```plaintext

public CachedConcurrentMap(String name, boolean localCache, LocalCachedMapOptions<K, V> options, Integer initialCapacity)
```

Creates a Map using a Redis cache when possible.

-   `name` — key to use in Redis. (This is not used when Redis is not configured).
-   `localCache` — whether to use [org.redisson.api.RLocalCachedMap](https://www.javadoc.io/doc/org.redisson/redisson/latest/org/redisson/api/RLocalCachedMap.html) or a [org.redisson.api.RMap](https://www.javadoc.io/doc/org.redisson/redisson/latest/org/redisson/api/RMap.html)
-   `option` — [LocalCachedMapOptions](https://www.javadoc.io/doc/org.redisson/redisson/latest/org/redisson/api/LocalCachedMapOptions.html) cache options. Only used when localCache is true.
-   `initialCapacity` — map initial capacity. Only used when Redis is not available.

### CachedSet

```plaintext

public class CachedSet<E> implements Set<E>
```

A cached Set that uses Redis or in memory cache depending on the server configuration. Uses a [org.redisson.api.RSet](https://www.javadoc.io/doc/org.redisson/redisson/latest/org/redisson/api/RSet.html) when a Redis server is configured, and a HashSet otherwise.

**Parameters:**

-   `<E>` — the type of elements maintained by this set. They must be Serializable to support Redis usage (refer to the Redisson documentation).

```plaintext

public CachedSet(String name)
```

Creates a cached Set using Redis if its configured.

**Parameters:**

-   `name` — the key to use when storing in Redis. Unused when Redis is not available.

```plaintext

public CachedSet(String name, boolean useCache)
```

Creates a cached Set using Redis if its configured.

**Parameters:**

-   `name` — the key to use when storing in Redis. Unused when Redis is not available.
-   `useCache` — whether to use a [org.redisson.api.RSet](https://www.javadoc.io/doc/org.redisson/redisson/latest/org/redisson/api/RSet.html) or a [org.redisson.api.RSetCache](https://www.javadoc.io/doc/org.redisson/redisson/latest/org/redisson/api/RSetCache.html). Ignored when Redis is not available.

### CachedList

```plaintext

public class CachedList<E> implements List<E>
```

A cached Set that uses Redis or in memory cache depending on the server configuration. Uses a [org.redisson.api.RSet](https://www.javadoc.io/doc/org.redisson/redisson/latest/org/redisson/api/RSet.html) when a Redis server is configured, and a HashSet otherwise.

**Parameters:**

-   `<E>` — the type of elements maintained by this set. They must be Serializable to support Redis usage (refer to the Redisson documentation).

```plaintext

public CachedList(String name)
```

Creates a cached List using Redis if its configured.

**Parameters:**

-   `name` — the key to use when storing in Redis. Unused when Redis is not available.

```plaintext

public CachedList(String name, Codec codec)
```

Creates a cached List using Redis if its configured.

**Parameters:**

-   `name` — the key to use when storing in Redis. Unused when Redis is not available.
-   `codec` — the codec to use when serializing elements. See [Codec](https://www.javadoc.io/doc/org.redisson/redisson/latest/org/redisson/client/codec/Codec.html). Unused when Redis is not available.
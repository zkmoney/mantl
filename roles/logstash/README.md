# Logstash

Logging role for deploying and managing [Logstash](http://logstash.net)
with Docker and systemd as a part of the ELK stack.

## Variables

You can use these variables to customize your Logstash installations:

``` sourceCode yaml
logstash_output_elasticsearch:
  host: "elasticsearch.example.com"
  protocol: "http"
```

``` sourceCode yaml
logstash_output_kafka:
  broker_list: "broker1:port,broker2:port,..."
  topic_id: "logstash"
```


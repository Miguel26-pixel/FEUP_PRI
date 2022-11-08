FROM solr:9.0

COPY json_ds2.json /data/json_ds2.json

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]

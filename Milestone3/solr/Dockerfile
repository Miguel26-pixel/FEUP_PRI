FROM solr:8.1

COPY final_ds2.json /data/final_ds2.json

COPY schema_ds2.json /data/schema_ds2.json

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]

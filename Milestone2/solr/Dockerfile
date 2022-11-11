FROM solr:9.0

COPY final_ds2.json final_ds2.json

COPY schema_ds2.json schema_ds2.json

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]

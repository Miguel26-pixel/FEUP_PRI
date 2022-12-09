#!/usr/bin/env bash

precreate-core test_core

# Start Solr in background mode so we can use the API to upload the schema
solr start

sleep 3

# Schema definition via API
curl -X POST -H 'Content-type:application/json' \
    --data-binary @/data/schema_ds2.json \
    http://localhost:8983/solr/test_core/schema

# Populate collection
bin/post -c test_core /data/final_ds2.json

# Restart in foreground mode so we can access the interface
solr restart -f



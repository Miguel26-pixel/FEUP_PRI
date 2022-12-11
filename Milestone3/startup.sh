#!/usr/bin/env bash

precreate-core test_core

# Start Solr in background mode so we can use the API to upload the schema
solr start

# Schema definition via API
curl -X POST -H 'Content-type:application/json' \
    --data-binary schema_ds2.json \
    http://localhost:8983/solr/test_core/ds2

# Populate collection
bin/post -c test_core final_ds2_eng.json

# Restart in foreground mode so we can access the interface
solr restart -f



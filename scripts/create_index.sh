#!/usr/bin/env bash

es_port=9200
es_host="node2"
es_index="weixin"
JSON_FILE="weixin.json"

sed -i '2s/".*":/"'${es_index}'":/' ${JSON_FILE} && echo
curl -XDELETE 'http://'${es_host}':'${es_port}'/'${es_index}'?pretty' && echo
curl -XPUT 'http://'${es_host}':'${es_port}'/'${es_index} && echo
curl -XPUT 'http://'${es_host}':'${es_port}'/'${es_index}'/'${es_index}'/_mapping' -d @${JSON_FILE} && echo

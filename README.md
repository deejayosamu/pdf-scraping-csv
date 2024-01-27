Description
============

This space is made for the seminar work of `Information Retrieval & Knowledge Retrieval` course in FH Kufstein.<br><br>

- `pdf-scraping.ipynb`: extracts information from pdf file and make it csv files.
- `searching.ipynb`: search information using 'pysolr' module
- `getSome.py`: made for extracting information using regular expression
- `answer.py` : made for generating easy-look information
- `solr-9.4.0`: Apache Solr is an open-source search platform built on Apache Lucene.


Notice
=======

To use Apache solr, you should execute these commands.

1. Start SolrCloud.<br>`bin/solr start -e cloud`
2. Create collection.<br>`bin/solr create -c benz-price-list-new -s 2 -rf 2`
3. Generate Catchcall Copyfield.<br>`curl -X POST -H 'Content-type:application/json' --data-binary '{"add-copy-field" : {"source":"*","dest":"_text_"}}' http://localhost:8983/solr/films/schema`
4. Index the data.<br>`bin/post -c benz-price-list-new /data`
<br><br>
***
To delete collection,<br>
`bin/solr delete -c [collection_name]`<br><br>
To stop solr,<br>
`bin/solr stop -all`<br><br>
To restart,<br>
`./bin/solr start -c -p 8983 -s example/cloud/node1/solr` : restart node1<br>
`./bin/solr start -c -p 7574 -s example/cloud/node2/solr -z localhost:9983` : restart node2








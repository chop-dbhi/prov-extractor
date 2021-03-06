# PROV Extractor

[![Build Status](https://travis-ci.org/chop-dbhi/prov-extractor.svg?branch=master)](https://travis-ci.org/chop-dbhi/origins-extractor-service) [![Coverage Status](https://img.shields.io/coveralls/chop-dbhi/prov-extractor.svg)](https://coveralls.io/r/chop-dbhi/prov-extractor)

The PROV Extractor service exposes an HTTP interface for extracting provenance about the structure of common systems and formats. The provenance data is encoded in the [W3C PROV-JSON](http://www.w3.org/Submission/2013/SUBM-prov-json-20130424/) format for ease of use.

## Install

Docker image (recommended). All dependencies are included.

```
docker run -p 5000:5000 dbhi/prov-extractor
```

Manual. Extractor dependencies need to be installed manually.

```
pip install prov-extractor
```

**Optional Dependencies**

- `psycopg2`
- `pymysql`
- `Oracle-CX`
- `pymongo`
- `PyVCF`
- `PyMongo`
- `OpenPyXL`

## Supported Sources

- Relational Databases
    - PostgreSQL
    - MySQL
    - SQLite
    - Oracle
- Document Stores
    - Mongodb
- Delimited Files
    - CSV, TSV (any delimited)
- Data Dictionaries
    - Column-based attributes
- Microsoft Excel
- File System
- Variant Call Format (VCF) Files
- REDCap (MySQL)
- REDCap (REST API)
- REDCap (CSV)
- Harvest (REST API)
- GitHub Issues
- Git

## HTTP Interface

**`GET /`**

Return a list of available sources.

```bash
$ curl http://localhost:5000
[{
    "name": "postgresql",
    "description": "Extractor for PostgreSQL databases.",
    "links": {
        "self": "http://localhost:5000/postgresql/",
    },

    ...
}]

```

**`GET /<source>/`**

Return a description information and the POST options for extracting provenance from a source. The output is in the [JSON Schema](http://json-schema.org/) format.

```bash
$ curl http://localhost:5000/postgresql/
{
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "postgresql",
    "description": "Extractor for PostgreSQL databases.",
    "required": ["database"],
    "properties": {
        "database": {
            "description": "The name of the database."
            "type": "string",
        },
        "host": {
            "description": "The hostname of the server.",
            "type": "string",
            "default": "locahost",
        },
        "port": {
            "description": "The port of the server.",
            "type": "integer",
            "default": 5432,
        },

        ...
    }
}
```

**`POST /<source>/`**

Generates a provenance extract from the source.

```bash
$ curl -X POST -H 'Content-Type: application/json' http://localhost:5000/postgresql/ -d '
{
    "database": "chinook",
    "host": "213.48.19.100",
    "port": 5432,
    "user": "nobody",
    "password": "nothing"
}'
```

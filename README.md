# scrapy-cm
Scrapy crawlers for working with ContentMine

## Installation

1. Clone this repository. 
2. Change into this directory.
3. _Set up a Python3 virtualenv (optional but recommended)._
4. Install scrapy with `pip install scrapy`.

## Running a crawl

A single-item test crawl can be run by passing a `rows` parameter as well as the query:

    scrapy crawl ethosapi -a "query=coronavirus OR coronaviruses" -a "rows=1"

Once you're sure it's working, you can attempt to download all the hits:

    scrapy crawl ethosapi -a "query=coronavirus OR coronaviruses"

By default, the results will be output to a folder called `cproject`, using the [CProject](https://github.com/ContentMine/workshop-resources/blob/master/software-tutorials/cproject/README.md#what-is-a-cproject) layout. Some more details about the downloads will be placed in a `cm_results.jsonl` file (in [JSON Lines format](http://jsonlines.org/)) in the output directory.

The output directory can be altered by setting an environent variable. For example, if the CProject folder is called `/home/name/MyProject`, then do something like this (or an equivalent depending on what shell you use) before running the crawl:

    export CPROJECT_FOLDER="/home/name/MyProject"

When run, the spider should now place the results and log in your chosen folder.


### Medrxiv Example

There is also an experimental crawler for the Medrxiv preprint server. It can be run like this:

    scrapy crawl medrxiv -a "query=(virus* OR viral) AND epidemic*"

The <./run-medrxiv-test.sh> file shows an example of how to run a crawl and download to a particular folder.

Note that at present:

 - This spider has no `rows` parameter, so will always attempt to download all matching preprints.
 - The spider only tries to download PDFs, as it's not yet clear whether full-text HTML is available and, if so, how the crawler can tell when that is the case.


## Ideas

- Also support DOAJ API search and download.
- Dockerized version.
- Extend pipeline to generate `scholarly.html` from the `fulltext.pdf` using e.g. Apache Tika if it's available (via [the `item_completed` hook](https://docs.scrapy.org/en/latest/topics/media-pipeline.html#scrapy.pipelines.files.FilesPipeline.item_completed)).

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
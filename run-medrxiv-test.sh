#!/bin/sh

mkdir -p medrxiv-test
export CPROJECT_FOLDER="${PWD}/medrxiv-test"
echo "Outputting to ${CPROJECT_FOLDER}..."

echo "Running a Medrxiv query that should only have around 13 hits..."
scrapy crawl medrxiv -a "query=monte-carlo AND Tom"

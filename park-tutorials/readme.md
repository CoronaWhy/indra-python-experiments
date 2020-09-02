# My Experiments with the tutorials


## Intentions
These experiments are just baby steps to learn the massive Indra ecosystem (and, I'll confess, learn Python).

## Experiments
From time to time, I might create directories for outputs of these experiments for further study.

### indra8.py
This is a single PMCID test which performs all filtering. It is presently configured to run Reach running locally.
My experience running Reach locally is that it is sensitive to which version of Scala is in play. I found that it required version 2.12; it was developed on 2.11, but my Mac had 2.13 installed, so I had to bring down 2.12 and export the path to 2.12 before running the boot command, which is 
```sbt 'run-main org.clulab.reach.export.server.ApiServer'```

The process is simple: just clone the Reach repo, navigate to that directory, then boot it. It takes care of compiling by itself.

### indra9.py
This processes an array of PMCIds all the way through filtering and accumulating the final Statements in a single JSON file, as well as an HTML file for browsing.

Note that it is using the online version of Reach. There is a more up-to-date version of Reach which can be built and used by supplying the additional URL parameter to Reach.

### indra10.py
This is an experiment using PubMed search terms to collect Statements. It is incomplete since it does not go the whole distance and perform filtering.


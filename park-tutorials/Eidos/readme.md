#Eidos experiments
Eidos is a wrapper around the Indra ecosystem. It grants a web view, and can talk over a REST api

### eidos1.py
This is the first simple test suggested online

### eidos2.py
This is a complex sentence, conjunctive subjects and objects around a single predicate. In an ideal situation, it should be possible
to harvest at least 6 Statements from this sentence. Those statements, in a raw form, look like:

* { obesity, associated with, saturated fats }
* { obesity, associated with, palm oil }
* { type 2 diabetes mellitus, associated with, saturated fats }
* { type 2 diabetes mellitus, associated with, palm oil }
* { nonalcoholic fatty liver disease, associated with, saturated fats}
* { nonalcoholic fatty liver disease, associated with, palm oil }

### eidos-remote1.json
This is the output of the same sentence processed in eidos2.py. It is different in this sense:<br/>
It is returned by a remote call to Eidos from a Java client which will serve as a calling and processing agent in a machine reading platform.

### eidos-remote2.json
This is the output of a remote call to Eidos with the entire abstract from a PubMed document<br/>
https://pubmed.ncbi.nlm.nih.gov/17160142/



#exploring pubmed search

from indra import literature
from indra.sources import reach

#some constants
retmax = 100000
query = 'Magnesium AND CKD' #'elevated homocysteine' #'cardiac arrest' #'atrial fibrillation' #intention to run against an array of query strings 
#code
pmids = literature.pubmed_client.get_ids(query, retmax=retmax)

print('Got %d pmids' % len(pmids))
#print(pmids)
paper_contents = {}
for pmid in pmids:
    content, content_type = literature.get_full_text(pmid, 'pmid')
    if content_type == 'abstract':
        paper_contents[pmid] = content
    if len(paper_contents) == 10:
        break
#TODO need to move analysis up into the above loop
# in order to add PMID to each into the statements made from Reach so we can track docID
# WAIT! Below, we know what the pmid is; we can use that
literature_stmts = []
for pmid, content in paper_contents.items():
  print(pmid)
  print(content)
  rp = reach.process_text(content, url=reach.local_text_url)
  #TODO add a forloop here which takes all statements and adds pmid to the statement
  # then adds that statement to literature_stmts
  # turns out that doesn't work: sx == statement which is not JSON
  # appears we must store jSON objects in literature_stats to keep pmid around
  if rp:
    for stx in rp.statements:
      jstmt = {}
      jstmt.update({"pmid": pmid, "stmt": stx})
      print(jstmt)
      literature_stmts.append(jstmt)

print('Got %d statements' % len(literature_stmts))
for st in literature_stmts:
  print(st)
  #print('%s with evidence "%s"' % (st.stmt, st.stmt.evidence[0].text))

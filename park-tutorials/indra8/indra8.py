
from indra.tools import assemble_corpus as ac
from indra.statements import stmts_to_json_file
from indra.assemblers.html import HtmlAssembler
from indra.sources import reach
tp = reach.process_pmc('PMC4455820', url=reach.local_nxml_url)
if tp:
  stmts = tp.statements
  print(stmts)
  stmts = ac.filter_grounded_only(stmts)  # Filter out ungrounded agents
  stmts = ac.run_preassembly(stmts,       # Run preassembly
                            return_toplevel=False,
                            normalize_equivalences=True,     # Optional: rewrite equivalent groundings to one standard
                            normalize_opposites=True,        # Optional: rewrite opposite groundings to one standard
                            normalize_ns='WM')               # Use 'WM' namespace to normalize equivalences and opposites 
  stmts = ac.filter_belief(stmts, 0.8)    # Apply belief cutoff of e.g., 0.8
  stmts_to_json_file(stmts, 'PMC4455820.json')
  ha = HtmlAssembler(stmts)
  ha.save_model('PMC4455820.html')

# 
# 
# 
# 
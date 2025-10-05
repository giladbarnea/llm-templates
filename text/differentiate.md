Merge the given texts into a single text.
Avoid naive concatenation, which would have high recall but bad signal-to-noise ratio.
A good merge eliminates redundancies by selecting or creating the best version of any overlapping content.
The merge shouldn't be long—only as much as needed to capture the union of all points made.
Only tell me which points are shared between the texts, which are unique to the first text, and which are unique to the second text. If there are contradictory items between the texts, mention them. Contradictory items are those that cannot be trivially reconciled and would require semantic acrobatics to merge. Reference the item names as they appear in the original texts.
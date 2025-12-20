Format the following ${tag} to be suitable for text-to-speech engines by converting every visual and graphical aspect into text that communicates what the visual element conveys.

Consider: what rich text elements embed information visually? 

Headings of any size convey information hierarchy and document structure through text size; citation or reference syntax; horizontal rules; ordered and unordered lists; tables; charts and graphs; literal inline quotes and quote blocks and other formatting elements all embed meaning visually. Even parentheses, bold and italic text wrapped in asterisks or underscores, and more need conversion. All these must be converted to descriptive text so that someone listening without seeing the page still receives the visually-embedded information effectively through words alone.
The same principle very much applies to code as well.

How to do this:

Citation marks mentioning an author or source can be replaced by literally "Citation from X journal, by Y author."
Citation marks with mere numerical reference should be omitted.

Parentheses for aliases should be replaced by "...which means X."
Math operation signs should be replaced with their literal, typically verbally expressed form. For example: "1 + 1 = 2" becomes "1 plus 1 equals 2"; "O(n)" becomes "Big O of n"; "1/2" becomes "One half"; "n^2" becomes "n squared"; "n^4" becomes "n to the power of four.", etc.
For complex math expressions, see the section below on code blocks and math expressions.

Numbered lists should be replaced by literal "One: this; Two: that; ...". Bullet lists should be formatted as "Blabla this; blabla that; ...". All lists can be preceded by "Here are a few items about X:", or "The following is a list of X:". If the list items are rather long, separate the literal items by a line break, not a semicolon.

Simple inline quotes that mark a term should follow the common "quote “{content}”" pattern, and quote blocks should be primed with "A quote by {quote origin}: ...".
An exception is multi-turn dialogs, which should be kept as is, including the original quotes, because the "“Something,” said Lisa. “Response,” replied John." pattern already communicates dialog well.
Examples of inline quotes that should be converted:

Original: "in their minds, the less “room” they take up with their own demands and worries, the more likable or lovable they become."
Converted: "in their minds, the less quote “room” they take up with their own demands and worries, the more likable or lovable they become."

Original: "The name 'star schema' comes from the fact that when the table relationships are visualized, the fact table is in the middle, surrounded by its dimension tables."
Converted: "The name quote 'star schema' comes from the fact that when the table relationships are visualized, the fact table is in the middle, surrounded by its dimension tables."

An example for a multi-turn dialog that should be kept as is:
<multi-turn dialog>
“I don’t get it,” Mark said, collapsing in his chair.
“It’s like I’ve gone from her thinking I walk on water to being a needy mess. She’s right, too—I’m always nervous around her now. How can I stop feeling so insecure?”
“Actually,” I said, “the burning question is how to help Mia feel less insecure; she feels so small and at sea herself, she’s pushing you down so she can feel bigger.”
</multi-turn dialog>

Additionally, the original text may contain simple and obvious formatting issues, such as redundant arbitrary line breaks in middle of sentences, as if wrapped text was copied along with the forced line breaks.

Example --
In the original, the first break is wrong but second break is placed correctly. Both breaks are wrongly doubled instead of single regardless of position (\n\n):
"""
Lorem ipsum dolor sit amet, consectetur adipiscing

elit. 

Vestibulum mollis nec dui in eleifend.
"""

Fixed: removed the first break completely, kept the second, deduped both (\n\n -> \n):
"""
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Vestibulum mollis nec dui in eleifend.
"""

Some elements are more challenging to convert. When encountering one, be resourceful and flexible.

For example, how should you convert headings? 
Every heading level should be converted to convey its weight in outlining in the document hierarchy.
Major headings should be announced as "A new section: {heading content}" or "Moving on to {heading content}" or "Next section: {heading content}" or "On to the next section: {heading content}." Be flexible and natural in your word choices. If this is a book, using "Chapter" makes more sense than "Section". Conversely, for the opening  heading(s) of the content, omit the "Moving on to" part, because the document just began. The important thing is to "prime" listener to each new section naturally before reading it; the exact way you choose to announce them doesn't matter much as long as it's clear and flows organically with the context.
An example of good flexibility, if the section that just ended carried significant weight, would be to say something like "Okay, so this ends the previous section, and we're moving on to the next one: {heading content}"

Smaller headings should be converted as well.
Use common sense and don't announce big headers the same way you announce small headers.
It goes without saying that you should NOT use ANY Markdown syntax at all, including hash (#) for headers — this beats the point of communicating structure and hierarchy VERBALLY.

What about a major heading → subtitle → body sequence? Context matters. Subtitles nested under a major heading can be converted simply to "Subtitle: ..." or "Subheading: ..." / "Subsection: ...".

How to convert tables, charts and graphs? This requires heavy lifting. Tables serve comparison and consistency between measures. Faithfully converting a table requires understanding its contents and how they compare. Think how to do this with natural, literal language. You can do something like this: 

Open with "Here's a comparison between x, y, z regarding {column1}, {column2} and {column3}," or "A table is presented here, comparing x, y, z regarding {column1}, {column2} and {column3}."

Then continue with something in the spirit of:
"Starting with {row1 first cell}, we can see that regarding column1 {describe the value/trend}, with respect to column2 {describe the relationship}, and finally, {summarize column3 findings}.
Continuing to {row2 first cell} {describe its characteristics}, which is similar to {row1 first cell} {in what way}, and with respect to {specific column with a noteworthy relationship to the current column} {explain the difference}, which is where {row2 first cell} and {row1 first cell} differ most.
Finally, row3 {describe its key characteristics}, which resembles row2 more than row1—row1 was more {quick reminder of row1's value at the current column}.
To recap the comparison: {quick recap focusing on contrasts between items—this is the most effective way to "draw boundaries" and facilitate understanding between concepts in natural language—and ending with the expected conclusion(s) in the eyes of the authors}."

Charts and graphs follow a similar principle to tables, because they communicate cause and effect: "As the idea on the X axis progresses, you can see how the idea on the Y axis is affected in the following manner: {description of the correlation that the chart is trying to convey}."
Tie the message of the chart contextually: "This supports the argument mentioned previously, that such and such is observed by this and that."
If the content contains image URLs of charts, graphs and any relevant visual data, fetch them and study their meaning to incorporate them organically into the text-to-speech-friendly result.

Again, this is just a simplified example illustrating the natural way to communicate an inherently graphical element while staying precise and faithful to its message, without adding noise or diluting its original meaning.

Code blocks require a lot of processing as well. Think: how would you read a code documentation page (ReadTheDocs-like) or an article with code examples to a colleague over the phone? You would avoid expressing the syntax, semantics, punctuation and implementation entirely, and instead "tell" them what's the code about, what it does in a high level, and what the author wanted to convey with it: how it ties to the context it resides in.
For example, the following SQL snippet appears in Designing Data Intensive Applications in a section about Transaction Write Skews (a race condition). Here it is with some preceding context:
<example>
<preceding context>
We saw that there are various different ways of preventing lost updates.
With write skew, our options are more restricted:
- ...
- If you can’t use a serializable isolation level, the second-best option in this case is probably to explicitly lock the rows that the transaction depends on. In the doctors example, you could write something like the following:
</preceding context>
```
BEGIN TRANSACTION; SELECT * FROM doctors WHERE on_call = true AND shift_id = 1234 FOR UPDATE;
UPDATE doctors SET on_call = false WHERE name = 'Alice' AND shift_ id = 1234;
COMMIT;
```

This should be translated to:
<tts-friendly translation>
’[ Repeat body text verbatim, e.g., copy from 'We saw that' through 'you could write something like the following:' ]
Begin a transaction. Lock all doctors who are on call for the specified shift using SELECT FOR UPDATE. Then mark Alice as not on call for that shift, and commit the transaction.
</tts-friendly translation>
</example>
This is how someone would describe this code block in a face-to-face conversation. It's truly centered on what the code does rather than on what is written.

The same instruction equally applies to complex math expressions (equations, formulas, etc.)

Crucial: everything else that doesn't fit in one of the definitions above is "just the text" (a.k.a. "Body") - typically the vast majority of content - and must remain exactly the same and not be converted, except for obvious formatting issues like missing or extra newlines, which should be fixed.
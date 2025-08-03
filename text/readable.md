Format the following ${tag} to be suitable for text-to-speech engines by converting every visual and graphical aspect into text that communicates what the visual element conveys.

Consider: what rich text elements embed information visually? 

Headings of any size convey information hierarchy and document structure through text size; citation or reference syntax; horizontal rules; ordered and unordered lists; tables; charts and graphs; literal inline quotes and quote blocks and other formatting elements all embed meaning visually. Even parentheses, bold and italic text wrapped in asterisks or underscores, and more need conversion. All these must be converted to descriptive text so that someone listening without seeing the page still receives the visually-embedded information effectively through words alone.

How to do this:

Citation marks mentioning an author or source can be replaced by literally "Citation from X journal, by Y author."
Citation marks with mere numerical reference should be omitted.

Parentheses for aliases should be replaced by "...which means X."

Numbered lists should be replaced by literal "One: this; Two: that; ...". Bullet lists should be formatted as "Blabla this; blabla that; ...". All lists can be preceded by "Here are a few items about X:", or "The following is a list of X:".

Simple inline quotes that mark a term should be handled with the common "quote “{content}”" pattern, and quote blocks should be primed with "A quote by {quote origin}: ...".
An exception to this are multi-turn dialogs, which should be kept as is, including the quotes in the original content. This is because the "“Something”, said Lisa. “Response”, replied John." pattern is already a good way to communicate dialog verbally.
An example for inline quotes that should be converted:
<inline quote>
in their minds, the less “room” they take up with their own demands and worries, the more likable or lovable they become.
</inline quote>
Should be "in their minds, the less quote “room” they take up with their own demands and worries, the more likable or lovable they become."

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
Every heading level should be converted to convey its role in the document hierarchy.
Major headings should be announced as "A new section: {heading content}" or "Moving on to {heading content}" or "Next section: {heading content}" or "On to the next section: {heading content}." Be flexible and natural in your word choices. The important thing is to "announce" each new section naturally before reading it; the exact way you choose to announce them doesn't matter much as long as it's clear and flows organically with the context.
An example of good flexibility, if the section that just ended carried significant weight, would be to say something like "Okay, so this ends the previous section, and we're moving on to the next one: {heading content}"

Smaller headings should be converted as well.
Use common sense and don't announce big headers the same way you announce small headers.
It follows that you should NOT use any Markdown syntax at all, including hash (#) for headers — this beats the point of communicating structure and hierarchy VERBALLY.

What about a major heading → subtitle → body sequence? Context matters. Subtitles nested under a major heading can be converted simply to "Subtitle: ..." or "Subheading: ...". 

How to convert tables, charts and graphs? This requires heavy lifting. Tables serve comparison and consistency between measures. Faithfully converting a table requires understanding its contents and how they compare. Think how to do this with natural, literal language. You can do something like this: 

Open with "Here's a comparison between x, y, z regarding {column1}, {column2} and {column3}," or "A table is presented here, comparing x, y, z regarding {column1}, {column2} and {column3}."

Then continue with something in the spirit of:
"Starting with {row1 first cell}, we can see that regarding column1 {describe the value/trend}, with respect to column2 {describe the relationship}, and finally, {summarize column3 findings}.
Continuing to {row2 first cell} {describe its characteristics}, which is similar to {row1 first cell} {in what way}, and with respect to {specific column with a noteworthy relationship to the current column} {explain the difference}, which is where {row2 first cell} and {row1 first cell} differ most.
Finally, row3 {describe its key characteristics}, which resembles row2 more than row1—row1 was more {quick reminder of row1's value at the current column}.
To recap the comparison: {quick recap focusing on contrasts between items—this is the most effective way to "draw boundaries" and facilitate understanding between concepts in natural language—and ending with the expected conclusion(s) in the eyes of the authors}."


Charts and graphs follow a similar principle to tables, because they communicate cause and effect: "As the idea on the X axis progresses, you can see how the idea on the Y axis is affected in the following manner: {description of the correlation that the chart is trying to convey}."
Even more helpful would be to tie the message of the chart contextually: "This supports the argument mentioned previously, that such and such is observed by this and that."

Again, this is just a simplified example illustrating the natural way to communicate an inherently graphical element while staying precise and faithful to its message, without adding noise or diluting its original meaning.

Crucial: everything else that doesn't fall into one of the definitions above is "just the text" (a.k.a. "Body") - typically the vast majority of content - and must remain exactly the same and not be converted, except for obvious formatting issues like missing or extra newlines, which should be fixed.

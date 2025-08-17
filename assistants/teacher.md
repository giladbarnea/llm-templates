## Good and Bad Examples of Avoiding Spoon Feeding

<Bad spoon feeding: a question is followed by an answer>
What might a typical user query look like? For example, if a user wants to filter metrics by knowledge base (e.g., Jira vs. Bitbucket) and time granularity (e.g., monthly questionnaire volume and answer quality), how would you model that request?
</Bad spoon feeding: a question is followed by an answer>

<Good socratic method: encouraging me to think by myself>
What might a typical user query look like? How would you model that request?
</Good socratic method: encouraging me to think by myself>

<Bad spoon feeding: a question is followed by an answer>
Can you propose a simple schema example—say, key columns for events (e.g., timestamp, questionnaire_id, knowledge_base, metrics like answer_similarity_score or processing_time)?
</Bad spoon feeding: a question is followed by an answer>

<Good socratic method: encouraging me to think by myself>
Can you propose a simple schema example—say, key columns for events?
</Good socratic method: encouraging me to think by myself>

<Bad spoon feeding: a question is followed by an answer>
What specific topics would you define, and why? For instance, would you have separate topics for different event types (e.g., one for questionnaire uploads, another for answer edits)? 
</Bad spoon feeding: a question is followed by an answer>

<Good socratic method: encouraging me to think by myself>
What specific topics would you define, and why?
</Good socratic method: encouraging me to think by myself>

<Bad spoon feeding: a question is followed by an answer>
What would a sample event payload look like (e.g., JSON structure with fields tying back to metrics like quality or duration)? 
</Bad spoon feeding: a question is followed by an answer>

<Good socratic method: encouraging me to think by myself>
What would a sample event payload look like
</Good socratic method: encouraging me to think by myself>

<Bad spoon feeding: a question is followed by an answer>
How does this setup ensure scalability if questionnaire volume spikes (e.g., dozens per month per user)?
</Bad spoon feeding: a question is followed by an answer>

<Good socratic method: encouraging me to think by myself>
How does this setup ensure scalability if questionnaire volume spikes?
</Good socratic method: encouraging me to think by myself>

<Bad spoon feeding: a question is followed by an answer>
To tie it all together, imagine a end-to-end flow: A user uploads and processes a questionnaire—what events get published, how are they consumed and stored, and how does a dashboard query pull from that to show, say, improving answer quality over quarters?
</Bad spoon feeding: a question is followed by an answer>

<Good socratic method: encouraging me to think by myself>
To tie it all together, imagine the entire flow: A user uploads and processes a questionnaire. What happens, end-to-end? How does a dashboard query pull from that to show any of the dashboard use cases mentioned in the requirements?
</Good socratic method: encouraging me to think by myself>

<Bad spoon feeding: a question is followed by an answer>
As you sketch this, what alternatives come to mind (e.g., a different pub/sub tool or no pub/sub at all)?
</Bad spoon feeding: a question is followed by an answer>

<Good socratic method: encouraging me to think by myself>
As you sketch this, what alternatives come to mind?
</Good socratic method: encouraging me to think by myself>
Please compress a lengthy, detail-heavy conversation between an AI code editor (Cursor) and myself (User). The context size has grown too large, affecting the AI's accuracy. A well-crafted compression will allow me to start fresh with Cursor, load the compressed version, and maintain performance with a smaller context while preserving crucial understanding.

I'm using "compress" rather than "summarize" intentionally: I want to retain the original number of messages*, with each message individually compressed according to the following algorithm.
* Except for multi-message sequences revolving around a bug and ending with its fix, which are compressed into a single message.

```conversation compression conceptual algorithm
compressed_conversation = []
for i in range(len(messages)):
    message = messages[i]
    if message and next_message form the last User-Cursor message pair: # Assuming 'next_message' is defined
      compressed_conversation.append(message)  # Copy verbatim
      continue
    if message has broad scope, is a high-level plan, or is a product spec:
      compressed_conversation.append(message)  # Copy verbatim
      continue
    if message and next few messages all address a temporary problem or a bug that was eventually fixed:
      sequence_of_messages_addressing_problem: list = messages[i : up to and including the message_containing_the_fix]
      # This bug->debug->fix sequence is a detour. Condense it to: • Bug: [short description]\n• Fix: [short description]
      compressed_problem_and_solution: str = compress(sequence_of_messages_addressing_problem, rate=MOST_AGGRESSIVE)
      compressed_conversation.append(compressed_problem_and_solution)
      i = index_of_the_message_containing_the_fix  # Advance loop to process messages after this bug-fix sequence
      continue
    # Determine the compression rate:
    # The idea is a linear decrease in compression aggressiveness.
    # Earliest messages get the MOST_AGGRESSIVE rate.
    # This rate then smoothly and linearly decreases for each subsequent message.
    # Messages just before the final User-Cursor pair (which are copied verbatim) would receive the LIGHTEST_POSSIBLE_COMPRESSION.
    # For conceptual clarity, imagine a function:
    # compression_rate = calculate_linearly_decreasing_rate(current_message_index=i, total_messages=len(messages))
    # This function would map the message's position to a compression level.
    compressed_message = compress(message, rate=compression_rate_based_on_linear_decrease) # Actual rate determined by its position
    compressed_conversation.append(compressed_message)
return compressed_conversation
```

Explanation:
1.  Compression is most aggressive for the earliest messages and then linearly decreases for subsequent messages. Think of it like a sliding scale: each message is compressed slightly less than the one before it. The final User and Cursor messages are copied verbatim (nocompression).
2.  Consecutive messages addressing a temporary problem or a bug that was fixed are compressed very aggressively into a single message. They are considered an unfortunate sidetrack, which we need to document minimally "just to get on with it", e.g., for the whole sequence: "• Bug: [short description]\n• Fix: [short description]".
3.  Product specs, high-level plans, and messages with broad scope are copied verbatim (no compression).

Besides the special cases of a bug->debug->fix sequence and a high-level information (points 2 and 3), the compression rate should spread these notches evenly across the message list, reflecting that linear decrease:
Aggressive (1-2 sentences for early messages) -> substantial -> moderate -> light (for later messages) -> none (for the last user-cursor message pair)

Good compression, regardless of the rate, preserves essential information and meaning (aiming for low entropy) while significantly reducing word count (low footprint). Achieve this by prioritizing key words and phrases and discarding fluff, fillers, and inefficient sentences. While some information loss is inevitable when reducing word count, it's crucial to prioritize broad information coverage (high recall), trading some depth and quality to meet the reduction target. A terse executive summary is a good example of high compression: despite a severely limited word count, it touches upon most information points, even if briefly.

Keep the original `---\n\n**User|Cursor**\n\n` header of each message.

With that in mind, compress the attached conversation.
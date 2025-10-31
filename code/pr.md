Review this PR on two fronts:

1. Most important: false positives and false negatives. False positives = invented or extra logic/features not in the plan. False negatives = missing or unintentionally broken logic or features that previously worked before the change (i.e., an unintentional regression)
2. Nearly as important: hard bugs in the new “true positive” logic that wasn't eliminated in step (1) . Specifically, unequivocal bugs in state management, API usage, or similar. Not style or best practices—only concrete, real bugs.
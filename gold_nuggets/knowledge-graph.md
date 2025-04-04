# Professional Knowledge Capture

Given the following work note, extract all relevant entities and relations to store in the MCP Memory knowledge graph for optimal technical recall and searchability later.

## Work Note
[Date: YYYY-MM-DD]
[Full text of work note]

## Extract the following:

1. NOTE ID (use format "WorkNote-three-to-six-keywords-describing-the-note")
2. SYSTEMS/PRODUCTS mentioned (software, platforms, services)
3. TECHNICAL TOPICS discussed (both explicit and implicit)
4. PROBLEMS/CHALLENGES encountered or addressed
5. SOLUTIONS/IMPLEMENTATIONS described
6. INSIGHTS/LEARNINGS discovered

For each category, be thorough and include both explicitly mentioned and implied elements. Prioritize recall over precision - if something might be relevant, include it.

Then generate the exact MCP Memory commands needed to store this information:
1. Commands to create the work note entity
2. Commands to create/ensure all other entities exist
3. Commands to create relations from the work note to all entities
4. Commands to create meaningful relations between entities themselves

---

# Example

Given the following work note, extract all relevant entities and relations to store in the MCP Memory knowledge graph for optimal technical recall later.

## Work Note
[Date: 2025-03-05]
The Descope auth key also controls the read/write permissions per individual REST endpoint in the platform backend. For example, the public descope key used by the frontend SDK can only write to the /events-collect/v1/events. Writing e2e tests for events-collect/v1/events proved infeasible due to the need to set up or mock test-dedicated authentication. We decided not to write e2e tests at this point in time.

## Involved:
- Descope
- Authentication Permissions
- REST Endpoints
- Platform Backend
- Frontend
- SDK
- events-collect/v1/events REST Endpoint
- End-to-end tests

## Relations:
Descope:
- Responsible for authentication
- Enforces read/write permissions on REST Endpoints
- Provides API Keys

Platform Backend:
- Exposes REST Endpoints
- Has to do with Events Collection

Frontend:
- Uses SDK to capture events

SDK:
- Makes POST requests to the events-collect/v1/events endpoint
- Authenticates with a public Descope API key with write permissions to the events-collect/v1/events endpoint

events-collect/v1/events:
- REST API endpoint for collecting events




## Extract the following:

1. NOTE ID: WorkNote-descope-auth-key-controls-read-write-permissions
2. SYSTEMS/PRODUCTS: Descope, Platform Backend, Frontend, SDK, events-collect, events-collect/v1/events, End-to-end tests
3. TECHNICAL TOPICS: Authentication, REST Endpoints, Permissions, Events, Collection, Events Collection, Testing, End-to-end tests, API Keys
4. PROBLEMS/CHALLENGES: "Writing e2e tests for events-collect/v1/events proved infeasible due to the need to set up or mock test-dedicated authorization."
5. SOLUTIONS/IMPLEMENTATIONS: "Decided not to write e2e tests at this point in time."
6. INSIGHTS/LEARNINGS: "The descope auth key controls the read/write permissions per individual REST endpoint in the platform backend.", "The public descope key used by the frontend SDK can only write to /events-collect/v1/events."

MCP Memory Commands:

```jsonc
// 1. Create the WorkNote
create_entities({
  "entities": [{
    "name": "WorkNote-descope-auth-key-controls-read-write-permissions",
    "entityType": "WorkNote",
    "observations": [
      "The descope auth key also controls the read/write permissions per individual REST endpoint in the platform backend. For example, the public descope key used by the frontend SDK can only write to /events-collect/v1/events."
    ]
  }]
})

// 2. Ensure Systems/Products entities exist
create_entities({
  "entities": [
    {"name": "Descope", "entityType": "System", "observations": ["Authentication service", "Used by the frontend SDK to authenticate requests to the backend"]},
    {"name": "Platform Backend", "entityType": "System", "observations": ["Backend service with REST endpoints", "Contains the events-collect/v1/events endpoint", "Does Events Collection", "Communicates with the frontend SDK via REST"]},
    {"name": "Frontend", "entityType": "System", "observations": ["Utilizes the SDK to capture events"]},
    {"name": "SDK", "entityType": "Project", "observations": ["Used by the frontend to capture events", "Makes POST requests to the events-collect/v1/events endpoint", "Authenticates with a Descope API key with write permissions to the events-collect/v1/events endpoint"]},
    {"name": "events-collect/v1/events", "entityType": "REST Endpoint", "observations": ["REST API endpoint for collecting events"]},
	{"name": "End-to-end tests", "entityType": "Test", "observations": ["Weren't written due to effort associated with setting up test-specific authorization"]}
  ]
})

// 3. Create/ensure Technical Topic entities exist
create_entities({
  "entities": [
    {"name": "Authentication", "entityType": "TechnicalTopic", "observations": ["Nigh-synonyms: Authorization"]},
    {"name": "Permissions", "entityType": "TechnicalTopic", "observations": ["Read/write access controls", "Enforced by Descope", "Nigh-synonyms: Credentials"]},
    {"name": "Events", "entityType": "TechnicalTopic", "observations": ["Data collected from users"]},
    {"name": "Events Collection", "entityType": "TechnicalTopic", "observations": ["User data is collected from the frontend via the SDK and sent to the backend"]},
	{"name": "REST Endpoints", "entityType": "TechnicalTopic", "observations": ["Exposed by the Platform Backend", "Requested by the Frontend SDK", "Have to do with Events Collection"]},
	{"name": "API Keys", "entityType": "TechnicalTopic", "observations": ["Dictate access permissions to REST Endpoints", "Publicly used by the Frontend SDK to authenticate requests to the backend"]},
	{"name": "Testing", "entityType": "TechnicalTopic", "observations": []},
  ]
})

// 4. Create/ensure Problem/Challenge entities exist
create_entities({
  "entities": [
    {"name": "Writing e2e tests for events-collect/v1/events", "entityType": "Problem", "observations": []}
  ]
})

// 5. Create/ensure Solution/Implementation entities exist
create_entities({
  "entities": [
    {"name": "Decided not to write e2e tests at this point in time.", "entityType": "Solution", "observations": ["Infeasible due to the need to set up or mock test-dedicated authorization"]}
  ]
})

// 6. Create/ensure Insight/Learning entities exist
create_entities({
  "entities": [
    {"name": "Descope auth key controls read/write permissions per endpoint", "entityType": "Insight", "observations": ["Authentication mechanism"]},
	{"name": "The public descope key used by the frontend SDK can only write to /events-collect/v1/events", "entityType": "Insight", "observations": []},
  ]
})

// 7. Connect WorkNote to all relevant entities
create_relations({
  "relations": [
    {"from": "WorkNote-descope-auth-key-controls-read-write-permissions", "to": "Descope", "relationType": "mentions"},
    {"from": "WorkNote-descope-auth-key-controls-read-write-permissions", "to": "Platform Backend", "relationType": "mentions"},
    {"from": "WorkNote-descope-auth-key-controls-read-write-permissions", "to": "Frontend", "relationType": "mentions"},
    {"from": "WorkNote-descope-auth-key-controls-read-write-permissions", "to": "Authentication", "relationType": "involves"},
    {"from": "WorkNote-descope-auth-key-controls-read-write-permissions", "to": "Authorization", "relationType": "involves"},
    {"from": "WorkNote-descope-auth-key-controls-read-write-permissions", "to": "REST Endpoints", "relationType": "involves"},
    {"from": "WorkNote-descope-auth-key-controls-read-write-permissions", "to": "Permissions", "relationType": "involves"},
    {"from": "WorkNote-descope-auth-key-controls-read-write-permissions", "to": "Service Calls", "relationType": "involves"},
    {"from": "WorkNote-descope-auth-key-controls-read-write-permissions", "to": "Permission Checking", "relationType": "addresses"},
    {"from": "WorkNote-descope-auth-key-controls-read-write-permissions", "to": "Authorization Check", "relationType": "describes"},
    {"from": "WorkNote-descope-auth-key-controls-read-write-permissions", "to": "Descope auth key controls read/write permissions per endpoint", "relationType": "contains"},

  ]
})

// 8. Create meaningful connections between entities
create_relations({
  "relations": [
    {"from": "Descope", "to": "Authentication", "relationType": "provides"},
    {"from": "Descope", "to": "Permissions", "relationType": "enforces"},
    {"from": "Descope", "to": "API Keys", "relationType": "provides"},
	
    {"from": "REST Endpoints", "to": "Permissions", "relationType": "access governed by"},
    {"from": "REST Endpoints", "to": "Platform Backend", "relationType": "exposed by"},
	
	{"from": "API Keys", "to": "REST Endpoints", "relationType": "controls access to"},
    
	{"from": "Frontend Service", "to": "Service Calls", "relationType": "makes"},
    {"from": "Permission Checking", "to": "Authorization Check", "relationType": "addresses"},
  ]
})
```

## Technical Knowledge Management Tips

1. **Be systematic with technical terms**: Use consistent terminology for systems, libraries, and technologies
2. **Capture implementation details**: Focus on specifics you might forget, like config settings or API behaviors
3. **Include cross-dependencies**: Note how changes to one system affect others
4. **Record gotchas and edge cases**: These are particularly valuable for future recall
5. **Tag with related technologies**: Even when not explicitly mentioned (e.g., if discussing Descope, tag with OAuth if relevant)
6. **Link to architectural concepts**: Connect specific implementations to broader patterns and principles

When querying later, you can use technical terms, system names, or problem areas to retrieve comprehensive results:

```
// Search for all authentication-related notes
search_nodes({"query": "Authentication OR Descope OR OAuth"})

// Search for endpoint-related information
search_nodes({"query": "REST Endpoints OR API"})
```

This approach ensures you'll be able to retrieve critical technical details months later when you inevitably need to remember "that one thing about Descope permissions" or similar hard-to-remember implementation details.

---

```mdx
{/* started conversation with HelpfulAssistant 06.03 
<Knowledge-Graph-Instructions>

# Professional Knowledge Capture

Given the following work note, extract all relevant entities and relations to store in the MCP Memory knowledge graph for optimal technical recall and searchability later.

## Work Note

[Date: YYYY-MM-DD]

[Full text of work note]

## Extract the following:

1. NOTE ID (use format "WorkNote-three-to-six-keywords-describing-the-note")

2. SYSTEMS/PRODUCTS mentioned (software, platforms, services)

3. TECHNICAL TOPICS discussed (both explicit and implicit)

4. PROBLEMS/CHALLENGES encountered or addressed

5. SOLUTIONS/IMPLEMENTATIONS described

6. INSIGHTS/LEARNINGS discovered

For each category, be thorough and include both explicitly mentioned and implied elements. Prioritize recall over precision - if something might be relevant, include it.

Then generate the exact MCP Memory commands needed to store this information:

1. Commands to create the work note entity

2. Commands to create/ensure all other entities exist

3. Commands to create relations from the work note to all entities

4. Commands to create meaningful relations between entities themselves

---

# Example

Given the following work note, extract all relevant entities and relations to store in the MCP Memory knowledge graph for optimal technical recall later.

## Work Note

[Date: 2025-03-05]

The Descope auth key also controls the read/write permissions per individual REST endpoint in the platform backend. For example, the public descope key used by the frontend SDK can only write to /events-collect/v1/events. Writing e2e tests for events-collect/v1/events proved infeasible due to the need to set up or mock test-dedicated authorization. We decided not to write e2e tests at this point in time.

## Extract the following:

1. NOTE ID: WorkNote-descope-auth-key-controls-read-write-permissions

2. SYSTEMS/PRODUCTS: Descope, Platform Backend, Frontend, SDK, events-collect, events-collect/v1/events, End-to-end tests

3. TECHNICAL TOPICS: Authentication, REST Endpoints, Permissions, Events, Collection, Events Collection, Testing, End-to-end tests, API Keys

4. PROBLEMS/CHALLENGES: "Writing e2e tests for events-collect/v1/events proved infeasible due to the need to set up or mock test-dedicated authorization."

5. SOLUTIONS/IMPLEMENTATIONS: "Decided not to write e2e tests at this point in time."

6. INSIGHTS/LEARNINGS: "The descope auth key controls the read/write permissions per individual REST endpoint in the platform backend.", "The public descope key used by the frontend SDK can only write to /events-collect/v1/events."

</Knowledge-Graph-Instructions>

---

Help me work on the attached WIP instructions. In the instructions, I need to specify the relations between the defined entities, as mentioned in the attached text, systematically.

For example, the Descope relations:

Responsible for authentication

Enforces permissions

Provides API keys

Platform Backend:

Exposes REST Endpoints

Contains the events-collect/v1/events endpoint

Does Events Collection

Frontend:

Uses the SDK to capture events

SDK:

Makes POST REST requests to events-collect/v1/events endpoint

Used to capture events

Authenticates with a public Descope API key

events-collect/v1/events REST endpoint:

Entrypoint for capturing events

End-to-end tests:

Require setting up or mocking test-dedicated authorization


*/}
```
In this project, communication between components occurs via REST calls, pub/sub with NATS, or code import and execution. I need help mapping out a call hierarchy tree starting from a specific entry point. This is challenging because communication via both REST and pub/sub cannot be inferred through static analysis. REST endpoints, NATS consumer registrations, and publish expressions can only be identified through strings.

For example, core/data/events-pipeline/events-commit/src/main.py defines:
```python
@consumer.worker(stream="events-pipeline", subject="commit")
async def commit_events(events: list[ReportedEvent]):
```

Publish expressions must be located by grepping for `events-pipeline.commit` or even `events-pipeline` in general. Additionally, multiple consumers can be defined for each stream.subject.

Similarly for REST endpoints; application/agents/src/agents/agents/controller.py defines:
```python
@router.post("/")
async def run_hunch(body: HunchRequest):
```

This only indicates that the last part of the URL is /run_hunch; to determine the complete URL, we must traverse the router-tree through a combinationof static analysis and resourcefulness. In the agents/controller.py example, the top of the file defines `router = get_router("/hunch", "v1")` — giving us the preceding part, so now we have 'hunch/run_hunch'. Next, we need to determine who imports and uses `router`. It's imported by application/agents/src/agents/router.py — `from agents.agents.controller import router as agent_router` — note the import alias — and used as:
```python
router = APIRouter(prefix="/agents")
router.include_router(agent_router)
```

We now have another piece, and continuing up the tree to application/agents/src/main.py, we finally see that the agents router is imported to be passed to init_server.

Another point about NATS: Subjects can include star-wildcards like `"*.run-job"` which match only one token in the subject (e.g., `foo.run-job`), can be dynamically defined like `f"{job_id}.*"`, or use the greater-than wildcard like `"events-pipeline.>"` which matches one or more subject tokens (e.g., `events-pipeline.foo.bar.baz`). This is not trivial and, as I mentioned, requires resourcefulness.

Tips:
1. The frontend only communicates with the `analytics` sub-project, which serves as the gateway for the rest of the backend.
2. data-sdk often acts as the interface and glue between different services, functioning as a middleman and wrapping DB and pub/sub operations (ClickHouse/ch and NATS "eventing").

Let's start with core/data/events-pipeline/events-collect/src/router.py collect_events.
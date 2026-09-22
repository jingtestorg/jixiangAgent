# Specification: hello-world-agent

> **Guidelines**: Read all applicable guidelines before executing ANY tasks below:
> - [guidelines.md](../guidelines.md) — Universal execution rules
> - [guidelines-agent.md](../guidelines-agent.md) — Universal agent patterns
> - [guidelines-agent-python.md](../guidelines-agent-python.md) — Python implementation details
> - [guidelines-agent-skills.md](../guidelines-agent-skills.md) — Runtime skills patterns
> - [guidelines-agent-mcp.md](../guidelines-agent-mcp.md) — MCP integration patterns

---

## Basic Setup

- [x] Read the project input (`product-requirements-document.md`, `intent.md`)
- [x] Bootstrap agent code in `assets/hello-world-agent/` using instructions from the sap-agent-bootstrap section. (invoke from inside `assets/hello-world-agent/`, use copy commands — do NOT create files manually)
- [x] Install dependencies, validate the agent starts and responds at `/.well-known/agent.json`

---

## Runtime Skills

No runtime skills needed — this is a single-step demo agent with no complex multi-step workflows or domain-specific knowledge requirements.

---

## Project-Specific Tasks

## REQ-01: Receive and Process Any Message

- [x] Verify the bootstrapped agent's `stream()` method accepts any non-empty input message via the A2A protocol
- [x] Confirm `/.well-known/agent.json` is accessible and returns valid agent metadata after startup

## REQ-02: Respond with "Hello World"

- [x] Open `assets/hello-world-agent/app/agent.py` and update the `@prompt_section` body (`get_system_prompt`) so the system prompt instructs the LLM to always respond with "Hello World" regardless of the input message
- [x] Verify that any input message results in a response containing "Hello World"

## REQ-03: Deploy to SAP BTP via A2A Protocol

- [x] Invoke the `setup-solution` skill to create `solution.yaml` and `assets/hello-world-agent/asset.yaml`
- [x] Confirm `asset.yaml` references the correct asset name `hello-world-agent` and type `agent`
- [x] Confirm `solution.yaml` is valid and references the `hello-world-agent` asset

---

## Business Instrumentation

- [x] Implement business step instrumentation for all three milestones from the PRD, using structured logging (`[MILESTONE_ID].[achieved|missed]: [description]`) and OpenTelemetry custom spans:
  - **M1** — Message Received: log `M1.achieved: message received and processing started` when a non-empty message is received; log `M1.missed: message handler was not invoked or input was empty` otherwise
  - **M2** — Response Delivered: log `M2.achieved: Hello World response delivered successfully` when the "Hello World" response is emitted; log `M2.missed: response generation failed or returned empty` otherwise
  - **M3** — Deployment Verified: log `M3.achieved: agent endpoint verified on SAP BTP` on successful deployment verification; log `M3.missed: deployment or endpoint verification failed` on failure
- [x] Extract business logic from `stream()` into a plain async helper to avoid `GeneratorExit` context errors (see guidelines-agent-python.md)
- [x] Verify `bootstrap(app)` is called after `app = server.build()` in `main.py`

---

## MCP Tool Integration

No MCP servers or external APIs required for this use case. Skip all MCP wiring tasks.

---

## Testing

- [x] `conftest.py` only sets `IBD_TESTING=true`
- [x] Write one integration test in `assets/hello-world-agent/tests/` that executes the end-to-end agent flow: calls the agent's `invoke` function with a sample message and asserts the response contains "Hello World" (mocked LLM responses, runs offline)
- [x] Run `pytest` from `assets/hello-world-agent/` (no args) — if coverage < 70%, add tests until threshold is met
- [x] Verify `assets/hello-world-agent/app/agent.py` has exactly 9 decorated functions — run `grep -c "^@agent_model\|^@agent_config\|^@prompt_section" assets/hello-world-agent/app/agent.py` and confirm it returns 9; if more than 9, remove extras and replace with plain Python constants
- [x] Run `pytest` again from `assets/hello-world-agent/` (no args) to generate final `test_report.json`
- [x] Verify `test_report.json` exists in `assets/hello-world-agent/` — if not, run pytest again until it does

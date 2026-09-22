# Hello World Agent

A minimal AI agent demonstration on SAP BTP that responds "Hello World" to any incoming message.

## Business challenge

A developer or engineer exploring SAP BTP needs a simple, working AI agent to verify the platform setup and understand how agents are built and deployed. The agent must receive a message and reliably respond with "Hello World".

## Business Goals & Success Criteria

| Metric | Baseline | Target | Timeline | Process / Capability | Source |
|--------|----------|--------|----------|----------------------|--------|
| Correct response to any message | — | 100% of messages return "Hello World" | — | IT Service Development / Agent Verification | user |

## Key Milestones

- **M1 — Message Received**: Agent successfully receives an incoming message from a user or system.
- **M2 — Response Delivered**: Agent returns "Hello World" as the response.
- **M3 — Deployment Verified**: Agent is deployed to SAP BTP and accessible via the A2A protocol endpoint.

## Business Architecture (RBA)

### End-to-End Process

Manage Information Technology

### Process Hierarchy

```
Manage Information Technology (E2E)
└── Manage Information Technology (Phase)
    └── Develop or acquire IT services (BPS-457_001)
        └── Acquire IT infrastructure and solutions
```

### Summary

This demonstration agent maps to the "Manage Information Technology" E2E process, specifically the sub-process of developing or acquiring IT services — representing a developer validating their SAP BTP agent infrastructure.

## Fit Gap Analysis

| Requirement (business) | Standard asset(s) found | API ORD ID | MCP Server ORD ID | MCP Server Version | Webhook API ORD ID | Data Product ORD ID | Gap? | Notes / assumptions |
|------------------------|-------------------------|------------|-------------------|--------------------|--------------------|---------------------|------|---------------------|
| Agent receives and responds to messages | SAP AI Core (runtime) | — | — | — | — | — | No | Python A2A agent handles this natively on SAP BTP |
| Platform deployment verification | SAP BTP / SAP Build | — | — | — | — | — | No | Covered by standard deploy-solution skill |

### Key findings

- No external SAP APIs or MCP servers are required for a Hello World agent.
- SAP AI Core provides the LLM runtime; no custom integrations are needed.
- The fit-gap analysis confirms no capability gaps — standard SAP BTP tooling fully covers this use case.
- SAP LeanIX tools are available for IT architecture management but are not needed for this demo.
- All requirements are met with the standard Python A2A agent pattern.

## Recommendations

### Hello World AI Agent on SAP BTP

#### Executive Summary

Minimal Python A2A agent deployed on SAP BTP for platform validation.

#### Recommended Solution

A pro-code Python agent using the A2A protocol, bootstrapped with the SAP agent template. The agent uses SAP AI Core as the LLM backend and is instrumented with OpenTelemetry for observability. It responds to any incoming message with "Hello World".

#### Recommended solution category

AI Agent

#### Intent fit
95%

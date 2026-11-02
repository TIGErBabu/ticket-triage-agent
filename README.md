# ticket-triage-agent

A support-ticket triage agent. It reads a ticket, classifies it, routes it to the
right queue, drafts a reply, and escalates to a human when it isn't confident.

## Why this project

My first project (doc-chat-rag) proved I can build RAG. This one is about the two
things that actually separate an AI engineer from someone who wired up an API
once: agents that take actions, and evals — measuring whether the agent is any
good instead of vibes-checking three examples and calling it done.

## What it does (v1 scope)

1. Take in a support ticket (subject, body, customer tier, product area).
2. Classify it: category, priority, sentiment.
3. Route it to a queue: billing / technical / account / general.
4. Draft a reply grounded in a small help-center knowledge base.
5. Escalate to a human when confidence is low, or the ticket is high-priority
   and angry. Both happen in support constantly; pretending otherwise makes a
   demo, not a tool.

## Architecture (planned)

- LangGraph state machine: classify -> route -> draft -> confidence gate ->
  send or escalate
- Tool calling: knowledge-base search, ticket-history lookup, queue assignment
- Evals: a labeled ticket set; score classification accuracy, routing accuracy,
  and escalation precision/recall
- Observability: Langfuse traces, prompt versions, latency and cost per run
- FastAPI front door, Docker locally, AWS for the deployed demo

## Trade-offs I'm thinking about

- Hand-rolled evals before any eval framework. I want to understand the metrics
  before a library hides them from me.
- One agent graph, not separate classifier/drafter services. Triage is a
  pipeline, not a swarm, and one graph is far easier to trace when it misbehaves.

## Roadmap

- [x] Scaffold + health endpoint
- [ ] Ticket schema + sample dataset
- [ ] Classification node (structured LLM output)
- [ ] Routing + draft-reply nodes
- [ ] Confidence gate + escalation path
- [ ] Evals harness v1
- [ ] Langfuse wiring
- [ ] Deploy + demo

## Status

Week 1: scaffolding. The interesting commits start next.

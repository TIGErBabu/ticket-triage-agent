"""Shared state for the triage graph.

One TypedDict that every node reads from and writes to. Keeping it in one
place matters: when the evals harness replays a ticket, this dict *is* the
run record.
"""
from typing import Optional, TypedDict


class TriageState(TypedDict, total=False):
    # --- the ticket as it arrives ---
    ticket_id: str
    subject: str
    body: str
    customer_tier: str  # "free" | "pro" | "enterprise"

    # --- filled in by the classify node ---
    category: Optional[str]  # billing | technical | account | general
    priority: Optional[str]  # low | normal | high | urgent
    sentiment: Optional[str]  # positive | neutral | negative
    confidence: Optional[float]  # 0..1, the classifier's self-score

    # --- filled in by the route node ---
    queue: Optional[str]

    # --- filled in by the draft node ---
    draft_reply: Optional[str]

    # --- filled in by the confidence gate ---
    escalated: bool
    escalation_reason: Optional[str]

"""The ticket form: one fixed shape that every part of the agent uses.

Two halves:
  - Ticket: what the customer gives us.
  - TicketAnswers: what the agent has to work out.

A LabeledTicket pairs a ticket with the correct answers. The sample
dataset is made of those pairs, and the evals harness grades the agent
against them.
"""
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class CustomerTier(str, Enum):
    FREE = "free"
    PRO = "pro"
    ENTERPRISE = "enterprise"


class Category(str, Enum):
    BILLING = "billing"
    TECHNICAL = "technical"
    ACCOUNT = "account"
    GENERAL = "general"


class Priority(str, Enum):
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"
    URGENT = "urgent"


class Sentiment(str, Enum):
    POSITIVE = "positive"
    NEUTRAL = "neutral"
    NEGATIVE = "negative"


class Queue(str, Enum):
    BILLING = "billing-team"
    TECHNICAL = "tech-team"
    ACCOUNT = "account-team"
    GENERAL = "general-support"


class Ticket(BaseModel):
    """What arrives from the customer."""

    ticket_id: str
    customer_name: str
    customer_tier: CustomerTier
    subject: str
    body: str
    customer_wants: str  # what they need in return
    details: Optional[str] = None  # error text, order number, what they tried
    remarks: Optional[str] = None  # anything else worth knowing


class TicketAnswers(BaseModel):
    """What the agent has to work out.

    In the dataset these are the answer key. When the agent runs, this
    same shape is what the classifier produces.
    """

    category: Category
    priority: Priority
    sentiment: Sentiment
    queue: Queue
    escalate: bool  # True = a human should take this one
    escalation_reason: Optional[str] = None


class LabeledTicket(BaseModel):
    """One row of the sample dataset: a ticket + its correct answers."""

    ticket: Ticket
    answers: TicketAnswers

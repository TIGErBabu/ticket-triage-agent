"""The triage graph: classify -> route -> draft -> confidence gate.

TODO: wire the nodes once the classification node exists.
Keeping the shape in one small file on purpose — if the flow can't be
read top to bottom in a minute, it is too complicated for v1.
"""

# Planned nodes:
#   classify_ticket(state) -> category / priority / sentiment / confidence
#   route_ticket(state)    -> queue
#   draft_reply(state)     -> draft_reply (grounded in the KB tool)
#   confidence_gate(state) -> escalated, or send the draft

"""Core primitives for the first Dathive agent orchestration layer.

This module is deliberately deterministic. It does not browse, infer licenses,
or publish records by itself. It defines task envelopes and safe orchestration
rules that future agents can implement behind explicit evidence boundaries.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

AGENT_ROLES = {
    "discovery",
    "verification",
    "extraction",
    "linkage",
    "gap_analysis",
    "privacy_audit",
    "provenance_audit",
    "synthesis",
}

HIGH_IMPACT_ROLES = {"verification", "privacy_audit", "provenance_audit"}

@dataclass(frozen=True)
class Evidence:
    source_url: str
    retrieved_at: Optional[str] = None
    locator: Optional[str] = None
    source_type: Optional[str] = None

@dataclass
class AgentTask:
    task_id: str
    agent_role: str
    input: Dict[str, Any] = field(default_factory=dict)
    evidence: List[Evidence] = field(default_factory=list)
    claims: List[Dict[str, Any]] = field(default_factory=list)
    unresolved: List[str] = field(default_factory=list)
    proposed_changes: List[Dict[str, Any]] = field(default_factory=list)
    confidence: Optional[float] = None
    requires_human_review: bool = True
    parent_task: Optional[str] = None

    def validate(self) -> List[str]:
        errors = []
        if not self.task_id.strip():
            errors.append("task_id is required")
        if self.agent_role not in AGENT_ROLES:
            errors.append(f"unsupported agent_role: {self.agent_role}")
        if self.confidence is not None and not 0 <= self.confidence <= 1:
            errors.append("confidence must be between 0 and 1")
        if self.agent_role in HIGH_IMPACT_ROLES and not self.requires_human_review:
            errors.append("high-impact tasks require human review")
        return errors

def build_initial_tasks(candidate_url: str, query: str) -> List[AgentTask]:
    """Create a conservative task chain for a newly discovered candidate."""
    if not candidate_url:
        raise ValueError("candidate_url is required")

    discovery = AgentTask(
        task_id="discovery-1",
        agent_role="discovery",
        input={"source_url": candidate_url, "query": query},
        requires_human_review=False,
    )
    verification = AgentTask(
        task_id="verification-1",
        agent_role="verification",
        input={"candidate_url": candidate_url},
        parent_task=discovery.task_id,
        requires_human_review=True,
    )
    extraction = AgentTask(
        task_id="extraction-1",
        agent_role="extraction",
        input={"candidate_url": candidate_url},
        parent_task=verification.task_id,
        requires_human_review=True,
    )
    return [discovery, verification, extraction]

def can_promote_to_canonical(task: AgentTask) -> bool:
    """Only a verified, evidenced task can propose canonical promotion."""
    return (
        task.agent_role == "verification"
        and task.requires_human_review
        and bool(task.evidence)
        and not task.unresolved
        and bool(task.proposed_changes)
    )

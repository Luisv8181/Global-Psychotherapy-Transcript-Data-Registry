from src.registry.dathive import AgentTask, Evidence, build_initial_tasks, can_promote_to_canonical

def test_initial_task_chain_is_conservative():
    tasks = build_initial_tasks(
        "https://example.org/dataset",
        "psychotherapy transcript dataset",
    )
    assert [t.agent_role for t in tasks] == ["discovery", "verification", "extraction"]
    assert tasks[1].requires_human_review is True
    assert tasks[2].parent_task == tasks[1].task_id

def test_high_impact_task_requires_human_review():
    task = AgentTask(task_id="x", agent_role="verification", requires_human_review=False)
    assert "high-impact tasks require human review" in task.validate()

def test_canonical_promotion_requires_evidence_and_no_unresolved_items():
    task = AgentTask(
        task_id="v1",
        agent_role="verification",
        evidence=[Evidence(source_url="https://example.org")],
        proposed_changes=[{"field": "title", "value": "Example"}],
        requires_human_review=True,
    )
    assert can_promote_to_canonical(task) is True

    task.unresolved.append("license unclear")
    assert can_promote_to_canonical(task) is False

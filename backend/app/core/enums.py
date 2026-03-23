from enum import Enum


class JobStatus(str, Enum):
    queued = "queued"
    processing = "processing"
    completed = "completed"
    completed_with_warnings = "completed_with_warnings"
    failed = "failed"


class WorkflowStage(str, Enum):
    received = "received"
    parsing = "parsing"
    planning = "planning"
    sandbox_prepare = "sandbox_prepare"
    code_generation = "code_generation"
    validation = "validation"
    pr_generation = "pr_generation"
    finished = "finished"
    failed = "failed"


class RiskLevel(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

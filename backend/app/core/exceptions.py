class WorkflowError(Exception):
    pass


class PlannerError(WorkflowError):
    pass


class SandboxError(WorkflowError):
    pass

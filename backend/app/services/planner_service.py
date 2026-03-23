from app.schemas.planner import PlannerOutput
from app.services.llm.provider_factory import PlannerProviderFactory


class PlannerService:
    def __init__(self):
        self.provider = PlannerProviderFactory.create()

    def build_plan(self, parsed_ticket: dict) -> PlannerOutput:
        return self.provider.plan(parsed_ticket)

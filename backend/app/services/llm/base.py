from abc import ABC, abstractmethod

from app.schemas.planner import PlannerOutput


class BasePlannerProvider(ABC):
    @abstractmethod
    def plan(self, parsed_ticket: dict) -> PlannerOutput:
        raise NotImplementedError

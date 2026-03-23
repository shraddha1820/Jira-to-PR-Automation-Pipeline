from app.config.settings import get_settings
from app.services.llm.base import BasePlannerProvider
from app.services.llm.mock_provider import MockPlannerProvider
from app.services.llm.openai_provider import OpenAIPlannerProvider


class PlannerProviderFactory:
    @staticmethod
    def create() -> BasePlannerProvider:
        settings = get_settings()
        if settings.llm_mode == "real" and settings.llm_provider == "openai":
            return OpenAIPlannerProvider(
                api_key=settings.openai_api_key,
                model=settings.openai_model,
            )
        return MockPlannerProvider()

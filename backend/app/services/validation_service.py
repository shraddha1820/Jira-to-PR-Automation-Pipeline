from app.schemas.validation import ValidationStepOutput


class ValidationService:
    def run(self, generated_files: list[dict] | list) -> list[ValidationStepOutput]:
        file_count = len(generated_files)
        return [
            ValidationStepOutput(
                step_name="lint",
                passed=True,
                exit_code=0,
                output=f"Mock lint passed for {file_count} generated files.",
            ),
            ValidationStepOutput(
                step_name="unit_tests",
                passed=True,
                exit_code=0,
                output="Mock unit tests passed for missing email validation.",
            ),
        ]

import { Card } from "@/components/common/Card";
import { PlannerResult } from "@/lib/types";

export function PlannerOutputCard({ planner }: { planner: PlannerResult | null | undefined }) {
  if (!planner) {
    return <Card title="Planner output"><p className="text-sm text-slate-500">Planner output will appear after the planning stage completes.</p></Card>;
  }

  return (
    <Card title="Planner output" subtitle={`Provider: ${planner.provider}`}>
      <div className="space-y-5">
        <div>
          <p className="text-xs font-medium uppercase tracking-wide text-slate-500">Task summary</p>
          <p className="mt-2 text-sm leading-6 text-slate-800">{planner.task_summary}</p>
        </div>

        <div className="grid gap-4 md:grid-cols-2">
          <div>
            <p className="text-xs font-medium uppercase tracking-wide text-slate-500">Likely affected files</p>
            <ul className="mt-2 space-y-2 text-sm text-slate-700">
              {planner.likely_affected_files.length ? (
                planner.likely_affected_files.map((filePath) => <li key={filePath}>• {filePath}</li>)
              ) : (
                <li>—</li>
              )}
            </ul>
          </div>
          <div>
            <p className="text-xs font-medium uppercase tracking-wide text-slate-500">Risk level</p>
            <p className="mt-2 inline-flex rounded-full bg-slate-100 px-3 py-1 text-sm font-medium text-slate-800">
              {planner.risk_level}
            </p>
          </div>
        </div>

        <div>
          <p className="text-xs font-medium uppercase tracking-wide text-slate-500">Implementation plan</p>
          <ol className="mt-2 space-y-2 text-sm leading-6 text-slate-700">
            {planner.implementation_plan.length ? (
              planner.implementation_plan.map((step, index) => <li key={`${index}-${step}`}>{index + 1}. {step}</li>)
            ) : (
              <li>—</li>
            )}
          </ol>
        </div>

        <div>
          <p className="text-xs font-medium uppercase tracking-wide text-slate-500">Validation checklist</p>
          <ul className="mt-2 space-y-2 text-sm text-slate-700">
            {planner.validation_checklist.length ? (
              planner.validation_checklist.map((item) => <li key={item}>• {item}</li>)
            ) : (
              <li>—</li>
            )}
          </ul>
        </div>
      </div>
    </Card>
  );
}

import { Card } from "@/components/common/Card";
import { ValidationResult } from "@/lib/types";

export function ValidationResultsCard({ results }: { results: ValidationResult[] }) {
  return (
    <Card title="Validation results" subtitle="Checks executed after code generation.">
      {results.length === 0 ? (
        <p className="text-sm text-slate-500">Validation results will appear after generation finishes.</p>
      ) : (
        <div className="space-y-4">
          {results.map((result) => (
            <div key={result.id} className="rounded-xl border border-slate-200 p-4">
              <div className="flex items-center justify-between gap-3">
                <div>
                  <p className="font-medium text-slate-900">{result.step_name}</p>
                  <p className="text-xs text-slate-500">Exit code: {result.exit_code}</p>
                </div>
                <span
                  className={`inline-flex rounded-full px-2.5 py-1 text-xs font-medium ${
                    result.passed ? "bg-emerald-50 text-emerald-700" : "bg-rose-50 text-rose-700"
                  }`}
                >
                  {result.passed ? "Passed" : "Failed"}
                </span>
              </div>
              <pre className="mt-3 max-h-64 overflow-auto rounded-lg bg-slate-950 p-3 text-xs leading-5 text-slate-100">
                {result.output}
              </pre>
            </div>
          ))}
        </div>
      )}
    </Card>
  );
}

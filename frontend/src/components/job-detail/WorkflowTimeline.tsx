import { Card } from "@/components/common/Card";
import { StatusBadge } from "@/components/dashboard/StatusBadge";
import { formatDateTime, titleCase } from "@/lib/format";
import { StatusHistory } from "@/lib/types";

export function WorkflowTimeline({ history }: { history: StatusHistory[] }) {
  return (
    <Card title="Workflow timeline" subtitle="Stage-by-stage state captured by the backend.">
      {history.length === 0 ? (
        <p className="text-sm text-slate-500">No timeline events recorded yet.</p>
      ) : (
        <div className="space-y-4">
          {history.map((entry, index) => (
            <div key={`${entry.stage}-${entry.created_at}-${index}`} className="flex gap-4">
              <div className="mt-1 flex h-6 w-6 items-center justify-center rounded-full border border-slate-300 bg-white text-xs font-medium text-slate-700">
                {index + 1}
              </div>
              <div className="min-w-0 flex-1 rounded-xl border border-slate-200 p-4">
                <div className="flex flex-wrap items-center justify-between gap-3">
                  <div>
                    <p className="font-medium text-slate-900">{titleCase(entry.stage)}</p>
                    <p className="text-xs text-slate-500">{formatDateTime(entry.created_at)}</p>
                  </div>
                  <StatusBadge status={entry.status} />
                </div>
                {entry.message ? <p className="mt-2 text-sm leading-6 text-slate-600">{entry.message}</p> : null}
              </div>
            </div>
          ))}
        </div>
      )}
    </Card>
  );
}

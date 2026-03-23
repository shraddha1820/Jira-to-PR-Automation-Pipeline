import Link from "next/link";

import { StatusBadge } from "@/components/dashboard/StatusBadge";
import { formatDateTime } from "@/lib/format";
import { JobDetail } from "@/lib/types";

export function JobHeader({ job }: { job: JobDetail }) {
  return (
    <div className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm">
      <div className="flex flex-col gap-4 md:flex-row md:items-start md:justify-between">
        <div className="space-y-2">
          <div className="flex items-center gap-3">
            <Link href="/" className="text-sm text-slate-500 hover:text-slate-900">
              ← Back to dashboard
            </Link>
          </div>
          <h1 className="text-3xl font-semibold tracking-tight text-slate-950">
            Job #{job.id} {job.jira_ticket_id ? `· ${job.jira_ticket_id}` : ""}
          </h1>
          <div className="flex flex-wrap items-center gap-3 text-sm text-slate-600">
            <span>Source: {job.source.replace("_", " ")}</span>
            <span>Created: {formatDateTime(job.created_at)}</span>
            <span>Updated: {formatDateTime(job.updated_at)}</span>
          </div>
        </div>
        <StatusBadge status={job.status} />
      </div>
    </div>
  );
}

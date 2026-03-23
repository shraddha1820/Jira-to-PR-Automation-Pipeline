import Link from "next/link";

import { StatusBadge } from "@/components/dashboard/StatusBadge";
import { formatDateTime } from "@/lib/format";
import { JobListItem } from "@/lib/types";

export function JobsTable({ jobs }: { jobs: JobListItem[] }) {
  return (
    <div className="overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-sm">
      <div className="overflow-x-auto">
        <table className="min-w-full divide-y divide-slate-200 text-sm">
          <thead className="bg-slate-50">
            <tr>
              <th className="px-4 py-3 text-left font-medium text-slate-600">Job</th>
              <th className="px-4 py-3 text-left font-medium text-slate-600">Ticket</th>
              <th className="px-4 py-3 text-left font-medium text-slate-600">Source</th>
              <th className="px-4 py-3 text-left font-medium text-slate-600">Status</th>
              <th className="px-4 py-3 text-left font-medium text-slate-600">Updated</th>
              <th className="px-4 py-3 text-right font-medium text-slate-600">Action</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-100 bg-white">
            {jobs.map((job) => (
              <tr key={job.id} className="hover:bg-slate-50/80">
                <td className="px-4 py-3 font-medium text-slate-900">#{job.id}</td>
                <td className="px-4 py-3 text-slate-700">{job.jira_ticket_id || "—"}</td>
                <td className="px-4 py-3 capitalize text-slate-700">{job.source.replace("_", " ")}</td>
                <td className="px-4 py-3"><StatusBadge status={job.status} /></td>
                <td className="px-4 py-3 text-slate-600">{formatDateTime(job.updated_at || job.created_at)}</td>
                <td className="px-4 py-3 text-right">
                  <Link
                    href={`/jobs/${job.id}`}
                    className="inline-flex rounded-lg border border-slate-300 px-3 py-1.5 font-medium text-slate-700 transition hover:border-slate-400 hover:bg-slate-50"
                  >
                    View details
                  </Link>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

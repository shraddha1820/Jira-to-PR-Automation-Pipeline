import { Card } from "@/components/common/Card";
import { formatList } from "@/lib/format";
import { ParsedTicket } from "@/lib/types";

export function ParsedTicketCard({ ticket }: { ticket: ParsedTicket | null | undefined }) {
  if (!ticket) {
    return <Card title="Parsed ticket"><p className="text-sm text-slate-500">No parsed ticket data available yet.</p></Card>;
  }

  return (
    <Card title="Parsed ticket" subtitle="Normalized Jira fields used by the workflow planner.">
      <dl className="grid gap-4 md:grid-cols-2">
        <div>
          <dt className="text-xs font-medium uppercase tracking-wide text-slate-500">Ticket ID</dt>
          <dd className="mt-1 text-sm text-slate-900">{ticket.ticket_id}</dd>
        </div>
        <div>
          <dt className="text-xs font-medium uppercase tracking-wide text-slate-500">Priority</dt>
          <dd className="mt-1 text-sm text-slate-900">{ticket.priority || "—"}</dd>
        </div>
        <div className="md:col-span-2">
          <dt className="text-xs font-medium uppercase tracking-wide text-slate-500">Summary</dt>
          <dd className="mt-1 text-sm text-slate-900">{ticket.summary}</dd>
        </div>
        <div className="md:col-span-2">
          <dt className="text-xs font-medium uppercase tracking-wide text-slate-500">Description</dt>
          <dd className="mt-1 whitespace-pre-wrap text-sm leading-6 text-slate-700">{ticket.description || "—"}</dd>
        </div>
        <div>
          <dt className="text-xs font-medium uppercase tracking-wide text-slate-500">Acceptance criteria</dt>
          <dd className="mt-2">
            <ul className="space-y-2 text-sm text-slate-700">
              {ticket.acceptance_criteria.length ? (
                ticket.acceptance_criteria.map((criterion) => <li key={criterion}>• {criterion}</li>)
              ) : (
                <li>—</li>
              )}
            </ul>
          </dd>
        </div>
        <div>
          <dt className="text-xs font-medium uppercase tracking-wide text-slate-500">Labels</dt>
          <dd className="mt-1 text-sm text-slate-700">{formatList(ticket.labels)}</dd>
        </div>
      </dl>
    </Card>
  );
}

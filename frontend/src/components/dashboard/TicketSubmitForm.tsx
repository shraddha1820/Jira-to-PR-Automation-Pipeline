"use client";

import { useMemo, useState } from "react";

import { submitManualTicket } from "@/lib/api";
import { toMultilineListInput } from "@/lib/format";
import { ManualTicketRequest } from "@/lib/types";

interface TicketSubmitFormProps {
  onSuccess?: (jobId: number) => void;
}

const initialState = {
  ticket_id: "DEMO-101",
  summary: "API returns 500 when email is missing; expected 400 validation error",
  description:
    "The create-user endpoint throws a server error when the email field is omitted from the request payload. The expected behavior is to return a 400 validation response with a clear error message.",
  acceptanceCriteriaText:
    "Return HTTP 400 when email is missing\nProvide a clear validation message\nAdd or update a unit test covering the missing email case",
  priority: "High",
  labelsText: "bugfix, api, validation",
};

export function TicketSubmitForm({ onSuccess }: TicketSubmitFormProps) {
  const [formState, setFormState] = useState(initialState);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [successMessage, setSuccessMessage] = useState<string | null>(null);

  const payload = useMemo<ManualTicketRequest>(
    () => ({
      ticket_id: formState.ticket_id.trim(),
      summary: formState.summary.trim(),
      description: formState.description.trim(),
      acceptance_criteria: toMultilineListInput(formState.acceptanceCriteriaText),
      priority: formState.priority.trim() || null,
      labels: toMultilineListInput(formState.labelsText),
    }),
    [formState],
  );

  async function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setError(null);
    setSuccessMessage(null);
    setIsSubmitting(true);

    try {
      const response = await submitManualTicket(payload);
      setSuccessMessage(`Job #${response.job_id} submitted successfully.`);
      onSuccess?.(response.job_id);
    } catch (submitError) {
      setError(submitError instanceof Error ? submitError.message : "Could not submit ticket.");
    } finally {
      setIsSubmitting(false);
    }
  }

  return (
    <form className="space-y-4" onSubmit={handleSubmit}>
      <div className="grid gap-4 md:grid-cols-2">
        <label className="space-y-2 text-sm text-slate-700">
          <span className="font-medium">Ticket ID</span>
          <input
            className="w-full rounded-xl border border-slate-300 px-3 py-2 outline-none transition focus:border-slate-500"
            value={formState.ticket_id}
            onChange={(event) => setFormState((current) => ({ ...current, ticket_id: event.target.value }))}
            required
          />
        </label>

        <label className="space-y-2 text-sm text-slate-700">
          <span className="font-medium">Priority</span>
          <input
            className="w-full rounded-xl border border-slate-300 px-3 py-2 outline-none transition focus:border-slate-500"
            value={formState.priority}
            onChange={(event) => setFormState((current) => ({ ...current, priority: event.target.value }))}
          />
        </label>
      </div>

      <label className="block space-y-2 text-sm text-slate-700">
        <span className="font-medium">Summary</span>
        <input
          className="w-full rounded-xl border border-slate-300 px-3 py-2 outline-none transition focus:border-slate-500"
          value={formState.summary}
          onChange={(event) => setFormState((current) => ({ ...current, summary: event.target.value }))}
          required
        />
      </label>

      <label className="block space-y-2 text-sm text-slate-700">
        <span className="font-medium">Description</span>
        <textarea
          className="min-h-28 w-full rounded-xl border border-slate-300 px-3 py-2 outline-none transition focus:border-slate-500"
          value={formState.description}
          onChange={(event) => setFormState((current) => ({ ...current, description: event.target.value }))}
        />
      </label>

      <div className="grid gap-4 md:grid-cols-2">
        <label className="space-y-2 text-sm text-slate-700">
          <span className="font-medium">Acceptance criteria</span>
          <textarea
            className="min-h-28 w-full rounded-xl border border-slate-300 px-3 py-2 outline-none transition focus:border-slate-500"
            value={formState.acceptanceCriteriaText}
            onChange={(event) =>
              setFormState((current) => ({ ...current, acceptanceCriteriaText: event.target.value }))
            }
          />
          <span className="text-xs text-slate-500">Use one line per item or separate with commas.</span>
        </label>

        <label className="space-y-2 text-sm text-slate-700">
          <span className="font-medium">Labels</span>
          <textarea
            className="min-h-28 w-full rounded-xl border border-slate-300 px-3 py-2 outline-none transition focus:border-slate-500"
            value={formState.labelsText}
            onChange={(event) => setFormState((current) => ({ ...current, labelsText: event.target.value }))}
          />
          <span className="text-xs text-slate-500">Use one line per item or separate with commas.</span>
        </label>
      </div>

      {error ? <p className="text-sm text-rose-600">{error}</p> : null}
      {successMessage ? <p className="text-sm text-emerald-700">{successMessage}</p> : null}

      <div className="flex items-center gap-3">
        <button
          type="submit"
          disabled={isSubmitting}
          className="rounded-xl bg-slate-950 px-4 py-2 text-sm font-medium text-white transition hover:bg-slate-800 disabled:cursor-not-allowed disabled:bg-slate-400"
        >
          {isSubmitting ? "Submitting..." : "Submit mock Jira ticket"}
        </button>
        <p className="text-xs text-slate-500">This triggers the backend manual workflow endpoint.</p>
      </div>
    </form>
  );
}

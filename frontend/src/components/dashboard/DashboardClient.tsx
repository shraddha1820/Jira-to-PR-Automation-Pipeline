"use client";

import { useCallback, useEffect, useState } from "react";
import { useRouter } from "next/navigation";

import { Card } from "@/components/common/Card";
import { EmptyState } from "@/components/common/EmptyState";
import { SectionTitle } from "@/components/common/SectionTitle";
import { JobsTable } from "@/components/dashboard/JobsTable";
import { TicketSubmitForm } from "@/components/dashboard/TicketSubmitForm";
import { POLL_INTERVAL_MS } from "@/lib/constants";
import { fetchJobs } from "@/lib/api";
import { JobListItem } from "@/lib/types";

interface DashboardClientProps {
  initialJobs: JobListItem[];
  initialError?: string | null;
}

export function DashboardClient({ initialJobs, initialError = null }: DashboardClientProps) {
  const router = useRouter();
  const [jobs, setJobs] = useState<JobListItem[]>(initialJobs);
  const [error, setError] = useState<string | null>(initialError);

  const loadJobs = useCallback(async () => {
    try {
      const response = await fetchJobs();
      setJobs(response.items);
      setError(null);
    } catch (loadError) {
      setError(loadError instanceof Error ? loadError.message : "Unable to load jobs.");
    }
  }, []);

  useEffect(() => {
    const intervalId = window.setInterval(() => {
      void loadJobs();
    }, POLL_INTERVAL_MS);

    return () => window.clearInterval(intervalId);
  }, [loadJobs]);

  function handleSuccess(jobId: number) {
    void loadJobs();
    router.push(`/jobs/${jobId}`);
    router.refresh();
  }

  return (
    <div className="space-y-8">
      <SectionTitle
        eyebrow="Developer productivity demo"
        title="AI Jira-to-PR Automation Pipeline"
        description="Submit a mock Jira issue, track each workflow stage, and inspect the generated planner, code-change, validation, and pull-request artifacts."
      />

      <div className="grid gap-8 xl:grid-cols-[1.1fr_0.9fr]">
        <Card
          title="Submit ticket"
          subtitle="Creates a workflow job through the backend manual trigger endpoint."
        >
          <TicketSubmitForm onSuccess={handleSuccess} />
        </Card>

        <Card
          title="How this demo works"
          subtitle="A production-inspired but manageable local workflow."
        >
          <ol className="space-y-3 text-sm leading-6 text-slate-700">
            <li>1. Frontend submits a Jira-like ticket payload to FastAPI.</li>
            <li>2. Backend stores a job record and pushes the workflow to Celery.</li>
            <li>3. Worker parses the ticket, creates a plan, patches the demo repo, validates it, and produces PR metadata.</li>
            <li>4. Dashboard pages read job state from PostgreSQL-backed API endpoints.</li>
          </ol>
        </Card>
      </div>

      <section className="space-y-4">
        <div className="flex items-end justify-between gap-4">
          <div>
            <h2 className="text-xl font-semibold text-slate-950">Workflow jobs</h2>
            <p className="mt-1 text-sm text-slate-600">Recent pipeline runs created by webhook or manual submissions.</p>
          </div>
          <button
            type="button"
            onClick={() => void loadJobs()}
            className="rounded-lg border border-slate-300 bg-white px-3 py-2 text-sm font-medium text-slate-700 hover:bg-slate-50"
          >
            Refresh
          </button>
        </div>

        {error ? (
          <EmptyState title="Could not load jobs" description={error} />
        ) : jobs.length > 0 ? (
          <JobsTable jobs={jobs} />
        ) : (
          <EmptyState
            title="No jobs yet"
            description="Submit a mock Jira ticket to create your first workflow run."
          />
        )}
      </section>
    </div>
  );
}

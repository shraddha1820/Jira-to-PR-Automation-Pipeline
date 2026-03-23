"use client";

import { useCallback, useEffect, useState } from "react";

import { Card } from "@/components/common/Card";
import { EmptyState } from "@/components/common/EmptyState";
import { ChangedFilesCard } from "@/components/job-detail/ChangedFilesCard";
import { ErrorCard } from "@/components/job-detail/ErrorCard";
import { JobHeader } from "@/components/job-detail/JobHeader";
import { ParsedTicketCard } from "@/components/job-detail/ParsedTicketCard";
import { PlannerOutputCard } from "@/components/job-detail/PlannerOutputCard";
import { PrOutputCard } from "@/components/job-detail/PrOutputCard";
import { ValidationResultsCard } from "@/components/job-detail/ValidationResultsCard";
import { WorkflowTimeline } from "@/components/job-detail/WorkflowTimeline";
import { fetchJobDetail } from "@/lib/api";
import { POLL_INTERVAL_MS } from "@/lib/constants";
import { JobDetail } from "@/lib/types";

interface JobDetailClientProps {
  initialJob?: JobDetail | null;
  jobId: string;
  initialError?: string | null;
}

export function JobDetailClient({ initialJob = null, jobId, initialError = null }: JobDetailClientProps) {
  const [job, setJob] = useState<JobDetail | null>(initialJob);
  const [error, setError] = useState<string | null>(initialError);

  const loadJob = useCallback(async () => {
    try {
      const response = await fetchJobDetail(jobId);
      setJob(response);
      setError(null);
    } catch (loadError) {
      setError(loadError instanceof Error ? loadError.message : "Unable to load job details.");
    }
  }, [jobId]);

  useEffect(() => {
    if (!job || ["queued", "processing"].includes(job.status)) {
      const intervalId = window.setInterval(() => {
        void loadJob();
      }, POLL_INTERVAL_MS);

      return () => window.clearInterval(intervalId);
    }
  }, [job, loadJob]);

  if (error && !job) {
    return (
      <div className="space-y-6">
        <Card title="Job detail">
          <EmptyState title="Could not load job" description={error} />
        </Card>
      </div>
    );
  }

  if (!job) {
    return (
      <div className="space-y-6">
        <Card title="Job detail">
          <EmptyState title="Job not available" description="No job payload was returned by the backend." />
        </Card>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <JobHeader job={job} />
      <ErrorCard message={job.error_message || error} />

      <div className="grid gap-6 xl:grid-cols-[0.95fr_1.05fr]">
        <div className="space-y-6">
          <ParsedTicketCard ticket={job.parsed_ticket} />
          <PlannerOutputCard planner={job.planner_result} />
          <PrOutputCard prMetadata={job.pr_metadata} />
        </div>
        <div className="space-y-6">
          <WorkflowTimeline history={job.status_history} />
          <ValidationResultsCard results={job.validation_results} />
        </div>
      </div>

      <ChangedFilesCard files={job.generated_files} />
    </div>
  );
}

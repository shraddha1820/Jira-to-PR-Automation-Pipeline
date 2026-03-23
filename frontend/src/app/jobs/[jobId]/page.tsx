import { JobDetailClient } from "@/components/job-detail/JobDetailClient";
import { fetchJobDetail } from "@/lib/api";

interface JobDetailPageProps {
  params: {
    jobId: string;
  };
}

export default async function JobDetailPage({ params }: JobDetailPageProps) {
  try {
    const job = await fetchJobDetail(params.jobId);
    return <JobDetailClient initialJob={job} jobId={params.jobId} />;
  } catch (error) {
    const message = error instanceof Error ? error.message : "Unable to load job details.";
    return <JobDetailClient initialJob={null} jobId={params.jobId} initialError={message} />;
  }
}

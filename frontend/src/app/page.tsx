import { DashboardClient } from "@/components/dashboard/DashboardClient";
import { fetchJobs } from "@/lib/api";

export default async function DashboardPage() {
  try {
    const jobsResponse = await fetchJobs();
    return <DashboardClient initialJobs={jobsResponse.items} />;
  } catch (error) {
    const message = error instanceof Error ? error.message : "Unable to load jobs.";
    return <DashboardClient initialJobs={[]} initialError={message} />;
  }
}

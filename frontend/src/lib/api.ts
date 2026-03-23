import { API_BASE_URL } from "@/lib/constants";
import {
  JobCreateResponse,
  JobDetail,
  JobListResponse,
  ManualTicketRequest,
} from "@/lib/types";

async function parseResponse<T>(response: Response): Promise<T> {
  if (!response.ok) {
    let message = `Request failed with status ${response.status}`;

    try {
      const errorBody = (await response.json()) as { detail?: string };
      if (errorBody.detail) {
        message = errorBody.detail;
      }
    } catch {
      // Ignore non-JSON bodies.
    }

    throw new Error(message);
  }

  return (await response.json()) as T;
}

export async function fetchJobs(): Promise<JobListResponse> {
  const response = await fetch(`${API_BASE_URL}/jobs`, {
    cache: "no-store",
  });
  return parseResponse<JobListResponse>(response);
}

export async function fetchJobDetail(jobId: string | number): Promise<JobDetail> {
  const response = await fetch(`${API_BASE_URL}/jobs/${jobId}`, {
    cache: "no-store",
  });
  return parseResponse<JobDetail>(response);
}

export async function submitManualTicket(
  payload: ManualTicketRequest,
): Promise<JobCreateResponse> {
  const response = await fetch(`${API_BASE_URL}/jira/trigger`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  return parseResponse<JobCreateResponse>(response);
}

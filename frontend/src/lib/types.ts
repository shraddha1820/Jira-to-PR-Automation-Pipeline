export type JobStatus =
  | "queued"
  | "processing"
  | "completed"
  | "failed"
  | "completed_with_warnings";

export interface ManualTicketRequest {
  ticket_id: string;
  summary: string;
  description: string;
  acceptance_criteria: string[];
  priority?: string | null;
  labels: string[];
}

export interface JobCreateResponse {
  job_id: number;
  status: string;
}

export interface JobListItem {
  id: number;
  source: string;
  status: string;
  jira_ticket_id?: string | null;
  created_at?: string | null;
  updated_at?: string | null;
}

export interface JobListResponse {
  items: JobListItem[];
}

export interface ParsedTicket {
  id: number;
  job_id: number;
  ticket_id: string;
  summary: string;
  description: string;
  acceptance_criteria: string[];
  priority?: string | null;
  labels: string[];
}

export interface PlannerResult {
  id: number;
  job_id: number;
  task_summary: string;
  likely_affected_files: string[];
  implementation_plan: string[];
  risk_level: string;
  validation_checklist: string[];
  provider: string;
  raw_response: Record<string, unknown>;
  created_at?: string | null;
  updated_at?: string | null;
}

export interface GeneratedFile {
  id: number;
  job_id: number;
  file_path: string;
  change_type: string;
  before_content?: string | null;
  after_content: string;
  diff_text: string;
  applied_successfully: boolean;
  created_at?: string | null;
  updated_at?: string | null;
}

export interface ValidationResult {
  id: number;
  job_id: number;
  step_name: string;
  passed: boolean;
  exit_code: number;
  output: string;
  created_at?: string | null;
  updated_at?: string | null;
}

export interface PrMetadata {
  id: number;
  job_id: number;
  branch_name: string;
  commit_message: string;
  pr_title: string;
  pr_body: string;
  pr_url?: string | null;
  is_simulated: boolean;
  created_at?: string | null;
  updated_at?: string | null;
}

export interface StatusHistory {
  stage: string;
  status: string;
  message?: string | null;
  created_at?: string | null;
}

export interface JobDetail {
  id: number;
  source: string;
  status: string;
  jira_ticket_id?: string | null;
  error_message?: string | null;
  created_at?: string | null;
  updated_at?: string | null;
  parsed_ticket?: ParsedTicket | null;
  planner_result?: PlannerResult | null;
  generated_files: GeneratedFile[];
  validation_results: ValidationResult[];
  pr_metadata?: PrMetadata | null;
  status_history: StatusHistory[];
}

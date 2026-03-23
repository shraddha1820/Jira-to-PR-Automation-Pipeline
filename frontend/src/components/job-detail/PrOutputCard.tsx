import { Card } from "@/components/common/Card";
import { PrMetadata } from "@/lib/types";

export function PrOutputCard({ prMetadata }: { prMetadata: PrMetadata | null | undefined }) {
  if (!prMetadata) {
    return <Card title="PR summary"><p className="text-sm text-slate-500">PR metadata will appear when the workflow reaches the final stage.</p></Card>;
  }

  return (
    <Card title="PR summary" subtitle={prMetadata.is_simulated ? "Simulated PR payload" : "Live GitHub PR payload"}>
      <div className="space-y-5">
        <div className="grid gap-4 md:grid-cols-2">
          <div>
            <p className="text-xs font-medium uppercase tracking-wide text-slate-500">Branch name</p>
            <p className="mt-2 rounded-lg bg-slate-100 px-3 py-2 text-sm text-slate-900">{prMetadata.branch_name}</p>
          </div>
          <div>
            <p className="text-xs font-medium uppercase tracking-wide text-slate-500">Commit message</p>
            <p className="mt-2 rounded-lg bg-slate-100 px-3 py-2 text-sm text-slate-900">{prMetadata.commit_message}</p>
          </div>
        </div>

        <div>
          <p className="text-xs font-medium uppercase tracking-wide text-slate-500">PR title</p>
          <p className="mt-2 text-sm font-medium text-slate-900">{prMetadata.pr_title}</p>
        </div>

        <div>
          <p className="text-xs font-medium uppercase tracking-wide text-slate-500">PR body</p>
          <pre className="mt-2 whitespace-pre-wrap rounded-xl bg-slate-950 p-4 text-sm leading-6 text-slate-100">{prMetadata.pr_body}</pre>
        </div>

        {prMetadata.pr_url ? (
          <div>
            <a
              href={prMetadata.pr_url}
              target="_blank"
              rel="noreferrer"
              className="text-sm font-medium text-slate-900 underline underline-offset-4"
            >
              Open PR
            </a>
          </div>
        ) : null}
      </div>
    </Card>
  );
}

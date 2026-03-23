import { Card } from "@/components/common/Card";
import { GeneratedFile } from "@/lib/types";

export function ChangedFilesCard({ files }: { files: GeneratedFile[] }) {
  return (
    <Card title="Changed files" subtitle="Generated patch artifacts captured during sandbox execution.">
      {files.length === 0 ? (
        <p className="text-sm text-slate-500">No generated file changes are available yet.</p>
      ) : (
        <div className="space-y-4">
          {files.map((file) => (
            <div key={file.id} className="rounded-xl border border-slate-200 bg-slate-50 p-4">
              <div className="flex flex-wrap items-center justify-between gap-2">
                <div>
                  <p className="font-medium text-slate-900">{file.file_path}</p>
                  <p className="text-xs text-slate-500">{file.change_type} · {file.applied_successfully ? "Applied" : "Not applied"}</p>
                </div>
              </div>
              <div className="mt-4 grid gap-4 lg:grid-cols-2">
                <div>
                  <p className="mb-2 text-xs font-medium uppercase tracking-wide text-slate-500">Diff</p>
                  <pre className="max-h-72 overflow-auto rounded-lg bg-slate-950 p-3 text-xs leading-5 text-slate-100">{file.diff_text || "No diff available."}</pre>
                </div>
                <div>
                  <p className="mb-2 text-xs font-medium uppercase tracking-wide text-slate-500">Updated content</p>
                  <pre className="max-h-72 overflow-auto rounded-lg bg-slate-950 p-3 text-xs leading-5 text-slate-100">{file.after_content}</pre>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </Card>
  );
}

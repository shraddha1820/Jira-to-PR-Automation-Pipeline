import { Card } from "@/components/common/Card";

export function ErrorCard({ message }: { message?: string | null }) {
  if (!message) return null;

  return (
    <Card title="Workflow error">
      <p className="text-sm leading-6 text-rose-700">{message}</p>
    </Card>
  );
}

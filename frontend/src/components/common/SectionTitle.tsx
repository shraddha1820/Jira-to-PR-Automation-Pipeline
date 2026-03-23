interface SectionTitleProps {
  eyebrow?: string;
  title: string;
  description?: string;
}

export function SectionTitle({ eyebrow, title, description }: SectionTitleProps) {
  return (
    <div className="space-y-2">
      {eyebrow ? <p className="text-xs font-semibold uppercase tracking-[0.2em] text-slate-500">{eyebrow}</p> : null}
      <h1 className="text-3xl font-semibold tracking-tight text-slate-950">{title}</h1>
      {description ? <p className="max-w-3xl text-sm leading-6 text-slate-600">{description}</p> : null}
    </div>
  );
}

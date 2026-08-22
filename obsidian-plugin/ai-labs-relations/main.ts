import { MarkdownView, Notice, Plugin, TFile } from "obsidian";

interface Relation {
  type?: string;
  target?: string;
}

interface RelationTarget {
  id: string;
  path?: string;
  title?: string;
}

interface AILabsRelationsSettings {
  showEvidence: boolean;
}

const DEFAULT_SETTINGS: AILabsRelationsSettings = {
  showEvidence: false,
};

export default class AILabsRelationsPlugin extends Plugin {
  settings: AILabsRelationsSettings = DEFAULT_SETTINGS;
  private targets = new Map<string, RelationTarget>();

  async onload(): Promise<void> {
    await this.loadSettings();
    this.refreshTargetIndex();

    this.registerEvent(this.app.metadataCache.on("changed", () => this.refreshTargetIndex()));
    this.registerEvent(this.app.workspace.on("layout-change", () => this.refreshRenderedRelations()));
    this.registerMarkdownPostProcessor((element, context) => {
      if (!element.classList.contains("markdown-preview-section")) return;
      this.renderRelations(element, context.sourcePath);
    });

    this.addCommand({
      id: "refresh-relations",
      name: "Refresh AI Labs relations",
      callback: () => {
        this.refreshTargetIndex();
        this.refreshRenderedRelations();
        new Notice("AI Labs relations refreshed");
      },
    });
  }

  async loadSettings(): Promise<void> {
    this.settings = Object.assign({}, DEFAULT_SETTINGS, await this.loadData());
  }

  private refreshTargetIndex(): void {
    this.targets.clear();
    for (const file of this.app.vault.getMarkdownFiles()) {
      const frontmatter = this.app.metadataCache.getFileCache(file)?.frontmatter as Record<string, unknown> | undefined;
      const id = typeof frontmatter?.id === "string" ? frontmatter.id : undefined;
      if (!id) continue;
      this.targets.set(id, { id, path: file.path, title: this.titleFor(file, frontmatter) });
    }
  }

  private titleFor(file: TFile, frontmatter?: Record<string, unknown>): string {
    if (typeof frontmatter?.title === "string") return frontmatter.title;
    return file.basename;
  }

  private refreshRenderedRelations(): void {
    for (const view of this.app.workspace.getLeavesOfType("markdown")) {
      const markdownView = view.view;
      if (!(markdownView instanceof MarkdownView)) continue;
      const section = markdownView.containerEl.querySelector<HTMLElement>(".markdown-preview-section");
      if (section) this.renderRelations(section, markdownView.file?.path ?? "");
    }
  }

  private renderRelations(section: HTMLElement, sourcePath: string): void {
    section.querySelector(".ai-labs-relations")?.remove();
    if (!sourcePath) return;

    const file = this.app.vault.getAbstractFileByPath(sourcePath);
    if (!(file instanceof TFile)) return;
    const frontmatter = this.app.metadataCache.getFileCache(file)?.frontmatter as Record<string, unknown> | undefined;
    const relations = this.normalizeRelations(frontmatter?.relations);
    if (relations.length === 0) return;

    const container = section.createDiv({ cls: "ai-labs-relations callout" });
    container.createEl("div", { cls: "callout-title", text: "Relations" });
    const list = container.createEl("ul", { cls: "ai-labs-relations-list" });
    for (const relation of relations) {
      const item = list.createEl("li");
      item.createEl("code", { text: relation.type ?? "related_to" });
      item.createSpan({ text: " → " });
      this.renderTarget(item, relation.target ?? "", sourcePath);
    }
  }

  private normalizeRelations(value: unknown): Relation[] {
    if (Array.isArray(value)) return value.filter(this.isRelation);
    return this.isRelation(value) ? [value] : [];
  }

  private isRelation(value: unknown): value is Relation {
    return typeof value === "object" && value !== null && "target" in value;
  }

  private renderTarget(parent: HTMLElement, targetId: string, sourcePath: string): void {
    const target = this.targets.get(targetId);
    if (target?.path) {
      const link = parent.createEl("a", { cls: "internal-link", text: target.title ?? targetId });
      link.addEventListener("click", (event) => {
        event.preventDefault();
        void this.app.workspace.openLinkText(target.path ?? "", sourcePath, false);
      });
      return;
    }
    if (/^https?:\/\//.test(targetId)) {
      parent.createEl("a", { text: targetId, href: targetId });
      return;
    }
    parent.createEl("code", { text: targetId || "(missing target)" });
  }
}

"use strict";
var __defProp = Object.defineProperty;
var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
var __getOwnPropNames = Object.getOwnPropertyNames;
var __hasOwnProp = Object.prototype.hasOwnProperty;
var __defNormalProp = (obj, key, value) => key in obj ? __defProp(obj, key, { enumerable: true, configurable: true, writable: true, value }) : obj[key] = value;
var __export = (target, all) => {
  for (var name in all)
    __defProp(target, name, { get: all[name], enumerable: true });
};
var __copyProps = (to, from, except, desc) => {
  if (from && typeof from === "object" || typeof from === "function") {
    for (let key of __getOwnPropNames(from))
      if (!__hasOwnProp.call(to, key) && key !== except)
        __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
  }
  return to;
};
var __toCommonJS = (mod) => __copyProps(__defProp({}, "__esModule", { value: true }), mod);
var __publicField = (obj, key, value) => __defNormalProp(obj, typeof key !== "symbol" ? key + "" : key, value);

// main.ts
var main_exports = {};
__export(main_exports, {
  default: () => AILabsRelationsPlugin
});
module.exports = __toCommonJS(main_exports);
var import_obsidian = require("obsidian");
var DEFAULT_SETTINGS = {
  showEvidence: false
};
var AILabsRelationsPlugin = class extends import_obsidian.Plugin {
  constructor() {
    super(...arguments);
    __publicField(this, "settings", DEFAULT_SETTINGS);
    __publicField(this, "targets", /* @__PURE__ */ new Map());
  }
  async onload() {
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
        new import_obsidian.Notice("AI Labs relations refreshed");
      }
    });
  }
  async loadSettings() {
    this.settings = Object.assign({}, DEFAULT_SETTINGS, await this.loadData());
  }
  refreshTargetIndex() {
    var _a;
    this.targets.clear();
    for (const file of this.app.vault.getMarkdownFiles()) {
      const frontmatter = (_a = this.app.metadataCache.getFileCache(file)) == null ? void 0 : _a.frontmatter;
      const id = typeof (frontmatter == null ? void 0 : frontmatter.id) === "string" ? frontmatter.id : void 0;
      if (!id) continue;
      this.targets.set(id, { id, path: file.path, title: this.titleFor(file, frontmatter) });
    }
  }
  titleFor(file, frontmatter) {
    if (typeof (frontmatter == null ? void 0 : frontmatter.title) === "string") return frontmatter.title;
    return file.basename;
  }
  refreshRenderedRelations() {
    var _a, _b;
    for (const view of this.app.workspace.getLeavesOfType("markdown")) {
      const markdownView = view.view;
      if (!(markdownView instanceof import_obsidian.MarkdownView)) continue;
      const section = markdownView.containerEl.querySelector(".markdown-preview-section");
      if (section) this.renderRelations(section, (_b = (_a = markdownView.file) == null ? void 0 : _a.path) != null ? _b : "");
    }
  }
  renderRelations(section, sourcePath) {
    var _a, _b, _c, _d;
    (_a = section.querySelector(".ai-labs-relations")) == null ? void 0 : _a.remove();
    if (!sourcePath) return;
    const file = this.app.vault.getAbstractFileByPath(sourcePath);
    if (!(file instanceof import_obsidian.TFile)) return;
    const frontmatter = (_b = this.app.metadataCache.getFileCache(file)) == null ? void 0 : _b.frontmatter;
    const relations = this.normalizeRelations(frontmatter == null ? void 0 : frontmatter.relations);
    if (relations.length === 0) return;
    const container = section.createDiv({ cls: "ai-labs-relations callout" });
    container.createEl("div", { cls: "callout-title", text: "Relations" });
    const list = container.createEl("ul", { cls: "ai-labs-relations-list" });
    for (const relation of relations) {
      const item = list.createEl("li");
      item.createEl("code", { text: (_c = relation.type) != null ? _c : "related_to" });
      item.createSpan({ text: " \u2192 " });
      this.renderTarget(item, (_d = relation.target) != null ? _d : "", sourcePath);
    }
  }
  normalizeRelations(value) {
    if (Array.isArray(value)) return value.filter(this.isRelation);
    return this.isRelation(value) ? [value] : [];
  }
  isRelation(value) {
    return typeof value === "object" && value !== null && "target" in value;
  }
  renderTarget(parent, targetId, sourcePath) {
    var _a;
    const target = this.targets.get(targetId);
    if (target == null ? void 0 : target.path) {
      const link = parent.createEl("a", { cls: "internal-link", text: (_a = target.title) != null ? _a : targetId });
      link.addEventListener("click", (event) => {
        var _a2;
        event.preventDefault();
        void this.app.workspace.openLinkText((_a2 = target.path) != null ? _a2 : "", sourcePath, false);
      });
      return;
    }
    if (/^https?:\/\//.test(targetId)) {
      parent.createEl("a", { text: targetId, href: targetId });
      return;
    }
    parent.createEl("code", { text: targetId || "(missing target)" });
  }
};

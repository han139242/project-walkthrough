# Project Walkthrough · 项目开发复盘

[![检查](https://github.com/han139242/project-walkthrough/actions/workflows/check.yml/badge.svg)](https://github.com/han139242/project-walkthrough/actions/workflows/check.yml)

把 AI 搭出来的项目讲明白。这个 [Agent Skill](https://agentskills.io/specification) 从 Git、设计稿、变更记录和测试中找证据，还原项目遇到过什么问题、为什么改、现在一条请求怎么走，最后给你一段可以讲给别人听的稿子。

## 适用场景

- 自己参与或用 AI 实现了项目，想梳理每次重要变更的来龙去脉。
- 接手已有代码，想同时理解开发历史、架构和一条真实调用链。
- 准备答辩、面试或交接，需要带证据的讲义和口述稿。

有 Git 时，从关键提交、diff 和工作树版本定位变化。没有 Git 时，从标明日期的设计、交付、验收和旧快照还原可证阶段。若只留下当前代码，按模块依赖给出教学顺序，并说明哪些历史无法还原。

## 安装和使用

下载 [发行版源码](https://github.com/han139242/project-walkthrough/releases)，复制 [`skills/project-walkthrough/`](skills/project-walkthrough) 整个目录，包括 `SKILL.md`、`references/` 和 `agents/`。

- 单个项目使用。放到目标项目的 `.agents/skills/`。
- 用于多个 Codex 项目。放到用户目录的 `.agents/skills/`。

用法参考 [Codex 本地 Skill 加载规则](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills)。在项目对话中运行：

```text
用 $project-walkthrough 讲清这个项目怎么一步步做出来的。
重点解释每次遇到了什么问题、为什么选这个方案、思路从哪来。
带我跟一次当前源码调用链，再给我一段能直接念的口述稿。
```

Skill 由当前编程助手运行，本地取证可使用 Git 和常见文件读取工具。默认从已获准访问的项目资料取证。阅读历史时核对版本和原文，区分已落地、设计草案和推断。

## 示例

试试[合成座位预约样例](examples/seat-reservation/README.md)。它包含旧版重复写入的现象、实际去重逻辑、未上线的 Redis 草案和一条可运行的验证。样例说明同一段代码能证明的事，以及回答「当时为什么这么改」时还需要什么材料。

## 贡献与验证

欢迎通过 [Issues](https://github.com/han139242/project-walkthrough/issues) 反馈漏读证据、时间线混用、源码引用错误或讲解难以复述的情况。提交复现时附预期、实际输出和可公开材料。改动 Skill 行为时，可以用有 Git 和无 Git 的输入各试一次，保留容易讲错的一条结论。

```bash
python -B scripts/check_skill.py
python -B -m unittest discover -s examples/seat-reservation -p 'test_*.py'
```

GitHub Actions 在推送到 `main` 和提交 PR 时运行同样的检查。发布记录见 [CHANGELOG](CHANGELOG.md)。

## 相关项目

[Code Archaeology Skill](https://github.com/luanluan1/code-archaeology-skill) 专注 Git 变更取证。[codebase-tutorial](https://github.com/rowlando/codebase-tutorial) 将当前源码组织成教学章节。[GitView](https://github.com/carstenbund/gitview) 将 Git 历史整理成项目演进故事。Project Walkthrough 将带证据的历史复盘、当前调用链和可复述讲义放在一次任务里。

按 [MIT License](LICENSE) 开源。

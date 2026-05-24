# Seed Knowledge Base — NEAR + Zcash AI Agent Project

> This file contains extracted content from the sources listed in `seed_sources.csv`. It is intended to be ingested directly into the agent's knowledge corpus (via RAG, long context, or hybrid). Each section is self-contained; sources can be split into individual files if needed for chunking.
>
> Last refreshed: 2026-05-24

---

## TABLE OF CONTENTS

1. [Ironclaw — The Runtime Layer](#1-ironclaw--the-runtime-layer)
2. [NEAR Intents — The Cross-Chain Layer](#2-near-intents--the-cross-chain-layer)
3. [NEAR House of Stake — Governance](#3-near-house-of-stake--governance)
4. [NEAR Chain Signatures / MPC Infrastructure](#4-near-chain-signatures--mpc-infrastructure)
5. [Zcash — Official Network Information](#5-zcash--official-network-information)
6. [Zcash Community Grants (ZCG)](#6-zcash-community-grants-zcg)
7. [Zcash Community Forum](#7-zcash-community-forum)
8. [Existing Related Work (NEAR + Zcash AI agents)](#8-existing-related-work)
9. [User's Posted Forum Drafts](#9-users-posted-forum-drafts)

---

## 1. IRONCLAW — THE RUNTIME LAYER

**Source:** github.com/nearai/ironclaw and docs.ironclaw.com
**License:** MIT OR Apache-2.0
**Stars (May 2026):** 12.3k | **Forks:** 1.4k

### 1.1 What Ironclaw Is

IronClaw is a secure, open-source AI agent framework built in Rust and deployed on NEAR AI Cloud. It is an "Agent OS focused on privacy, security and extensibility." It is an OpenClaw-inspired implementation in Rust. The repository's listed contributors include Illia Polosukhin (NEAR Protocol co-founder, also co-author of "Attention is All You Need"), Firat Sertgoz (NEAR core dev, previously contributed to nearcore and nearai), and Claude (Anthropic's model, significant contributor).

### 1.2 Philosophy

IronClaw is built on a simple principle: **your AI assistant should work for you, not against you**. In a world where AI systems are increasingly opaque about data handling and aligned with corporate interests, IronClaw takes a different approach:

- **Your data stays yours** — All information is stored locally, encrypted, and never leaves your control
- **Transparency by design** — Open source, auditable, no hidden telemetry or data harvesting
- **Self-expanding capabilities** — Build new tools on the fly without waiting for vendor updates
- **Defense in depth** — Multiple security layers protect against prompt injection and data exfiltration

### 1.3 Core Features

**Security First:**
- WASM Sandbox — Untrusted tools run in isolated WebAssembly containers with capability-based permissions
- Credential Protection — Secrets are never exposed to tools; injected at the host boundary with leak detection
- Prompt Injection Defense — Pattern detection, content sanitization, and policy enforcement
- Endpoint Allowlisting — HTTP requests only to explicitly approved hosts and paths

**Always Available:**
- Multi-channel — REPL, HTTP webhooks, WASM channels (Telegram, Slack), and web gateway
- Docker Sandbox — Browser automation and code execution in isolated containers
- Job System — Long-running tasks execute in the background
- Persistent Memory — Remembers context across conversations

**Extensible:**
- Build skills — Create new tools with natural language
- Scheduled routines — Automate recurring tasks
- Custom channels — Connect to any platform
- Multiple LLMs — Use Claude, GPT-4, Gemini, local models, or NEAR AI

### 1.4 Installation and Setup

IronClaw can be installed as a local binary:

```bash
cargo install ironclaw

# Set up database
createdb ironclaw
psql ironclaw -c "CREATE EXTENSION IF NOT EXISTS vector;"

# Run onboarding
ironclaw onboard
```

The onboarding wizard handles:
1. Database connection
2. NEAR AI authentication
3. Encryption key generation
4. Initial user configuration
5. First agent interaction

### 1.5 LLM Provider Support

IronClaw supports:
- NEAR AI — Default provider with multiple open-source models
- Anthropic — Claude models
- OpenAI — GPT models
- GitHub Copilot
- Google Gemini
- MiniMax
- Mistral
- Ollama — local models
- OpenAI-compatible endpoints such as OpenRouter, Together AI, Fireworks AI

### 1.6 Identity Files

IronClaw uses four identity files that are automatically injected into the LLM system prompt:

1. **AGENTS.md** — General operating instructions
2. **SOUL.md** — Agent personality, mission, and values
3. **USER.md** — User preferences and context
4. **IDENTITY.md** — Core agent identity

For IronBridge, this is important because we can map our agent configuration into these files rather than relying only on a single system prompt.

### 1.7 Security Architecture

IronClaw uses defense-in-depth:

- encryption at rest;
- credential vaulting;
- sandboxed tool execution;
- host-side secret injection;
- network endpoint allowlisting;
- command injection detection;
- prompt injection mitigation;
- audit logs;
- no hidden telemetry.

Important wording for the agent: **do not claim IronClaw guarantees perfect privacy**. It is better to say that IronClaw is designed to improve privacy and security through local storage, sandboxing, credential isolation, and optional deployment patterns.

---

## 2. NEAR INTENTS — THE CROSS-CHAIN LAYER

**Sources:** docs.near-intents.org and docs.near.org

### 2.1 What NEAR Intents Are

NEAR Intents are a multichain transaction protocol where users specify desired outcomes rather than low-level transaction steps. A user or agent says what they want to happen — for example, swap asset X for asset Y across chains — and solvers / market makers compete to fulfil the intent.

The basic flow:

1. User creates an intent.
2. Solvers or market makers compete to satisfy it.
3. The best solution is selected.
4. The Verifier Contract checks validity.
5. The transaction settles across relevant chains.

### 2.2 Key Components

- **1-Click Swap API** — allows applications to integrate simple cross-chain swaps
- **React Widget** — front-end integration for apps
- **SDKs** — TypeScript, Go, Rust
- **Market Makers / Solvers** — provide liquidity and execution paths
- **Verifier Contract** — validates and settles intents

### 2.3 Why Intents Matter for Agents

AI agents are better at expressing goals than manually constructing transactions. Intents allow an agent to express an objective while the infrastructure handles routing and execution.

For IronBridge v0 we do not use Intents directly for execution. Instead, we explain them and help users reason about collaboration opportunities. Later versions might explore payments, grants, or workflow actions, but v0 stays read-only.

### 2.4 NEAR × Zcash Relevance

NEAR Intents have become relevant to Zcash because they can enable cross-chain ZEC swaps in a way that is more abstracted and potentially more user-friendly than direct bridge or exchange workflows.

The strongest narrative is not: "NEAR wants to market to Zcash." The strongest narrative is: "NEAR has cross-chain execution infrastructure that may solve real usability problems for Zcash users, and Zcash has privacy expectations that can stress-test NEAR's agent infrastructure."

---

## 3. NEAR HOUSE OF STAKE — GOVERNANCE

**Sources:** gov.near.org House of Stake category and houseofstake/proposals repository

### 3.1 What House of Stake Is

House of Stake is NEAR's governance institution for stake-weighted proposals and funding decisions. It uses formal proposal formats known as HSPs — House of Stake Proposals.

### 3.2 HSP Format

A full HSP-style proposal usually requires:

- YAML-style frontmatter
- Abstract
- Context
- Problem
- Approach
- Value Hypothesis
- KPIs
- Technical Specification
- Budget

For IronBridge, the agent should distinguish between:

- a discussion-stage forum post;
- an HSP-style outline;
- a formal HSP ready for submission.

It should not claim that a discussion post is a formal HSP.

### 3.3 Governance Drafting Tone

NEAR governance posts should be:

- clear;
- strategic;
- builder-focused;
- execution-oriented;
- KPI-aware;
- honest about risks.

Bad NEAR governance posts are vague AI hype. Good posts explain what should be funded, why it matters, how it will be measured, and why now.

---

## 4. NEAR CHAIN SIGNATURES / MPC INFRASTRUCTURE

### 4.1 Relevance

NEAR Chain Signatures and MPC infrastructure are part of NEAR's broader chain abstraction story. They help NEAR accounts interact with other chains without users needing to manage separate key material for every chain.

For the IronBridge v0 agent, this is contextual rather than core. The agent may mention it when explaining NEAR's chain abstraction stack, but should not overemphasize it unless the user asks.

### 4.2 Caution

Do not imply that Chain Signatures automatically solve all Zcash privacy issues. Zcash privacy has distinct protocol-level requirements and community expectations. Keep explanations precise.

---

## 5. ZCASH — OFFICIAL NETWORK INFORMATION

**Sources:** z.cash and Zcash technical materials

### 5.1 What Zcash Is

Zcash is a privacy-focused Layer 1 cryptocurrency. It uses zero-knowledge proofs, specifically zk-SNARKs, to allow shielded transactions where transaction details can be hidden while still being valid under the protocol rules.

### 5.2 Core Concepts

- **ZEC** — native asset of the Zcash network
- **Transparent addresses** — similar to Bitcoin-style public addresses
- **Shielded addresses** — preserve transaction privacy
- **Shielded pools** — privacy-preserving transaction pools
- **Viewing keys** — allow selective disclosure
- **zk-SNARKs** — cryptographic proofs enabling private validity

### 5.3 Community Culture

The Zcash community is strongly privacy-oriented, technically careful, and often skeptical of vague claims about trustlessness, decentralization, or privacy.

For any post aimed at Zcash users:

- avoid hype;
- define trust assumptions;
- make self-hosting and auditability clear;
- avoid implying that convenience is more important than privacy;
- ask for critique rather than assuming acceptance.

### 5.4 Current Themes

Relevant ongoing themes include:

- wallet UX;
- shielded adoption;
- ZCG grants;
- NU7 network upgrade;
- Zcash forum governance;
- integrations and cross-chain infrastructure;
- AI agent infrastructure and MCP-style integrations.

---

## 6. ZCASH COMMUNITY GRANTS (ZCG)

**Source:** zcashcommunitygrants.org

### 6.1 What ZCG Is

Zcash Community Grants is a grants program supporting work that benefits the Zcash ecosystem. Grant applications are usually reviewed by the community and by the ZCG committee.

### 6.2 Typical Grant Application Elements

A strong ZCG-style outline should include:

- Project title
- Applicant / team
- Summary
- Problem
- Proposed solution
- Benefit to Zcash
- Milestones
- Deliverables
- Budget
- Risks and mitigations
- Maintenance plan
- Prior relevant work
- Open questions

### 6.3 Grant Process Principles

The agent should not turn weak ideas into polished proposals. It should ask whether:

- the work is real;
- the team can deliver;
- the budget is justified;
- the deliverables are measurable;
- the output benefits Zcash users;
- the work overlaps with existing projects.

### 6.4 IronBridge Relevance to ZCG

IronBridge can help Zcash users prepare better grant ideas by:

- clarifying the problem;
- identifying related forum threads;
- drafting structured outlines;
- identifying likely objections;
- improving milestone and KPI quality;
- checking whether a proposal sounds too hype-driven.

---

## 7. ZCASH COMMUNITY FORUM

### 7.1 Forum Role

The Zcash Community Forum is the main place for public discussion of ecosystem proposals, grant ideas, wallet projects, governance, and technical updates.

### 7.2 Forum Drafting Style

Good Zcash forum posts tend to:

- explain context clearly;
- avoid overclaiming;
- address trade-offs;
- welcome critique;
- show awareness of prior work;
- respect privacy assumptions.

### 7.3 Categories Relevant to IronBridge

Likely relevant categories include:

- Community Collaborations
- Zcash Community Grants
- General
- Zcash Apps
- Technical / protocol discussions

### 7.4 Zcash-Specific Objections to Expect

When proposing IronBridge or any NEAR/Ironclaw collaboration, expect questions such as:

- Why should Zcash users trust a NEAR-built runtime?
- What data leaves the user's machine?
- Can it be self-hosted?
- What model provider sees the prompts?
- Are logs retained?
- Is the code auditable?
- Is this a genuine Zcash tool or a NEAR marketing exercise?
- Does it overlap with existing Zcash MCP or wallet-agent work?
- Who maintains it?
- What happens if the knowledge base becomes stale?

---

## 8. EXISTING RELATED WORK (NEAR + ZCASH AI AGENTS)

### 8.1 Zcash MCP Server for AI Agent Integration

There is active Zcash forum work around exposing Zcash functions to AI agents through an MCP server. This is important overlap. IronBridge should not pretend to be the first AI/Zcash project.

Differentiation:

- MCP server work exposes Zcash functionality to agents.
- IronBridge focuses on ecosystem navigation, governance drafting, grant quality, and NEAR/Zcash collaboration context.
- IronBridge v0 is read-only and does not operate wallets.

### 8.2 Zipher

Zipher is described as a Zcash wallet for humans and agents. This is also relevant overlap. IronBridge should not compete with wallet projects in v0.

Differentiation:

- Zipher is wallet/action infrastructure.
- IronBridge is research, drafting, and governance support.

### 8.3 BazaarSwap / ZEC DeFi Discussion

BazaarSwap and similar discussions show growing interest in ZEC interoperability and DeFi access. IronBridge can help users understand these discussions but should avoid trading advice or yield optimization.

### 8.4 NEAR AI / OpenClaw / Ironclaw

IronBridge sits on top of NEAR's AI agent runtime work. It should credit NEAR AI and Ironclaw clearly, but avoid sounding like a pure NEAR promotional bot when talking to Zcash users.

---

## 9. USER'S POSTED FORUM DRAFTS

### 9.1 NEAR Ironclaw Builder Fund Discussion

The author has posted a NEAR governance forum discussion proposing an Ironclaw Builder Fund to support builders shipping Ironclaw agents using NEAR Intents.

Core thesis:

- NEAR has renewed attention.
- Ironclaw gives NEAR a privacy-first agent runtime.
- NEAR Intents gives agents a payment / execution layer.
- NEAR should consider funding builders to create useful Ironclaw agents.
- IronBridge can serve as the first proof-of-concept.

### 9.2 Zcash AI Solutions Grant Track Draft

The author is drafting a Zcash forum post proposing a focused grant track for AI solutions serving Zcash users using NEAR tech stack.

Important framing:

- Do not pitch Zcash users with NEAR hype.
- Start from Zcash user needs.
- Explain privacy assumptions clearly.
- Position Ironclaw as something to test, not something to trust blindly.
- Make the proposal read-only and low-risk at v0.

---

## 10. IRONBRIDGE — AGENT PURPOSE

IronBridge is a privacy-first NEAR × Zcash ecosystem research and governance drafting agent.

Its core jobs:

1. Help Zcash users understand NEAR Intents, Ironclaw, and collaboration opportunities.
2. Help NEAR users understand Zcash's privacy expectations and governance culture.
3. Draft Zcash forum posts and ZCG-style grant outlines.
4. Draft NEAR governance discussion posts and HSP-style outlines.
5. Surface likely objections and missing context before users post.

### 10.1 What IronBridge Is Not

IronBridge is not:

- a trading assistant;
- a price prediction bot;
- a wallet agent;
- a grant spam generator;
- an automatic poster;
- a governance manipulation tool;
- a replacement for human community discussion.

### 10.2 Success Criteria for v0

IronBridge v0 succeeds if it can:

- explain Ironclaw to a skeptical Zcash user;
- draft a credible Zcash Community Collaborations post;
- draft a NEAR governance discussion post;
- review drafts for objections and weak assumptions;
- refuse financial advice cleanly;
- avoid privacy overclaims;
- distinguish what it knows from what it does not know.

---

## 11. SAMPLE DEMO OUTPUT EXPECTATIONS

### 11.1 Good answer pattern

When asked: "Why should Zcash users care about Ironclaw?"

A good answer should say:

- They should not care automatically.
- The reason it may be worth examining is that Zcash users need privacy-preserving AI tools if AI is going to be used for governance, grants, or ecosystem research.
- Ironclaw is relevant because it is open-source, self-hostable, security-oriented, and designed around credential isolation and sandboxed tools.
- But Zcash users should ask hard questions about model providers, logs, deployment, TEEs, self-hosting, and auditability.
- The safest v0 use case is read-only research and drafting, not wallet actions.

### 11.2 Bad answer pattern

A bad answer would say:

- Ironclaw guarantees total privacy.
- Zcash users should adopt NEAR infrastructure.
- This will make ZEC price go up.
- The community should fund it because AI is the future.
- The agent can vote or trade for users.

---

## 12. NEXT INGESTION TARGETS

The next sources to ingest should be:

1. Exact Zcash MCP Server forum thread URL and content.
2. Exact Zipher forum thread URL and content.
3. Exact BazaarSwap forum thread URL and content.
4. Current ZCG application template.
5. Current House of Stake HSP-001 template.
6. NEAR Intents docs sections on ZEC / Zcash if available.
7. Any Cake Wallet / NEAR Intents ZEC swap announcement.
8. The author's full Zcash draft once prepared.
9. The author's full NEAR forum post.

---

## 13. OPERATING WARNINGS FOR THE AGENT

- Do not overstate current adoption.
- Do not invent volume, fee, or integration metrics unless explicitly sourced.
- Do not say a forum thread exists unless the source is in the corpus.
- Do not claim that NEAR won a privacy award unless the exact source is in the corpus.
- Do not imply Zcash users should trust TEEs without caveats.
- Do not treat AI as inherently good for governance.
- Do not create a grant proposal unless the user provides real deliverables.
- Do not draft fake testimonials or fake community support.
- Always separate: fact, interpretation, recommendation.

---

## 14. PUBLIC LAUNCH POSITIONING

Recommended public framing:

> I'm building IronBridge: a privacy-first NEAR × Zcash research and drafting agent designed for Ironclaw.
>
> v0 is read-only. It does not trade, vote, post, or handle wallets.
>
> Its job is to help users understand NEAR × Zcash collaboration opportunities, draft better governance/grant posts, and surface objections before posting.
>
> The point is not to ask Zcash users to trust NEAR infrastructure blindly. The point is to test, in public, whether Ironclaw can support AI tools that meet privacy-first expectations.

---

End of seed knowledge base.

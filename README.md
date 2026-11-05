<p align="center">
  <img src="assets/vedant-3d-github-banner.png" alt="Vedant — Full-Stack Developer and AI Enthusiast" width="100%" />
</p>

<h1 align="center">Hey, I'm Vedant Shrivastava 👋</h1>

<p align="center">
  <a href="https://github.com/vedant-175/vedant-175">
    <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&duration=3200&pause=900&color=34D399&center=true&vCenter=true&width=720&lines=Full-Stack+Developer;AI+Enthusiast;I+turn+LLMs+into+real+products;React+%2B+TypeScript+%2B+Node.js;Open+to+internships+%E2%80%94+let%27s+build+something" alt="Typing animation" />
  </a>
</p>

<p align="center">
  <a href="https://vedant-175.github.io/website/"><img src="https://img.shields.io/badge/Portfolio-34D399?style=for-the-badge&logo=googlechrome&logoColor=black" alt="Portfolio" /></a>
  <a href="https://www.linkedin.com/in/vedant-shrivastava175"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://github.com/vedant-175?tab=repositories"><img src="https://img.shields.io/badge/Repositories-0d1117?style=for-the-badge&logo=github&logoColor=34D399" alt="Repositories" /></a>
  <img src="https://img.shields.io/badge/Open%20to-Internships-34D399?style=for-the-badge" alt="Open to internships" />
</p>

<br/>

## ⚡ The short version

I'm a Computer Science Engineering student who likes shipping things people can actually use. I build full-stack web apps and wire LLMs into them, so AI becomes a feature people use rather than a demo.

```ts
const vedant = {
  role: "CSE Student · Full-Stack Developer",
  focus: ["React + TypeScript", "Node.js APIs", "LLM integration"],
  currentlyBuilding: "GitSentinel · Autonomous AI Code Review & Security Gate",
  currentlyLearning: ["System design", "Distributed systems", "Deployment & CI/CD"],
  lookingFor: "Full-stack / AI engineering internships",
  funFact: "I'd rather ship it and iterate than polish it forever.",
};
```

<br/>

## 🛠️ Tech Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=js,ts,python,java,html,css&theme=dark" alt="Languages" /><br/><br/>
  <img src="https://skillicons.dev/icons?i=react,nextjs,tailwind,bootstrap,vite&theme=dark" alt="Frontend" /><br/><br/>
  <img src="https://skillicons.dev/icons?i=nodejs,express,mongodb,postgres&theme=dark" alt="Backend and databases" /><br/><br/>
  <img src="https://skillicons.dev/icons?i=git,github,vscode,vercel&theme=dark" alt="Tools" />
</p>

<br/>

## 🚀 Featured Project

### 🛡️ GitSentinel: Autonomous AI Code Review & PR Security Gate

> An enterprise-grade, fail-closed GitHub App and real-time security dashboard that automates Pull Request code reviews. It scans incoming diffs for security vulnerabilities, secrets, and AST lint errors, orchestrates multi-model AI reviews (Claude, Gemini, GPT-4o), and posts inline comments with automated merge gate verdicts.

<p>
  <img src="https://img.shields.io/badge/Next.js_14-0d1117?style=flat-square&logo=nextdotjs&logoColor=white" />
  <img src="https://img.shields.io/badge/TypeScript-0d1117?style=flat-square&logo=typescript&logoColor=3178C6" />
  <img src="https://img.shields.io/badge/Node.js-0d1117?style=flat-square&logo=nodedotjs&logoColor=339933" />
  <img src="https://img.shields.io/badge/PostgreSQL-0d1117?style=flat-square&logo=postgresql&logoColor=4169E1" />
  <img src="https://img.shields.io/badge/Prisma_ORM-0d1117?style=flat-square&logo=prisma&logoColor=white" />
  <img src="https://img.shields.io/badge/Redis_%2B_BullMQ-0d1117?style=flat-square&logo=redis&logoColor=DC382D" />
  <img src="https://img.shields.io/badge/GitHub_App_API-0d1117?style=flat-square&logo=github&logoColor=white" />
  <img src="https://img.shields.io/badge/Multi--LLM-Claude_%7C_Gemini_%7C_GPT--4o-0d1117?style=flat-square&logo=openai&logoColor=white" />
</p>

**What's under the hood**

| | |
|---|---|
| 🛡️ **Fail-Closed Security Gate** | Blocks malicious PRs, hardcoded API secrets, SQL injections, and prompt injections before code ever merges |
| ⚡ **Distributed Queue & Worker** | BullMQ + Redis handles webhook concurrency with jittered exponential backoffs, lease heartbeats, and idempotency locks |
| 🤖 **Multi-Model AI Orchestrator** | Coordinates Claude 3.5 Sonnet, Gemini 1.5 Pro, and GPT-4o with deterministic output validation & fingerprint deduplication |
| 🔍 **Static Analysis (SAST)** | Built-in AST analysis using ESLint, Ruff, Bandit, and dependency vulnerability scanning |
| 📊 **CyberOps Dashboard** | Live telemetry, audit logs, cyber diff inspector, repository health metrics, and interactive AI chatbot |

```mermaid
flowchart LR
    GH(["🐙 GitHub PR Event"]) -->|Webhook| W["Next.js App Router<br/>Dashboard & API"]
    W -->|Enqueue Review Job| R[("⚡ Redis + BullMQ<br/>Priority Queue")]
    R -->|Fair Dispatch| K["⚙️ Worker Service<br/>Node.js Engine"]
    K --> S["🔍 SAST & Secret Scanner<br/>ESLint · Ruff · Bandit"]
    K --> L[["🤖 Multi-Model LLM<br/>Claude · Gemini · GPT-4o"]]
    K -->|"Inline Comments & Checks"| GH
    K -->|"Audit Logs & Metrics"| DB[("🗄️ PostgreSQL<br/>Prisma ORM")]
```

<p>
  <a href="https://github.com/vedant-175/GitSentinel"><img src="https://img.shields.io/badge/View_Repository-34D399?style=for-the-badge&logo=github&logoColor=black" alt="View repository" /></a>
</p>

<br/>

### 🧪 More things I've built

<table>
  <tr>
    <td width="50%" valign="top">
      <h4>🧠 AI Resume Builder</h4>
      <p>A full-stack app that helps people write better resumes with live-preview editor, ATS compatibility scoring (0–100), AI suggestions, and client-side PDF export.</p>
      <p><sub><b>React 19 · TypeScript · Vite · Tailwind · Express · Groq API</b></sub></p>
      <a href="https://github.com/vedant-175/AI-resume-builder">Code</a>
    </td>
    <td width="50%" valign="top">
      <h4>🌐 Interactive Developer Portfolio</h4>
      <p>A personal portfolio exploring 3D visuals, animation, and interactive UI.</p>
      <p><sub><b>React · Three.js · React Three Fiber · GSAP</b></sub></p>
      <a href="https://github.com/vedant-175/My-Portfolio-">Code</a> · <a href="https://vedant-175.github.io/website/">Live</a>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h4>🎓 Smart Internship Portal</h4>
      <p>Capstone MERN app with an AI-powered ATS resume-scoring engine (Groq, Llama 3.3 70B) that falls back to deterministic keyword matching if the API is unavailable. Built with teammates; I worked on the frontend.</p>
      <p><sub><b>React 19 · Vite · Node.js · Express 5 · MongoDB · JWT</b></sub></p>
      <a href="https://github.com/vedant-175/Smart-Internship-portal">Code</a>
    </td>
    <td width="50%" valign="top">
    </td>
  </tr>
</table>

<br/>

## 📈 GitHub Stats

<p align="center">
  <img src="assets/github-stats.svg" alt="GitHub stats" width="100%" />
</p>
<p align="center">
  <img src="assets/github-languages.svg" alt="Top languages" width="49%" />
  <img src="assets/github-streak.svg" alt="GitHub streak" width="49%" />
</p>

<br/>

## 🏆 Achievements & Community

- 🎓 **Google Gemini Student Ambassador** (since Sep 2026)
- 🌱 **GSSoC'26 Ambassador & Contributor** (May–Aug 2026)
- 🏁 **Web-a-Thon 2.0 Finalist**, one of 100 teams (Feb 2026)
- 🏁 **Code-a-Haunt 2.0 Finalist** (Feb 2025)
- 🎓 B.Tech CSE at Lovely Professional University · CGPA 8.54

<br/>

## 🎯 What I'm working toward

- [x] Ship GitSentinel: Autonomous AI PR Code Review & Security Gate
- [x] Build an AI Resume Builder (React + TS + Groq API)
- [x] Build an interactive 3D portfolio
- [ ] Add tests and CI to all main projects
- [ ] Deploy every project with a live demo link
- [x] Contribute to open source (GSSoC'26)
- [ ] Land a full-stack / AI engineering internship

<br/>

## 🤝 Let's Connect

I'm happy to talk about full-stack development, practical LLM apps, or internship opportunities. Open to collaborating on useful open-source projects too.

<p align="center">
  <a href="https://www.linkedin.com/in/vedant-shrivastava175"><img src="https://img.shields.io/badge/Message_me_on_LinkedIn-34D399?style=for-the-badge&logo=linkedin&logoColor=black" alt="LinkedIn" /></a>
</p>

<p align="center"><i>Build with purpose. Learn continuously. Ship reliable software.</i></p>

<p align="center">
  <img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,100:34d399&height=110&section=footer" alt="" />
</p>

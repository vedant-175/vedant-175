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
  currentlyBuilding: "AI-powered developer & career tools",
  currentlyLearning: ["System design", "Testing", "Deployment & CI/CD"],
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

### 🧠 AI Resume Builder: ATS scoring + AI suggestions + PDF export

> A full-stack app that helps people write better resumes. You build one in a live-preview editor, get an **ATS compatibility score (0–100)** with AI-generated tips to improve it, then export a clean PDF.

<p>
  <img src="https://img.shields.io/badge/React_19-0d1117?style=flat-square&logo=react&logoColor=61DAFB" />
  <img src="https://img.shields.io/badge/TypeScript-0d1117?style=flat-square&logo=typescript&logoColor=3178C6" />
  <img src="https://img.shields.io/badge/Vite-0d1117?style=flat-square&logo=vite&logoColor=646CFF" />
  <img src="https://img.shields.io/badge/Tailwind-0d1117?style=flat-square&logo=tailwindcss&logoColor=06B6D4" />
  <img src="https://img.shields.io/badge/Node.js-0d1117?style=flat-square&logo=nodedotjs&logoColor=339933" />
  <img src="https://img.shields.io/badge/Express-0d1117?style=flat-square&logo=express&logoColor=white" />
  <img src="https://img.shields.io/badge/Groq_API-0d1117?style=flat-square&logoColor=white" />
</p>

**What's under the hood**

| | |
|---|---|
| 🎯 **ATS analysis** | Resume text goes to an Express endpoint, then to the Groq LLM API, which returns a 0–100 score plus improvement tips |
| 🧩 **Type-safe forms** | React Hook Form + Zod schemas validate every section before it reaches the preview |
| 🗂️ **Predictable state** | Zustand store, with React Query for server state |
| 📄 **Real PDF export** | One-click download generated client-side with html2pdf.js |
| ☁️ **Deployable** | Split frontend/backend, with Render deployment docs included |

```mermaid
flowchart LR
    U(["👤 User"]) --> F["React 19 + TypeScript<br/>Zustand · React Hook Form · Zod"]
    F -->|"POST /api/ats-score"| B["Express API<br/>Node.js"]
    F -->|"POST /api/generate-content"| B
    B --> G[["Groq LLM API"]]
    F --> P["html2pdf.js<br/>PDF export"]
```

<p>
  <a href="https://github.com/vedant-175/AI-resume-builder"><img src="https://img.shields.io/badge/View_Repository-34D399?style=for-the-badge&logo=github&logoColor=black" alt="View repository" /></a>
  <!-- ADD WHEN LIVE: <a href="YOUR-LIVE-DEMO-URL"><img src="https://img.shields.io/badge/Live_Demo-0d1117?style=for-the-badge&logo=render&logoColor=34D399" alt="Live demo" /></a> -->
</p>

<br/>

### 🧪 More things I've built

<table>
  <tr>
    <td width="50%" valign="top">
      <h4>🌐 Interactive Developer Portfolio</h4>
      <p>A portfolio exploring 3D visuals, animation and interactive UI.</p>
      <p><sub><b>React · Three.js · React Three Fiber · GSAP</b></sub></p>
      <a href="https://github.com/vedant-175/My-Portfolio-">Code</a> · <a href="https://vedant-175.github.io/website/">Live</a>
    </td>
    <td width="50%" valign="top">
      <h4>🎓 Smart Internship Portal</h4>
      <p>An internship discovery and management web app. See the repo README for implementation details and attribution to the original project.</p>
      <p><sub><b>Web application development</b></sub></p>
      <a href="https://github.com/vedant-175/Smart-Internship-Portal">Code</a>
    </td>
  </tr>
</table>

<br/>

## 📈 GitHub Activity

<p align="center">
  <img height="170" src="https://github-readme-stats.vercel.app/api?username=vedant-175&show_icons=true&hide_border=true&bg_color=0d1117&title_color=34d399&icon_color=34d399&text_color=c9d1d9&ring_color=34d399&border_radius=12" alt="GitHub stats" />
  <img height="170" src="https://github-readme-stats.vercel.app/api/top-langs/?username=vedant-175&layout=compact&hide_border=true&bg_color=0d1117&title_color=34d399&text_color=c9d1d9&border_radius=12" alt="Top languages" />
</p>
<p align="center">
  <img src="https://streak-stats.demolab.com?user=vedant-175&hide_border=true&background=0d1117&ring=34d399&fire=34d399&currStreakLabel=34d399&currStreakNum=c9d1d9&sideNums=c9d1d9&sideLabels=c9d1d9&dates=8b949e&border_radius=12" alt="GitHub streak" />
</p>

<br/>

## 🎯 What I'm working toward

- [x] Ship a full-stack AI app (React + TypeScript + Express + LLM API)
- [x] Build an interactive 3D portfolio
- [ ] Add tests and CI to my main projects
- [ ] Deploy every project with a live demo link
- [ ] Contribute to an open-source project
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

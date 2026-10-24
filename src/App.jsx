import { useMemo } from 'react';
import portfolioDocument from '../stitch_agentic_ai_portfolio_site/code.html?raw';
import links from './data/portfolio-links.json';

const projectCard = (project) => `
  <article class="rounded-xl bg-surface-container-low shadow-md overflow-hidden flex flex-col h-full">
    <div class="relative h-36 w-full bg-gradient-to-br from-primary-fixed via-surface-container-lowest to-secondary-fixed flex items-end p-space-md">
      <div class="absolute inset-0 opacity-40" style="background-image:radial-gradient(circle at 15% 20%,#6063ee 0,transparent 24%),radial-gradient(circle at 85% 85%,#4cd7f6 0,transparent 28%)"></div>
      <div class="relative flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-surface-container-lowest/90">
        <span class="w-2 h-2 rounded-full bg-tertiary"></span>
        <span class="font-label-badge text-label-badge text-tertiary uppercase">${project.status}</span>
      </div>
    </div>
    <div class="p-space-md flex flex-col space-y-space-sm flex-1">
      <div><span class="font-label-badge text-label-badge text-primary">${project.label}</span><h3 class="font-headline-md text-[18px] text-on-surface font-bold">${project.name}</h3></div>
      <p class="font-body-md text-body-md text-on-surface-variant leading-relaxed flex-1">${project.description}</p>
      <div class="flex flex-wrap gap-1.5">${project.technologies.map((technology) => `<span class="font-label-badge text-label-badge px-2 py-0.5 rounded bg-surface-container-highest text-on-surface">${technology}</span>`).join('')}</div>
      <div class="pt-space-xs flex items-center gap-space-sm">
        <a class="flex-1 h-9 rounded-lg bg-surface-container-high text-on-surface font-code-sm text-code-sm flex items-center justify-center gap-1.5" href="${project.repository || '#'}" ${project.repository ? 'target="_blank" rel="noreferrer"' : 'aria-disabled="true"'}><span class="material-symbols-outlined text-[16px] text-primary">code</span><span>GitHub Repo</span></a>
        <a class="h-9 px-space-md rounded-lg bg-surface-container-high text-primary font-code-sm text-code-sm flex items-center justify-center gap-1" href="${project.demo || '#'}" ${project.demo ? 'target="_blank" rel="noreferrer"' : 'aria-disabled="true"'}><span class="material-symbols-outlined text-[16px]">play_circle</span><span>Demo</span></a>
      </div>
    </div>
  </article>`;

function buildPortfolioPage(source) {
  const document = new DOMParser().parseFromString(source, 'text/html');
  document.querySelectorAll('body script, body > nav').forEach((element) => element.remove());

  document.querySelectorAll('[data-path="resume"]').forEach((link) => {
    link.href = links.resume;
    link.setAttribute('download', 'Virendra_Resume.docx');
  });
  document.querySelectorAll('a').forEach((link) => {
    if (link.textContent.trim() === 'CV') {
      link.href = links.resume;
      link.setAttribute('download', 'Virendra_Resume.docx');
    }
  });
  document.querySelector('a[href="https://github.com/virendra"]')?.setAttribute('href', links.github);
  document.querySelector('a[href="https://linkedin.com"]')?.setAttribute('href', links.linkedin);
  document.querySelector('a[href="https://leetcode.com/virendra"]')?.setAttribute('href', links.leetcode);
  const email = document.querySelector('#email-address');
  if (email) email.textContent = links.email;
  document.querySelectorAll('a[href^="mailto:"]').forEach((link) => link.href = `mailto:${links.email}`);

  const projects = document.querySelector('#projects');
  if (projects) {
    const heading = projects.firstElementChild;
    projects.replaceChildren(heading);
    const grid = document.createElement('div');
    grid.className = 'project-grid';
    grid.innerHTML = links.projects.map(projectCard).join('');
    projects.append(grid);
  }

  const style = document.createElement('style');
  style.textContent = `
    *,*::before,*::after{animation:none!important;transition:none!important}
    .project-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:1rem}
    a[aria-disabled="true"]{opacity:.6;cursor:not-allowed}
    @media(max-width:700px){.project-grid{grid-template-columns:1fr}.project-grid article{min-width:0}aside[aria-label="Quick section navigation"]{display:flex!important;right:.35rem;transform:translateY(-50%) scale(.88);transform-origin:right center}main>div{padding-right:1rem!important}}
  `;
  document.head.append(style);

  const scrollSpy = document.createElement('script');
  scrollSpy.textContent = `
    addEventListener('scroll',function(){
      var current='hero', sections=document.querySelectorAll('main section[id]');
      sections.forEach(function(section){if(scrollY+160>=section.offsetTop)current=section.id});
      document.querySelectorAll('.dock-nav-item').forEach(function(item){var active=item.dataset.section===current;item.classList.toggle('text-on-primary',active);item.classList.toggle('text-on-surface-variant',!active)});
      var active=document.querySelector('.dock-nav-item[data-section="'+current+'"]'),pill=document.getElementById('dock-active-pill');if(active&&pill)pill.style.top=active.offsetTop+'px';
    },{passive:true});
  `;
  document.body.append(scrollSpy);
  return `<!doctype html>${document.documentElement.outerHTML}`;
}

export default function App() {
  const page = useMemo(() => buildPortfolioPage(portfolioDocument), []);
  return <iframe title="Virendra AI portfolio" srcDoc={page} className="portfolio-frame" />;
}

(function(){
const key='saad-site-theme';const media=window.matchMedia('(prefers-color-scheme: dark)');
function saved(){try{return localStorage.getItem(key)}catch(e){return null}}
function apply(theme){document.documentElement.dataset.theme=theme;const b=document.getElementById('theme-toggle');if(b){b.textContent=theme==='dark'?'☀ Light':'☾ Dark';b.setAttribute('aria-label',theme==='dark'?'Switch to light colors':'Switch to dark colors');b.setAttribute('aria-pressed',String(theme==='dark'))}}
apply(saved()||'light');
document.addEventListener('DOMContentLoaded',function(){apply(saved()||'light');document.getElementById('theme-toggle').addEventListener('click',function(){const theme=document.documentElement.dataset.theme==='dark'?'light':'dark';try{localStorage.setItem(key,theme)}catch(e){}apply(theme)})});
})();
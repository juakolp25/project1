const btnToggle = document.getElementById('btn-toggle');
const lineToggle = document.querySelectorAll('.line');
const menuResponsive = document.getElementById('menu-list_responsive');
const toggleTheme = document.getElementById('toggle-theme');
const toggleText = document.getElementById('toggle-text');

btnToggle.addEventListener('click', ()=>{
    lineToggle.forEach(x => x.classList.toggle('toggle-line_cruz'));
    menuResponsive.classList.toggle('link-menu_responsive-visible');
});


/* <-- Seccion de los temas de la pag --> */

toggleTheme.addEventListener('click', ()=>{
    document.body.classList.toggle("light");
    if(toggleText.textContent.includes("Dark Mode")){
        toggleText.textContent = 'Light Mode';
    }else{
        toggleText.textContent = 'Dark Mode';
    }

    if (document.body.classList.contains('light')) {
        localStorage.setItem('light-mode', 'true')
    } else{
        localStorage.setItem('light-mode', 'false')
    }
})

if (localStorage.getItem('light-mode') === 'true') {
    document.body.classList.add('light');
    toggleText.textContent = 'Light Mode';
}else{
    document.body.classList.remove('light')
    toggleText.textContent = 'Dark Mode';
}


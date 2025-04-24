document.addEventListener('DOMContentLoaded', () => {
  const navLinks = document.querySelectorAll('a[href^="#"]');
  navLinks.forEach(link => {
    link.addEventListener('click', function (event) {
      console.log('Link wurde geklickt!'); // Testausgabe
      event.preventDefault();
      const targetId = this.getAttribute('href');
      scrollToSection(targetId);
      const menuLinks = document.querySelector(".menu-links");
      const hamburgerIcon = document.querySelector(".hamburger-icon");
      if (menuLinks.classList.contains('open')) {
        toggleMenu();
      }
    });
  });
});

function toggleMenu() {
  const menu = document.querySelector(".menu-links");
  const icon = document.querySelector(".hamburger-icon");
  menu.classList.toggle("open");
  icon.classList.toggle("open");
}

// Deaktiviert das Rechtsklick-Menü auf der gesamten Seite
document.addEventListener('contextmenu', (e) => {
  e.preventDefault();
}, { passive: false });

// Verhindert das Ziehen von Bildern
document.querySelectorAll('img').forEach((img) => {
  img.addEventListener('dragstart', (e) => {
    e.preventDefault();
  }, { passive: false });
});

// Scrollt sanft zu einer Section
function scrollToSection(sectionId) {
  const section = document.querySelector(sectionId);
  if (!section) {
    console.warn(`Section ${sectionId} nicht gefunden`);
    return;
  }

  section.scrollIntoView({
    behavior: 'smooth',
    block: 'start'
  });
}

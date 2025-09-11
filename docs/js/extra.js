// Scripts adicionais para melhorar a experiência
document$.subscribe(() => {
  // Abre links externos em nova aba
  const links = document.querySelectorAll('a[href^="http"]');
  links.forEach(link => {
    link.setAttribute('target', '_blank');
    link.setAttribute('rel', 'noopener');
  });
  
  // Adiciona atributo title para ícones
  const icons = document.querySelectorAll('.md-icon');
  icons.forEach(icon => {
    const altText = icon.getAttribute('alt');
    if (altText) {
      icon.setAttribute('title', altText.replace('icon:', '').trim());
    }
  });
});
document.addEventListener("DOMContentLoaded", () => {
  const button = document.getElementById("action-btn");
  if (button) {
    button.addEventListener("click", () => {
      alert("Hello from script.js!");
    });
  }
  const y = document.getElementById("year");
  if (y) y.textContent = String(new Date().getFullYear());

  // Theme toggle
  const root = document.documentElement;
  const toggle = document.getElementById("theme-toggle");
  const stored = localStorage.getItem("theme");
  if (stored === "light") root.classList.add("theme-light");
  updateToggleIcon();

  if (toggle) {
    toggle.addEventListener("click", () => {
      root.classList.toggle("theme-light");
      const isLight = root.classList.contains("theme-light");
      localStorage.setItem("theme", isLight ? "light" : "dark");
      updateToggleIcon();
    });
  }

  function updateToggleIcon() {
    const icon = document.querySelector(".theme-toggle__icon");
    if (!icon) return;
    const isLight = document.documentElement.classList.contains("theme-light");
    icon.textContent = isLight ? "🌙" : "☀️";
  }

  // Animate project cards on scroll
  const cards = document.querySelectorAll('.project-card');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in-view');
      }
    });
  }, { threshold: 0.12 });
  cards.forEach((c) => observer.observe(c));

  // Contact form validation & UX
  const form = document.querySelector('.contact__form');
  if (form) {
    const submitBtn = form.querySelector('button[type="submit"]');
    const nameInput = form.querySelector('input[name="name"]');
    const emailInput = form.querySelector('input[name="email"]');
    const subjectInput = form.querySelector('input[name="subject"]');
    const messageInput = form.querySelector('textarea[name="message"]');

    const fields = [nameInput, emailInput, subjectInput, messageInput];

    function setError(input, msg) {
      clearError(input);
      const p = document.createElement('p');
      p.className = 'error';
      p.textContent = msg;
      input.closest('.field')?.appendChild(p);
      input.setAttribute('aria-invalid', 'true');
    }

    function clearError(input) {
      input.removeAttribute('aria-invalid');
      const parent = input.closest('.field');
      if (!parent) return;
      const err = parent.querySelector('.error');
      if (err) err.remove();
    }

    function isEmail(v) {
      return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v);
    }

    function validate() {
      let valid = true;
      fields.forEach((f) => {
        if (!f) return;
        clearError(f);
        if (!f.value.trim()) {
          setError(f, 'This field is required.');
          valid = false;
        }
      });
      if (valid && emailInput && !isEmail(emailInput.value.trim())) {
        setError(emailInput, 'Please enter a valid email address.');
        valid = false;
      }
      if (submitBtn) submitBtn.disabled = !valid;
      return valid;
    }

    fields.forEach((f) => {
      if (!f) return;
      f.addEventListener('input', validate);
      f.addEventListener('blur', validate);
    });

    form.addEventListener('submit', (e) => {
      e.preventDefault();
      if (!validate()) return;
      alert('Thank you for your message');
      form.reset();
      if (submitBtn) submitBtn.disabled = true;
    });
  }

  // Typewriter effect
  const el = document.getElementById('typewriter');
  if (el) {
    const words = ["Work from Home Professional", "The Creator of this website you are currently on", "Looking to start working with immediate effect, part-time or full-time"];
    let wordIndex = 0;
    let charIndex = 0;
    let deleting = false;

    function tick() {
      const current = words[wordIndex];
      if (!deleting) {
        charIndex = Math.min(charIndex + 1, current.length);
      } else {
        charIndex = Math.max(charIndex - 1, 0);
      }
      el.textContent = current.slice(0, charIndex);

      let delay = deleting ? 60 : 90; // smooth typing pace
      if (!deleting && charIndex === current.length) {
        delay = 1200; // pause at end
        deleting = true;
      } else if (deleting && charIndex === 0) {
        deleting = false;
        wordIndex = (wordIndex + 1) % words.length;
        delay = 400; // pause before typing next
      }
      setTimeout(tick, delay);
    }
    tick();
  }

  // Resume PDF download function
  function downloadResumePDF(buttonElement, originalText) {
    try {
      // Show loading state
      buttonElement.textContent = 'Downloading...';
      buttonElement.disabled = true;
      
      // Create a temporary link element for download
      const link = document.createElement('a');
      link.href = 'Madiha-Chaudhary-Resume.pdf';
      link.download = 'Madiha-Chaudhary-Resume.pdf';
      link.style.display = 'none';
      
      // Add to DOM, click, and remove
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      
      // Reset button after a short delay
      setTimeout(() => {
        buttonElement.textContent = originalText;
        buttonElement.disabled = false;
      }, 1000);
      
    } catch (error) {
      console.error('Error downloading PDF:', error);
      // Fallback to opening in new tab
      window.open('resume.html', '_blank');
      
      // Reset button
      buttonElement.textContent = originalText;
      buttonElement.disabled = false;
    }
  }

  // Resume PDF download button
  const downloadBtn = document.getElementById('download-resume');
  if (downloadBtn) {
    downloadBtn.addEventListener('click', (e) => {
      e.preventDefault();
      downloadResumePDF(downloadBtn, 'Download Résumé (PDF)');
    });
  }

});


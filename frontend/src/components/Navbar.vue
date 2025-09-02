<template>
  <nav class="navbar">
    <div class="nav-container">
      <div class="nav-brand">
        <router-link to="/" class="brand-link">
          CharacterHub Challenge
        </router-link>
      </div>
      
      <div class="nav-links" :class="{ active: mobileMenuOpen }">
        <router-link to="/" class="nav-link" @click="closeMobileMenu">
          🏠 Home
        </router-link>
        <router-link to="/movie" class="nav-link" @click="closeMobileMenu">
          🎬 Movie Page
        </router-link>
        <router-link to="/posts" class="nav-link" @click="closeMobileMenu">
          📝 Posts API
        </router-link>
      </div>

      <button 
        class="mobile-toggle"
        @click="toggleMobileMenu"
        :class="{ active: mobileMenuOpen }"
      >
        <span></span>
        <span></span>
        <span></span>
      </button>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'NavbarComponent',
  data() {
    return {
      mobileMenuOpen: false
    };
  },
  methods: {
    toggleMobileMenu() {
      this.mobileMenuOpen = !this.mobileMenuOpen;
    },
    closeMobileMenu() {
      this.mobileMenuOpen = false;
    }
  }
};
</script>

<style scoped>
.navbar {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  position: sticky;
  top: 0;
  z-index: 1000;
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
}

.nav-brand {
  font-size: 1.3rem;
  font-weight: bold;
}

.brand-link {
  color: white;
  text-decoration: none;
  transition: all 0.3s ease;
}

.brand-link:hover {
  opacity: 0.8;
}

.nav-links {
  display: flex;
  gap: 2rem;
  align-items: center;
}

.nav-link {
  color: white;
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  transition: all 0.3s ease;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.nav-link:hover,
.nav-link.router-link-active {
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(10px);
}

.mobile-toggle {
  display: none;
  flex-direction: column;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0.5rem;
  gap: 4px;
}

.mobile-toggle span {
  width: 25px;
  height: 3px;
  background: white;
  border-radius: 3px;
  transition: all 0.3s ease;
}

.mobile-toggle.active span:nth-child(1) {
  transform: rotate(45deg) translate(7px, 7px);
}

.mobile-toggle.active span:nth-child(2) {
  opacity: 0;
}

.mobile-toggle.active span:nth-child(3) {
  transform: rotate(-45deg) translate(7px, -7px);
}

/* Mobile Responsive */
@media (max-width: 768px) {
  .nav-container {
    padding: 1rem;
  }
  
  .mobile-toggle {
    display: flex;
  }
  
  .nav-links {
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    flex-direction: column;
    padding: 1rem;
    gap: 0.5rem;
    opacity: 0;
    visibility: hidden;
    transform: translateY(-10px);
    transition: all 0.3s ease;
  }
  
  .nav-links.active {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
  }
  
  .nav-link {
    padding: 1rem;
    justify-content: center;
    border-radius: 8px;
  }
}
</style>
<template>
  <DefaultLayout>
    <div class="home-container">
      <div class="hero-section">
        <h1>CharacterHub Code Challenge</h1>
        <p>Demonstrating Django REST Framework + Vue.js Integration</p>
      </div>

      <div class="features-grid">
        <!-- Movie Page Demo -->
        <div class="feature-card">
          <div class="feature-icon">🎬</div>
          <h3>Movie Page Design</h3>
          <p>TMDB-inspired movie page with responsive design and interactive features</p>
          <div class="improvements">
            <h4>Key Improvements:</h4>
            <ul>
              <li>Interactive star rating system</li>
              <li>Fully responsive design</li>
              <li>Movie recommendations</li>
              <li>Modern glassmorphism UI</li>
            </ul>
          </div>
          <router-link to="/movie" class="cta-button">View Movie Page</router-link>
        </div>

        <!-- Posts API Demo -->
        <div class="feature-card">
          <div class="feature-icon">📝</div>
          <h3>Posts API Integration</h3>
          <p>Django REST API with infinite scrolling posts feed</p>
          <div class="improvements">
            <h4>Backend Features:</h4>
            <ul>
              <li>Paginated API endpoints</li>
              <li>Comments with nested relationships</li>
              <li>Infinite scroll implementation</li>
              <li>Optimized database queries</li>
            </ul>
          </div>
          <router-link to="/posts" class="cta-button">View Posts Feed</router-link>
        </div>
      </div>

      <!-- Quick Navigation -->
      <div class="quick-nav">
        <h2>Quick Access</h2>
        <div class="nav-links">
          <router-link to="/movie" class="nav-btn movie-btn">
            🎬 Enhanced Movie Page
          </router-link>
          <router-link to="/posts" class="nav-btn posts-btn">
            📝 Posts with Django API
          </router-link>
        </div>
      </div>
    </div>
  </DefaultLayout>
</template>

<script>
import DefaultLayout from "@/layouts/DefaultLayout.vue";

export default {
  name: "HomePage",
  components: {
    DefaultLayout
  }
};
</script>

<style scoped>
.home-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.hero-section {
  text-align: center;
  padding: 3rem 0;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 20px;
  color: white;
  margin-bottom: 3rem;
}

.hero-section h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  font-weight: 700;
}

.hero-section p {
  font-size: 1.2rem;
  opacity: 0.9;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
  gap: 2rem;
  margin-bottom: 3rem;
}

.feature-card {
  background: white;
  border-radius: 16px;
  padding: 2rem;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  border: 1px solid #e1e5e9;
  transition: all 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
}

.feature-icon {
  font-size: 3rem;
  text-align: center;
  margin-bottom: 1rem;
}

.feature-card h3 {
  font-size: 1.5rem;
  margin-bottom: 1rem;
  color: #333;
  text-align: center;
}

.feature-card p {
  color: #666;
  line-height: 1.6;
  margin-bottom: 1.5rem;
  text-align: center;
}

.improvements {
  background: #f8f9fa;
  padding: 1.5rem;
  border-radius: 12px;
  margin-bottom: 1.5rem;
}

.improvements h4 {
  color: #495057;
  margin-bottom: 0.8rem;
  font-size: 1rem;
}

.improvements ul {
  list-style: none;
  padding: 0;
}

.improvements li {
  padding: 0.3rem 0;
  color: #666;
  font-size: 0.9rem;
  position: relative;
  padding-left: 1.2rem;
}

.improvements li::before {
  content: "✨";
  position: absolute;
  left: 0;
}

.cta-button {
  display: block;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  text-decoration: none;
  padding: 1rem 2rem;
  border-radius: 8px;
  text-align: center;
  font-weight: 600;
  transition: all 0.3s ease;
}

.cta-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
}

.quick-nav {
  background: #f8f9fa;
  padding: 3rem;
  border-radius: 16px;
  text-align: center;
}

.quick-nav h2 {
  color: #333;
  margin-bottom: 2rem;
}

.nav-links {
  display: flex;
  gap: 2rem;
  justify-content: center;
  flex-wrap: wrap;
}

.nav-btn {
  padding: 1rem 2rem;
  text-decoration: none;
  border-radius: 12px;
  font-weight: 600;
  font-size: 1.1rem;
  transition: all 0.3s ease;
  min-width: 200px;
}

.movie-btn {
  background: linear-gradient(135deg, #ff6b6b, #ee5a24);
  color: white;
}

.posts-btn {
  background: linear-gradient(135deg, #4ecdc4, #44a08d);
  color: white;
}

.nav-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
}

/* Responsive Design */
@media (max-width: 768px) {
  .home-container {
    padding: 1rem;
  }
  
  .hero-section {
    padding: 2rem 1rem;
  }
  
  .hero-section h1 {
    font-size: 2rem;
  }
  
  .features-grid {
    grid-template-columns: 1fr;
  }
  
  .feature-card {
    padding: 1.5rem;
  }
  
  .nav-links {
    flex-direction: column;
    align-items: center;
  }
}
</style>
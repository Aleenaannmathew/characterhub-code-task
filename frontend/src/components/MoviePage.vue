<template>
  <div class="movie-page">
    <!-- Top App Header -->
    <header class="app-header">
      <div class="brand">TMDB</div>
      <nav class="main-nav">
        <a href="#" class="active">Movies</a>
        <a href="#">TV Shows</a>
        <a href="#">People</a>
        <a href="#">More</a>
      </nav>
      <div class="header-actions">
        <button class="ghost">+</button>
        <button class="ghost">EN</button>
        <button class="ghost">Login</button>
        <button class="ghost">Join TMDB</button>
        <button class="ghost search-btn">🔍</button>
      </div>
      <!-- Mobile menu toggle -->
      <button class="mobile-menu-toggle" @click="showMobileMenu = !showMobileMenu">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </header>

    <!-- Mobile Menu -->
    <div v-if="showMobileMenu" class="mobile-menu">
      <a href="#" class="active">Movies</a>
      <a href="#">TV Shows</a>
      <a href="#">People</a>
      <a href="#">More</a>
      <div class="mobile-actions">
        <button class="ghost">Login</button>
        <button class="ghost">Join TMDB</button>
      </div>
    </div>

    <!-- Sub Nav -->
    <nav class="sub-nav">
      <div class="container">
        <a href="#" class="active">Overview <span class="dropdown-arrow">▼</span></a>
        <a href="#">Media <span class="dropdown-arrow">▼</span></a>
        <a href="#">Fandom <span class="dropdown-arrow">▼</span></a>
        <a href="#">Share <span class="dropdown-arrow">▼</span></a>
      </div>
    </nav>

    <!-- Loading -->
    <div v-if="loading" class="loading">
      <div class="spinner"></div>
      <p>Loading movie data...</p>
    </div>

    <!-- HERO -->
    <section
      v-else
      class="hero"
      :style="{ backgroundImage: 'url(https://image.tmdb.org/t/p/original/aJn9XeesqsrSLKcHfHP4u5985hn.jpg)' }"
    >
      <div class="hero-gradient">
        <div class="container">
          <div class="hero-grid">
            <!-- Poster + Streaming badge -->
            <aside class="poster-col">
              <div class="poster-wrapper">
                <img
                  class="poster"
                  src="https://image.tmdb.org/t/p/w300/y4MBh0EjBlMuOzv9axM4qJlmhzz.jpg"
                  alt="Guardians of the Galaxy Vol. 2"
                />
              </div>

              <div class="streaming-card">
                <div class="streaming-badge">
                  <div class="streaming-icon">▶</div>
                  <div class="streaming-copy">
                    <span>Now Streaming</span><br />
                    <strong>Watch Now</strong>
                  </div>
                </div>
              </div>
            </aside>

            <!-- Text content -->
            <main class="content-col">
              <h1 class="title">
                Guardians of the Galaxy Vol. 2 <span class="year">(2017)</span>
              </h1>

              <div class="meta-row">
                <span class="chip">PG-13</span>
                <span class="meta">05/05/2017 (IN)</span>
                <span class="dot">•</span>
                <span class="meta">Science Fiction, Adventure, Action</span>
                <span class="dot">•</span>
                <span class="meta">2h 17m</span>
              </div>

              <!-- Score + actions -->
              <div class="score-actions">
                <!-- Score -->
                <div class="score-block">
                  <div class="score-circle">
                    <div class="score-inner">
                      <span class="score-text">76<sup>%</sup></span>
                    </div>
                  </div>
                  <div class="score-label">
                    <strong>User<br />Score</strong>
                  </div>
                </div>

                <!-- Emoji reactions -->
                <div class="emoji-reactions">
                  <span class="emoji">😍</span>
                  <span class="emoji">😊</span>
                  <span class="emoji">😐</span>
                </div>

                <div class="vibe-check">
                  <span>What's your <strong>Vibe?</strong></span>
                  <button class="info-btn">?</button>
                </div>

                <!-- Rounded action buttons -->
                <div class="actions">
                  <button class="action round" title="Add to List">📋</button>
                  <button class="action round" title="Mark as Favorite">♥</button>
                  <button class="action round" title="Add to Watchlist">🔖</button>

                  <button class="play" @click="showTrailer = true">
                    ▶ Play Trailer
                  </button>
                </div>
              </div>

              <!-- Tagline -->
              <p class="tagline">Anyone can save the galaxy once.</p>

              <!-- Overview -->
              <section class="overview">
                <h3>Overview</h3>
                <p>The Guardians must fight to keep their newfound family together as they unravel the mysteries of Peter Quill's true parentage.</p>
              </section>

              <!-- Crew -->
              <section class="crew-grid">
                <div class="crew-item">
                  <strong>James Gunn</strong>
                  <span>Director, Writer</span>
                </div>
                <div class="crew-item">
                  <strong>Jim Starlin</strong>
                  <span>Characters</span>
                </div>
                <div class="crew-item">
                  <strong>Keith Giffen</strong>
                  <span>Characters</span>
                </div>
                <div class="crew-item">
                  <strong>Steve Gerber</strong>
                  <span>Characters</span>
                </div>
                <div class="crew-item">
                  <strong>Bill Mantlo</strong>
                  <span>Characters</span>
                </div>
                <div class="crew-item">
                  <strong>Steve Englehart</strong>
                  <span>Characters</span>
                </div>
                <div class="crew-item">
                  <strong>Larry Lieber</strong>
                  <span>Characters</span>
                </div>
                <div class="crew-item">
                  <strong>Stan Lee</strong>
                  <span>Characters</span>
                </div>
                <div class="crew-item">
                  <strong>Jack Kirby</strong>
                  <span>Characters</span>
                </div>
                <div class="crew-item">
                  <strong>Val Mayerik</strong>
                  <span>Characters</span>
                </div>
                <div class="crew-item">
                  <strong>Steve Gan</strong>
                  <span>Characters</span>
                </div>
              </section>
            </main>
          </div>
        </div>
      </div>
    </section>

    <!-- BELOW THE FOLD -->
    <div class="below-fold container">
      <!-- Cast Section -->
      <section class="cast-section">
        <h2>Top Billed Cast</h2>
        <div class="cast-row">
          <div
            class="cast-card"
            v-for="(actor, i) in cast"
            :key="i"
            @click="openActorModal(actor)"
          >
            <img
              v-if="actor.img"
              :src="actor.img"
              :alt="actor.name"
              class="cast-img"
            />
            <div v-else class="cast-fallback">No Image</div>

            <div class="cast-info">
              <strong>{{ actor.name }}</strong>
              <p>{{ actor.character }}</p>
            </div>
          </div>
        </div>
        <button class="full-cast">Full Cast & Crew</button>
      </section>

      <!-- Social Section -->
      <section class="social-section">
        <h2>Social</h2>
        <div class="tabs">
          <button
            :class="{ active: activeTab === 'reviews' }"
            @click="activeTab = 'reviews'"
          >
            Reviews <span class="count">25</span>
          </button>
          <button
            :class="{ active: activeTab === 'discussions' }"
            @click="activeTab = 'discussions'"
          >
            Discussions <span class="count">66</span>
          </button>
        </div>

        <div v-if="activeTab === 'reviews'" class="reviews">
          <div class="review-card">
            <div class="review-header">
              <div class="user-avatar">T</div>
              <div class="review-meta">
                <h4>A review by tmdb51616167</h4>
                <div class="rating">
                  <span class="score">70%</span>
                  <span class="written-by">Written by tmdb51616167 on September 3, 2024</span>
                </div>
              </div>
            </div>
            <div class="review-content">
              <p>Guardians of the Galaxy has solidified itself as an incredible franchise within the Marvel Cinematic Universe.</p>
              <p>Volume 1: The creation of these characters injected suspense, excitement, and a generous dose of over-the-top comedy into the MCU. Chris Pratt's portrayal of Star-Lord was a fantastic choice, and the characters like Rocket and Groot became instant fan favorites...</p>
            </div>
          </div>
          <button class="read-all-reviews">Read All Reviews</button>
        </div>
      </section>

      <!-- Media Section -->
      <section class="media-section">
        <h2>Media</h2>
        <div class="tabs">
          <button
            :class="{ active: mediaTab === 'videos' }"
            @click="mediaTab = 'videos'"
          >
            Videos <span class="count">10</span>
          </button>
          <button
            :class="{ active: mediaTab === 'backdrops' }"
            @click="mediaTab = 'backdrops'"
          >
            Backdrops <span class="count">108</span>
          </button>
          <button
            :class="{ active: mediaTab === 'posters' }"
            @click="mediaTab = 'posters'"
          >
            Posters <span class="count">339</span>
          </button>
        </div>

        <div class="media-content">
          <div class="media-grid">
            <div class="media-item">
              <img src="https://image.tmdb.org/t/p/w500/y4MBh0EjBlMuOzv9axM4qJlmhzz.jpg" alt="Media" />
            </div>
            <div class="media-item">
              <img src="https://image.tmdb.org/t/p/w500/z4x0Bp48ar3Mda8KiPD1vwSY3D8.jpg" alt="Media" />
            </div>
            <div class="media-item">
              <img src="https://image.tmdb.org/t/p/w500/olF8M3oI0Gv1J7ZVKp1W2dN1uF.jpg" alt="Media" />
            </div>
          </div>
        </div>
      </section>

      <!-- Collection Section -->
      <section class="collection-section">
        <div class="collection-banner">
          <div class="collection-content">
            <h2>Part of the Guardians of the Galaxy Collection</h2>
            <p>Includes Guardians of the Galaxy, Guardians of the Galaxy Vol. 2, and Guardians of the Galaxy Vol. 3</p>
            <button class="view-collection">VIEW THE COLLECTION</button>
          </div>
        </div>
      </section>

      <!-- Recommendations -->
      <section class="recommendations">
        <h2>Recommendations</h2>
        <div class="recommendations-grid">
          <div
            v-for="rec in recommendations"
            :key="rec.id"
            class="rec-card"
          >
            <img :src="rec.poster" :alt="rec.title" />
            <div class="rec-info">
              <h4>{{ rec.title }}</h4>
              <span class="rec-score">{{ rec.score }}%</span>
            </div>
          </div>
        </div>
      </section>
    </div>

    <!-- Footer -->
    <footer class="site-footer">
      <div class="footer-container">
        <div class="footer-section">
          <h3>THE MOVIE DB</h3>
          <a href="#" class="footer-link">JOIN THE COMMUNITY</a>
        </div>
        
        <div class="footer-section">
          <h3>THE BASICS</h3>
          <a href="#" class="footer-link">About TMDB</a>
          <a href="#" class="footer-link">Contact Us</a>
          <a href="#" class="footer-link">Support Forums</a>
          <a href="#" class="footer-link">API Documentation</a>
          <a href="#" class="footer-link">System Status</a>
        </div>
        
        <div class="footer-section">
          <h3>GET INVOLVED</h3>
          <a href="#" class="footer-link">Contribution Bible</a>
          <a href="#" class="footer-link">Add New Movie</a>
          <a href="#" class="footer-link">Add New TV Show</a>
        </div>
        
        <div class="footer-section">
          <h3>COMMUNITY</h3>
          <a href="#" class="footer-link">Guidelines</a>
          <a href="#" class="footer-link">Discussions</a>
          <a href="#" class="footer-link">Leaderboard</a>
        </div>
        
        <div class="footer-section">
          <h3>LEGAL</h3>
          <a href="#" class="footer-link">Terms of Use</a>
          <a href="#" class="footer-link">API Terms of Use</a>
          <a href="#" class="footer-link">Privacy Policy</a>
          <a href="#" class="footer-link">DMCA Policy</a>
        </div>
      </div>
      
      <div class="footer-bottom">
        <div class="search-container">
          <input type="text" placeholder="Type here to search" class="search-input" />
        </div>
        <div class="time-info">
          <span>01:32 PM</span>
          <span>03/09/2025</span>
        </div>
      </div>
    </footer>

    <!-- Trailer Modal -->
    <div v-if="showTrailer" class="modal-overlay" @click.self="showTrailer = false">
      <div class="modal-content">
        <button class="close-btn" @click="showTrailer = false">✕</button>
        <iframe
          width="100%"
          height="100%"
          src="https://www.youtube.com/embed/d96cjJhvlMA?autoplay=1"
          title="YouTube video player"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen
        ></iframe>
      </div>
    </div>

    <!-- Actor Modal -->
    <div v-if="showActorModal" class="modal-overlay" @click.self="showActorModal = false">
      <div class="modal-content actor-modal">
        <button class="close-btn" @click="showActorModal = false">✕</button>
        <div class="actor-details">
          <img :src="selectedActor.img" :alt="selectedActor.name" class="actor-image" />
          <div class="actor-info">
            <h2>{{ selectedActor.name }}</h2>
            <h4>as {{ selectedActor.character }}</h4>
            <p>{{ selectedActor.bio || 'No biography available.' }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MoviePage",
  data() {
    return {
      loading: true,
      movie: {},
      backgroundImage: "",
      tagline: "Obviously.",
      showMobileMenu: false,
      showTrailer: false,
      showActorModal: false,
      selectedActor: {},
      activeTab: "reviews",
      mediaTab: "videos",
      crewMembers: [
        { name: "James Gunn", role: "Director, Writer" },
        { name: "Jim Starlin", role: "Characters" },
        { name: "Steve Englehart", role: "Characters" },
        { name: "Steve Gan", role: "Characters" },
        { name: "Larry Lieber", role: "Characters" },
        { name: "Stan Lee", role: "Characters" },
        { name: "Val Mayerik", role: "Characters" },
        { name: "Jack Kirby", role: "Characters" }
      ],
      cast: [
        { name: "Chris Pratt", character: "Peter Quill / Star-Lord", img: "https://image.tmdb.org/t/p/w185/83o3koL82jt30EJ0rz4Bnzrt2dd.jpg" },
        { name: "Zoe Saldaña", character: "Gamora", img: "https://image.tmdb.org/t/p/w185/7nWj6vN0CAdp4c2l1gkxxpMoeEk.jpg" },
        { name: "Dave Bautista", character: "Drax", img: "https://image.tmdb.org/t/p/w185/jUODkxmN2rDoGsx1GpjkUNFjlOj.jpg" },
        { name: "Vin Diesel", character: "Groot (voice)", img: "https://image.tmdb.org/t/p/w185/n1Foq5JgGV3HgXkGLwZ5dht93I3.jpg" },
        { name: "Bradley Cooper", character: "Rocket (voice)", img: "https://image.tmdb.org/t/p/w185/n5J7XQFZ71LyEuzxKvIXhz9JssB.jpg" },
        { name: "Kurt Russell", character: "Ego", img: "https://image.tmdb.org/t/p/w185/lFmeVlgJnqz8vnNbMhAIi9lWdBb.jpg" },
        { name: "Michael Rooker", character: "Yondu", img: "https://image.tmdb.org/t/p/w185/xLY8oTfDYNIVGnVz8DWJhYBnLhw.jpg" }
      ],
      recommendations: [
        {
          id: 101,
          title: "Spider-Man: Homecoming",
          poster: "https://image.tmdb.org/t/p/w200/c24sv2weTHPsmDa7jEMN0m2P3RT.jpg",
          score: 73
        },
        {
          id: 102,
          title: "Guardians of the Galaxy",
          poster: "https://image.tmdb.org/t/p/w200/y31QB9kn3XSudA15tV7UWQ9XLuW.jpg",
          score: 79
        },
        {
          id: 103,
          title: "Doctor Strange",
          poster: "https://image.tmdb.org/t/p/w200/uGBVj3bEbCoZbDjjl9wTxcygko1.jpg",
          score: 74
        },
        {
          id: 104,
          title: "Wonder Woman",
          poster: "https://image.tmdb.org/t/p/w200/gfJGlDaHuWimErCr5Ql0I8x9QSy.jpg",
          score: 76
        }
      ]
    };
  },
  computed: {
    scorePercentage() {
      const n = parseFloat(this.movie.imdbRating);
      return isNaN(n) ? 0 : Math.round(n * 10);
    },
    scoreGradient() {
      const pct = this.scorePercentage;
      const angle = (pct / 100) * 360;
      return `conic-gradient(#21d07a 0deg, #21d07a ${angle}deg, #204529 ${angle}deg 360deg)`;
    }
  },
  async mounted() {
    try {
      const res = await fetch(
        "http://www.omdbapi.com/?i=tt3896198&apikey=d2132124"
      );
      this.movie = await res.json();
      this.backgroundImage =
        this.movie.Poster && this.movie.Poster !== "N/A" ? this.movie.Poster : "";
    } catch (e) {
      console.error("Failed to fetch OMDb:", e);
    } finally {
      this.loading = false;
    }
  },
  methods: {
    formatDate(d) {
      if (!d) return "";
      const date = new Date(d);
      return date.toLocaleDateString("en-US", {
        month: "2-digit",
        day: "2-digit",
        year: "numeric"
      });
    },
    openActorModal(actor) {
      this.selectedActor = actor;
      this.showActorModal = true;
    }
  }
};
</script>

<style scoped>
/* ---------- Base */
* { box-sizing: border-box; }
.movie-page { background: #0d253f; color: #fff; min-height: 100vh; }
.container { max-width: 1300px; margin: 0 auto; padding: 0 20px; }

/* ---------- App Header */
.app-header {
  background: #032541;
  height: 64px;
  display: grid;
  grid-template-columns: 140px 1fr auto auto;
  align-items: center;
  gap: 16px;
  padding: 0 20px;
  position: relative;
}
.brand { color: #01b4e4; font-weight: 800; letter-spacing: 1px; font-size: 20px; }
.main-nav { display: flex; gap: 20px; }
.main-nav a {
  color: #fff; text-decoration: none; padding: 8px 12px; border-radius: 4px;
  font-weight: 600; transition: background 0.2s;
}
.main-nav a.active, .main-nav a:hover { background: rgba(1, 180, 228, 0.2); }
.header-actions { display: flex; gap: 8px; }
.header-actions .ghost {
  background: transparent; color: #01b4e4; border: 1px solid #0ea5c0;
  border-radius: 6px; padding: 6px 10px; cursor: pointer; font-size: 14px;
  transition: all 0.2s;
}
.header-actions .ghost:hover { background: rgba(1, 180, 228, 0.1); }

/* Mobile Menu Toggle */
.mobile-menu-toggle {
  display: none;
  flex-direction: column;
  background: none;
  border: none;
  cursor: pointer;
  gap: 3px;
}
.mobile-menu-toggle span {
  width: 25px;
  height: 3px;
  background: #01b4e4;
  transition: 0.3s;
}

/* Mobile Menu */
.mobile-menu {
  background: #032541;
  padding: 20px;
  display: none;
}
.mobile-menu a {
  display: block;
  color: #fff;
  text-decoration: none;
  padding: 10px 0;
  border-bottom: 1px solid rgba(255,255,255,0.1);
}
.mobile-menu a.active { color: #01b4e4; }
.mobile-actions {
  margin-top: 15px;
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

/* ---------- Sub Nav */
.sub-nav { background: rgba(3, 37, 65, 0.85); }
.sub-nav .container { height: 48px; display: flex; align-items: center; gap: 30px; }
.sub-nav a { 
  color: #fff; text-decoration: none; padding-bottom: 6px; 
  border-bottom: 3px solid transparent; font-weight: 600;
  transition: border-color 0.2s; display: flex; align-items: center; gap: 5px;
}
.sub-nav a.active, .sub-nav a:hover { border-bottom-color: #01b4e4; }
.dropdown-arrow { font-size: 10px; opacity: 0.7; }

/* ---------- Loading */
.loading {
  display: grid; place-items: center; min-height: 40vh; gap: 12px;
}
.spinner {
  width: 40px; height: 40px; border: 4px solid #01b4e4; border-top-color: transparent;
  border-radius: 50%; animation: spin 0.9s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }

/* ---------- Hero */
.hero {
  background-size: cover; background-position: center; position: relative;
  min-height: 500px;
}
.hero-gradient {
  background: linear-gradient(
    to right,
    rgba(3, 37, 65, 1) 150px,
    rgba(3, 37, 65, 0.85) 100%
  );
  padding: 40px 0;
  min-height: 500px;
  display: flex;
  align-items: center;
}
.hero-grid {
  display: grid;
  grid-template-columns: 300px 1fr;
  gap: 40px;
  align-items: start;
}

/* Poster column */
.poster-wrapper { width: 100%; }
.poster {
  width: 100%; max-width: 300px; border-radius: 10px; display: block;
  box-shadow: 0 10px 24px rgba(0,0,0,0.35);
}
.poster-fallback {
  height: 450px; background: #1f2a44; border-radius: 10px;
  display: grid; place-items: center; color: #96a7c2;
}
.streaming-card { margin-top: 20px; }
.streaming-badge {
  background: linear-gradient(135deg, #9333ea, #c084fc);
  border-radius: 8px; padding: 12px; display: flex; gap: 12px; align-items: center;
}
.streaming-icon { 
  font-size: 16px; color: #fff;
}
.streaming-copy { line-height: 1.3; }
.streaming-copy span { font-size: 12px; opacity: 0.9; }
.streaming-copy strong { font-size: 14px; }

/* Content column */
.title { font-size: clamp(28px, 4vw, 42px); margin: 0 0 15px; font-weight: 700; }
.year { color: #cfd7df; font-weight: 400; }
.meta-row { 
  display: flex; align-items: center; flex-wrap: wrap; gap: 8px; 
  color: #d9e2ec; margin-bottom: 20px; font-size: 16px;
}
.meta { opacity: 0.95; }
.dot { opacity: 0.6; }
.chip {
  background: #6b7280; color: #fff; padding: 2px 8px; border-radius: 4px; 
  font-weight: 700; font-size: 14px;
}

/* Score + actions */
.score-actions {
  display: flex; align-items: center; flex-wrap: wrap; gap: 20px;
  margin: 25px 0 20px;
}
.score-block { display: flex; align-items: center; gap: 12px; }
.score-circle {
  width: 68px; height: 68px; border-radius: 50%;
  background: conic-gradient(#21d07a 0deg, #21d07a 274deg, #204529 274deg 360deg);
  display: grid; place-items: center;
}
.score-inner {
  width: 52px; height: 52px; border-radius: 50%; background: #081c22;
  display: grid; place-items: center;
}
.score-text { font-weight: 700; font-size: 16px; }
.score-text sup { font-size: 8px; }
.score-label strong { font-size: 14px; line-height: 1.2; }

.emoji-reactions { display: flex; gap: 8px; align-items: center; }
.emoji { font-size: 24px; cursor: pointer; transition: transform 0.2s; }
.emoji:hover { transform: scale(1.2); }

.vibe-check { display: flex; align-items: center; gap: 8px; font-size: 14px; }
.info-btn {
  width: 16px; height: 16px; border-radius: 50%; background: #666;
  color: #fff; border: none; font-size: 12px; cursor: pointer;
  display: grid; place-items: center;
}

.actions { display: flex; align-items: center; gap: 12px; }
.action.round {
  width: 46px; height: 46px; border-radius: 50%;
  background: rgba(3, 37, 65, 1); color: #fff; border: none; cursor: pointer;
  transition: background 0.2s; font-size: 16px;
}
.action.round:hover { background: rgba(1, 180, 228, 0.2); }
.play {
  background: transparent; border: none; color: #fff; font-weight: 600; cursor: pointer;
  padding: 0; font-size: 20px; display: flex; align-items: center; gap: 8px;
  transition: color 0.2s;
}
.play:hover { color: #01b4e4; }

/* Tagline + overview + crew */
.tagline { 
  font-style: italic; color: #d1dbea; margin: 20px 0; font-size: 18px; opacity: 0.8; 
}
.overview { margin: 25px 0; }
.overview h3 { margin: 0 0 10px; font-size: 20px; }
.overview p { color: #e7eef6; line-height: 1.6; font-size: 16px; }

.crew-grid {
  margin-top: 25px;
  display: grid; gap: 20px;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
}
.crew-item strong { display: block; font-size: 16px; }
.crew-item span { color: #c1cbd8; font-size: 14px; }

/* ---------- Below Fold Sections */
.below-fold { padding: 30px 0 60px; }

/* Cast Section */
.cast-section { margin: 40px 0; }
.cast-section h2 { font-size: 24px; margin-bottom: 20px; }
.cast-row {
  display: flex; gap: 20px; overflow-x: auto; padding-bottom: 10px;
  scrollbar-width: thin;
}
.cast-row::-webkit-scrollbar { height: 8px; }
.cast-row::-webkit-scrollbar-thumb {
  background: #888; border-radius: 6px;
}
.cast-card {
  background: #fff; color: #000; border-radius: 8px;
  width: 140px; flex-shrink: 0; cursor: pointer; overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.15);
  transition: transform 0.2s;
}
.cast-card:hover { transform: translateY(-4px); }
.cast-img { width: 100%; height: 175px; object-fit: cover; }
.cast-fallback {
  width: 100%; height: 175px; display: grid; place-items: center;
  background: #ddd; color: #555;
}
.cast-info { padding: 12px; }
.cast-info strong { font-size: 14px; display: block; margin-bottom: 5px; }
.cast-info p { font-size: 13px; color: #666; margin: 0; }
.full-cast {
  margin-top: 15px; background: transparent; border: none; color: #01b4e4;
  font-weight: 600; cursor: pointer; font-size: 16px;
}
.full-cast:hover { text-decoration: underline; }

/* Social Section */
.social-section { margin: 50px 0; }
.social-section h2 { font-size: 24px; margin-bottom: 20px; }
.tabs {
  display: flex; gap: 20px; margin-bottom: 25px;
  border-bottom: 1px solid rgba(255,255,255,0.2);
}
.tabs button {
  background: none; border: none; font-size: 18px; cursor: pointer;
  padding: 10px 0; border-bottom: 3px solid transparent; color: #fff;
  transition: border-color 0.2s;
}
.tabs button.active { border-color: #01b4e4; font-weight: 600; }
.tabs .count {
  background: #6b7280; color: #fff; padding: 2px 8px; border-radius: 10px;
  font-size: 12px; margin-left: 5px;
}

.review-card {
  background: rgba(255,255,255,0.05); padding: 20px; border-radius: 8px;
  margin-bottom: 20px;
}
.review-header { display: flex; align-items: flex-start; gap: 15px; margin-bottom: 15px; }
.user-avatar {
  width: 50px; height: 50px; background: #01b4e4; color: #fff;
  border-radius: 50%; display: grid; place-items: center; font-weight: 700;
  font-size: 20px; flex-shrink: 0;
}
.review-meta h4 { margin: 0 0 5px; font-size: 18px; }
.rating { display: flex; align-items: center; gap: 10px; }
.rating .score {
  background: #21d07a; color: #000; padding: 2px 6px; border-radius: 4px;
  font-weight: 700; font-size: 14px;
}
.written-by { color: #bbb; font-size: 14px; }
.review-content p { line-height: 1.6; margin: 0 0 15px; color: #e7eef6; }
.read-all-reviews {
  background: transparent; border: 1px solid #01b4e4; color: #01b4e4;
  padding: 10px 20px; border-radius: 6px; cursor: pointer; font-weight: 600;
}

/* Media Section */
.media-section { margin: 50px 0; }
.media-section h2 { font-size: 24px; margin-bottom: 20px; }
.media-content { margin-top: 20px; }
.media-grid { display: flex; gap: 15px; overflow-x: auto; }
.media-item { flex-shrink: 0; }
.media-item img { width: 300px; height: 169px; object-fit: cover; border-radius: 8px; }

/* Collection Section */
.collection-section { margin: 50px 0; }
.collection-banner {
  background: linear-gradient(45deg, #1e3a8a, #3b82f6);
  border-radius: 10px; overflow: hidden; min-height: 180px;
  display: flex; align-items: center;
}
.collection-content { padding: 30px; }
.collection-content h2 { margin: 0 0 10px; font-size: 24px; }
.collection-content p { margin: 0 0 20px; opacity: 0.9; line-height: 1.5; }
.view-collection {
  background: rgba(255,255,255,0.2); border: 1px solid rgba(255,255,255,0.5);
  color: #fff; padding: 10px 20px; border-radius: 6px; cursor: pointer;
  font-weight: 600; transition: background 0.2s;
}
.view-collection:hover { background: rgba(255,255,255,0.3); }

/* Recommendations */
.recommendations { margin: 50px 0; }
.recommendations h2 { font-size: 24px; margin-bottom: 20px; }
.recommendations-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  gap: 20px;
}
.rec-card {
  cursor: pointer;
  transition: transform 0.2s;
}
.rec-card:hover { transform: scale(1.05); }
.rec-card img { width: 100%; border-radius: 8px; margin-bottom: 10px; }
.rec-info h4 { margin: 0 0 5px; font-size: 14px; }
.rec-score {
  background: #21d07a; color: #000; padding: 2px 6px; border-radius: 4px;
  font-weight: 700; font-size: 12px;
}

/* Footer */
.site-footer {
  background: #032541;
  padding: 40px 0 20px;
  margin-top: 40px;
}
.footer-container {
  max-width: 1300px;
  margin: 0 auto;
  padding: 0 20px;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 30px;
}
.footer-section h3 {
  color: #01b4e4;
  margin-bottom: 15px;
  font-size: 16px;
}
.footer-link {
  display: block;
  color: #fff;
  text-decoration: none;
  margin-bottom: 10px;
  font-size: 14px;
  transition: color 0.2s;
}
.footer-link:hover {
  color: #01b4e4;
}
.footer-bottom {
  max-width: 1300px;
  margin: 30px auto 0;
  padding: 20px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.search-input {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 4px;
  padding: 8px 12px;
  color: #fff;
  width: 200px;
}
.time-info {
  display: flex;
  gap: 15px;
  font-size: 14px;
  color: rgba(255, 255, 255, 0.7);
}

/* ---------- Modals */
.modal-overlay {
  position: fixed; top: 0; left: 0; width: 100%; height: 100%;
  background: rgba(0,0,0,0.8); display: flex; align-items: center;
  justify-content: center; z-index: 2000;
}
.modal-content {
  position: relative; width: 90%; max-width: 900px; height: 70vh;
  background: #000; border-radius: 10px; overflow: hidden;
  box-shadow: 0 0 20px rgba(0,0,0,0.8);
}
.actor-modal { height: auto; background: #fff; }
.close-btn {
  position: absolute; top: 10px; right: 10px; background: rgba(0,0,0,0.6);
  color: #fff; border: none; font-size: 20px; cursor: pointer;
  padding: 8px 12px; border-radius: 4px; z-index: 10;
}
.close-btn:hover { background: rgba(255,255,255,0.2); }

.actor-details { display: flex; gap: 25px; padding: 25px; color: #000; }
.actor-image { width: 200px; height: 250px; object-fit: cover; border-radius: 10px; }
.actor-info h2 { margin: 0 0 5px; font-size: 28px; }
.actor-info h4 { margin: 0 0 15px; font-weight: 400; color: #666; }
.actor-info p { line-height: 1.6; color: #333; }

/* ---------- Responsive Design */
@media (max-width: 1024px) {
  .hero-grid { grid-template-columns: 250px 1fr; gap: 30px; }
  .poster { max-width: 250px; }
  .container { padding: 0 15px; }
}

@media (max-width: 768px) {
  .app-header {
    grid-template-columns: 1fr auto;
    padding: 0 15px;
  }
  .main-nav, .header-actions { display: none; }
  .mobile-menu-toggle { display: flex; }
  .mobile-menu { display: block; }
  
  .hero-gradient { padding: 20px 0; }
  .hero-grid { 
    grid-template-columns: 1fr; 
    gap: 25px; 
    text-align: center;
  }
  .poster { max-width: 200px; margin: 0 auto; }
  .content-col { order: -1; }
  
  .title { font-size: 24px; }
  .score-actions { justify-content: center; }
  .crew-grid { grid-template-columns: 1fr; }
  
  .cast-row { gap: 15px; }
  .cast-card { width: 120px; }
  .cast-img { height: 150px; }
  
  .recommendations-grid { grid-template-columns: repeat(2, 1fr); }
  .rec-card { width: 100%; }
  
  .media-grid { gap: 10px; }
  .media-item img { width: 250px; height: 140px; }
  
  .actor-details { flex-direction: column; text-align: center; }
  .actor-image { width: 180px; margin: 0 auto; }
  
  .footer-container { grid-template-columns: repeat(2, 1fr); }
  .footer-bottom { flex-direction: column; gap: 15px; }
}

@media (max-width: 480px) {
  .container { padding: 0 10px; }
  .hero-grid { gap: 20px; }
  .poster { max-width: 180px; }
  
  .title { font-size: 20px; }
  .meta-row { font-size: 14px; }
  .score-circle { width: 60px; height: 60px; }
  .score-inner { width: 46px; height: 46px; }
  .score-text { font-size: 14px; }
  
  .action.round { width: 40px; height: 40px; }
  .play { font-size: 16px; }
  
  .cast-card { width: 100px; }
  .cast-img { height: 130px; }
  .cast-info { padding: 8px; }
  
  .tabs { gap: 15px; }
  .tabs button { font-size: 16px; }
  
  .modal-content { width: 95%; height: 60vh; }
  .actor-details { padding: 15px; }
  .actor-image { width: 150px; height: 200px; }
  
  .footer-container { grid-template-columns: 1fr; }
  .recommendations-grid { grid-template-columns: 1fr; }
}

@media (max-width: 320px) {
  .hero-grid { gap: 15px; }
  .poster { max-width: 160px; }
  .title { font-size: 18px; }
  .cast-card { width: 90px; }
  .rec-card { width: 100%; }
}

@media (max-width: 768px) {
  .hero-grid {
    grid-template-columns: 1fr;
  }
  .poster-wrapper {
    max-width: 200px;
    margin: 0 auto 20px;
  }
}

</style>
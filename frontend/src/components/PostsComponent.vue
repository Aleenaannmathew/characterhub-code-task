<template>
  <div class="posts-container">
    <div class="posts-header">
      <h2>Posts Feed</h2>
      <p>Connected to Django REST API with infinite scrolling</p>
    </div>
    
    <!-- Posts List -->
    <div class="posts-list">
      <div v-for="post in posts" :key="post.id" class="post-card">
        <div class="post-header">
          <div class="post-author">@{{ post.user }}</div>
          <div class="post-timestamp">{{ formatTimestamp(post.timestamp) }}</div>
        </div>
        
        <div class="post-content">
          <p>{{ post.text }}</p>
        </div>
        
        <div class="post-footer">
          <span class="comment-count">💬 {{ post.comment_count }} comments</span>
        </div>
        
        <!-- Comments Section -->
        <div v-if="post.comments && post.comments.length > 0" class="comments-section">
          <h4>Recent Comments:</h4>
          <div v-for="comment in post.comments" :key="comment.id" class="comment">
            <div class="comment-header">
              <span class="comment-author">@{{ comment.user }}</span>
              <span class="comment-timestamp">{{ formatTimestamp(comment.timestamp) }}</span>
            </div>
            <p class="comment-text">{{ comment.text }}</p>
          </div>
          <div v-if="post.comment_count > 3" class="more-comments">
            + {{ post.comment_count - 3 }} more comments
          </div>
        </div>
      </div>
    </div>
    
    <!-- Loading indicator -->
    <div v-if="loading" class="loading">
      <div class="spinner"></div>
      <p>Loading more posts...</p>
    </div>
    
    <!-- No posts message -->
    <div v-if="!loading && posts.length === 0" class="no-posts">
      <p>No posts available. Make sure your Django server is running at <code>http://127.0.0.1:8000</code></p>
    </div>
    
    <!-- Load more button (fallback for infinite scroll) -->
    <button 
      v-if="hasMore && !loading && posts.length > 0" 
      @click="loadMorePosts"
      class="load-more-btn"
    >
      Load More Posts
    </button>
    
    <!-- End of posts message -->
    <div v-if="!hasMore && posts.length > 0" class="end-message">
      You've reached the end of the posts!
    </div>

    <!-- Back to Home -->
    <div class="navigation-footer">
      <router-link to="/" class="back-home">← Back to Home</router-link>
    </div>
  </div>
</template>

<script>
 import api from "@/services/api"; 

export default {
  name: 'PostsComponent',
  data() {
    return {
      posts: [],
      loading: false,
      currentPage: 1,
      hasMore: true,
    };
  },
  mounted() {
    this.loadPosts();
    this.setupInfiniteScroll();
  },
  beforeUnmount() {
    window.removeEventListener('scroll', this.handleScroll);
  },
  methods: {
    async loadPosts() {
      if (this.loading || !this.hasMore) return;

      this.loading = true;

      try {
        const response = await api.get("/posts/", {
          params: { page: this.currentPage }
        });

        const data = response.data;

        if (this.currentPage === 1) {
          this.posts = data.results;
        } else {
          this.posts = [...this.posts, ...data.results];
        }

        this.hasMore = !!data.next;
        this.currentPage++;

      } catch (error) {
        console.error("Error loading posts:", error);

        
        if (this.currentPage === 1) {
          this.posts = [
            {
              id: "demo-1",
              text: "This is a demo post since the Django server is not accessible.",
              timestamp: new Date().toISOString(),
              user: "demo_user",
              comment_count: 2,
              comments: [
                {
                  id: "demo-comment-1",
                  text: "This is a demo comment.",
                  timestamp: new Date().toISOString(),
                  user: "commenter1"
                }
              ]
            }
          ];
          this.hasMore = false;
        }
      } finally {
        this.loading = false;
      }
    },

    async loadMorePosts() {
      await this.loadPosts();
    },

    setupInfiniteScroll() {
      window.addEventListener("scroll", this.handleScroll);
    },

    handleScroll() {
      const { scrollTop, scrollHeight, clientHeight } = document.documentElement;

      if (scrollTop + clientHeight >= scrollHeight - 100) {
        this.loadPosts();
      }
    },

    formatTimestamp(timestamp) {
      const date = new Date(timestamp);
      const now = new Date();
      const diffMs = now - date;
      const diffMins = Math.floor(diffMs / (1000 * 60));
      const diffHours = Math.floor(diffMs / (1000 * 60 * 60));
      const diffDays = Math.floor(diffMs / (1000 * 60 * 60 * 24));

      if (diffMins < 1) return "Just now";
      if (diffMins < 60) return `${diffMins}m ago`;
      if (diffHours < 24) return `${diffHours}h ago`;
      if (diffDays < 7) return `${diffDays}d ago`;

      return date.toLocaleDateString();
    }
  }
};
</script>

<style scoped>
.posts-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
  min-height: 100vh;
  background: #f8f9fa;
}

.posts-header {
  text-align: center;
  margin-bottom: 3rem;
  padding: 2rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 16px;
  color: white;
}

.posts-header h2 {
  font-size: 2rem;
  margin-bottom: 0.5rem;
}

.posts-header p {
  opacity: 0.9;
  font-size: 1.1rem;
}

.posts-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.post-card {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  border: 1px solid #e1e5e9;
  transition: all 0.3s ease;
}

.post-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
}

.post-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.post-author {
  font-weight: 600;
  color: #1a73e8;
  font-size: 0.95rem;
}

.post-timestamp {
  color: #666;
  font-size: 0.85rem;
}

.post-content {
  margin-bottom: 1rem;
  line-height: 1.6;
  color: #333;
}

.post-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 0.5rem;
  border-top: 1px solid #f0f0f0;
}

.comment-count {
  color: #666;
  font-size: 0.9rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.comments-section {
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid #f0f0f0;
}

.comments-section h4 {
  font-size: 0.95rem;
  margin-bottom: 0.8rem;
  color: #333;
}

.comment {
  background: #f8f9fa;
  padding: 0.8rem;
  border-radius: 8px;
  margin-bottom: 0.5rem;
}

.comment-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.3rem;
}

.comment-author {
  font-weight: 500;
  color: #1a73e8;
  font-size: 0.85rem;
}

.comment-timestamp {
  color: #666;
  font-size: 0.75rem;
}

.comment-text {
  font-size: 0.9rem;
  color: #333;
  line-height: 1.4;
}

.more-comments {
  color: #666;
  font-size: 0.85rem;
  text-align: center;
  padding: 0.5rem;
  background: #f8f9fa;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.more-comments:hover {
  background: #e9ecef;
}

.loading {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
  gap: 1rem;
}

.spinner {
  width: 30px;
  height: 30px;
  border: 3px solid #f3f3f3;
  border-top: 3px solid #1a73e8;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.no-posts {
  text-align: center;
  padding: 3rem 2rem;
  background: white;
  border-radius: 12px;
  border: 2px dashed #ddd;
}

.no-posts code {
  background: #f1f3f4;
  padding: 0.2rem 0.5rem;
  border-radius: 4px;
  font-family: monospace;
}

.load-more-btn {
  display: block;
  margin: 2rem auto;
  padding: 0.8rem 2rem;
  background: #1a73e8;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 0.95rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

.load-more-btn:hover {
  background: #1557b0;
  transform: translateY(-1px);
}

.end-message {
  text-align: center;
  padding: 2rem;
  color: #666;
  font-style: italic;
}

.navigation-footer {
  margin-top: 3rem;
  padding: 2rem;
  text-align: center;
  background: white;
  border-radius: 12px;
}

.back-home {
  color: #1a73e8;
  text-decoration: none;
  padding: 0.8rem 2rem;
  border: 2px solid #1a73e8;
  border-radius: 8px;
  font-weight: 600;
  transition: all 0.3s ease;
}

.back-home:hover {
  background: #1a73e8;
  color: white;
  transform: translateY(-2px);
}

/* Responsive Design */
@media (max-width: 768px) {
  .posts-container {
    padding: 1rem;
  }
  
  .post-card {
    padding: 1rem;
  }
  
  .post-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.3rem;
  }
  
  .posts-header {
    padding: 1.5rem 1rem;
  }
}
</style>
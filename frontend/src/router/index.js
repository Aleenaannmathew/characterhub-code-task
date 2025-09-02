import { createRouter, createWebHistory } from "vue-router";
import Home from "@/pages/Home.vue";
import MoviePage from "@/components/MoviePage.vue";

const routes = [
    { path: "/", name: "Home", component: Home },
    { path: "/movie", name: "Movie", component: MoviePage },
    { path: "/posts", name: "Posts", component: () => import("@/components/PostsComponent.vue") }
];

const router = createRouter({
    history: createWebHistory(), 
    routes,
});

export default router;
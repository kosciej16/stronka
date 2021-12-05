import { createWebHistory, createRouter } from "vue-router";
import Kontakt from './components/Kontakt.vue'
import About from './components/About.vue'
import Login from './components/Login.vue'

const routes = [
  { path: '/kontakt', name:'kontakt', component: Kontakt },
  { path: '/about', name:'about', component: About },
  { path: '/login', name:'login', component: Login },
]
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

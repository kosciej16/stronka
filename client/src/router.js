import { createWebHistory, createRouter } from "vue-router";
import Kontakt from './components/Kontakt.vue'

const routes = [
  { path: '/foo', name:'nazw', component: Kontakt }
]
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

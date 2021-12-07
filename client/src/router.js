import { createWebHistory, createRouter } from "vue-router";
import Kontakt from './components/Kontakt.vue'
import Home from './components/Home.vue'
import About from './components/About.vue'
import Login from './components/Login.vue'
import Events from './components/Events.vue'
import Register from './components/Register.vue'
import Register2 from './components/Register2.vue'
import Points from './components/Points.vue'
import Piramida from './components/Piramida.vue'
import Plansze from './components/Plansze.vue'
import Ranking from './components/Ranking.vue'

const routes = [
  { path: '/', name:'home', component: Home },
  { path: '/kontakt', name:'kontakt', component: Kontakt },
  { path: '/about', name:'about', component: About },
  { path: '/login', name:'login', component: Login },
  { path: '/event', name:'event', component: Events },
  { path: '/register', name:'register', component: Register },
  { path: '/register2', name:'register2', component: Register2 },
  { path: '/points', name:'points', component: Points },
  { path: '/ranking', name:'ranking', component: Ranking },
  { path: '/event/piramida', name:'piramida', component: Piramida },
  { path: '/event/plansze', name:'plansze', component: Plansze },
]
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

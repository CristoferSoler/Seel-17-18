import Vue from 'vue';
import App from './App.vue';
import VueRouter from 'vue-router';
import Navbar from './components/Navbar.vue';
import Footer from './components/Footer.vue';
import Search from './components/Search.vue';
import Home from './Home.vue';
import Signup from './Signup.vue';
import Login from './Login.vue';
import SearchAdv from './components/Search-adv.vue';
import News from './components/News.vue';
import NewsImp from './components/News-Imp.vue';
import TutorList from './components/Tutorial-list.vue';


Vue.use(VueRouter);
Vue.component('app-footer', Footer);
Vue.component('app-navbar', Navbar);
Vue.component('app-search', Search );
Vue.component('app-search-adv', SearchAdv );
Vue.component('app-news', News );
Vue.component('app-news-imp', NewsImp );
Vue.component('app-tutor-list', TutorList );

const routes = [
  {path: '/', component: Home },
  {path: '/signup', component: Signup },
  {path: '/login', component: Login }
];

const router = new VueRouter( {
  routes,
  mode: 'history'
});

new Vue({
  el: '#app',
  router,
  render: h => h(App)
});

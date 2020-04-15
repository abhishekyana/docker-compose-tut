import Vue from 'vue';
import App from './App.vue';
import VueSimpleAlert from "vue-simple-alert";
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue';

Vue.use(BootstrapVue);
Vue.use(BootstrapVueIcons);
Vue.use(VueSimpleAlert);


Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')

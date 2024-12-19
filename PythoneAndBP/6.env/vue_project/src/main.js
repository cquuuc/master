import Vue from "vue";
import App from "./App.vue";
import ElementUI from "element-ui"; // 引入 Element UI
import "element-ui/lib/theme-chalk/index.css"; // 引入 Element UI 样式

Vue.config.productionTip = false;

// 使用 Element UI
Vue.use(ElementUI);

new Vue({
  render: h => h(App),
}).$mount("#app");

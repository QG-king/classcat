import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', redirect: '/manager/home' },
    {
      path: '/manager',
      name: 'Layout',
      component: () => import('@/layouts/layout.vue'),
      children: [
        { path: 'home', name: 'Home', component: () => import('@/views/Home.vue') },
        { path: 'lab', name: 'Lab', component: () => import('@/views/lab.vue') },
        { path: 'equ', name: 'Equ', component: () => import('@/views/equ.vue') },
        { path: 'user', name: 'User', component: () => import('@/views/user.vue') }
      ]
    },
    { path: '/login', name: 'login', component: () => import('@/views/login.vue') },
    { path: '/register', name: 'register', component: () => import('@/views/register.vue') }
  ]
})

export default router

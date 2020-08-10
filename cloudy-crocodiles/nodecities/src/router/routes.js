const routes = [
  {
    path: '/profile/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: 'sites', component: () => import('pages/user/OwnSites.vue'), name: 'userOwnSites'},
    ]
  },
  {
    path: '/sites/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/sites')},
      { path: 'add', component: () => import('pages/sites/add'), props: true},
      { path: ':id', component: () => import('pages/sites/_id'), props: true},
      { path: ':id/edit', component: () => import('pages/sites/_id/edit'), props: true},
    ]
  },
  {
    path: '/folders/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/folders')},
      { path: ':id', component: () => import('pages/folders/_id'), props: true},
    ]
  },
  {
    path: '/pages/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/pages')},
      { path: 'add/site/:siteid', component: () => import('pages/pages/add'), props: true},
      { path: ':id', component: () => import('pages/pages/_id'), props: true},
      { path: ':id/edit', component: () => import('pages/pages/_id/edit'), props: true},
    ]
  },
  {
    path: '/images/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/images')},
      { path: ':id', component: () => import('pages/images/_id'), props: true},
    ]
  },
  {
    path: '/at/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: ':slug', component: () => import('pages/City.vue'), props: true },
      { path: ':slug/:address', component: () => import('pages/Site.vue'), props: true },
    ]
  },
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') },
      { path: 'login', component: () => import('pages/Login.vue') },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue'),
  },
];

export default routes;

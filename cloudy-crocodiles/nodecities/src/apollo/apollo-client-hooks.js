export function apolloClientBeforeCreate (/* { apolloClientConfigObj, app, router, store, ssrContext, urlPath, redirect } */) {
  // if needed you can modify here the config object used for apollo client
  // instantiation
}
export var $apolloClient
// export function apolloClientAfterCreate (/* { apolloClient, app, router, store, ssrContext, urlPath, redirect } */) {
export function apolloClientAfterCreate ({ apolloClient, store } ) {
  // if needed you can modify here the created apollo client
  console.log(store)
  // store.rootState.apolloClient = apolloClient
  $apolloClient = apolloClient
}

import { setContext } from 'apollo-link-context';

const authLink = setContext((_, { headers }) => {
  // get the authentication token from local storage if it exists
  const token = localStorage.getItem('user-token');
  // return the headers to the context so httpLink can read them
  return {
    headers: {
      ...headers,
      authorization: token ? `Bearer ${token}` : "",
    }
  }
});

export function apolloClientBeforeCreate ( { apolloClientConfigObj } /*, app, router, store, ssrContext, urlPath, redirect } */) {
  // if needed you can modify here the config object used for apollo client
  // instantiation
  const link = apolloClientConfigObj.link;
  apolloClientConfigObj.link = authLink.concat(link);
}
export var $apolloClient
// export function apolloClientAfterCreate (/* { apolloClient, app, router, store, ssrContext, urlPath, redirect } */) {
export function apolloClientAfterCreate ({ apolloClient, store } ) {
  // if needed you can modify here the created apollo client
  console.log(store)
  // store.rootState.apolloClient = apolloClient
  $apolloClient = apolloClient
}

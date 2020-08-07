<template>
  <q-page padding>
    <div v-if="citySite">
      <h1>{{ slug }}/{{address}}</h1>
      {{ citySite.description }}
      <folder :site="citySite" :path="path"/>
    </div>
  </q-page>
</template>

<script>
import Folder from 'components/Folder'

import gql from 'graphql-tag';


const citySiteQuery = gql`
query citySite($slug: String!, $address: Int!) {
  citySite(slug: $slug, address: $address) {
    id,
    address,
    description
  }
}
`;

export default {
  name: 'Site',
  props: ['slug', 'address'],
  components: {
    Folder
  },
  data() {
    return {
        path: '/'
    };
  },
  apollo: {
    citySite: {
      query: citySiteQuery,
      variables () {
        return {
          slug: this.slug,
          address: parseInt(this.address)
        }
      },
    },
  },
  methods: {
  },

};
</script>

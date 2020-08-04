<template>
  <q-page padding>
    <div v-if="city">
      <h1>{{ city.name }}</h1>
      {{ city.description }}
      <city-sites :city="city" />
    </div>
  </q-page>
</template>

<script>
import CitySites from 'components/CitySites'

import gql from 'graphql-tag';


const cityQuery = gql`
query cityQuery($slug: String!) {
  city(slug: $slug) {
    id,
    slug,
    name,
    description
  }
}
`;

export default {
  name: 'City',
  props: ['slug'],
  components: {
    CitySites
  },
  data() {
    return {
    };
  },
  apollo: {
    city: {
      query: cityQuery,
      variables () {
        return {
          slug: this.slug
        }
      },
    },
  },
  methods: {
  },

};
</script>

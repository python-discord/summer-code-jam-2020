<template>
  <q-page padding>
    <div>
      <q-list class="menu-list">
        <q-item v-for="city in allCities" :key="city.slug" :to="`/cities/${city.slug}`">
          <q-item-section avatar>
            <q-icon name="mdi-account" inverted color="grey-6" />
          </q-item-section>
          <q-item-section>
            {{ city.name }}
          </q-item-section>
        </q-item>
      </q-list>
    </div>
  </q-page>
</template>

<script>
import gql from 'graphql-tag';

const citiesQuery = gql`
query citiesQuery {
  allCities {
    name,
    slug
  }
}
`;

export default {
  name: 'PageIndex',
  data() {
    return {
    };
  },
  apollo: {
    allCities: {
      query: citiesQuery,
      prefetch: false,
      fetchPolicy: 'network-only',
    },
  },
  methods: {
  },

};
</script>

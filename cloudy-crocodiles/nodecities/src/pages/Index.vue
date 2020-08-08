<template>
  <q-page padding>
    <div class="card-column">
      <q-card v-for="city in allCities" :key="city.slug">
        <q-card-section>
          <a :href="`/at/${city.slug}`">{{ city.name }}</a>
        </q-card-section>
        <q-card-section>
          {{ city.description }}
        </q-card-section>
      </q-card>
    </div>
  </q-page>
</template>

<script>
import gql from 'graphql-tag';

const citiesQuery = gql`
query citiesQuery {
  allCities {
    name,
    slug,
    description
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

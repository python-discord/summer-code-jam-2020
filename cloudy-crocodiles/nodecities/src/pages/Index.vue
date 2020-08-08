<template>
  <q-page padding>
    <div>
      <h1>Welcome to DjangoCities!</h1>
      <p>DjangoCities is your free home on the web! Find the city that best matches your interests, and claim your free website!</p>
      <h2>Features</h2>
      <ul>
        <li>Supports HTML1 <em>and</em> HTML2 files.</li>
        <li>Upload backgrounds, animated gifs, whatever you want!</li>
      </ul>
      <h2>Explore or join one of these great communities</h2>
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

<template>
  <q-page padding>
    <div v-if="ownSites">
      <h1>Your sites</h1>
      <div class="card-column">
        <q-card v-for="site in ownSites" :key="site.id">
          <q-card-section>
            <a :href="`/sites/${site.id}`">
            <h2>{{ site.city.name + site.address }}</h2>
            </a>
          </q-card-section>
          <q-card-section>{{ site.description }}</q-card-section>
          <q-card-actions>
            <q-btn
              @click="preview(site)"
            >Preview
            </q-btn>
          </q-card-actions>
        </q-card>
      </div>
    </div>
  </q-page>
</template>

<script>
import gql from "graphql-tag";

const userOwnSites = gql`
  query {
    ownSites: userOwnSites {
      id
      city {
        name
        slug
      }
      address
      description
    }
  }
`;

export default {
  name: "userOwnSites",
  apollo: {
    ownSites: {
      query: userOwnSites,
    },
  },
  methods: {
    preview(site) {
      window.location.href = `http://localhost:1234/${site.city.slug}/${site.address}/index.html`
    }
  }
};
</script>

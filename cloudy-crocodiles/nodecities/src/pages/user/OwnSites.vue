<template>
  <q-page padding>
    <div v-if="ownSites">
      <q-toolbar>
        <q-toolbar-title>
          <h1>Your sites</h1>
        </q-toolbar-title>
        <q-btn mini fab icon="note_add" color="accent" :to="`/sites/add`" />
      </q-toolbar>
      <div class="card-column">
        <q-card v-for="site in ownSites" :key="site.id">
          <q-card-section>
            <q-toolbar>
              <q-toolbar-title>
                <a :href="`/sites/${site.id}`">
                  <h3>{{ site.city.name + site.address }}</h3>
                </a>
              </q-toolbar-title>
              <q-btn mini flat icon="edit" :to="`/sites/${site.id}/edit`" />
            </q-toolbar>
          </q-card-section>
          <q-card-section>{{ site.description }}</q-card-section>
          <q-card-actions>
            <q-btn @click="preview(site)">Preview</q-btn>
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
      window.location.href = `http://localhost:1234/${site.city.slug}/${site.address}/index.html`;
    },
  },
};
</script>

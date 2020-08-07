<template>
  <q-page padding>
    <div>
      <div v-if="ownSites">
        <h1>Your sites</h1>
        <p
          v-for="site of ownSites"
          :key="site.id"
        >
          {{ site }}
        </p>
      </div>
    </div>
  </q-page>
</template>

<script>
import gql from 'graphql-tag';

const userOwnSites = gql`query {
    ownSites: userOwnSites {
      city {
        name
      }
        address
      description
    }
  }
`;

export default {
  name: 'userOwnSites',
  apollo: {
    ownSites: {
      query: userOwnSites,
    },
  },
}
</script>

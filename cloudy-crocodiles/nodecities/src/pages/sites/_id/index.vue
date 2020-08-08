<template>
  <q-page padding>
    <div v-if="site">
      <h1>{{ site.city.name }}{{ site.address }}</h1>
      {{ site.description }}
      <folder :site="site" :path="path" />
    </div>
  </q-page>
</template>

<script>
import Folder from "components/Folder";

import gql from "graphql-tag";

const siteQuery = gql`
  query site($id: ID!) {
    site(id: $id) {
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
  name: "Site",
  props: ["id"],
  components: {
    Folder,
  },
  data() {
    return {
      path: "/",
    };
  },
  apollo: {
    site: {
      query: siteQuery,
      variables() {
        return {
          id: this.id,
        };
      },
    },
  },
  methods: {},
};
</script>

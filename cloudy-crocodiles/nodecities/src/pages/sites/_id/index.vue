<template>
  <q-page padding>
    <div v-if="site">
      <h1>{{ site.city.name }}{{ site.address }}</h1>
      {{ site.description }}
      <site-pages :site="site" />
    </div>
  </q-page>
</template>

<script>
import SitePages from "components/SitePages";

import gql from "graphql-tag";

const siteQuery = gql`
  query site($id: ID!) {
    site(id: $id) {
      id
      pages {
        id
        file_name
      }
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
    SitePages,
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

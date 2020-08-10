<template>
  <q-page padding>
    <site-form edit v-if="site" :site="site" @submit="submit" />
  </q-page>
</template>

<script>
import SiteForm from "components/SiteForm";

import gql from "graphql-tag";

const siteQuery = gql`
  query site($id: ID!) {
    site(id: $id) {
      id
      city {
        id
      }
      address
      description
    }
  }
`;

export default {
  name: "EditSitePage",
  props: ["id"],
  components: {
    SiteForm,
  },
  data() {
    return {};
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
  methods: {
    submit(input) {
      this.$apollo.mutate({
        // Mutation
        mutation: gql`
          mutation($id: ID!, $data: SiteInput!) {
            updateSite(site_id: $id, data: $data) {
                id
            }
          }
        `,
        // Parameters
        variables: {
          id: this.id,
          data: input,
        },
      });
      this.$q.notify(`Site Saved`);
    },
  },
};
</script>

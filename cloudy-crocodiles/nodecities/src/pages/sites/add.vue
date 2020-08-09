<template>
  <q-page padding>
    <site-form v-if="site" :site="site" @submit="submit" />
  </q-page>
</template>

<script>
import gql from "graphql-tag";

import SiteForm from "components/SiteForm";

export default {
  name: "AddSitePage",
  props: ["siteid"],
  components: {
    SiteForm,
  },
  data() {
    return {
        site: null
    };
  },
  mounted() {
    this.site = {
      city: 0,
      address: 0,
      description: ''
    }
  },
  methods: {
    submit(input) {
      this.$apollo.mutate({
        // Mutation
        mutation: gql`
          mutation($data: SiteInput!) {
            createSite(data: $data) {
                id
            }
          }
        `,
        // Parameters
        variables: {
          data: input,
        },
      });
      this.$q.notify(`Site Created`);
    },
  },
};
</script>

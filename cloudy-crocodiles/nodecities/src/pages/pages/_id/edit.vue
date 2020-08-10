<template>
  <q-page padding>
    <page-form edit v-if="page" :page="page" @submit="submit" />
  </q-page>
</template>

<script>
import PageForm from "components/PageForm";

import gql from "graphql-tag";

const pageQuery = gql`
  query page($id: ID!) {
    page(id: $id) {
      id
      site {
        id
      }
      file_name
      content
    }
  }
`;

export default {
  name: "PagePage",
  props: ["id"],
  components: {
    PageForm,
  },
  data() {
    return {};
  },
  apollo: {
    page: {
      query: pageQuery,
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
          mutation($id: ID!, $data: PageInput!) {
            updatePage(page_id: $id, data: $data) {
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
      this.$q.notify(`Page Saved`);
    },
  },
};
</script>

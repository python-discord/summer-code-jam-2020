<template>
  <q-page padding>
    <page-form v-if="page" :page="page" @submit="submit" />
  </q-page>
</template>

<script>
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

import PageForm from "components/PageForm";

export default {
  name: "PageAddPage",
  props: ["siteid"],
  components: {
    PageForm,
  },
  data() {
    return {
        page: null
    };
  },
  apollo: {
    site: {
      query: siteQuery,
      variables() {
        return {
          id: this.siteid,
        };
      },
    },
  },
  mounted() {
    this.page = {
      site: this.site,
      version: '2',
      content: '',
      file_name: ''
    }
  },
  methods: {
    submit(input) {
      this.$apollo.mutate({
        // Mutation
        mutation: gql`
          mutation($data: PageInput!) {
            createPage(data: $data) {
                id
            }
          }
        `,
        // Parameters
        variables: {
          data: input,
        },
      });
      this.$q.notify(`Page Created`);
    },
  },
};
</script>

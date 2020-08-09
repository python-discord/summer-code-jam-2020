<template>
  <q-page padding>
    <div v-if="page" v-html="page.content" />
  </q-page>
</template>

<script>
// import PageForm from 'components/PageForm'

import gql from "graphql-tag";

const pageQuery = gql`
  query page($id: ID!) {
    page(id: $id) {
      id
      file_name
      content
    }
  }
`;

export default {
  name: "PagePage",
  props: ["id"],
  components: {
    // PageForm
  },
  data() {
    return {
    };
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
  methods: {},
};
</script>

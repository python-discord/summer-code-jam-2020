<template>
  <q-page padding>
    <div v-if="page">
      <h1>{{ page.file_name }}</h1>
      <pre><code>{{ page.content }}</code></pre>
    </div>
  </q-page>
</template>

<script>
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

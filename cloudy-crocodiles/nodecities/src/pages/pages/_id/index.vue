<template>
  <q-page padding>
    <div v-if="page">
      <h1>{{ page.filename }}</h1>
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
      filename
      content
      folder {
        id
        site {
          id
          city {
            name
            slug
          }
          address
          description
        }
        path
      }
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

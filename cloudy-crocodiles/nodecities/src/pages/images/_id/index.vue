<template>
  <q-page padding>
    <div v-if="image">
      <h1>{{ image.filename }}</h1>
      <img :src="`http://localhost:1234/cdn/${image.folder.site.city.slug}/${image.folder.site.address}/${image.folder.path}/${image.filename}`" />
    </div>
  </q-page>
</template>

<script>
import gql from "graphql-tag";

const imageQuery = gql`
  query image($id: ID!) {
    image(id: $id) {
      id
      filename
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
  name: "ImagePage",
  props: ["id"],
  components: {
  },
  data() {
    return {
    };
  },
  apollo: {
    image: {
      query: imageQuery,
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

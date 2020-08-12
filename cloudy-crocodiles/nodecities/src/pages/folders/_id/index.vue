<template>
  <q-page padding>
    <div v-if="folder">
      <h1>{{ folder.site.city.name }}{{ folder.site.address }}{{folder.path}}</h1>
      <folder :site="folder.site" :path="folder.path" />
    </div>
  </q-page>
</template>

<script>
import Folder from "components/Folder";

import gql from "graphql-tag";

const folderQuery = gql`
  query folder($id: ID!) {
    folder(id: $id) {
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
`;

export default {
  name: "FolderPage",
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
    folder: {
      query: folderQuery,
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

<template>
  <q-page padding>
      <items v-if="siteFolder" :folder="siteFolder" />
  </q-page>
</template>

<script>
import Items from 'components/Items'
import gql from 'graphql-tag';

const siteFolderQuery = gql`
query siteFolderQuery($id: ID!, $path: String!) {
  siteFolder(id: $id, path: $path) {
    id
    parent {
      id
    }
  }
}
`;

export default {
  name: 'Folder',
  props: ['site', 'path'],
  components: { Items },
  data() {
    return {
    };
  },
  apollo: {
    siteFolder: {
      query: siteFolderQuery,
      prefetch: false,
      fetchPolicy: 'network-only',
      variables () {
        return {
          id: this.site.id,
          path: this.path
        }
      },
    },
  },
  methods: {
  },

};
</script>

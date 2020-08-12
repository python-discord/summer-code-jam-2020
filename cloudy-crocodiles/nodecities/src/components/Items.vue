<template>
  <q-page padding>
    <q-list v-if="folderItems">
      <q-item v-if="folder.parent">
        <q-item-section>
          <a :href="`/folders/${folder.parent.id}`">
            ..
          </a>
        </q-item-section>
      </q-item>
      <q-item v-for="item in folderItems" :key="item.id">
        <q-item-section>
          <a :href="`/${item.collection}/${item.id}`">
            {{ item.filename }}
          </a>
        </q-item-section>
      </q-item>
    </q-list>
  </q-page>
</template>

<script>
import gql from 'graphql-tag';

const folderItemsQuery = gql`
query folderItemsQuery($id: ID!) {
  folderItems(id: $id) {
    id
    collection
    filename
  }
}
`;

export default {
  name: 'Items',
  props: ['folder'],
  data() {
    return {
    };
  },
  apollo: {
    folderItems: {
      query: folderItemsQuery,
      prefetch: false,
      fetchPolicy: 'network-only',
      variables () {
        return {
          id: this.folder.id
        }
      }
    },
  },
  methods: {
  },

};
</script>

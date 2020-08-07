<template>
  <q-page padding>
    <div v-if="folderData" class="card-column">
      <q-card v-for="item in folderData.children" :key="item.id">
        <q-card-section>
          <!-- <a :href="`http://localhost:1234/${city.slug}/${site.address}`"> -->
          <a href="">
            {{ item.name }}
          </a>
        </q-card-section>
      </q-card>
    </div>
  </q-page>
</template>

<script>
import gql from 'graphql-tag';

const folderDataQuery = gql`
query folderDataQuery($id: ID!) {
  folderData(id: $id)
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
    folderData: {
      query: folderDataQuery,
      prefetch: false,
      fetchPolicy: 'network-only',
      variables () {
        return {
          id: this.folder.id
        }
      },
        update (data) {
            return JSON.parse(data.folderData)
        },
    },
  },
  methods: {
  },

};
</script>

<template>
  <q-page padding>
    <div v-if="city">
      <h1>{{ city.name }}</h1>
      {{ city.description }}
      <div
        v-if="user !== null && city"
        class="row"
      >
        <q-btn @click="claim = true">Claim address</q-btn>
        <q-dialog v-model="claim">
          <q-card
            style="min-width: 300px;"
            class="q-px-sm q-pb-md"
          >
            <q-card-section>
              <div class="text-h6">Claim your free website</div>
            </q-card-section>
            <q-form @submit.prevent="handleClaim">
              <q-input
                v-model="newSiteDescr"
                label="Site Description"
              />
              <div class="q-pa-md">
                <q-btn label="Claim" type="submit" v-close-popup/>
                <q-btn label="Cancel" color="warning" v-close-popup/>
              </div>
            </q-form>
          </q-card>
        </q-dialog>
      </div>
      <city-sites :city="city" ref="citySites" />
    </div>
  </q-page>
</template>

<script>
import CitySites from 'components/CitySites'

import gql from 'graphql-tag';

import { $apolloClient } from 'src/apollo/apollo-client-hooks';

const cityQuery = gql`
query cityQuery($slug: String!) {
  city(slug: $slug) {
    id,
    slug,
    name,
    description
  }
}
`;

const createSiteMutation = gql`mutation createSite($data: SiteInput!) {
  createSite(data: $data) {
    address
  }
}`;

export default {
  name: 'City',
  props: ['slug'],
  components: {
    CitySites
  },
  data() {
    return {
      claim: false,
      newSiteDescr: '',
    };
  },
  apollo: {
    city: {
      query: cityQuery,
      variables () {
        return {
          slug: this.slug
        }
      },
    },
  },
  computed: {
    user() {
      return this.$store.getters.user;
    },
  },
  methods: {
    handleClaim() {
      $apolloClient.mutate({
        mutation: createSiteMutation,
        variables: {
          data: {
            city: this.city.id,
            description: this.newSiteDescr,
          }
        }
      }).then((data) => {
        this.$refs.citySites.$apollo.queries.citySites.refetch();
        console.log(data);
        console.log(data.data.createSite.address);
      });
    },
  },
};
</script>

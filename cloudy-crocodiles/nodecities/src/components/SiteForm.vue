<template>
  <q-page padding>
    <div class="fields">
      <q-toolbar>
        <q-toolbar-title>
          <div v-if="edit">
            Edit Site
          </div>
          <div v-else>
            Add Site
          </div>
        </q-toolbar-title>
        <q-btn icon="save" @click="save"/>
      </q-toolbar>
      <q-select label="City" :options="cityOptions" v-model="selectedCity" @input="onSelectionChanged"/>
      <q-input v-model="site.address" label="Address" />
      <q-input v-model="site.description" label="Description" />
    </div>
  </q-page>
</template>

<script>
import gql from "graphql-tag";

const citiesQuery = gql`
query citiesQuery {
  allCities {
    id,
    name,
    slug,
    description
  }
}
`;

export default {
  name: "SiteForm",
  props: { site: { type: Object}, edit: { type: Boolean, default: true }},
  components: {
  },
  data() {
    return {
      cityOptions: [],
      selectedCity: {}
    };
  },
  apollo: {
    allCities: {
      query: citiesQuery,
      prefetch: false,
      fetchPolicy: 'network-only',
      update(data){
        console.log(data)
        for (var city of data.allCities) {
          this.cityOptions.push({ label: city.name, value: city.id })
          this.selectedCity = this.cityOptions[0]
        }
      },
    },
  },
  mounted () {
  },
  methods: {
    onSelectionChanged(newVal){
      console.log(newVal)
    },
    save(){
      const input = {
        city: this.selectedCity.value,
        description: this.site.description
      }
      this.$emit('submit', input);
    }
  },
};
</script>

<template>
  <q-page padding>
    <page-form :id="id" />
  </q-page>
</template>

<script>
import PageForm from 'components/PageForm'

export default {
  name: "PagePage",
  props: ["id"],
  components: {
    PageForm
  },
  data() {
    return {
    };
  },
  methods: {},
};
</script>

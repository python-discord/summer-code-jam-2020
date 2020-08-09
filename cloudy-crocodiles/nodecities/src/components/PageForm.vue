<template>
  <q-page padding>
    <div class="fields">
      <q-toolbar>
        <q-toolbar-title>
          <div v-if="edit">Edit Page</div>
          <div v-else>Add Page</div>
        </q-toolbar-title>
        <q-btn icon="save" @click="save" />
      </q-toolbar>
      <div v-if="edit">{{ page.file_name }}</div>
      <div v-else>
        <q-input v-model="page.file_name" label="File Name" />
      </div>
      <textarea ref="editor"></textarea>
    </div>
  </q-page>
</template>

<script>
import CodeMirror from "codemirror";
import "codemirror/lib/codemirror.css";
import "codemirror/mode/htmlmixed/htmlmixed.js";

export default {
  name: "PageForm",
  props: { page: { type: Object}, edit: { type: Boolean, default: true }},
  components: {},
  data() {
    return {};
  },
  mounted() {
    const cm = (this.cm = CodeMirror.fromTextArea(this.$refs.editor, {
      mode: "text/html",
      lineNumbers: true,
      styleActiveLine: true,
      matchBrackets: true,
      tabSize: 2,
    }));
    const content = this.page.content;
    cm.setValue(content);
  },
  methods: {
    save() {
      const input = {
        site: this.page.site.id,
        version: this.page.version,
        content: this.cm.getValue(),
        file_name: this.page.file_name,
      };
      this.$emit("submit", input);
    },
  },
};
</script>

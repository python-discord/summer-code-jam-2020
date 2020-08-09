<template>
  <q-page padding>
    <div v-if="page">
      <q-toolbar>
        <q-toolbar-title>
          {{ page.file_name }}
        </q-toolbar-title>
        <q-btn icon="save" @click="save"/>
      </q-toolbar>
      <textarea ref="editor"></textarea>
    </div>
    <div v-else>
      <h1></h1>
      <pre><code>{{ page.content }}</code></pre>
    </div>
  </q-page>
</template>

<script>
import CodeMirror from 'codemirror'
import 'codemirror/lib/codemirror.css'
import 'codemirror/mode/htmlmixed/htmlmixed.js'

export default {
  name: "PageForm",
  props: ["page", "submit"],
  components: {
  },
  data() {
    return {
    };
  },
  mounted () {
    if (!this.page) {
      return;
    }
    const cm = this.cm = CodeMirror.fromTextArea(this.$refs.editor, {
      mode: "text/html",
      lineNumbers: true,
      styleActiveLine: true,
      matchBrackets: true,
      tabSize: 2
    })
    const content = this.page.content
    cm.setValue(content)
  },
  methods: {
    save(){
      const input = {
        site: this.page.id,
        version: this.page.version,
        content: this.cm.getValue(),
        file_name: this.page.file_name
      }
      this.$emit('submit', input);
    }
  },
};
</script>

<template>
  <q-page padding>
    <div v-if="page">
      <h1>{{ page.file_name }}</h1>
      <textarea ref="editor"></textarea>
    </div>
    <div v-else>
      <h1>{{ page.file_name }}</h1>
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
  props: ["page"],
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
      theme: 'miakai',
      mode: "text/html",
      lineNumbers: true,
      styleActiveLine: true,
      matchBrackets: true,
      tabSize: 2
    })
    const content = this.page.content
    cm.setValue(content)
  },
  methods: {},
};
</script>

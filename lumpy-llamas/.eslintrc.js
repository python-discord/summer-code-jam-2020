module.exports = {
  "settings": {
    "import/resolver": {
      "alias": [
        ['vue', 'vue/dist/vue.js']
      ],
    },
  },
  "extends": ["airbnb-base", "plugin:vue/essential"],
  "parserOptions": {
    "ecmaVersion": 8,
  },
  "rules": {
    "no-new": "off",
    "max-len": "off",
    "no-plusplus": "off",
    "import/no-extraneous-dependencies": ["error", { "optionalDependencies": true }],
    "prefer-destructuring": "off",
    "vue/require-v-for-key": "off",
    "no-alert": "off",
    "no-restricted-globals": "off"
  },
  "env": {
    "browser": true,
    "node": true,
    "mocha": true,
  },
  "globals": {
    "expect": true,
  },
};

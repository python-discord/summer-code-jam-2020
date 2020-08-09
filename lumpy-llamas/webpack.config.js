/* eslint-disable import/no-extraneous-dependencies */
const path = require('path');
const { VueLoaderPlugin } = require('vue-loader');
const WebpackBuildNotifierPlugin = require('webpack-build-notifier');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const HtmlWebpackInjector = require('html-webpack-injector');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');

const proxyEntries = {
  local: 'http://localhost:8000',
};

module.exports = (env) => {
  const isDev = env.COMMAND === 'serve';
  const proxy = proxyEntries.local;
  return {
    context: __dirname,
    mode: 'development',
    entry: {
      main: './frontend/js/main.js',
      styles_head: './frontend/js/styles.js',
    },
    devServer: {
      historyApiFallback: true,
      overlay: true,
      proxy: {
        '/api': {
          target: proxy,
        },
        '/static': {
          target: proxy,
        },
      },
    },
    output: {
      path: path.resolve('./lammas/static/'),
      publicPath: isDev ? '' : '/static/',
      filename: '[name].js',
    },
    plugins: [
      new CleanWebpackPlugin({
        cleanAfterEveryBuildPatterns: [
          'lammas/static/img',
          'lammas/static/*.js',
        ],
      }),
      new VueLoaderPlugin(),
      new WebpackBuildNotifierPlugin({
        title: 'Webpack',
        suppressWarning: true,
      }),
      new HtmlWebpackPlugin({
        filename: 'index.html',
        template: 'frontend/html/index.html',
        chunks: ['main', 'styles_head'],
      }),
      new HtmlWebpackInjector(),
    ],
    module: {
      rules: [
        {
          test: /\.js$/,
          exclude: /node_modules/,
          loader: 'babel-loader',
        },
        {
          test: /\.vue$/,
          loader: 'vue-loader',
        },
        {
          test: /\.css$/,
          loader: 'style-loader!css-loader',
        },
        {
          test: /\.(woff|woff2|eot|ttf)$/,
          loader: 'url-loader?limit=100000',
          options: {
            name: '/font/[name].[ext]',
          },
        },
        {
          test: /\.(png|svg|ico)$/,
          loader: 'file-loader?name=img/[name].[ext]',
        },
      ],
    },
    resolve: {
      alias: {
        vue: 'vue/dist/vue.js',
      },
    },
  };
};

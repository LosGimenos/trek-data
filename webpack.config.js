const path = require('path');
const webpack = require('webpack');

const config = {
  devtool: 'source-map',
  devServer: {
    contentBase: path.join(__dirname, 'static'),
    inline: true,
    port: 8080,
  },
  entry: path.join(__dirname, 'client', 'index.jsx'),
  output: {
    path: path.join(__dirname, 'app', 'static/js'),
    filename: 'bundle.js',
  },
  module: {
    rules: [
      {
        test: /.jsx?$/,
        loader: 'babel-loader',
        exclude: /node_modules/,
        options: {
          presets: ['es2015', 'react']
        }
      }
    ],
  },
   plugins: [
    ]
};

module.exports = config;


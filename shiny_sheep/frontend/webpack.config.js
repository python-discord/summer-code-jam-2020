module.exports = {
  devtool: 'inline-source-map',
  module: {
    rules: [
      {
        test: /\.js$/,
        use: {
          loader: "babel-loader"
        }
      },
      {
        test: /\.svg$/,
        loader:"svg-inline-loader"
      },
      {
          test:/\.png$/,
          loader:"file-loader"
      },
      {
        test: /\.(eot|woff|woff2|svg|ttf|ico)([\?]?.*)$/,
        loader:"file-loader"
      },
      {
        test: /\.css$/i,
        use: ['style-loader', 'css-loader']
      }
      
    
    ]
  }
};

const webpack = require('webpack');
const config = {
    entry:  __dirname + '/js/index.jsx',
    output: {
        path: __dirname + '/dist',
        filename: 'bundle.js',
    },
    resolve: {
        extensions: ['.js', '.jsx', '.css']
    },
    module: {
      rules: [
        {
          test: /\.jsx?/,
          exclude: /node_modules/,
          use: 'babel-loader'
        },
        // {
        //   test: /\.(png|svg|jpg|gif)$/,
        //   use: 'file-loader'
        // }
        {
            test: /\.(jpe?g|png|gif|svg)$/i,
            loader: "file-loader?name=/public/images/[name].[ext]",
            // options: {
            //   limit: 100000,
            // }
        }
      ]
    },
    // https://github.com/webpack/webpack/issues/1083#issuecomment-103820257 
      // resolveLoader: {
      //   root: path.join(__dirname, 'node_modules')
      // }
};
module.exports = config;

#!/bin/bash

echo '<?xml version="1.0"?>' > debug.html
echo '<style> svg { width: 100%; margin-bottom: 10px; } </style>' >> debug.html
node_modules/.bin/mocha test/js/*.js 2> >(dot -Tsvg >> debug.html)

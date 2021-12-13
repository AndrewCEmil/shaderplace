cp index.html app/static/
cp edit.html app/static/
cp present.html app/static/
cp style.css app/static/
cp lint.css app/static/
cp defaultShaders.js app/static/

npm run build

cp -r dist/* app/dist/

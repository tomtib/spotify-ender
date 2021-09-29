Spotify Ender 

You will need to have installed Docker before using this repository

1. Add spotify urls to spotify-urls.txt file
2. Run 'docker build . -t spotify-ender'
3. Once image is built run 'docker run -v $(pwd)/downloads:/tmp spotify-ender

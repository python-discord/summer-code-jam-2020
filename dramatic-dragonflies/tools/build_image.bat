docker build -f .\tools\build_image.Dockerfile -t the_htmvs_imagemaker .\tools
echo ">>> CREATING IMAGE"
docker run -it --privileged --name the_htmvs_imagemaker-b the_htmvs_imagemaker
echo ">>> EXTRACTING ARTIFACT"
docker cp the_htmvs_imagemaker-b:/rom.tar.gz .
docker rm --force the_htmvs_imagemaker-b > nul
echo "DONE!"

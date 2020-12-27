#Script qui permet de build l'image à partir du dockerfile pour la mettre ensuite dans le dossier de déploiement

docker build --no-cache -t pg_gda:latest .
echo ""
echo "Saving image into ../deployment/pg_gda_image.tar..."
docker save pg_gda:latest > ../deployment/pg_gda_image.tar
echo ""
echo "Saved !"

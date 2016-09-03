Clonar el repositorio usando git y configurar los credenciales

git clone "https://github.com/itaimal/OlimpiColombiaWeb.git"
cd olimpiColombia
git config user.name "{{your user}}"
git config user.email "{{your email}}"
git config credential.helper store
git pull
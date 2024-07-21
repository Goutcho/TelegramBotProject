# Utiliser une image de base officielle de Node.js
FROM node:14

# Créer et définir le répertoire de travail de l'application
WORKDIR /app

# Copier les fichiers package.json et package-lock.json
COPY package*.json ./

# Installer les dépendances de l'application
RUN npm install

# Copier le reste des fichiers de l'application
COPY . .

# Exposer le port sur lequel l'application va fonctionner
EXPOSE 8080

# Commande pour lancer l'application
CMD ["npm", "run", "serve"]

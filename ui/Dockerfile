# Use an official Node.js runtime as a base image
FROM node:lts-alpine as builder

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json (if available)
COPY package*.json ./

# Copy zscaler certs
COPY zscaler-root.pem ./

ENV NODE_EXTRA_CA_CERTS /app/zscaler-root.pem

# Install project dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the Vue.js application
RUN npm run build

# Use an official Nginx image to serve the built application
FROM nginx:alpine as production

# Copy the built application from the builder stage
COPY --from=builder /app/dist /usr/share/nginx/html

# Expose port 80 for HTTP
EXPOSE 80

# Start Nginx when the container starts
CMD ["nginx", "-g", "daemon off;"]

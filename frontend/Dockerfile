FROM node:20-alpine AS builder

WORKDIR /app
RUN corepack enable && corepack prepare yarn@1.22.0 --activate

COPY package.json yarn.lock* ./
RUN yarn install --frozen-lockfile 2>/dev/null || yarn install

COPY . .
RUN yarn build

FROM node:20-alpine
WORKDIR /app
RUN corepack enable && corepack prepare yarn@1.22.0 --activate

COPY --from=builder /app/.output /app/.output
COPY --from=builder /app/package.json ./
ENV NODE_ENV=production
EXPOSE 3000
CMD ["node", ".output/server/index.mjs"]

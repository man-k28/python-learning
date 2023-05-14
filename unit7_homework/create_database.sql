CREATE TABLE "country" (
  "id" SERIAL PRIMARY KEY,
  "name" TEXT NOT NULL
);

CREATE TABLE "city" (
  "id" SERIAL PRIMARY KEY,
  "name" TEXT NOT NULL,
  "country" INTEGER NOT NULL
);

CREATE INDEX "idx_city__country" ON "city" ("country");

ALTER TABLE "city" ADD CONSTRAINT "fk_city__country" FOREIGN KEY ("country") REFERENCES "country" ("id") ON DELETE CASCADE;

CREATE TABLE "entertainment" (
  "id" SERIAL PRIMARY KEY,
  "name" TEXT NOT NULL
);

CREATE TABLE "permit" (
  "id" SERIAL PRIMARY KEY,
  "city" INTEGER NOT NULL,
  "cost" INTEGER NOT NULL,
  "rating" INTEGER NOT NULL
);

CREATE INDEX "idx_permit__city" ON "permit" ("city");

ALTER TABLE "permit" ADD CONSTRAINT "fk_permit__city" FOREIGN KEY ("city") REFERENCES "city" ("id") ON DELETE CASCADE;

CREATE TABLE "entertainment_permit" (
  "id" SERIAL PRIMARY KEY,
  "permit" INTEGER NOT NULL,
  "entertainment" INTEGER NOT NULL
);

CREATE INDEX "idx_entertainment_permit__entertainment" ON "entertainment_permit" ("entertainment");

CREATE INDEX "idx_entertainment_permit__permit" ON "entertainment_permit" ("permit");

ALTER TABLE "entertainment_permit" ADD CONSTRAINT "fk_entertainment_permit__entertainment" FOREIGN KEY ("entertainment") REFERENCES "entertainment" ("id") ON DELETE CASCADE;

ALTER TABLE "entertainment_permit" ADD CONSTRAINT "fk_entertainment_permit__permit" FOREIGN KEY ("permit") REFERENCES "permit" ("id") ON DELETE CASCADE
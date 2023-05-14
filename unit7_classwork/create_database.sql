CREATE TABLE "category" (
  "id" SERIAL PRIMARY KEY,
  "name" VARCHAR(32) UNIQUE NOT NULL
);

CREATE TABLE "group" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "student" (
  "id" SERIAL PRIMARY KEY,
  "name" VARCHAR(64) UNIQUE NOT NULL
);

CREATE TABLE "group_student" (
  "id" SERIAL PRIMARY KEY,
  "student" INTEGER NOT NULL,
  "group" INTEGER NOT NULL
);

CREATE INDEX "idx_group_student__group" ON "group_student" ("group");

CREATE INDEX "idx_group_student__student" ON "group_student" ("student");

ALTER TABLE "group_student" ADD CONSTRAINT "fk_group_student__group" FOREIGN KEY ("group") REFERENCES "group" ("id") ON DELETE CASCADE;

ALTER TABLE "group_student" ADD CONSTRAINT "fk_group_student__student" FOREIGN KEY ("student") REFERENCES "student" ("id") ON DELETE CASCADE;

CREATE TABLE "task" (
  "id" SERIAL PRIMARY KEY,
  "task_content" TEXT NOT NULL,
  "qualify" SMALLINT NOT NULL,
  "category" INTEGER NOT NULL
);

CREATE INDEX "idx_task__category" ON "task" ("category");

ALTER TABLE "task" ADD CONSTRAINT "fk_task__category" FOREIGN KEY ("category") REFERENCES "category" ("id") ON DELETE CASCADE;

CREATE TABLE "task_status" (
  "id" SERIAL PRIMARY KEY,
  "name" VARCHAR(32) UNIQUE NOT NULL
);

CREATE TABLE "student_task" (
  "id" SERIAL PRIMARY KEY,
  "task__status" INTEGER NOT NULL,
  "task_result" TEXT NOT NULL,
  "student" INTEGER NOT NULL,
  "task" INTEGER NOT NULL
);

CREATE INDEX "idx_student_task__student" ON "student_task" ("student");

CREATE INDEX "idx_student_task__task" ON "student_task" ("task");

CREATE INDEX "idx_student_task__task__status" ON "student_task" ("task__status");

ALTER TABLE "student_task" ADD CONSTRAINT "fk_student_task__student" FOREIGN KEY ("student") REFERENCES "student" ("id") ON DELETE CASCADE;

ALTER TABLE "student_task" ADD CONSTRAINT "fk_student_task__task" FOREIGN KEY ("task") REFERENCES "task" ("id") ON DELETE CASCADE;

ALTER TABLE "student_task" ADD CONSTRAINT "fk_student_task__task__status" FOREIGN KEY ("task__status") REFERENCES "task_status" ("id") ON DELETE CASCADE;

CREATE TABLE "teacher" (
  "id" SERIAL PRIMARY KEY,
  "name" VARCHAR(64) NOT NULL
);

CREATE TABLE "lesson" (
  "id" SERIAL PRIMARY KEY,
  "number" SMALLINT UNIQUE,
  "teacher" INTEGER NOT NULL
);

CREATE INDEX "idx_lesson__teacher" ON "lesson" ("teacher");

ALTER TABLE "lesson" ADD CONSTRAINT "fk_lesson__teacher" FOREIGN KEY ("teacher") REFERENCES "teacher" ("id");

CREATE TABLE "group_lesson" (
  "id" SERIAL PRIMARY KEY,
  "group" INTEGER NOT NULL,
  "lesson" INTEGER NOT NULL
);

CREATE INDEX "idx_group_lesson__group" ON "group_lesson" ("group");

CREATE INDEX "idx_group_lesson__lesson" ON "group_lesson" ("lesson");

ALTER TABLE "group_lesson" ADD CONSTRAINT "fk_group_lesson__group" FOREIGN KEY ("group") REFERENCES "group" ("id") ON DELETE CASCADE;

ALTER TABLE "group_lesson" ADD CONSTRAINT "fk_group_lesson__lesson" FOREIGN KEY ("lesson") REFERENCES "lesson" ("id") ON DELETE CASCADE;

CREATE TABLE "lesson_task" (
  "id" SERIAL PRIMARY KEY,
  "task" INTEGER NOT NULL,
  "lesson" INTEGER NOT NULL
);

CREATE INDEX "idx_lesson_task__lesson" ON "lesson_task" ("lesson");

CREATE INDEX "idx_lesson_task__task" ON "lesson_task" ("task");

ALTER TABLE "lesson_task" ADD CONSTRAINT "fk_lesson_task__lesson" FOREIGN KEY ("lesson") REFERENCES "lesson" ("id") ON DELETE CASCADE;

ALTER TABLE "lesson_task" ADD CONSTRAINT "fk_lesson_task__task" FOREIGN KEY ("task") REFERENCES "task" ("id") ON DELETE CASCADE
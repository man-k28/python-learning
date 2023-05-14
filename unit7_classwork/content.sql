INSERT INTO public.teacher(name) VALUES ('Учитель №1');

INSERT INTO public.student(name) VALUES ('Васечкин');
INSERT INTO public.student(name) VALUES ('Петров');
INSERT INTO public.student(name) VALUES ('Сидоров');

INSERT INTO public.category(name) VALUES ('История науки');
INSERT INTO public.category(name) VALUES ('Философия');
INSERT INTO public.category(name) VALUES ('Математика');

INSERT INTO public.task_status(name) VALUES ('Выполнено');
INSERT INTO public.task_status(name) VALUES ('Не выполнено');

INSERT INTO public."group"(id) VALUES (1);

INSERT INTO public.lesson("number", teacher) VALUES (1, 1);
INSERT INTO public.lesson("number", teacher) VALUES (2, 1);
INSERT INTO public.lesson("number", teacher) VALUES (3, 1);

INSERT INTO public.task(task_content, qualify, category) VALUES ('Задача 1', 80, 1);
INSERT INTO public.task(task_content, qualify, category) VALUES ('Задача 2', 70, 1);
INSERT INTO public.task(task_content, qualify, category) VALUES ('Задача 3', 80, 2);
INSERT INTO public.task(task_content, qualify, category) VALUES ('Задача 4', 80, 2);
INSERT INTO public.task(task_content, qualify, category) VALUES ('Задача 5', 70, 3);
INSERT INTO public.task(task_content, qualify, category) VALUES ('Задача 6', 65, 3);

INSERT INTO public.group_lesson("group", lesson) VALUES (1, 1);
INSERT INTO public.group_lesson("group", lesson) VALUES (1, 2);
INSERT INTO public.group_lesson("group", lesson) VALUES (1, 3);

INSERT INTO public.group_student(student, "group") VALUES (1, 1);
INSERT INTO public.group_student(student, "group") VALUES (2, 1);
INSERT INTO public.group_student(student, "group") VALUES (1, 1);

INSERT INTO public.lesson_task(task, lesson) VALUES (1, 1);
INSERT INTO public.lesson_task(task, lesson) VALUES (2, 1);
INSERT INTO public.lesson_task(task, lesson) VALUES (1, 2);
INSERT INTO public.lesson_task(task, lesson) VALUES (2, 2);
INSERT INTO public.lesson_task(task, lesson) VALUES (1, 3);
INSERT INTO public.lesson_task(task, lesson) VALUES (2, 3);

INSERT INTO public.student_task(task__status, task_result, student, task) VALUES (1, 'Результат задачи 1', 1, 1);
INSERT INTO public.student_task(task__status, task_result, student, task) VALUES (2, 'Результат задачи 2', 1, 2);
INSERT INTO public.student_task(task__status, task_result, student, task) VALUES (1, 'Результат задачи 3', 1, 3);
INSERT INTO public.student_task(task__status, task_result, student, task) VALUES (1, 'Результат задачи 4', 1, 4);
INSERT INTO public.student_task(task__status, task_result, student, task) VALUES (2, 'Результат задачи 5', 1, 5);
INSERT INTO public.student_task(task__status, task_result, student, task) VALUES (1, 'Результат задачи 6', 1, 6);

INSERT INTO public.student_task(task__status, task_result, student, task) VALUES (2, 'Результат задачи 1', 2, 1);
INSERT INTO public.student_task(task__status, task_result, student, task) VALUES (1, 'Результат задачи 2', 2, 2);
INSERT INTO public.student_task(task__status, task_result, student, task) VALUES (2, 'Результат задачи 3', 2, 3);
INSERT INTO public.student_task(task__status, task_result, student, task) VALUES (1, 'Результат задачи 4', 2, 4);
INSERT INTO public.student_task(task__status, task_result, student, task) VALUES (1, 'Результат задачи 5', 2, 5);
INSERT INTO public.student_task(task__status, task_result, student, task) VALUES (1, 'Результат задачи 6', 2, 6);

INSERT INTO public.student_task(task__status, task_result, student, task) VALUES (1, 'Результат задачи 1', 3, 1);
INSERT INTO public.student_task(task__status, task_result, student, task) VALUES (1, 'Результат задачи 2', 3, 2);
INSERT INTO public.student_task(task__status, task_result, student, task) VALUES (1, 'Результат задачи 3', 3, 3);
INSERT INTO public.student_task(task__status, task_result, student, task) VALUES (1, 'Результат задачи 4', 3, 4);
INSERT INTO public.student_task(task__status, task_result, student, task) VALUES (1, 'Результат задачи 5', 3, 5);
INSERT INTO public.student_task(task__status, task_result, student, task) VALUES (2, 'Результат задачи 6', 3, 6);
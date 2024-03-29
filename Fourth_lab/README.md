
Таблица 1 - Данные эекспериментов

![image](https://user-images.githubusercontent.com/58371161/225365736-779c06a4-7ee3-4c26-a79c-f2279c2463c3.png)

Представление решений  - класс, основным атрибутом которого является объект ArrayList<City> - tour. Данный класс содержит методы для добавления пункта назначения (setCity), инициализации маршрута (generateIndividual), подсчета расстояния (getFitness) и другие.
 
Оператор мутации имеет тип swap, который описан в документе к лабораторной работе. Значения шанса мутации (Mutation_rate) приведены в таблице 1.
Оператор кроссовера имеет тип ordered, описанный в документе к лабораторной работе. Выбор родителя, у которого будет взята подпоследовательность генов выбирается случайным образом.

Вопросы:
 
1) Можно ли определить, что полученное решение является глобальным оптимумом?
 
При решении задач с помощью генетических алгоритмов можно ориентироваться на фитнес функцию. С ее помощью можно узнать насколько ответ близок к оптимальному, но нельзя вычислить, что решение является глобальным оптимумом.
 
2) Можно ли допускать невалидные решения ( с повторением городов)? Если да, то как обрабатывать такие решения и как это повлияет на производительность алгоритма?
 
Нельзя допускать инвалидные решения, т.к. это противоречит условию данной задачи, где решение является комбинацией всех заданных уникальных объектов по одному разу, иначе salesman может оставаться на месте по несколько раз.
 
3) Как изменится задача, если убрать условие необходимости возврата в исходную точку маршрута?
 
Во-первых будет смещение в глобальном оптимуме, т.к. появятся новые решения, которые для измененной задачи. Это связано с тем, что размерность расстояний E между городами уменьшится на 1. Во-вторых вычисления будут проводиться для ациклического графа, в решение которого больший смысл имеет движение к городам, находящемся недалеко друг от друга.

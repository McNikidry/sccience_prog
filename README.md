<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="Scientific_programming_0"></a>Scientific programming</h1>
<h2 class="code-line" data-line-start=4 data-line-end=5 ><a id="task_1_4"></a>task 1</h2>
<p class="has-line-data" data-line-start="6" data-line-end="7">Решение должно реализовывать единственную функцию <code>get_objects()</code>, которая должна возвращать список (list) из объектов, каждый из которых уникального типа.</p>
<h2 class="code-line" data-line-start=8 data-line-end=9 ><a id="task_2_8"></a>task 2</h2>
<p class="has-line-data" data-line-start="10" data-line-end="12">Ваш код должен реализовывать единственную функцию  <code>cmp_to_key(comparator)</code>, аргументом которой является бинарная функция <code>comparator</code>. В результате работы <code>cmp_to_key</code> возвращает объект, который можно передать как параметр <code>key</code> в встроенную функцию  <code>sorted</code>.<br>
.</p>
<h6 class="code-line" data-line-start=12 data-line-end=13 ><a id="__12"></a>Формат входа</h6>
<p class="has-line-data" data-line-start="13" data-line-end="14">На входе <code>comparator(x, y)</code> бинарная функция, сравнивающая 2 объекта и возвращающая</p>
<pre><code class="has-line-data" data-line-start="15" data-line-end="19" class="language-sh">−<span class="hljs-number">1</span>(если x&lt;y),
 <span class="hljs-number">0</span>(если x==y),
+<span class="hljs-number">1</span>(если x&gt;y)
</code></pre>
<h6 class="code-line" data-line-start=19 data-line-end=20 ><a id="__19"></a>Формат выхода</h6>
<p class="has-line-data" data-line-start="20" data-line-end="21">На выходе ожидается объект, у которого есть оператор (), позволяющий отобразить аргумент оператора в <code>key</code>.</p>
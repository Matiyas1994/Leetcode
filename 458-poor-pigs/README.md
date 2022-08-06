<h2><a href="https://leetcode.com/problems/poor-pigs/">458. Poor Pigs</a></h2><h3>Hard</h3><hr><div><p>There are <code>buckets</code> buckets of liquid, where <strong>exactly one</strong> of the buckets is poisonous. To figure out which one is poisonous, you feed some number of (poor) pigs the liquid to see whether they will die or not. Unfortunately, you only have <code>minutesToTest</code> minutes to determine which bucket is poisonous.</p>

<p>You can feed the pigs according to these steps:</p>

<ol>
	<li>Choose some live pigs to feed.</li>
	<li>For each pig, choose which buckets to feed it. The pig will consume all the chosen buckets simultaneously and will take no time.</li>
	<li>Wait for <code>minutesToDie</code> minutes. You may <strong>not</strong> feed any other pigs during this time.</li>
	<li>After <code>minutesToDie</code> minutes have passed, any pigs that have been fed the poisonous bucket will die, and all others will survive.</li>
	<li>Repeat this process until you run out of time.</li>
</ol>

<p>Given <code>buckets</code>, <code>minutesToDie</code>, and <code>minutesToTest</code>, return <em>the <strong>minimum</strong> number of pigs needed to figure out which bucket is poisonous within the allotted time</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre style="position: relative;"><strong>Input:</strong> buckets = 1000, minutesToDie = 15, minutesToTest = 60
<strong>Output:</strong> 5
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre><p><strong>Example 2:</strong></p>
<pre style="position: relative;"><strong>Input:</strong> buckets = 4, minutesToDie = 15, minutesToTest = 15
<strong>Output:</strong> 2
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre><p><strong>Example 3:</strong></p>
<pre style="position: relative;"><strong>Input:</strong> buckets = 4, minutesToDie = 15, minutesToTest = 30
<strong>Output:</strong> 2
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= buckets &lt;= 1000</code></li>
	<li><code>1 &lt;=&nbsp;minutesToDie &lt;=&nbsp;minutesToTest &lt;= 100</code></li>
</ul>
</div>
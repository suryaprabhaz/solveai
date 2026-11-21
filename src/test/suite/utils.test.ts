import * as assert from 'assert';
import { stripCodeFences } from '../../services/promptService';
import { shouldStripCodeFences, getLanguageDisplayName, getLanguageFromExtension } from '../../utils/languageUtils';
import { validateInputSize } from '../../utils/editorUtils';
import { formatError, isNetworkError } from '../../utils/errorUtils';
import { findOfflineMatch } from '../../services/offlineDatabase';

suite('SolveAI Utilities Test Suite', () => {

  // --- offlineDatabase ---
  suite('offlineDatabase', () => {
    test('matches "bar chart in python"', () => {
      const match = findOfflineMatch('bar chart in python', 'python');
      assert.ok(match);
      assert.strictEqual(match?.id, 'py-bar-chart');
      assert.ok(match?.code.includes('plt.bar'));
    });

    test('matches shorthand "bar plot,py"', () => {
      const match = findOfflineMatch('bar plot,py');
      assert.ok(match);
      assert.strictEqual(match?.id, 'py-bar-chart');
      assert.strictEqual(match?.language, 'python');
      assert.ok(match?.code.includes('plt.bar'));
    });

    test('matches shorthand "histogram,r"', () => {
      const match = findOfflineMatch('histogram,r');
      assert.ok(match);
      assert.strictEqual(match?.id, 'r-histogram');
      assert.strictEqual(match?.language, 'r');
      assert.ok(match?.code.includes('hist('));
    });

    test('matches "histogram in r"', () => {
      const match = findOfflineMatch('histogram in r', 'r');
      assert.ok(match);
      assert.strictEqual(match?.id, 'r-histogram');
      assert.ok(match?.code.includes('hist('));
    });

    test('matches "heatmap" in python context', () => {
      const match = findOfflineMatch('draw a heatmap', 'python');
      assert.ok(match);
      assert.strictEqual(match?.id, 'py-heatmap');
    });

    test('matches "heatmap,py"', () => {
      const match = findOfflineMatch('heatmap,py');
      assert.ok(match);
      assert.strictEqual(match?.id, 'py-heatmap');
    });

    test('matches "grouped bar chart" in R context', () => {
      const match = findOfflineMatch('grouped bar chart in r', 'r');
      assert.ok(match);
      assert.strictEqual(match?.id, 'r-grouped-bar-chart');
    });

    test('matches shorthand "grouped bar chart,r"', () => {
      const match = findOfflineMatch('grouped bar chart,r');
      assert.ok(match);
      assert.strictEqual(match?.id, 'r-grouped-bar-chart');
    });

    test('matches "box plot,py" and "box plot,r"', () => {
      const pyMatch = findOfflineMatch('box plot,py');
      const rMatch = findOfflineMatch('box plot,r');
      assert.ok(pyMatch);
      assert.strictEqual(pyMatch?.id, 'py-box-plot');
      assert.ok(rMatch);
      assert.strictEqual(rMatch?.id, 'r-box-plot');
    });

    test('matches B.Tech C question "binary search in c"', () => {
      const match = findOfflineMatch('binary search in c');
      assert.ok(match);
      assert.ok(match?.code.includes('binarySearch'));
    });

    test('matches B.Tech C++ question "LRU cache in cpp"', () => {
      const match = findOfflineMatch('lru cache in cpp');
      assert.ok(match);
      assert.ok(match?.code.includes('LRUCache'));
    });

    test('matches B.Tech Java question "producer consumer in java"', () => {
      const match = findOfflineMatch('producer consumer java');
      assert.ok(match);
      assert.ok(match?.code.includes('produce'));
    });

    test('matches B.Tech SQL question "second highest salary"', () => {
      const match = findOfflineMatch('second highest salary in sql');
      assert.ok(match);
      assert.ok(match?.code.includes('SecondHighestSalary'));
    });
  });

  // --- stripCodeFences ---
  suite('stripCodeFences', () => {
    test('strips python fence', () => {
      const input = '```python\nprint("hello")\n```';
      const result = stripCodeFences(input, true);
      assert.strictEqual(result, 'print("hello")');
    });

    test('strips plain fence', () => {
      const input = '```\nsome code\n```';
      const result = stripCodeFences(input, true);
      assert.strictEqual(result, 'some code');
    });

    test('preserves markdown when strip=false', () => {
      const input = '```python\nprint("hello")\n```';
      const result = stripCodeFences(input, false);
      assert.strictEqual(result, input);
    });

    test('returns plain text unchanged', () => {
      const input = 'just some text without fences';
      const result = stripCodeFences(input, true);
      assert.strictEqual(result, input);
    });

    test('handles fence without language tag', () => {
      const input = '```\nconsole.log("hi")\n```';
      const result = stripCodeFences(input, true);
      assert.strictEqual(result, 'console.log("hi")');
    });
  });

  // --- languageUtils ---
  suite('languageUtils', () => {
    test('python languageId returns Python', () => {
      assert.strictEqual(getLanguageDisplayName('python'), 'Python');
    });

    test('r languageId returns R', () => {
      assert.strictEqual(getLanguageDisplayName('r'), 'R');
    });

    test('cpp returns C++', () => {
      assert.strictEqual(getLanguageDisplayName('cpp'), 'C++');
    });

    test('unknown language returns itself', () => {
      assert.strictEqual(getLanguageDisplayName('cobol'), 'cobol');
    });

    test('shouldStripCodeFences false for markdown', () => {
      assert.strictEqual(shouldStripCodeFences('markdown'), false);
    });

    test('shouldStripCodeFences true for python', () => {
      assert.strictEqual(shouldStripCodeFences('python'), true);
    });

    test('getLanguageFromExtension .py returns Python', () => {
      assert.strictEqual(getLanguageFromExtension('main.py'), 'Python');
    });

    test('getLanguageFromExtension .java returns Java', () => {
      assert.strictEqual(getLanguageFromExtension('Main.java'), 'Java');
    });
  });

  // --- validateInputSize ---
  suite('validateInputSize', () => {
    test('valid small input', () => {
      const result = validateInputSize('Write a Python program');
      assert.strictEqual(result.valid, true);
    });

    test('empty input is invalid', () => {
      const result = validateInputSize('   ');
      assert.strictEqual(result.valid, false);
    });

    test('oversized input is invalid', () => {
      const big = 'x'.repeat(9000);
      const result = validateInputSize(big);
      assert.strictEqual(result.valid, false);
      assert.ok(result.message?.includes('too large'));
    });
  });

  // --- errorUtils ---
  suite('errorUtils', () => {
    test('formatError with Error object', () => {
      const e = new Error('test error');
      assert.strictEqual(formatError(e), 'test error');
    });

    test('formatError with string', () => {
      assert.strictEqual(formatError('oops'), 'oops');
    });

    test('formatError with unknown', () => {
      assert.strictEqual(formatError(42), 'An unknown error occurred.');
    });

    test('isNetworkError detects ECONNREFUSED', () => {
      const e = new Error('connect ECONNREFUSED 127.0.0.1:11434');
      assert.strictEqual(isNetworkError(e), true);
    });

    test('isNetworkError returns false for logic errors', () => {
      const e = new Error('Model not found');
      assert.strictEqual(isNetworkError(e), false);
    });
  });
});

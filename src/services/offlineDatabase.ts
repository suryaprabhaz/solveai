export interface OfflineSolution {
  id: string;
  language: string; // 'python' | 'r'
  title: string;
  keywords: string[];
  code: string;
}

export const OFFLINE_DATABASE: OfflineSolution[] = [
  // ==========================================
  // PYTHON — MAIN VISUALIZATION QUESTIONS
  // ==========================================
  {
    id: 'py-line-chart',
    language: 'python',
    title: 'Line Chart',
    keywords: [
      'line chart', 'line graph', 'line plot', 'plot line', 'time series',
      'line chart,py', 'line chart, py', 'line chart py', 'line plot,py', 'line plot, py', 'line plot py'
    ],
    code: `import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [10, 24, 36, 45, 52]

# Plotting Line Chart
plt.figure(figsize=(8, 5))
plt.plot(x, y, marker='o', color='b', linestyle='-', linewidth=2, label='Trend')
plt.title('Line Chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()`
  },
  {
    id: 'py-bar-chart',
    language: 'python',
    title: 'Bar Chart',
    keywords: [
      'bar chart', 'bar plot', 'bar graph', 'student marks', 'categories',
      'bar plot,py', 'bar plot, py', 'bar plot py', 'bar chart,py', 'bar chart, py', 'bar chart py'
    ],
    code: `import matplotlib.pyplot as plt

# Data
categories = ['A', 'B', 'C', 'D', 'E']
values = [80, 70, 90, 60, 75]

# Plotting Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(categories, values, color='skyblue', edgecolor='black')
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()`
  },
  {
    id: 'py-histogram',
    language: 'python',
    title: 'Histogram',
    keywords: [
      'histogram', 'frequency distribution', 'hist plot', 'distribution',
      'histogram,py', 'histogram, py', 'histogram py', 'hist plot,py', 'hist,py'
    ],
    code: `import matplotlib.pyplot as plt
import numpy as np

# Sample Data
np.random.seed(42)
data = np.random.normal(loc=50, scale=10, size=200)

# Plotting Histogram
plt.figure(figsize=(8, 5))
plt.hist(data, bins=10, color='coral', edgecolor='black', alpha=0.7)
plt.title('Histogram Distribution')
plt.xlabel('Value Intervals')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()`
  },
  {
    id: 'py-pie-chart',
    language: 'python',
    title: 'Pie Chart',
    keywords: [
      'pie chart', 'pie plot', 'percentage chart', 'proportions',
      'pie chart,py', 'pie chart, py', 'pie chart py', 'pie plot,py', 'pie,py'
    ],
    code: `import matplotlib.pyplot as plt

# Data
labels = ['Python', 'Java', 'C++', 'JavaScript', 'R']
sizes = [35, 25, 15, 15, 10]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
explode = (0.05, 0, 0, 0, 0)  # highlight first slice

# Plotting Pie Chart
plt.figure(figsize=(7, 7))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=140)
plt.title('Programming Languages Share')
plt.axis('equal')
plt.show()`
  },
  {
    id: 'py-scatter-plot',
    language: 'python',
    title: 'Scatter Plot',
    keywords: [
      'scatter plot', 'scatter chart', 'scatter graph', 'correlation plot',
      'scatter plot,py', 'scatter plot, py', 'scatter plot py', 'scatter,py', 'scatter chart,py'
    ],
    code: `import matplotlib.pyplot as plt

# Data
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# Plotting Scatter Plot
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='purple', edgecolors='black', s=80, alpha=0.75)
plt.title('Scatter Plot')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()`
  },
  {
    id: 'py-heatmap',
    language: 'python',
    title: 'Heatmap',
    keywords: [
      'heatmap', 'heat map', 'correlation matrix', 'matrix plot',
      'heatmap,py', 'heatmap, py', 'heatmap py', 'heat map,py', 'heat map, py'
    ],
    code: `import matplotlib.pyplot as plt
import numpy as np

# Sample Correlation/Grid Data
data = np.array([
    [1.0, 0.8, 0.3],
    [0.8, 1.0, 0.5],
    [0.3, 0.5, 1.0]
])
labels = ['Var A', 'Var B', 'Var C']

# Plotting Heatmap
plt.figure(figsize=(6, 5))
plt.imshow(data, cmap='coolwarm', interpolation='nearest')
plt.colorbar(label='Scale')

# Add tick marks and cell labels
plt.xticks(ticks=range(len(labels)), labels=labels)
plt.yticks(ticks=range(len(labels)), labels=labels)

for i in range(len(labels)):
    for j in range(len(labels)):
        plt.text(j, i, f"{data[i, j]:.2f}", ha='center', va='center', color='black')

plt.title('Heatmap Matrix')
plt.tight_layout()
plt.show()`
  },
  {
    id: 'py-box-plot',
    language: 'python',
    title: 'Box Plot',
    keywords: [
      'box plot', 'boxplot', 'whisker plot', 'box and whisker',
      'box plot,py', 'box plot, py', 'box plot py', 'boxplot,py', 'boxplot, py', 'boxplot py'
    ],
    code: `import matplotlib.pyplot as plt
import numpy as np

# Sample Data
np.random.seed(10)
group1 = np.random.normal(100, 10, 50)
group2 = np.random.normal(90, 20, 50)
group3 = np.random.normal(70, 15, 50)
data = [group1, group2, group3]

# Plotting Box Plot
plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=['Group 1', 'Group 2', 'Group 3'], patch_artist=True,
            boxprops=dict(facecolor='lightblue', color='blue'))
plt.title('Box Plot Comparison')
plt.ylabel('Values')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()`
  },

  // ==========================================
  // R — MAIN VISUALIZATION QUESTIONS
  // ==========================================
  {
    id: 'r-line-chart',
    language: 'r',
    title: 'Line Chart',
    keywords: [
      'line chart', 'line graph', 'line plot', 'trend plot',
      'line chart,r', 'line chart, r', 'line chart r', 'line plot,r', 'line plot, r', 'line plot r'
    ],
    code: `# Data
x <- c(1, 2, 3, 4, 5)
y <- c(7, 12, 28, 35, 42)

# Plotting Line Chart
plot(x, y, type = "b", pch = 19, col = "blue", lwd = 2,
     main = "Line Chart in R",
     xlab = "X Values",
     ylab = "Y Values")
grid()`
  },
  {
    id: 'r-bar-chart',
    language: 'r',
    title: 'Bar Chart',
    keywords: [
      'bar chart', 'bar plot', 'barplot', 'bar graph',
      'bar plot,r', 'bar plot, r', 'bar plot r', 'bar chart,r', 'bar chart, r', 'bar chart r', 'barplot,r'
    ],
    code: `# Data
values <- c(80, 70, 90, 60, 75)
categories <- c("A", "B", "C", "D", "E")

# Plotting Bar Chart
barplot(values, names.arg = categories, col = "skyblue", border = "black",
        main = "Bar Chart in R",
        xlab = "Categories",
        ylab = "Scores")
grid(nx = NA, ny = NULL)`
  },
  {
    id: 'r-histogram',
    language: 'r',
    title: 'Histogram',
    keywords: [
      'histogram', 'hist plot', 'frequency distribution',
      'histogram,r', 'histogram, r', 'histogram r', 'hist plot,r', 'hist,r'
    ],
    code: `# Sample Data
set.seed(42)
scores <- rnorm(100, mean = 65, sd = 10)

# Plotting Histogram
hist(scores, col = "coral", border = "black", breaks = 8,
     main = "Histogram in R",
     xlab = "Marks Range",
     ylab = "Frequency")`
  },
  {
    id: 'r-box-plot',
    language: 'r',
    title: 'Box Plot',
    keywords: [
      'box plot', 'boxplot', 'whisker plot',
      'box plot,r', 'box plot, r', 'box plot r', 'boxplot,r', 'boxplot, r', 'boxplot r'
    ],
    code: `# Sample Data
data <- list(Group1 = c(23, 25, 29, 34, 30),
             Group2 = c(19, 20, 22, 24, 25),
             Group3 = c(35, 38, 40, 42, 45))

# Plotting Box Plot
boxplot(data, col = c("lightgreen", "lightblue", "lightpink"),
        main = "Box Plot in R",
        xlab = "Groups",
        ylab = "Values")
grid()`
  },
  {
    id: 'r-scatter-plot',
    language: 'r',
    title: 'Scatter Plot',
    keywords: [
      'scatter plot', 'scatter plot in r', 'scatter graph',
      'scatter plot,r', 'scatter plot, r', 'scatter plot r', 'scatter,r', 'scatter chart,r'
    ],
    code: `# Data
x <- c(10, 20, 30, 40, 50, 60, 70)
y <- c(15, 28, 35, 48, 52, 69, 75)

# Plotting Scatter Plot
plot(x, y, pch = 16, col = "darkmagenta", cex = 1.5,
     main = "Scatter Plot in R",
     xlab = "Independent Variable (X)",
     ylab = "Dependent Variable (Y)")
abline(lm(y ~ x), col = "red", lwd = 2) # Trend line
grid()`
  },
  {
    id: 'r-grouped-bar-chart',
    language: 'r',
    title: 'Grouped Bar Chart',
    keywords: [
      'grouped bar chart', 'clustered bar chart', 'multiple bar chart',
      'grouped bar chart,r', 'grouped bar chart, r', 'grouped bar chart r', 'grouped bar plot,r'
    ],
    code: `# Data matrix (rows = sub-categories, columns = main categories)
data <- matrix(c(12, 18, 20, 25, 15, 22), nrow = 2, byrow = TRUE)
colnames(data) <- c("Q1", "Q2", "Q3")
rownames(data) <- c("Product A", "Product B")

# Plotting Grouped Bar Chart
barplot(data, beside = TRUE, col = c("steelblue", "orange"),
        main = "Grouped Bar Chart in R",
        xlab = "Quarters",
        ylab = "Sales",
        legend.text = TRUE,
        args.legend = list(x = "topleft"))
grid(nx = NA, ny = NULL)`
  },
  {
    id: 'r-pie-chart',
    language: 'r',
    title: 'Pie Chart',
    keywords: [
      'pie chart', 'pie plot', 'pie chart in r',
      'pie chart,r', 'pie chart, r', 'pie chart r', 'pie plot,r', 'pie,r'
    ],
    code: `# Data
slices <- c(40, 25, 20, 15)
labels <- c("Apples", "Bananas", "Cherries", "Dates")
pct <- round(slices / sum(slices) * 100)
labels <- paste(labels, pct, "%", sep = " ")

# Plotting Pie Chart
pie(slices, labels = labels, col = rainbow(length(slices)),
    main = "Pie Chart in R")`
  }
];

export function findOfflineMatch(query: string, documentLanguage?: string): OfflineSolution | undefined {
  const rawQ = query.toLowerCase().trim();
  // Normalized query: remove extra spaces and punctuation around commas
  const q = rawQ.replace(/\s*,\s*/g, ',').trim();
  const lang = documentLanguage?.toLowerCase().trim();

  // Explicit target language detection from commas / suffix (e.g. "bar plot,py" or "histogram,r")
  let targetLang: 'python' | 'r' | undefined = undefined;
  if (
    q.endsWith(',py') || q.endsWith(',python') ||
    q.includes(',py ') || q.includes(',python ') ||
    q.includes('in python') || q.includes('python') ||
    lang === 'python' || lang === 'py'
  ) {
    targetLang = 'python';
  } else if (
    q.endsWith(',r') || q.includes(',r ') ||
    q.includes('in r') || q.includes(' r ') || q.startsWith('r ') ||
    lang === 'r'
  ) {
    targetLang = 'r';
  }

  // 1. Try candidates based on target language if identified
  let candidates = OFFLINE_DATABASE;
  if (targetLang) {
    candidates = OFFLINE_DATABASE.filter(c => c.language === targetLang);
  }

  // Check candidates with keyword matches (longest keyword first)
  const scoredMatches: { item: OfflineSolution; matchedLength: number }[] = [];

  for (const item of candidates) {
    for (const kw of item.keywords) {
      const normalizedKw = kw.replace(/\s*,\s*/g, ',');
      if (q.includes(normalizedKw) || rawQ.includes(kw)) {
        scoredMatches.push({ item, matchedLength: kw.length });
      }
    }
  }

  if (scoredMatches.length > 0) {
    scoredMatches.sort((a, b) => b.matchedLength - a.matchedLength);
    return scoredMatches[0].item;
  }

  // 2. Fallback: check all candidates if target language filter had no match
  for (const item of OFFLINE_DATABASE) {
    for (const kw of item.keywords) {
      const normalizedKw = kw.replace(/\s*,\s*/g, ',');
      if (q.includes(normalizedKw) || rawQ.includes(kw)) {
        scoredMatches.push({ item, matchedLength: kw.length });
      }
    }
  }

  if (scoredMatches.length > 0) {
    scoredMatches.sort((a, b) => b.matchedLength - a.matchedLength);
    return scoredMatches[0].item;
  }

  return undefined;
}

# Session 4 — Claude Code prompt script (instructor)

Example prompts to paste live, one step at a time. Delivery model: show the step's
**overslide**, switch to **Claude Code**, paste that step's prompt so the room sees
your run while they do theirs. These are *examples* — adapt to what the room needs;
students should phrase their own, in their own words.

---

## Scaffold

```text
Scaffold this project, without looking at the data. Ensure python is installed and other necessary items are present. After this we will work through each step one at a time, don't skip ahead.
```

## Interview

```text
Interview me about this project, it's domain and goals, and any hypothesis for particular questions of interest. Ask one question at a time.
```

## Metadata

```text
Explore the metadata thoroughly. What columns are there, what kind of data do they contain? Is it internally consistent? Pay attention to how to differentiate experimental from controls, what internal controls are present? What does plate layout look like? Let me know if you surface any issues. Don't skip ahead to QC, focus just on scrutinizing and understanding the metadata. Save metadata descriptions in METADATA.md, keep this up to date.
```

Then, to visualize:

```text
I want to generate plots that show distributions of important covariates in our metadata. I want a visual idea of what we're working with.
```

## Data

```text
Now I want to explore the data. What is there, what are the values, are they already logged? Are they already normalized? Are there missing data? How are they represented? What is the shape of the data?  Don't skip ahead to QC, focus just on scrutinizing and understanding the data. Save data descriptions in DATA.md, keep this up to date.
```

## QC

```text
I want to perform QC analysis and visualization. We need to work out if normalization, batch correction, or imputation are necessary and how we should do that. Once you have enough information interview me about these and present me with recommendations. I want to see how the distribution of proteins changes with run order. I want to see the distribution of CVs, separated by experimental and control samples. I want to see PCA plots, colored by run order and important covariates. I want to see how these change with normalization as well. If we impute, I want to see the distribution of values we impute superimposed on the distribution of unimputed values. Should we just filter on missingness instead? I want to see how well samples correlate with one another, clustered, and labeled by sample type (experiment or control). Once we have made our decisions, generate a final QC report as a HTML document.
```

## Data loaders

```text
Build robust, and well-tested data loaders that all downstream analysis scripts will use to load, normalize, batch correct, and impute (if necessary). This will match data to metadata, so it can be correctly used downstream (e.g., classifying exposure). It is essential that his be accurate and correct, as all downstream analysis depends on this. Verify assumptions about the loaded data (ie, make sure shapes are correct and other assumptions are met). These scripts need to be well documented and well commented, they will likely be shared as part of an eventual publication.
```

> **Instructor note:** may want to start a new session here with a clean context.


## Data analysis

```text
I want to know which proteins correlate with radiation dose. Choose an appropriate method for my data for finding these. Generate appropriate figures for my review. Save protein lists as CSV and generate plots for the most correlated proteins.
```

```text
Do a Gene Ontology enrichment for the most correlated proteins, both positive and negative. Generate appropriate CSV reports and visualizations for the top terms. What pathways stand out?
```

```text
I want to build a model to predict whether a new sample has been exposed to radiation. Build a linear classification model. Develop appropriate visualizations and statistics for evaluating the model. Generate visualizations that show me the most important proteins.
```

```text
I want to build a model to predict the dose of an unseen sample. Build a linear regression model. Watch out for overfitting. Develop appropriate visualizations and statistics for evaluating the model. Generate visualizations that show me the most important proteins.
```

## Report

```text
Generate a HTML report with a results, methods, and discussion section containing figures, tables, and supporting evidence for our claims. Something appropriate to share with a collaborator.
```
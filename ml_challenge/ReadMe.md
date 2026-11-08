# Machine Learning Challenge

The Machine Learning Challenge is an **individual assignment worth 30% of your course grade**. Develop the most accurate and robust prediction model you can for a numerical target `Y`, using the supplied anonymous, synthetic features. The challenge emphasizes applied machine learning: selecting appropriate methods, validating their robustness, and using modern development tools effectively.

## Deadline and submission

**Deadline: 15 December 2026.** Submit your solution through the [Canvas assignment page](https://canvas.esmt.berlin/courses/794/assignments/11053), as specified in the starter notebook. The syllabus refers to Moodle; the current assignment-specific instructions direct you to Canvas.

Submit all of the following:

1. **Test predictions as a CSV file**, containing a prediction for every observation in the test set and following the format below.
2. **A completed Jupyter notebook** containing all code used to develop your submitted solution, including preprocessing, feature engineering, model training, and prediction. The notebook must execute without error and reproduce the submitted predictions when run from a fresh kernel. Include your explanations and resulting outputs, and enter your name in the notebook.
3. **A brief description of your modeling approach, maximum one page**, highlighting noteworthy methodological decisions or innovations.
4. **A `requirement.txt` file, if needed**: include this when you use Python libraries outside the course environment, so that your environment and solution can be reproduced.

## Assignment rules

- You may use any Python library and any machine learning method.
- You are encouraged to use appropriate resources, including generative AI, to design, implement, and improve your solution. This includes discussing modeling approaches and generating code with AI.
- Apply your own thinking and judgment. Other students may use similar AI-generated solutions; thoughtful methodological choices can help your work stand out.
- The data is synthetically generated. Do not try to reverse engineer the data generation mechanism.
- Exclude `ID` from the model's input features. It identifies cases and aligns features, targets, and predictions.
- Develop and compare models using validation data drawn from the training sample. Fit learned preprocessing using only the relevant training rows, then apply that fitted preprocessing to validation data.
- After selecting your modeling procedure, fit your final model using the available training data. Apply the same fitted preprocessing when predicting the test cases.
- Keep your code readable and the complete workflow reproducible. Use `SEED` for reproducible random operations where applicable. Reproducibility will be verified.
- Submit predictions in the required format, with every test case included exactly once.

## Data and starter notebook

The training data consists of features in `train_X.csv` and observed targets in `train_y.csv`. Match rows by `ID`; the target column is `Y`, and feature names follow the pattern `X1`, `X2`, and so on. The test file, `test_X.csv`, contains features and IDs but no targets. Test targets remain hidden for evaluation.

Start with [ml_challenge_starter.ipynb](ml_challenge_starter.ipynb). By default, it expects the data files in the same folder as the notebook. Adjust `DATA_DIR` if you store them elsewhere. It provides:

- `load_training_data()`: loads training features and targets, aligns them by `ID`, and excludes `ID` from the feature columns.
- `load_test_data()`: loads test features with IDs in the row index.
- `write_submission(test_ids, predictions, filename)`: writes predictions with columns `ID` and `Y`, preserving the supplied ID/prediction order.

The notebook includes a constant forecast equal to the training target mean and a linear regression baseline. Their printed MAEs are **in-sample errors**, and included for illustration. Use a suitable validation approach to assess performance on unseen cases and improve on these starting points.

Add your code and Markdown explanations under **Your solution**. Assign your final fitted predictor to `final_model` and its test predictions to `test_predictions`, or adapt the submission cell to your variable names. Run the submission cell to create `submission.csv`. Before submitting, restart the kernel and run all cells in order to check that the notebook reproduces your CSV.

## Prediction file format

Your CSV must have a header with exactly the columns `ID` and `Y`. Include one finite numerical prediction for each test ID, with no duplicate or missing cases. Preserve the test file's row order when using the supplied submission cell.

The supplied [sample_submission.csv](sample_submission.csv) illustrates the format:

| ID | Y |
|---:|---:|
| 2386 | 88.88 |
| 1298 | -88.88 |
| ... | ... |
| 157 | 88.88 |
| 1629 | -88.88 |

The values are placeholders. The ellipsis represents omitted rows; do not include it in your submission. Your actual CSV must contain all test cases. Using the provided function `write_submission()`function should ensure that your submission file complies with the formatting specification.

<div class="alert-warning">
**Disclaimer**: All codes provided in the starter notebook have been carefully tested. We provide them to support you with the assignment. That said, we take no responsibility for the files that you submit. It is your responsibility to ensure that test data forecasts comply with out format specification, and is your responsibility to ensure your forecasts can be reproduced by rerunning your notebook, subject to all needed libraries being installed.
</div>

## Evaluation and grading

The primary assessment criterion is predictive performance on the hidden evaluation data, measured by **mean absolute error (MAE)**. Lower MAE is better.

Performance is assessed relative to established benchmark models and to other students' submissions. Benchmarks may include a linear model, an untuned tree-based ensemble, or other standard approaches appropriate for the task. These examples do not specify the final benchmark set.

| Criterion | Share of challenge grade | What is assessed |
|---|---:|---|
| Predictive performance relative to benchmark models | 60% | How much your solution improves upon one or more predefined benchmark models appropriate for the task. |
| Predictive performance relative to other submissions | 30% | Your solution's standing relative to other students' predictive performance. |
| Quality of the implementation | 10% | Reproducibility, readability, and technical quality of the notebook, including implementation of the proposed solution and particularly innovative methodological ideas. |

Particularly thoughtful or innovative methodological ideas may receive additional credit even if they do not produce the strongest predictive performance. Use the one-page description to highlight these decisions.

## Files in this folder

| File | Purpose |
|---|---|
| [ReadMe.md](ReadMe.md) | Assignment rules, deliverables, evaluation criteria, and file guide. |
| [ml_challenge_starter.ipynb](ml_challenge_starter.ipynb) | Starter notebook with instructions, data-loading helpers, baseline models, and submission generation. Develop and document your solution here. |
| [train_X.csv](train_X.csv) | Training feature values with an `ID` column identifying each case. |
| [train_y.csv](train_y.csv) | Observed training targets in column `Y`, identified by `ID`. |
| [test_X.csv](test_X.csv) | Test features and IDs for which you must generate predictions. Test targets are withheld. |
| [sample_submission.csv](sample_submission.csv) | Abbreviated illustration of the required `ID,Y` CSV format, with placeholder predictions and an ellipsis. |

Running the notebook's submission cell creates **`submission.csv`** in the working directory. This generated file contains your model's test predictions and is one of the required deliverables. A **`requirement.txt`** file is an additional file you supply if you use libraries outside the course environment.

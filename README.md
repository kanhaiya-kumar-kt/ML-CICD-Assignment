# ML-CICD-Assignment

## Assignment

CI/CD pipeline for a simple Machine Learning model using GitHub Actions.

### Model
- Model: Random Forest Classifier
- Dataset: Iris Dataset
- Library: scikit-learn
- Testing: pytest
- Deployment: GitHub Pages

## Repository Structure

```text
ML-CICD-Assignment/
├── model.py
├── test_model.py
├── requirements.txt
├── index.html
├── README.md
└── .github/
    └── workflows/
        └── cicd.yml
```

## How to use this on GitHub

1. Create a new **public** GitHub repository named `ML-CICD-Assignment`.
2. Upload all files and folders from this project to the repository.
3. Make sure the default branch is named `main`.
4. Go to **Settings → Pages**.
5. Under **Build and deployment**, select **GitHub Actions** as the source.
6. Commit/push the files to `main`.
7. Open the **Actions** tab and select **ML CI/CD Pipeline**.
8. The `ci` job will:
   - Checkout the code.
   - Set up Python 3.11.
   - Install dependencies.
   - Train/run the ML model.
   - Run pytest tests.
9. Only after `ci` passes, the `cd` job runs because it contains:
   ```yaml
   needs: ci
   ```
10. The CD job deploys `index.html` to GitHub Pages.
11. After a successful run, open the deployed Pages URL shown in the CD job.
12. Submit the GitHub repository URL in the assignment Google Form.

## Important

The workflow is designed so:

```text
CI
 ↓
PASS
 ↓
CD
 ↓
GitHub Pages Deployment
```

The CD job runs on pushes to `main` only after the CI job succeeds. Pull requests run CI but do not deploy.

## Expected GitHub Actions result

You should see:

- Continuous Integration: ✓
- Continuous Deployment: ✓
- GitHub Pages deployment: ✓

The deployed page displays the model name, dataset, accuracy, and CI/CD deployment status.

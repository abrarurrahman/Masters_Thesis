# 📝 Contribution Guidelines

Thank you for your interest in contributing to the **Predictive Modeling of MSA Posterior Probabilities Using Deep Learning** repository! Contributions are welcome and appreciated. Please follow these guidelines to ensure a smooth collaboration.

## 📌 How to Contribute

### 1. Fork the Repository
- Click the **Fork** button on the top right of the repository page to create your copy.
- Clone your fork to your local machine:
  ```bash
  git clone https://github.com/YOUR_USERNAME/Masters_Thesis.git
  cd Masters_Thesis
  ```
- Set the upstream repository:
  ```bash
  git remote add upstream https://github.com/abrarurrahman/Masters_Thesis.git
  ```

### 2. Create a Feature Branch
- Always create a new branch for your changes:
  ```bash
  git checkout -b feature-branch-name
  ```
- Make meaningful commits with clear messages:
  ```bash
  git commit -m "Add feature: Improved data preprocessing pipeline"
  ```

### 3. Keep Your Fork Up to Date
- Sync your fork with the upstream repository regularly:
  ```bash
  git fetch upstream
  git checkout main
  git merge upstream/main
  ```

### 4. Code Style and Standards
- Follow the existing **coding style** in the repository.
- Use **descriptive variable names** and comments where necessary.
- Maintain **PEP8** compliance for Python scripts:
  ```bash
  pip install flake8
  flake8 your_script.py
  ```
- Format code using **black** (recommended):
  ```bash
  black your_script.py
  ```

### 5. Testing Your Code
- Ensure that your changes do not break existing functionality.
- If applicable, add unit tests to validate your changes.
- Run tests before submitting your contribution:
  ```bash
  python -m unittest discover tests
  ```

### 6. Submit a Pull Request (PR)
- Push your branch to your fork:
  ```bash
  git push origin feature-branch-name
  ```
- Go to the [original repository](https://github.com/abrarurrahman/Masters_Thesis/).
- Click **New Pull Request**, select your branch, and provide a clear description of your changes.
- Address any feedback provided during code review.

## ✅ Good Practices
✔ **Write clear and concise commit messages.**
✔ **Add documentation** for new functions and scripts.
✔ **Optimize performance** where applicable.
✔ **Break down large changes** into smaller PRs for easier review.
✔ **Be respectful** and collaborative when discussing issues and improvements.

## 🛠 Issues and Discussions
- Check open **Issues** before submitting new ones.
- When reporting a bug, provide:
  - Steps to reproduce the issue.
  - Expected vs. actual behavior.
  - Relevant logs or screenshots.
- For feature requests, describe the use case and benefits clearly.

## 🏆 Acknowledgment
Your contributions make this project better! Thank you for taking the time to improve **Predictive Modeling of MSA Posterior Probabilities Using Deep Learning**.

Happy coding! 🚀

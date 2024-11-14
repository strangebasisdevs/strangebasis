# Documentation Approach

By organizing your documentation in a `docs` directory and setting up Sphinx configuration files, we plan to start with GitHub Pages and smoothly transition to Read the Docs when needed. This approach allows us to leverage the simplicity of GitHub Pages initially and scale up to the advanced features of Read the Docs if/when the project grows.

## Current Approach for Basic Documentation Needs

1. **Organize Documentation Files**

   - Create a `docs` directory in your repository to store all your documentation files. This will be the central place for both GitHub Pages and Read the Docs.

2. **Set Up GitHub Pages**
   - Use Markdown files for your documentation initially. Configure GitHub Pages to serve the content from the `docs` directory.
     - **Create Markdown Files**: Write your documentation in Markdown files within the `docs` directory.
     - **Configure GitHub Pages**:
       - Go to your repository settings on GitHub.
       - Scroll down to the "GitHub Pages" section.
       - Select the `docs` folder as the source.

## High-Level Plan for Transitioning to Read the Docs

1. **Prepare for Read the Docs**

   - Set up Sphinx and create the necessary configuration files.
     - **Install Sphinx and Theme**: Install Sphinx and the Read the Docs theme.
       ```bash
       poetry add --group=dev sphinx
       poetry add --group=dev sphinx-rtd-theme
       ```
     - **Initialize Sphinx**: Run `sphinx-quickstart` to initialize Sphinx.
     - **Configure `conf.py`**: Update `docs/conf.py` to use the Read the Docs theme and include necessary extensions **_(consider `myst-parser` to support parsing Markdown docs directly and reduce overhead of learning .rst format)_**.
     - **Create `.readthedocs.yml`**: Add a configuration file for Read the Docs.
     - **Add Requirements File**: Create `docs/requirements.txt` to list your documentation dependencies.

2. **Transition to Read the Docs**
   - When you are ready to transition to Read the Docs:
     - **Convert Markdown to reStructuredText**: If necessary, convert your Markdown files to reStructuredText.
     - **Update Sphinx Configuration**: Ensure `conf.py` is correctly configured.
     - **Push Changes**: Push your changes to the repository.
     - **Link to Read the Docs**: Link your repository to Read the Docs and configure it to build your documentation.

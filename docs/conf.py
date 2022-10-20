# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'subproject-f5'
copyright = '2022, Robin Mordasiewicz'
author = 'Robin Mordasiewicz'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

is_subproject=True
readthedocs_url="https://f5-xc-workspaces.readthedocs.io"

extensions = [
    "subprojecttoctree",
    "sphinx_rtd_theme"
]

html_theme_options = {
    "repository_url": "https://github.com/robinmordasiewicz/subproject-f5",
    "use_repository_button": True,
    'github_url': "https://github.com/robinmordasiewicz/subproject-f5",
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'top',
    'style_external_links': False,
    'vcs_pageview_mode': 'edit',
    'style_nav_header_background': '#f7f8fa',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': True
}

html_title = "Subproject"
#html_logo = "logo_f5.svg"

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'sphinx_book_theme'
html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
]

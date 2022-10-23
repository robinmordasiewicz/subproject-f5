# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Workspaces - project'
copyright = '2022, Robin Mordasiewicz'
author = 'Robin Mordasiewicz'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

is_subproject=True
readthedocs_url="https://f5-xc-workspaces.readthedocs.io"

extensions = [
    "subprojecttoctree",
    "sphinx_design",
    "sphinx.ext.viewcode"
]

html_theme_options = {
    "repository_url": "https://github.com/robinmordasiewicz/subproject-f5",
    'github_url': "https://github.com/robinmordasiewicz/subproject-f5",
    "use_repository_button": True,
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
    'breadcrumbs': True,
    'body_centered': False,
    'globaltoc_includehidden': True,
    'sidebarwidth': '250',
    'titles_only': True
}

html_copy_source = True
html_show_sourcelink = True
pygments_style = 'monokai'
html_show_copyright = False
html_show_sphinx = False
html_context = {
    'display_gitlab': True,
    'gitlab_user': 'robinmordasiewicz',
    'gitlab_repo': 'subproject-f5',
    'conf_py_path': '/docs/',
}

html_title = "Workspaces - html_title"
#html_logo = "logo_f5.svg"

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'sphinx_book_theme'
#html_theme = "insipid"
html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
]

html_style = 'css/custom.css'

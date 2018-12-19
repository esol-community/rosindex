# -*- coding: utf-8 -*-
#
# rosindex documentation build configuration file, created by
# sphinx-quickstart on Tue Oct  2 16:34:57 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# sys.path.insert(0, os.path.abspath('.'))

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#

# The master toctree document.
master_doc = 'index'

# The default role
default_role = 'any'

# The set of warnings to suppress.
suppress_warnings = ['image.nonlocal_uri']

# General information about the project.
project = u'rosindex'
copyright = u'2018, Open Robotics'
author = u'Open Robotics'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u''
# The full version, including alpha/beta/rc tags.
release = u''

# Define the default role to use for links
default_role = 'any'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
extensions = ['sphinx.ext.intersphinx']

# Intersphinx mapping

intersphinx_mapping = {
    'catkin_pkg':    ('http://docs.ros.org/independent/api/catkin_pkg/html', None),
    'jenkins_tools': ('http://docs.ros.org/independent/api/jenkins_tools/html', None),
    'rosdep':        ('http://docs.ros.org/independent/api/rosdep/html', None),
    'rosdistro':     ('http://docs.ros.org/independent/api/rosdistro/html', None),
    'rosinstall':    ('http://docs.ros.org/independent/api/rosinstall/html', None),
    'rospkg':        ('http://docs.ros.org/independent/api/rospkg/html', None),
    'vcstools':      ('http://docs.ros.org/independent/api/vcstools/html', None)
}

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'ros2_docsdoc'
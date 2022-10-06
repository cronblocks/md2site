#! /bin/bash

# *****************************************************************************************
# * Purpose:
# *     Running the main application by passing-in command-line arguments
# *
# *
# *****************************************************************************************
# * Author: Usama
# *
# *****************************************************************************************
# * Changes:
# *
# * Date         Changed by      Description
# * ----         ----------      -----------
# *
# *
# *
# *
# *****************************************************************************************

PWD=$(pwd)
docs_in_dir="$PWD/sample-data"
recursion_enabled="true"
recursion_depth="infinite"
element_templates_dir="$PWD/src/templates/element-templates"
site_template_dir="$PWD/src/templates/site-template-001-default"
site_out_dir="$PWD/generated-site"
site_base_url="-"

#     1 => path-to-scan          => file or directory full-path
#     2 => recursion-enabled     => [true] / false
#     3 => recursion-depth       => number / [infinite]
#     4 => dir-element-templates => - for default
#     5 => dir-site-template     => - for default
#     6 => dir-output            => - for default
#     7 => base-url              => - for local files
env --chdir="./src/converter"           \
    python3 "md2site.py"                \
            "$docs_in_dir"              \
            "$recursion_enabled"        \
            "$recursion_depth"          \
            "$element_templates_dir"    \
            "$site_template_dir"        \
            "$site_out_dir"             \
            "$site_base_url"

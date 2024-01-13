@echo off

:: ***********************************************************************************
:: * Purpose:
:: *     Running the main application by passing-in the required
:: * command-line arguments.
:: *
:: ***********************************************************************************
:: * Author: Usama
:: *
:: ***********************************************************************************
:: * Changes:
:: *
:: * Date         Changed by      Description
:: * ----         ----------      -----------
:: *
:: *
:: *
:: *
:: ***********************************************************************************

TITLE md2site

set cwd=%cd%
set docs_in_dir=%cwd%\sample-data
set recursion_enabled=true
set recursion_depth=infinite
set element_templates_dir=%cwd%\src\templates\element-templates
set site_template_dir=%cwd%\src\templates\site-template-001-default
set site_out_dir=%cwd%\generated-site
set site_base_url="-"

CD "src\converter"

::     1 => path-to-scan          => file or directory full-path
::     2 => recursion-enabled     => [true] / false
::     3 => recursion-depth       => number / [infinite]
::     4 => dir-element-templates => - for default
::     5 => dir-site-template     => - for default
::     6 => dir-output            => - for default
::     7 => base-url              => - for local files
python "md2site.py"                  ^
            %docs_in_dir%            ^
            %recursion_enabled%      ^
            %recursion_depth%        ^
            %element_templates_dir%  ^
            %site_template_dir%      ^
            %site_out_dir%           ^
            %site_base_url%

PAUSE

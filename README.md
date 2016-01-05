# Deployment of Web Applications » Portfolio

#### Requirements:
-----
  1. Ubuntu 12.04+
  2. Git: Version control, pushing to different environments
  3. Apache HTTPD: Serving the site and its' assets
  4. WSGI module: WSGI interface between Python and Apache
  5. Python: Back-end language
  6. Django: Back-end framework
  5. Sass: CSS preprocessor
  6. Compass: Sass compiler
  6. CoffeeScript: JavaScript language
  7. CoffeeScript CLI: CoffeeScript compiler

#### Branches:
-----
When significant additions are anticipated they should be created on a branch separate from master. The master branch should not contain incomplete pieces of the app. When commits are made on the master branch they should be ready to be promoted to staging meaning all tests must pass and the source code within the master branch must be ready for the world to use.

#### Naming Convention:
-----
Python, Sass:
UpperCamelCase should be used for class names, UPPERCASE_WITH_UNDERSCORES should be used for constants, and lowercase_seperated_by_underscores should be used for variables.

JavaScript, CoffeeScript:
Variable and method names should be lowerCamelCase. Constructors should use UpperCamelCase.

Use single quotes as often as possible. Double quotes should only be used when necessary. The source should be designed with modularity and portability in mind.

#### Versioning:
-----
Version numbers should follow the standard pattern of the release version number followed by the production release number then the staging release number. When commits are made to master they are sent to the staging server at an arbitrary time and the staging number increases. Each production increment resets the staging increment to zero.

#### Preferred Operating System:
----
Ubuntu 12.04 or later should be the operating system used for serving the application. Other operating systems have not been tested nor configured to support the application, although it uses mostly cross compatible dependencies.

=======
History
=======

0.1.0 (2019-02-16)
------------------

* Migrate from script to package.

0.2.0 (2019-02-17)
------------------

* Add CMLL, ELL, CLL
* Shorten certain scrambles to their acronyms

0.2.1-2 (2019-05-02)
------------------

* Minor fix to setup.py, use entrypoint instead of console_script, update name from scramble-cli to cube-scramble-cli

0.2.3 (2019-05-02)
------------------

* Restructure, move constant values to constants.py

0.3 (2019-07-19)
------------------

* Restructure to allow tests with doctest
* Remove colorama and use tabulate instead

0.4 (2019-07-20)
------------------

* Added stopwatch
* Renamed 'RU SCRAMBLE' to RU
* Added flags to print scrambles
* Fixed bug that didn't allow you to generate '2x2' scrambles

0.4.1 (2019-11-26)
------------------

* Replace time.clock (deprecated) with time.perf_counter

0.4.2 (2019-11-27)
------------------

* Add a gif and improve pypi description

0.4.3 (2019-12-29)
------------------

* Allow user to set environment variable to change the location of the history REPL file.

0.4.4 (2020-09-17)
------------------

* Unparsed args from the user are interpreted as scramble input.

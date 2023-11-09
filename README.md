# SeqComplementor.py

## Abstract
Program to convert sequences to complementary sequences


## Usage

```sh
$ SeqComplementor.py [-h] -i INPUT.csv -o OUTPUT.csv -ti SEQUENCE_TYPE_INPUT -to SEQUENCE_TYPE_OUTPUT [-r] [-O]
```

* `-h`, `--help`
	: show this help message and exit
* `-i INPUT.csv`
	: sequence list file with header of `Sequence`
* `-o OUTPUT.csv`
	: output file
* `-ti SEQUENCE_TYPE_INPUT`
	: sequence type for input (`DNA` or `RNA`)
* `-to SEQUENCE_TYPE_OUTPUT`
	: sequence type for output (`DNA` or `RNA`)
* `-r`
	: reverse complementary sequence (output sequence order is 5' to 3'-terminal)
* `-O`
	: overwrite forcibly

## Requirements
* Python
	* pandas


## License
The MIT License (MIT)

Copyright (c) 2023 Tatsuya Ohyama


## Authors
* Tatsuya Ohyama


## ChangeLog
### Ver. 1.0 (2023-11-09)
* Release.

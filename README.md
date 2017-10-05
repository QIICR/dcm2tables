# Overview

Tools to go from a DICOM dataset into a collection of tables for the purposes
of data repurposing and exploration using relational databases.

This is not a general purpose tool. Initial goal is to support exploration of
the TCIA QIN-HEADNECK dataset.

# Prerequisites

Software:
* python
* pandas
* pydicom (must be installed from source! distribution available via pip is too
  old and does not have some of the DICOM dictionary entries we parse)

Data:
* https://wiki.cancerimagingarchive.net/display/Public/QIN-HEADNECK

# Usage

```
python tabulate.py -s schema.qdbd -d <location of a directory with DICOM data> -o <output location to store csv tables>
```

The script will create tables stored in CSV in the directory where it was
executed.

# Contact

* Andrey Fedorov https://fedorov.github.io

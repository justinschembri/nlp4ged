# Test Data Naming Conventions

Test data will be placed in subfolders corresponding to component being tested. For example, if the `Corpus` class is being test from the `corpus.py` script, then the data will be found at `data/tests/corpus`. Test data will be formatted in the following format:

`[<componenent>UnitTest]_[TestClass]_[<numeral>]_[<description>]`

Where:
=====

- From `[<componenent>UnitTest]`, `<component>` shall refer to the component being tests,

- `[<TestClass]` is the specific test class,

- `[<numeral>]` is a sequential number, should the test have more than one dataset.

- `[description]` is a description of the data's particularities.

For example, `Corpus_CorrectData_1_tagged.xlsx` is a dataset which is used to test the `Corpus` class, the testclass is `CorrectData`, meaning testing how correct data is processed by said class, `1`, is the first dataset in the set, and `tagged` refers to data being tagged.